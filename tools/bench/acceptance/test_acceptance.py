"""Neutral acceptance tests, run against every arm's library.

An arm grading itself with tests it wrote proves nothing, so correctness is
scored here instead: the same adversarial suite against everybody, exercising
the things that actually break rather than the happy path.

Grouped by the round whose requirements they check, so an arm can pass round 1
and fail round 3 and we can see where it broke. Timing-dependent behaviour
(backoff, lease expiry) is configured through the constructor when the arm
accepts the keyword and waited out generously when it does not, since the
prompts never fixed those durations.
"""
import inspect
import json
import multiprocessing as mp
import time

import pytest

import jobqueue  # injected on sys.path by analyze.py


def make(path, **want):
    """Construct a Queue, passing only the tuning kwargs this arm accepts."""
    try:
        params = inspect.signature(jobqueue.Queue).parameters
        ok = {k: v for k, v in want.items() if k in params}
    except (TypeError, ValueError):
        ok = {}
    return jobqueue.Queue(str(path), **ok)


def drain(q, limit=200):
    out = []
    for _ in range(limit):
        j = q.claim()
        if j is None:
            break
        out.append(j)
    return out


# --------------------------------------------------------------- round 1

@pytest.mark.round1
def test_enqueue_claim_roundtrips_payload(tmp_path):
    q = make(tmp_path / "q")
    q.enqueue({"n": 1, "s": "x"})
    job = q.claim()
    assert job is not None
    assert job.payload == {"n": 1, "s": "x"}


@pytest.mark.round1
def test_claim_returns_none_when_empty(tmp_path):
    assert make(tmp_path / "q").claim() is None


@pytest.mark.round1
def test_a_claimed_job_is_not_handed_out_again(tmp_path):
    q = make(tmp_path / "q")
    q.enqueue({"n": 1})
    first = q.claim()
    assert first is not None
    assert q.claim() is None, "same job claimable twice"


@pytest.mark.round1
def test_survives_restart(tmp_path):
    q = make(tmp_path / "q")
    q.enqueue({"n": 7})
    del q
    again = make(tmp_path / "q")          # fresh instance, same location
    job = again.claim()
    assert job is not None and job.payload == {"n": 7}


@pytest.mark.round1
def test_done_is_durable(tmp_path):
    q = make(tmp_path / "q")
    q.enqueue({"n": 1})
    job = q.claim()
    q.done(job.id)
    del q
    assert make(tmp_path / "q").claim() is None, "completed job came back"


# --------------------------------------------------------------- round 2

@pytest.mark.round2
def test_failed_job_is_retried_then_dead_lettered(tmp_path):
    q = make(tmp_path / "q", max_attempts=3, base_delay=0.01, backoff=0.01)
    q.enqueue({"n": 1})
    seen = 0
    deadline = time.time() + 20
    while time.time() < deadline:
        job = q.claim()
        if job is None:
            if seen:
                break
            time.sleep(0.05)
            continue
        seen += 1
        q.fail(job.id)
        if seen > 12:
            pytest.fail("job retried well past any sane attempt limit")
    assert seen >= 2, "a failed job was never retried"
    assert q.claim() is None, "job still claimable after exhausting attempts"


@pytest.mark.round2
def test_failure_survives_restart(tmp_path):
    q = make(tmp_path / "q", max_attempts=5, base_delay=0.01, backoff=0.01)
    q.enqueue({"n": 1})
    job = q.claim()
    q.fail(job.id)
    del q                                  # process dies right after the failure
    again = make(tmp_path / "q", max_attempts=5, base_delay=0.01, backoff=0.01)
    deadline = time.time() + 15
    while time.time() < deadline:
        if again.claim() is not None:
            return
        time.sleep(0.05)
    pytest.fail("job lost across restart after a failure")


# --------------------------------------------------------------- round 3

def _grab(path, out, n):
    """Child process: claim as much as it can, report the ids."""
    try:
        q = jobqueue.Queue(str(path))
        got = []
        for _ in range(n):
            j = q.claim()
            if j is None:
                break
            got.append(str(j.id))
        out.put(got)
    except Exception as e:                  # noqa: BLE001 - reported, not raised
        out.put({"error": repr(e)})


@pytest.mark.round3
def test_concurrent_workers_never_share_a_job(tmp_path):
    path = tmp_path / "q"
    q = make(path)
    for i in range(40):
        q.enqueue({"n": i})
    del q

    ctx = mp.get_context("spawn")
    out = ctx.Queue()
    procs = [ctx.Process(target=_grab, args=(path, out, 40)) for _ in range(4)]
    for p in procs:
        p.start()
    results = [out.get(timeout=60) for _ in procs]
    for p in procs:
        p.join(timeout=30)

    errs = [r for r in results if isinstance(r, dict)]
    assert not errs, f"worker crashed: {errs}"

    claimed = [i for r in results for i in r]
    assert len(claimed) == len(set(claimed)), "one job handed to two workers"


@pytest.mark.round3
def test_crashed_worker_releases_its_job(tmp_path):
    path = tmp_path / "q"
    q = make(path, lease_seconds=1, lease_timeout=1, visibility_timeout=1)
    q.enqueue({"n": 1})
    stolen = q.claim()
    assert stolen is not None
    del q                                   # holder vanishes without done/fail

    watcher = make(path, lease_seconds=1, lease_timeout=1, visibility_timeout=1)
    deadline = time.time() + 30
    while time.time() < deadline:
        if watcher.claim() is not None:
            return
        time.sleep(0.2)
    pytest.fail("job held by a crashed worker never became available again")


# --------------------------------------------------------------- round 4

@pytest.mark.round4
def test_transitions_are_ordered_and_resumable(tmp_path):
    q = make(tmp_path / "q")
    for i in range(5):
        q.enqueue({"n": i})
    for _ in range(3):
        q.done(q.claim().id)

    first = list(q.transitions())
    assert len(first) >= 6, "transitions did not record enqueues and completions"

    half = first[: len(first) // 2]
    rest = list(q.transitions(after=half[-1].cursor))
    assert [r.cursor for r in rest] == [r.cursor for r in first[len(half):]], \
        "resuming from a cursor did not continue where it left off"

    del q
    after_restart = list(make(tmp_path / "q").transitions())
    assert len(after_restart) >= len(first), "transition log lost on restart"


@pytest.mark.round4
def test_counts_match_reality(tmp_path):
    q = make(tmp_path / "q")
    for i in range(10):
        q.enqueue({"n": i})
    done = [q.claim() for _ in range(4)]
    for j in done:
        q.done(j.id)

    counts = q.counts()
    assert isinstance(counts, dict) and counts, "counts() returned nothing usable"
    assert sum(counts.values()) == 10, f"counts do not sum to the job total: {counts}"
    assert 4 in counts.values(), f"no state holds the 4 completed jobs: {counts}"


@pytest.mark.round4
def test_counts_are_json_serialisable(tmp_path):
    q = make(tmp_path / "q")
    q.enqueue({"n": 1})
    json.dumps(q.counts())          # an admin view nobody can serve is not a view
