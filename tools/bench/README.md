# Distillation benchmark

Does an agent given a distilled document as its `CLAUDE.md` write different code?
Reading the documents cannot answer that. This runs the experiment.

## What it measures

Four arms build the same job queue from the same four round prompts. The rounds
add requirements the earlier rounds did not anticipate: retries, then concurrent
workers with crash recovery, then an ordered transition log and a live count
view. The arms differ in exactly one variable, the `CLAUDE.md` installed in the
project directory.

| arm | CLAUDE.md |
| --- | --- |
| `control` | none |
| `incumbent` | Nathan's own, plus its two `@`-referenced files |
| `general` | `bundle/DISTILLED.md` |
| `flavored` | `$FLAVORED`, default `bundle/DISTILLED-FOUNDATIONS.md` |

The score is line survival. Of the lines a round wrote, how many are still
standing at the end? A round-1 survival of 30% means the initial representation
was wrong for requirements that had not arrived yet and later rounds paid to
undo it. High survival means the design absorbed the change. That is the
property every claim in these documents is ultimately about, and it is the one
thing here that is objective rather than a matter of taste.

Read `analyze.py` before trusting the number. It excludes `.md` files so the
treatment and the README are not scored as work product, and it attributes
surviving lines with `git blame` against the final tree.

## Running it

The global `~/.claude/CLAUDE.md` must not contaminate the arms, so each arm gets
an isolated `CLAUDE_CONFIG_DIR`. That directory carries credentials as well as
memory, so `run.sh` copies `~/.claude/.credentials.json` into it. Nothing else
is copied, which is what suppresses the global memory while staying logged in.

`--bare` also suppresses the global file, but it disables LSP, hooks and plugins
and would measure a differently-capable agent than the one being evaluated. Use
the config-dir route.

```sh
export BENCH_ROOT=/tmp/distill-bench
for arm in control incumbent general flavored; do
    tools/bench/run.sh "$arm"
done
python3 tools/bench/analyze.py "$BENCH_ROOT"
```

Arms are independent and can run in parallel.

## Cost

Sixteen unattended Opus sessions, each a real coding round with tests. Budget
roughly 2-5M tokens for a full run. Pilot with `MODEL=claude-sonnet-5` first to
shake out the harness, then re-run on Opus for the result that counts. Swap the
fourth arm with `FLAVORED=DISTILLED-LISP.md` to test a different document.

## Caveats worth stating before anyone quotes a number

One task in one language. A job queue rewards the state and invariant material
and barely exercises the language-design claims, so a flavored arm losing here
is evidence about this task, not about that document.

`run.sh` uses `--dangerously-skip-permissions` because the run is unattended.
Every arm writes only inside `$BENCH_ROOT`.

A single run per arm is an anecdote. Model output varies between runs, and the
survival differences that matter are probably smaller than that variance, so
repeat each arm several times with different seeds before believing an ordering.
