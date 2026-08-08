#!/usr/bin/env python3
"""Score benchmark arms.

Lines of code is a hard number and the wrong target. What these documents claim
to produce is the smallest thing that is correct, testable, and tested, so that
is what gets measured:

  correctness  a neutral acceptance suite, the same for every arm, per round
  complexity   cyclomatic complexity of the library only, worst function and
               how many exceed the conventional threshold of 10
  coverage     what the arm's own tests actually reach
  survival     of the lines a round wrote, how many still stand at the end

Survival is kept because it is the only direct read on whether a design
absorbed the later requirements or was rewritten by them.

Run through the venv: make analyze
"""
import json
import os
import re
import subprocess
import sys
from collections import defaultdict

ROUNDS = [1, 2, 3, 4]
SKIP_NAMES = {"CLAUDE.md", "RTK.md", "tropes.md"}
HERE = os.path.dirname(os.path.abspath(__file__))
ACCEPT = os.path.join(HERE, "acceptance")
VENV_BIN = os.path.dirname(sys.executable)
TEST_RE = re.compile(r"(^|/)(test_|tests?/|conftest)")


def git(work, *a):
    return subprocess.run(["git", "-C", work, *a],
                          capture_output=True, text=True).stdout


def run(cmd, cwd=None, env=None, timeout=900):
    e = dict(os.environ)
    e["PATH"] = VENV_BIN + os.pathsep + e.get("PATH", "")
    if env:
        e.update(env)
    try:
        return subprocess.run(cmd, cwd=cwd, env=e, capture_output=True,
                              text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None


# ------------------------------------------------------------- correctness

def acceptance(work):
    """Pass rate per round from the neutral suite, run against this arm."""
    out = {}
    for r in ROUNDS:
        res = run([os.path.join(VENV_BIN, "pytest"), ACCEPT,
                   "-m", f"round{r}", "-q", "--tb=no", "-p", "no:cacheprovider"],
                  cwd=work, env={"PYTHONPATH": work}, timeout=420)
        if res is None:
            out[r] = (0, 0, "timeout")
            continue
        text = res.stdout + res.stderr
        m = re.search(r"(\d+) passed", text)
        f = re.search(r"(\d+) failed", text)
        e = re.search(r"(\d+) error", text)
        p = int(m.group(1)) if m else 0
        bad = (int(f.group(1)) if f else 0) + (int(e.group(1)) if e else 0)
        note = "" if (p or bad) else "no-collect"
        out[r] = (p, p + bad, note)
    return out


# -------------------------------------------------------------- complexity

def library_files(work):
    """Arm source that is not tests and not the treatment."""
    files = []
    for root, dirs, names in os.walk(work):
        dirs[:] = [d for d in dirs if d not in {".git", "__pycache__", ".venv"}]
        for n in names:
            if not n.endswith(".py"):
                continue
            rel = os.path.relpath(os.path.join(root, n), work)
            if TEST_RE.search("/" + rel.replace(os.sep, "/")):
                continue
            files.append(rel)
    return files


def complexity(work):
    files = library_files(work)
    if not files:
        return None
    res = run([os.path.join(VENV_BIN, "radon"), "cc", "-j", *files], cwd=work)
    if res is None or not res.stdout.strip():
        return None
    try:
        data = json.loads(res.stdout)
    except json.JSONDecodeError:
        return None
    scores = [b["complexity"] for blocks in data.values()
              if isinstance(blocks, list) for b in blocks]
    if not scores:
        return None
    mi = run([os.path.join(VENV_BIN, "radon"), "mi", "-j", *files], cwd=work)
    mi_avg = None
    if mi is not None and mi.stdout.strip():
        try:
            vals = [v["mi"] for v in json.loads(mi.stdout).values()
                    if isinstance(v, dict) and "mi" in v]
            mi_avg = sum(vals) / len(vals) if vals else None
        except (json.JSONDecodeError, KeyError, TypeError):
            pass
    return {"worst": max(scores),
            "mean": sum(scores) / len(scores),
            "over10": sum(1 for s in scores if s > 10),
            "funcs": len(scores),
            "mi": mi_avg}


# ---------------------------------------------------------------- coverage

def coverage(work):
    """What the arm's own tests reach in the arm's own library."""
    if run([os.path.join(VENV_BIN, "coverage"), "run", "--source=.",
            "-m", "pytest", "-q", "--tb=no", "-p", "no:cacheprovider"],
           cwd=work, timeout=600) is None:
        return None
    res = run([os.path.join(VENV_BIN, "coverage"), "json", "-o", "-"], cwd=work)
    if res is None or not res.stdout.strip():
        return None
    try:
        d = json.loads(res.stdout)
    except json.JSONDecodeError:
        return None
    tot = {"covered": 0, "num": 0}
    for path, f in d.get("files", {}).items():
        if TEST_RE.search("/" + path.replace(os.sep, "/")):
            continue
        s = f.get("summary", {})
        tot["covered"] += s.get("covered_lines", 0)
        tot["num"] += s.get("num_statements", 0)
    return 100 * tot["covered"] / tot["num"] if tot["num"] else None


# ---------------------------------------------------------------- survival

def introduced(work, r):
    n = 0
    for line in git(work, "diff", "--numstat", f"round{r-1}", f"round{r}").splitlines():
        p = line.split("\t")
        if len(p) != 3 or p[0] == "-":
            continue
        if os.path.basename(p[2]) in SKIP_NAMES or p[2].endswith(".md"):
            continue
        n += int(p[0])
    return n


def surviving(work):
    sha = {r: git(work, "rev-parse", f"round{r}").strip() for r in ROUNDS}
    by_sha = {v: k for k, v in sha.items()}
    counts = defaultdict(int)
    tree = [f for f in git(work, "ls-tree", "-r", "--name-only", "round4").splitlines()
            if os.path.basename(f) not in SKIP_NAMES and not f.endswith(".md")]
    for path in tree:
        for line in git(work, "blame", "--line-porcelain", "round4", "--", path).splitlines():
            tok = line.split()
            if tok and len(tok[0]) == 40 and tok[0].isalnum():
                counts[by_sha.get(tok[0])] += 1
    return counts


# -------------------------------------------------------------------- main

def main():
    root = sys.argv[1]
    arms = sys.argv[2:] or ["control", "incumbent", "general", "flavored"]
    rows = []

    for arm in arms:
        # Absolute: cwd changes to this dir, so a relative PYTHONPATH pointing
        # at it would stop resolving and every import would fail as a collection
        # error that looks exactly like a failing test.
        work = os.path.abspath(os.path.join(root, arm))
        if not os.path.isdir(os.path.join(work, ".git")):
            rows.append((arm, None))
            continue
        print(f"scoring {arm} ...", file=sys.stderr)
        intro = {r: introduced(work, r) for r in ROUNDS}
        surv = surviving(work)
        rows.append((arm, {
            "accept": acceptance(work),
            "cx": complexity(work),
            "cov": coverage(work),
            "intro": intro, "surv": surv,
            "final": sum(surv.values()),
        }))

    print(f"\n{'ARM':<11}{'r1':>7}{'r2':>7}{'r3':>7}{'r4':>7}"
          f"{'cover':>8}{'worst':>7}{'>10':>5}{'MI':>6}{'lines':>7}{'r1kept':>8}")
    print("-" * 80)
    for arm, d in rows:
        if d is None:
            print(f"{arm:<11}  (not run)")
            continue
        cx, cov = d["cx"], d["cov"]
        cells = []
        for r in ROUNDS:
            p, t, note = d["accept"][r]
            cells.append(f"{p}/{t}" if t else (note or "-"))
        cover = f"{cov:.0f}%" if cov is not None else "-"
        worst = str(cx["worst"]) if cx else "-"
        over = str(cx["over10"]) if cx else "-"
        mi = f"{cx['mi']:.0f}" if cx and cx["mi"] is not None else "-"
        kept = (f"{100 * d['surv'].get(1, 0) / d['intro'][1]:.0f}%"
                if d["intro"].get(1) else "n/a")
        print(f"{arm:<11}" + "".join(f"{c:>7}" for c in cells)
              + f"{cover:>8}{worst:>7}{over:>5}{mi:>6}{d['final']:>7}{kept:>8}")

    print("\nr1..r4  neutral acceptance suite, passed/total for that round's "
          "requirements")
    print("cover   arm's own tests, statement coverage of its own library")
    print("worst   highest cyclomatic complexity of any library function")
    print(">10     library functions above the conventional complexity threshold")
    print("MI      radon maintainability index, higher is better")
    print("r1kept  share of round-1 lines still standing at the end")


if __name__ == "__main__":
    main()
