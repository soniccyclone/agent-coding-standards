---
type: execution-plan
title: Good Programming Corpus — Technical Plan
description: Phased build pipeline for the OKF bundle. Structure only — no authors, subdomains, or source lists filled in yet. Each phase states its fan-out unit so it can be tasked out in parallel (bd/beads).
tags: [execution, okf, pipeline, fan-out]
---

# Technical Plan

Read order: [project-state.md](project-state.md) (decisions and standing rules —
source of truth for *why*) → this file (*how* those decisions become work).
This doc doesn't re-argue anything; every rule below just cites the
project-state.md thread that settled it. If a phase here seems to contradict a
thread, the thread wins and this file is wrong and needs fixing.

Nothing in this file is content yet — no author names, no subdomain list, no
source links. It's the pipeline shape so we can argue about *that* before
either of us spends a token filling it in.

## Bundle target structure

The OKF bundle this pipeline builds toward (directory layout, not decided
content):

```
bundle/
├── index.md
├── log.md                  # chronological ingest audit trail, per Karpathy pattern
├── axes/
│   ├── index.md
│   └── <axis>.md            # one per primer.md §2 axis, fixed set, authored once
├── figures/
│   ├── index.md
│   └── <figure>.md          # type: figure
├── works/
│   ├── index.md
│   └── <figure>/<work>.md   # type: work, nested under owning figure
├── lessons/
│   ├── index.md
│   └── <lesson>.md          # type: lesson, links figure + work + axis
├── tensions/
│   ├── index.md
│   └── <tension>.md         # type: tension, status: open|resolved
└── resolutions/
    └── index.md              # synthesis view over resolved tensions (shape TBD, see PS thread 4)
```

