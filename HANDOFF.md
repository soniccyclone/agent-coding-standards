# Handoff

For an agent picking this repo up on a different machine with no memory of the
work. Read this file first, then `docs/planning/technical-plan.md`. Written
2026-08-07.

## What this is

A corpus of 95 computer-science figures, their works, and abstract **lessons**
extracted from those works — claims about *how to think*, never summaries, zero
copy-paste. Everything lives under `bundle/`. The planning docs under
`docs/planning/` are the project's memory and are more important than they look;
several of them exist specifically to stop a future agent repeating a mistake.

The shipped artifacts are the `bundle/DISTILLED*.md` files. Those are what a user
pastes into their own `CLAUDE.md` to make their coding agent work better. They are
written for **other people**, not for Nathan — his own `CLAUDE.md` is the thing
this project is trying to beat, not a constraint to fit inside.

## State as of 2026-08-07

Phases 1 through 7 are closed. Phase 8 is untouched by instruction. Phase 9 is
open with 12 items.

- 95 figures, 450 works, 2,950 lessons, 21 resolved tensions
- 446/450 works carry `extraction: complete`; the other 4 have no obtainable
  source and are marked `SOURCE-UNOBTAINABLE`
- `python3 tools/lint.py` reports CLEAN
- Seven distilled documents exist: the general `DISTILLED.md` plus flavored
  companions for LISP, TYPES, VERIFICATION, UNIX, MODULARITY, COMPLEXITY

## The one outstanding work item

**`bundle/DISTILLED-FOUNDATIONS.md` was never written.** Its agent died three
times to connection errors without producing a file. Everything else in the
tradition series landed.

Figures: turing, godel, post, kolmogorov, church, chaitin, rabin, kleene, peter,
hilbert, hartmanis. The brief that produced the other six is reproduced in
`docs/planning/phase7-lisp.md` in substance; the shape is:

> One agent, holding the whole tradition, no chunking and no subagents. Read
> `DISTILLED.md` and `DISTILLED-LISP.md` first and do not duplicate them — LISP is
> the model for register and for turning a stance into tests a reader can run.
> Read the `## Lessons` rollup in `bundle/figures/<name>/index.md` for every figure,
> then scan lesson titles and read the decision-changing ones in full. Target
> 1,200–1,500 words, every claim attributed inline, plain prose, no bulleted lists
> of bolded phrases. Write incrementally — agents die constantly and only what is
> on disk survives.

The stance to hand it, as a starting hypothesis it should feel free to reject:
some questions have no procedure that answers them, some objects are irreducibly
complex, and knowing which is which changes what you attempt. Resist writing a
theory lecture; every claim must cash out in a decision an ordinary service
developer could make.

## Standing instructions from Nathan — these do not change

1. **Never `git commit --amend`.** History rewriting is his call. Corrections go
   in a new commit or in the planning docs. This is a standing preference.
2. **Commit freely, but do not push unless asked.** He asks when he wants it.
3. **Do not start Phase 8.** Ideas backlog only.
4. **Read the whole source.** No page budgets, no sampling the important parts —
   guessing which parts matter introduces bias drift.
5. **Do not hand-edit `bundle/axes/*.md` or `bundle/subdomains/*.md`.** They are
   generated. See "what was lost" below.

## Lessons that will bite you, in order of how much they cost

**Diagnose from disk, never from a workflow's return value.** This has held every
single time it came up, and the last instance was the most extreme: a workflow
reported `0 returned, 6 died` after burning 2M tokens, and three complete,
correct documents were sitting on disk. The agents had written everything and
died at the return step. Had the return been trusted, six agents would have been
relaunched to redo finished work. Always `ls` and read the files.

**Workflow resume did not replay from cache.** Documented behaviour says
unchanged agents replay; in practice all six re-ran and all six died. Prefer a
fresh, narrowly-scoped run over a resume, and prefer a single `Agent` call over a
workflow when only one unit of work is left.

**Large structured output stalls agents.** Three reviewers stalled for six
retry attempts each returning an 80-element verdict array. The fix that works
everywhere on this project: have the agent **write a file** and return a small
count. Every agent that wrote files succeeded; every agent returning a big array
died.

