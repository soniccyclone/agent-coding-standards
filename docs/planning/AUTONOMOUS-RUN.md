---
type: execution-plan
title: Standing Orders for an Unattended Run
description: What an agent should do when it wakes up in this repo with no human present. Written 2026-07-31 before a ~12h unattended window; read this first, then act.
tags: [execution, okf, autonomous, standing-orders]
---

# Standing Orders for an Unattended Run

**If you are a fresh agent that was just started by the keep-alive job, read this
whole file before doing anything.** You have no memory of the conversation that
created it. Everything you need is here or in the docs it points at.

Nathan authorised an unattended run on 2026-07-31 covering Phases 4 through 7. He
is away for roughly twelve hours. He explicitly said: resolve Phase 5 tensions on
your own judgement rather than waiting for him, and mark every such decision so he
can overturn it later.

## Ground rules that do not change

1. **Never `git commit --amend`.** History rewriting is Nathan's call. If a past
   commit message is wrong, record the correction in a new commit or in the
   planning docs. This is a standing preference, not a situational one.
2. **Commit constantly. Push after every commit during this run.** Nathan is not
   here to sync. Work that is not pushed does not exist.
3. **Do not start Phase 8.** Ideas backlog only; he said leave it alone.
4. **Do not touch `bundle/axes/*.md` or `bundle/subdomains/*.md` by hand.** Those
   15 files are rebuilt mechanically by `scratchpad/rebuild-backlinks.py --write`.
   Concurrent hand edits corrupt them.
5. **Write incrementally.** Every agent that died this session lost only what it
   had not yet written. Never batch up work to save at the end.
6. **Read the whole source.** No page budgets, no sampling "the important parts".
   Guessing which parts matter introduces bias drift.

## Order of work

Do these in order. Do not skip ahead; later phases depend on earlier ones.

### 1. Finish Phase 4
Check state first:
```
python3 scratchpad/integrity.py
```
A work is done when its frontmatter carries `extraction: complete`, or it carries
`SOURCE-UNOBTAINABLE` (four works have no obtainable source — see flags H.7).

To find what is left:
```
grep -L 'extraction: complete' bundle/figures/*/works/*.md | xargs grep -L SOURCE-UNOBTAINABLE
```
Book-length works are read by launching a subagent per figure with the workflow
script at `scratchpad/p4-ocr-fanout.js`. Agents die constantly to connection
drops; that is normal and not a reason to change approach. What matters is that
each one writes a coverage note with a resume line number **before** it starts
reading, so the next agent resumes instead of restarting.

### 2. Phase 4 closeout
- Repair any integrity findings (`integrity.py --repair`).
- Rebuild shared indexes (`rebuild-backlinks.py --write`).
- Write the figure rollup (`## Lessons` prose in `bundle/figures/<fig>/index.md`)
  for every figure that has lessons but no rollup. `integrity.py` lists them.
  Match the voice of an existing one — `bundle/figures/brewer/index.md` is a good
  model: one dense paragraph, ~250 words, synthesising how that figure thinks.

### 3. Phase 5 — tension pass
See `docs/planning/technical-plan.md` §Phase 5 for the spec. In summary: find
places where two figures' lessons genuinely contradict, open a `tension` file per
real conflict, and record it in ledger.md's tension index.

**Nathan's instruction for this run: resolve them yourself.** Do not leave them
`status: open` waiting for him. But every resolution must be unmistakably marked
as an agent decision so he can review and overturn:

- Set `status: resolved-by-llm` (not `resolved`).
- Include a `**LLM DECISION — Nathan may overturn.**` line at the top of the
  resolution section, stating what was decided, the reasoning, and what the
  strongest counter-argument was.
- Add the tension to the ledger index with the same marker.

Candidate tensions already spotted during extraction are listed in
`docs/planning/phase4-flags.md` section D. Start there, then look for more.

A real tension is two figures giving incompatible advice about the same decision,
not merely different emphasis. Being wrong about what counts as a tension is
cheap; inventing one to hit a quota is not.

### 4. Phase 6 — lint pass
`scratchpad/integrity.py` already covers much of it. The full check list is in
technical-plan.md §Phase 6. Output is a punch list, not bundle content — write it
to `docs/planning/phase6-lint.md`.

### 5. Phase 7 — distillation
Derive the short `@`-referenceable document that **replaces** CLAUDE.md's content.
Start from the root rollup `bundle/index.md`, which has been a running draft since
Phase 1 — this is a refinement, not a from-scratch synthesis. See
technical-plan.md §Phase 7 and project-state.md §5.

**Do not overwrite Nathan's CLAUDE.md.** Write the artifact to
`bundle/DISTILLED.md` and tell him it is ready to swap in. Replacing his global
instructions unasked is exactly the kind of irreversible, outward-facing change to
leave for him.

## Things that will bite you

- **Bash may become unavailable** mid-run (classifier outages happened repeatedly
  on 2026-07-31). Read/Write/Edit keep working. Wait and retry rather than
  redesigning around it.
- **`survey_text_layer: ocr`** means a prepared transcript exists at the path in
  the work file's `**Reading copy:**` line. Read that, not the PDF. Prose is
  reliable; **notation is not** — never transcribe a formula from an OCR text.
- **`full` does not mean born-digital.** Some PDFs carry someone else's OCR layer
  with the same notation-mangling and no marker.
- **The workflow return value undercounts badly.** It only captures agents that
  survived to return. Always measure the corpus on disk, never the return value.
- **A quiet monitor means the monitor is wrong**, not that nothing happened. This
  has been true every time it came up.
- **A coverage note's position line is a floor, not a fact.** Three separate agents
  proved this on 2026-07-31. On `wirth/project-oberon` the line read 22341 while the
  whole of chapter 14 had already been mined — six lessons cited it. On
  `hoare/communicating-sequential-processes-book` the prior pass had read ~400 lines
  past what it recorded. **The trustworthy coverage record is the set of sections
  named in the `**Source:**` lines of the lessons that cite the work**, not the
  hand-written position line. Before resuming any partially-read work, audit the
  Source lines first and tabulate which sections are already represented; that is
  what actually locates the resume point. Doing this saved a full re-read of a
  chapter on Project Oberon.

## Confidence tiers — do not silently launder these

`extraction: complete` does not mean the same thing everywhere. Four tiers exist,
documented in `phase4-flags.md` H.8 and H.10. Tier 4 in particular means "attested
on the union of several passes' coverage notes, no single reader saw the whole
work". If you attest something on the strength of a prior pass's note rather than
your own reading, say so in the coverage note.

## When you finish, or run out of things you may do

Write a status summary to `docs/planning/RUN-REPORT.md` — what completed, what
did not, what needs Nathan. Commit and push it. Then stop. Do not invent new scope.
