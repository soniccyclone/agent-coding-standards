---
type: project-state
title: Good Programming Corpus — Live State
description: Running scoreboard of open threads while we argue this out. Update in place each session; don't let resolved points get re-litigated, don't let open ones get quietly dropped.
tags: [state, church-turing, occam, copyright, okf, canon]
---

# Project State

Read order: [primer.md](primer.md) (standing rules) → [good-programming-corpus-overview.md](good-programming-corpus-overview.md)
(project shape, format, figure ledger) → [church-turing-primitives-debate.md](church-turing-primitives-debate.md)
(frozen transcript, why §5's default exists) → this file (source of truth —
decisions and why) → [technical-plan.md](technical-plan.md) (how those decisions
become a phased, fan-out-able build pipeline).

This file is the one expected to keep changing shape as we argue. The debate
transcript is history — don't edit it, don't re-derive it, cite it.
Execution mechanics (phases, fan-out units, bundle directory layout) live in
technical-plan.md now — don't duplicate pipeline detail here, link to it.

## Threads

### 1. Primitive-count axis, Church vs Turing — RESOLVED (narrow claim)
Under the primitive-count axis specifically, two-primitive lambda calculus beats
four-plus-primitive TM by default, absent a stated axis to the contrary. Settled
in the transcript, including the geocentrism/heliocentrism parallel and the
"state is just address-indexed data" response to the state-density objection.
Not up for re-argument.

**Still open inside this thread:** the transcript itself flags the physical
Church-Turing thesis / Landauer counter — computation is physically realized as
matter undergoing state transitions, so mechanism could be ontologically prior
to any calculus describing it — as "a live counter-argument, not fully defeated
here." That's a real crack, not a formality. Worth a dedicated round before
treating §5 as load-bearing for anything past the narrow primitive-count claim.

### 2. Does the primitive-count default license rejecting Turing-style *figures*? — RESOLVED
Not a peer-axis split (the two-axis compromise floated earlier is withdrawn).
Resolution is a hierarchy, not a truce: lambda calculus is the pure theory of
computation; the Turing-machine lineage is the implementation target that pure
thought gets mapped *down onto*, not a competing first-order way of thinking
about programming. Design thought happens in Church-style terms — composition,
substitution, small primitive basis. The mechanism layer (cache locality,
register allocation, concurrency, the whole Turing-lineage systems corpus) is
real and necessary, but it's the compilation target, not the source of good
abstractions.

**Core thesis (Nathan's, the project's actual spine):** thinking about
programming in Church/Lisp-style terms produces *better abstractions*, and
better abstractions produce two concrete, checkable outcomes — higher
development velocity (expression stays close to thought, so there's less
translation loss between intent and code) and a smaller primitive surface that
formal static analysis can actually reason over, enabling optimization the
implementation layer couldn't find on its own. Net claim: this produces more
stable codebases, faster, than starting from Turing-style mechanism-first
thinking. This is an instrumental/empirical claim, not just an axiomatic
preference — which is a feature, since it means individual `lesson` files
derived from it are checkable against real cases as the bundle grows, not just
asserted. Primary text anchor: SICP — substitution-model-first design, procedures
as abstractions, and the final chapters' explicit mapping of the pure evaluator
down onto a register machine are the worked example of exactly this hierarchy.

**Resolving tension (first entry for the bundle's `tension` type once McCarthy
and Russell are formally ingested):** McCarthy → Russell. Lisp doesn't trace
*directly* to lambda calculus, but is unambiguously in its lineage. Russell (to
be added to the figure queue) is the case study for how to hold the hierarchy
correctly: understanding exactly which trade-offs are required to bring the
purity of computational thought into mechanically implemented reality, without
mistaking the mechanical mapping for the source of the thinking. This is the
resolution pattern thread 4's `tension` type exists to capture — apparent
conflict (Church vs. Turing as competing philosophies) dissolved by recognizing
they operate at different layers (design thought vs. implementation target),
not by picking a winner.

Practical consequence for vetting: Dijkstra/Hoare/Kernighan/Pike/Lampson etc.
aren't rejected by this — they get vetted and placed at the implementation-mapping
layer of the corpus (how pure form compiles onto real mechanism) rather than
the design-thought layer that determines abstraction quality. Layer placement,
not rejection, is the outcome of the gate now.

### 3. Scope and copyright of ingestion — RESOLVED (publish is the intent, not a maybe)
Publishing is the actual goal, so the posture is built for that from the start
rather than "safe privately, revisit later":