## Standing rules this pipeline enforces (pointers, not restatements)
- Types fixed at five: `figure`, `work`, `axis`, `lesson`, `tension` — [project-state.md §4](project-state.md#4-okf-type-taxonomy--resolved).
- Public sources only, no paywalled/DRM'd works ingested into the bundle — [§3](project-state.md#3-scope-and-copyright-of-ingestion--resolved-publish-is-the-intent-not-a-maybe).
- Lessons are abstract (how to *think*), never technique/expression-level; zero copy-paste at any length — [§3](project-state.md#3-scope-and-copyright-of-ingestion--resolved-publish-is-the-intent-not-a-maybe).
- Vetting outcome is layer placement, not reject/accept — every figure lands at
  the design-thought layer or the implementation-mapping layer (or both) — [§2](project-state.md#2-does-the-primitive-count-default-license-rejecting-turing-style-figures--resolved).
- Worldview is a conversational note during vetting, never a bundle field —
  [§4a](project-state.md#4a-author-worldview-context--resolved-process-note-not-a-bundle-field).
- Bundle first, distilled `@`-referenceable doc second, not in parallel — [§5](project-state.md#5-final-deliverable-shape--confirmed).

## Planning/execution boundary

Everything up to and including this line happens in `docs/planning/*.md` — the
four argument docs (primer, overview, debate transcript, project-state) plus
this plan. **Phase 0 is the seam.** From Phase 0 onward, work stops being
"argue in markdown about the project" and starts being "generate real OKF
files in the bundle." Nothing before Phase 0 produces a `figure`/`work`/
`lesson`/`axis`/`tension` file; nothing from Phase 0 on modifies the four
planning docs except to log status (figure ledger updates, thread edits if a
later phase surfaces something that reopens a decision).

Bundle root isn't pinned down yet — assuming top-level `bundle/` at the repo
root (sibling to `docs/`, not nested under `docs/planning/`), since an OKF
bundle is meant to be portable/shippable on its own rather than living inside
the argument-docs tree. Flag if that's wrong before Phase 0 runs; the tree
diagram above and everything downstream assumes it.

## Pipeline

Each phase lists a **fan-out unit** — the thing that gets split into parallel
tasks — so phases map directly onto bd/beads tickets without restructuring.

### Phase 0 — Bundle scaffolding
**Fan-out unit:** none, one-time setup.
**Do:** create the directory structure above; write the six `axis` files from
primer.md §2 (expressiveness, verifiability, parallelizability,
hardware-affinity, cognitive load, primitive-count) — fixed, small, and a hard
dependency for Phase 4, so it happens before any figure work starts.
**Output:** empty bundle skeleton + populated `axes/`.
**Depends on:** nothing.

### Phase 1 — Author discovery (fan-out by CS subdomain)
**Fan-out unit:** one CS subdomain per task.
**Do:** for each subdomain, produce a candidate author list (name, rough
era/lineage, why they're a candidate). Subdomain taxonomy itself is a Phase 1
output, not a precondition — first task under this phase is drafting that
list.
**Output:** candidate roster, unvetted. No `figure` files yet — candidates
aren't figures until Phase 2 accepts them.
**Depends on:** Phase 0 (scaffolding, not content).

### Phase 2 — Vetting (sequential, Nathan-in-the-loop)
**Fan-out unit:** one candidate figure per pass — not parallelizable the same
way as the others, since layer placement and tension-spotting need live
judgment, not independent agent runs.
**Do:** run each candidate through the primer.md gate; assign layer placement
(design-thought / implementation-mapping / both, per §2); note worldview
conversationally per §4a (not written to the file); flag any immediately
visible tension against an already-accepted figure.
**Output:** `figure` file created for each accepted candidate, with layer
placement in frontmatter. Rejected candidates logged in the figure ledger
(project-state.md → good-programming-corpus-overview.md) with reason, not
silently dropped.
**Depends on:** Phase 1 roster.

### Phase 3 — Source discovery (fan-out per accepted figure)
**Fan-out unit:** one accepted figure per task. This is the phase Nathan named
directly — parallel per-author pull of the full public-source list.
**Do:** for each accepted figure, enumerate every publicly accessible
whitepaper, essay, talk, interview, or repo (arxiv, personal sites, publisher
open-access copies, conference proceedings, public GitHub) with a direct link.
No paywalled/DRM'd sources per §3 — if a figure's material only exists
paywalled, flag it, don't substitute a summary of it.
**Output:** one `work` file per source, nested under its figure, link-only —
no content extraction yet.
**Depends on:** Phase 2 (can start per-figure as soon as that figure clears
vetting, doesn't need to wait for the whole roster).

### Phase 4 — Lesson extraction (fan-out per work)
**Fan-out unit:** one `work` per task (or batched per figure if a figure has
many small works).
**Do:** read the source, extract abstract lesson(s) — how it teaches someone to
*think* about programming, cited back to the work, linked to the `axis` file(s)
it scores on. Zero reproduction of source text per §3.
**Output:** `lesson` files, cross-linked to figure + work + axis. A work with no
distinct lesson beyond what's already captured gets marked read-no-new-lesson,
not skipped silently.
**Depends on:** Phase 0 (axis files must exist to link against), Phase 3 (per-work).

### Phase 5 — Tension pass
**Fan-out unit:** loosely parallelizable for *spotting* candidate tensions
(e.g. one pass per subdomain or per pair of figures with overlapping axes);
**resolution itself is sequential and Nathan-guided**, same reasoning as Phase 2.
**Do:** scan accumulated lessons for cross-figure contradiction; open a
`tension` file (`status: open`) per real conflict found; Nathan walks through
resolution per the pattern already modeled for McCarthy→Russell in
project-state.md §2; resolution gets written into the file, `status: resolved`.
**Output:** `tension` files, increasingly `resolved` over time. Feeds
`resolutions/index.md` once there's enough of them (shape still TBD per §4).
**Depends on:** Phase 4 (needs lessons to find contradictions between).

### Phase 6 — Lint pass
**Fan-out unit:** none, single mechanical sweep, but cheap to re-run — not a
one-time phase, a recurring check.
**Do:** Karpathy-pattern lint — orphaned files (no inbound links), lessons
citing no axis, figures with no lessons, dead source links, open tensions that
have gone stale.
**Output:** punch list, not bundle content.
**Depends on:** whatever's been built so far; re-run after every batch of
Phases 3-5 work lands, not just once at the end.

### Phase 7 — Distillation
**Fan-out unit:** none, single synthesis pass.
**Do:** derive the short `@`-referenceable CLAUDE.md-replacement doc from the
full bundle, once there's enough bundle to distill from — per §5, this
replaces the current CLAUDE.md content, doesn't sit alongside it.
**Output:** the actual pluggable guidance doc — the deliverable everything else
was in service of.
**Depends on:** Phases 3-6 substantially complete, at least for the first
distillation pass; can re-run distillation as the bundle grows.

## Open before Phase 1 can start
Nothing blocking — Phase 0 has no content dependencies and Phase 1's first
task (drafting the subdomain taxonomy) is self-contained. Flag here if that
changes.