**Never encode prevalence as a quality filter.** The Phase 7 strike prompt
included "it only bites in a specialist context most codebases never enter". That
is self-defeating here — the corpus exists *because* most code is bad, so "most
codebases never do this" is evidence *for* a claim. Combined with the other test
it formed a pincer that only admitted claims near median practice. It measurably
ate Gödel, Rabin, Curry, Kleene, Scott, Church and Sussman. The criterion is
deleted; the surviving distinction is **transferability, not prevalence** — a
claim must survive translation into an ordinary service in a mainstream language,
but need not be something people currently do. Full write-up in
`docs/planning/phase7-selection.md`.

**Slice by tradition, not by subdomain.** The first distillation fanned out ten
agents by subdomain and lost whole traditions, because a tradition is a stance
that cuts across every subdomain — sliced nine ways it belongs to none and every
fragment looks minor. Worse, each fragment gets judged through whatever lens the
reviewer already holds, and almost all training code is Algol-descended, so that
lineage's instincts arrive feeling like neutral engineering judgement. One agent
holding one tradition whole is what fixed it.

**A quiet monitor means the monitor is wrong.** Also every time.

**`extraction: complete` does not mean the same thing everywhere.** Four
confidence tiers, documented in `docs/planning/phase4-flags.md` H.8 and H.10.
Tier 4 means "attested on the union of several passes' notes, no single reader saw
the whole work". Do not launder these.

**A coverage note's position line is a floor, not a fact.** The trustworthy record
is the set of sections named in the `**Source:**` lines of the lessons citing that
work.

## What was lost in the handoff, and what to do about it

The previous session's tooling lived in a session-scoped temp directory that no
longer exists. Only `tools/lint.py` was in the repo and survived.

- **`integrity.py`** — gone, but `tools/lint.py` covers its checks and more.
  Run `python3 tools/lint.py`; it takes `--quiet` and exits 1 on findings.
- **`rebuild-backlinks.py`** — gone. It regenerated the 15 shared
  `bundle/axes/*.md` and `bundle/subdomains/*.md` backlink files from lesson
  frontmatter. Those files are currently correct and lint-clean, so you only need
  to rewrite it **if you add or retag lessons**. When you do: it must match
  `^title: "(.*)"` with double quotes, because single-quoted titles silently fall
  back to filename stems and produce lessons that appear in every shared index
  under the wrong name. That bug shipped once.
- **Phase 7 raw JSON** (candidates, verdicts, tally) — gone, but the full kill
  list with every reviewer's reasoning survives in readable form in
  `docs/planning/phase7-selection.md`.

## Open decisions for Nathan, not for you

- **Whether to regenerate `DISTILLED.md`.** The argument against merging the
  tradition documents back into one: merging re-applies majority pressure, and
  majority pressure is exactly what flattened the traditions the first time. The
  proposed alternative is a lean cross-tradition core plus the flavored
  companions. Not yet decided.
- **Document lengths run over target.** DISTILLED 1,683, COMPLEXITY 2,137, UNIX
  1,840, MODULARITY 1,675 against a stated 1,200–1,500. Flagged rather than
  trimmed unilaterally.
- **Benchmarking.** He plans to judge outputs himself by feeding different
  documents as `CLAUDE.md` and comparing. Use `CLAUDE_CONFIG_DIR` pointed at a
  scratch dir to suppress the global `CLAUDE.md` while keeping LSP alive — note
  `--bare` also works but disables LSP, hooks and plugins, which he does not want.
  Use `--append-system-prompt-file`, never `--system-prompt-file`; the latter
  *replaces* Claude Code's system prompt and would measure a different thing.
  He wants a chunkier task than a toy app, with sequential requirements added over
  rounds, since every claim in these documents is about whether a design absorbs
  change or fights it.

## Phase 9

Twelve known, specific gaps are queued in `docs/planning/technical-plan.md` under
Phase 9. It is deliberately distinct from Phase 6: Phase 6 finds problems
mechanically, Phase 9 holds problems already found and named, each recorded with
how it was found. The first three are extraction gaps where a conflict is real in
the source texts but only one side was ever ingested — Cox's rebuttal of Brooks,
Knuth's side of the goto argument, and Russell's absence from the figure set.