- **Public sources only.** If a figure's best material lives in a paywalled or
  DRM'd work (TAOCP included), don't ingest that work into the publishable
  bundle. Use their freely available papers, arxiv preprints, essays, talks,
  interviews, and public repos instead. For Knuth specifically: skip TAOCP,
  use his published papers and essays (arxiv and elsewhere) — the literate
  programming philosophy, the algorithm-analysis discipline, "premature
  optimization" itself, are all in freely accessible material, not locked
  behind the book. If a figure genuinely has no adequate public-source lesson,
  that figure's lesson gets skipped or flagged, not sourced from a paywalled
  book anyway.
- **Lessons are abstract, never technique-level.** Every `lesson` file answers
  "what does this teach about *how to think* about programming," not "here is
  a paraphrase of what they built or wrote." No copy-paste, ever, of any
  length — not code, not prose, not close paraphrase. This isn't just a
  copyright hedge: methods, ideas, and ways of thinking are the one thing
  copyright never covers (17 U.S.C. § 102(b)) — expression is what's
  protected, and abstract lessons by construction don't carry the source's
  expression forward. That's a stronger position than "distill carefully,"
  it's "the content category itself sits outside protection."
- Citations (figure, work, link) stay on every lesson regardless — citation
  isn't a copyright requirement here, it's intellectual honesty and lets a
  reader go verify the lesson against the source.

### 4. OKF `type` taxonomy — RESOLVED
Five types, fixed: `figure` (person), `work` (paper/essay/talk/repo, public-source
only per thread 3, attributed to a figure), `lesson` (abstract lesson — how to
*think* about programming, never technique/expression-level — cross-linked to
the figure and the axis it scores on), `axis` (one concept file per optimization
axis from primer.md §2, so every lesson has something concrete to link against
and the lint pass can flag lessons that cite none), `tension` (unresolved
cross-figure disagreement — included from the start, not deferred: Nathan
expects a lot of these given the author list already in mind, e.g. a future
Dijkstra-vs-Knuth-on-goto conflict).

Tensions get a resolution path, not just a record. Each `tension` file carries
a `status: open | resolved` field; when Nathan walks through resolving one
(most are expected to already be resolved in his own thinking via some
abstraction that dissolves the apparent conflict — the tension file captures
that reasoning, not just restates the disagreement), the resolution gets
written into the file itself. Once there's a meaningful number resolved, the
bundle gets a root-level `resolutions/index.md` (or equivalent) surfacing them
as a standalone synthesis — plausibly the most novel piece of the whole corpus,
since it's not "what did figure X say" but "here's where two lines of good-programming
thinking looked like they conflicted, and here's the abstraction that shows
they didn't." Exact resolutions-section shape (separate directory vs. an index
view over `tension` files) deferred until there are enough tensions logged to
know which structure actually reads better.

Doc-level types already in use (`reasoning-primer`, `project-overview`,
`discussion-log`, `project-state`) are a separate vocabulary for
`docs/planning/` and don't leak into the bundle's.

### 4a. Author worldview context — RESOLVED, process note (not a bundle field)
When we walk the figure list, each figure gets a worldview/belief-system note
(with a confidence flag when the record's thin or disputed) appended in
conversation for Nathan's own reading context — not written into any OKF
`figure` file, not a schema field, not used to disqualify or weight anyone.
Explicitly not the religious-vetting-axis proposal raised and dropped earlier
in this thread — that's still off the table for the bundle itself. This note
exists purely so Nathan can hold a figure's stated worldview in mind while
reading findings; it has no effect on what gets ingested or how a lesson scores.

### 5. Final deliverable shape — CONFIRMED
Two artifacts. Build the full OKF bundle first — one file per figure/work/lesson,
browsable, cited, this is the wiki per the Karpathy ingest/query/lint pattern.
Distill the short `@`-referenceable guidance doc from the bundle afterward, once
there's enough bundle to distill from. Don't build them in parallel.

## Figure ledger
Authoritative copy lives in [good-programming-corpus-overview.md](good-programming-corpus-overview.md#status-of-figures-discussed-so-far).
Don't fork a second copy here — update that section and link to it.

## Next session checklist
- [ ] Fold thread 2's hierarchy resolution (design-thought layer vs.
      implementation-mapping layer) and thread 3's rules (public-source-only,
      abstract-lesson-only, no copy-paste at any length) into primer.md as
      standing rules — they govern every future ingest, shouldn't live only
      in this state file.
- [ ] Add McCarthy and Russell to the figure queue; McCarthy→Russell is the
      first `tension`+resolution pair once ingestion starts.
- [ ] For each figure Nathan stages, confirm a public-source reading list exists
      before vetting — if it doesn't, that's a reason to flag the figure, not
      to reach for a paywalled work anyway.
- [x] Thread 2 (figure-rejection inference gap) — resolved: hierarchy, not
      rejection; Turing-lineage figures land at the implementation layer.
- [x] Thread 4 (type taxonomy) — resolved: figure, work, lesson, axis, tension.
- [x] Thread 5 (deliverable shape) — confirmed: full bundle, then distill.
