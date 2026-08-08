# Distillation benchmark

Does an agent given a distilled document as its `CLAUDE.md` write different
code? Reading the documents cannot answer that. This runs the experiment.

```sh
make bench-pilot     # cheap shakeout on sonnet
make bench           # the real thing, on opus
make analyze         # re-score the newest run
```

## What it measures

Lines of code is a hard number and the wrong target. What these documents claim
to produce is the smallest thing that is correct, testable and tested, so that
is what gets scored.

| column | what it is |
| --- | --- |
| `r1`..`r4` | neutral acceptance suite, passed/total for that round's requirements |
| `cover` | statement coverage the arm's *own* tests reach in its own library |
| `worst` | highest cyclomatic complexity of any library function |
| `>10` | library functions above the conventional complexity threshold |
| `MI` | radon maintainability index, higher is better |
| `r1kept` | share of round-1 lines still standing at the end |

`r1kept` is the one direct read on whether a design absorbed the later
requirements or was rewritten by them. Low means the initial representation was
wrong for requirements that had not arrived and rounds 2-4 paid to undo it.

Correctness is scored by `acceptance/`, the same adversarial suite against every
arm, because an arm grading itself with tests it wrote proves nothing. It checks
the things that actually break: durability across restart, a failure surviving a
crash, two workers never sharing a job, a crashed worker's job coming back,
transitions resuming from a cursor, counts summing to reality.

## The arms

Four arms build the same job queue from the same four round prompts, differing
in exactly one variable: the `CLAUDE.md` installed in the project directory.

| arm | CLAUDE.md |
| --- | --- |
| `control` | none |
| `incumbent` | Nathan's own, plus its two `@`-referenced files |
| `general` | `bundle/DISTILLED.md` |
| `flavored` | `$FLAVORED`, default `bundle/DISTILLED-FOUNDATIONS.md` |

The rounds add requirements the earlier rounds did not anticipate: retries, then
concurrent workers with crash recovery, then an ordered transition log and a
live count view. Rounds 3 and 4 are where a wrong round-1 representation gets
expensive, which is the whole point of the escalation.

## Reading the output

Output lands in `bench-runs/<timestamp>/` and stays there. Not `/tmp` — the
generated code is the artifact worth reading, and the numbers only tell you
which arm to go read.

Each arm is a git repo with a tag per round, so the evolution is reviewable:

```sh
git -C bench-runs/<stamp>/general log --stat
git -C bench-runs/<stamp>/general diff round1 round3      # what round 3 cost
git -C bench-runs/<stamp>/general show round1:jobqueue.py # the initial design
```

Per-round session logs, including token usage and cost, are under
`bench-runs/<stamp>/logs/<arm>/`.

## Mechanics worth knowing

The round prompts fix four method names so a neutral suite can run against every
arm. Everything that matters is still free: storage format, what the states are,
how concurrency is handled, whether counts are derived or maintained, how
transitions are recorded. Naming `enqueue` does not tell anyone how to build it.

`--bare` looks like the way to suppress the global `~/.claude/CLAUDE.md` and is
not: it disables CLAUDE.md discovery entirely, so the arm's document would not
load either, and it drops LSP, hooks and plugins, which measures a
differently-capable agent than the one being evaluated. The lever is an isolated
`CLAUDE_CONFIG_DIR`. That directory carries credentials as well as memory, so
`run.sh` seeds it with `.credentials.json` and nothing else.

`run.sh` uses `--dangerously-skip-permissions` because the run is unattended.
Every arm writes only inside its own directory under `bench-runs/`.

## Caveats, before anyone quotes a number

One task in one language. A job queue rewards the state, invariant and
concurrency material and barely exercises the language-design claims, so a
flavored arm losing here is evidence about this task, not about that document.

A single run per arm is an anecdote. Model output varies between runs and the
differences worth caring about are plausibly smaller than that variance, so
repeat each arm several times before believing an ordering.

Complexity and coverage are cheap to game and the agent is not trying to game
them, which is exactly why they are worth reading alongside the code rather than
instead of it.
