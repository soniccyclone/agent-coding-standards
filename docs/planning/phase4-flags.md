---
type: execution-plan
title: Phase 4 Flag Backlog
description: Punch list from Phase 4 lesson-extraction agents — Phase 3 data errors found by reading the real sources, Phase 5 tension candidates, and sourcing notes worth keeping. Live doc; entries get struck as they're resolved.
tags: [execution, okf, phase-4, lint, punch-list]
---

# Phase 4 Flag Backlog

Phase 4's agents are the first pass in this project to read the actual source
texts end to end. That turned them into an unplanned audit of Phase 3's
metadata: every entry below was found by comparing a `work` file's claims
against the document it points at. Kept as a live punch list rather than
folded into ledger.md, because most items are per-file corrections and the
Phase 6 lint pass is their natural consumer.

Status key: `[ ]` open · `[x]` applied · `[?]` needs Nathan's judgment.

## A. Work-file data errors (agent-verified against the real source)

- [x] **abrial** / `formal-methods-in-industry-achievements-problems-future.md` —
  description claims the talk surveys "Z, B, and by extension the emerging
  Event-B." The paper never discusses Z; §2 explicitly narrows to the B method
  alone, and Event-B appears only as a forward reference to a then-forthcoming
  book. Rewritten to name the two Siemens driverless-rail cases (Paris Métro
  line 14, Roissy shuttle).
- [x] **boehm** / `a-view-of-20th-and-21st-century-software-engineering.md` —
  description attributed a "helpful and hard to overdo / helpful up to a point /
  primarily situation-dependent" trichotomy and a COCOMO synthesis to this
  paper. None of the three phrases appears in it (that sort is from other Boehm
  writing). Rewritten to the paper's real shape: a decade-by-decade
  thesis/antithesis/synthesis reading of the field, closing with per-decade
  timeless principles versus aging practices.
- [x] **booch** / `the-promise-the-limits-and-the-beauty-of-software.md` —
  `year: 2011` was taken from the YouTube upload date. Four independent
  internal datings put the talk in 2007: Booch refers to giving the BCS Turing
  Lecture "earlier this year" (2007), to interviewing Backus "last year" and to
  Backus being dead (died March 2007), to anticipating Halo 3's release
  (September 2007), and to his 2006 heart surgery as "a year ago." Corrected to
  2007 with a note that the upload postdates the talk.
- [x] **chaitin** / `on-the-length-of-programs-for-computing-finite-binary-sequences.md`
  — recorded as JACM 16(1), 1969, pp. 145-159, but the PDF at the URL is the
  1966 original, JACM 13(4), pp. 547-569. JACM 16(1) is the *sequel*
  ("...: Statistical Considerations"). Corrected to 1966 to match the artifact.
- [x] **chaitin** / `an-invitation-to-algorithmic-information-theory.md` — lecture
  located at the University of Auckland; the transcript's own header says the
  talk was given 24 April 1996 at a University of **New Mexico** CS colloquium.
  Auckland is the *host* of the copy (Calude's page), which was the source of
  the confusion. Corrected.
- [x] **brinch-hansen** / `the-nucleus-of-a-multiprogramming-system.md` — page
  range `238-241`; the PDF's own copyright footnote reads CACM 13(4), April
  1970, **238-242**. Corrected.
- [x] **brinch-hansen** / `structured-multiprogramming.md` — description framed
  the paper as arguing "in the same spirit as the structured-programming case
  against goto." The paper makes no goto analogy; its comparisons are
  cobegin/coend against fork/join and conditional critical regions against
  semaphores. Interpretive claim removed.
- [x] **chuck-moore** / `forth-a-language-for-interactive-computing.md` —
  description credits the 1970 Mohasco paper with a "threaded-code
  interpreter." The paper has no threaded code: definitions store the source
  character string and the scanner re-interprets that text. Moore's own
  retrospective dates indirect-threaded code to NRAO in 1971, after this paper.
  Corrected to "text-interpreting definitions."
- [x] **corbato** / `introduction-and-overview-of-the-multics-system.md` —
  description attributes an enumerated nine-design-goals list to this 1965
  kickoff paper. That list is in the 1972 retrospective; the 1965 paper argues
  objectives in prose. Corrected.
- [x] **corbato** / `multics-the-first-seven-years.md` — description says it
  "candidly assesses where the system met its original ambitions and where it
  fell short." The paper claims substantial progress toward all nine goals with
  none importantly compromised; its actual candour is about the unanticipated
  design-iteration phase and day-to-day crash statistics. Corrected.
- [x] **cox** / `what-if-theres-a-silver-bullet.md` — description claims the
  essay "warns that whoever builds that marketplace first gains a durable
  competitive advantage." The body never argues this. Its real contribution is a
  Copernican framing of paradigm shift plus the argument that incumbent
  practitioners are bystanders while consumers drive the change. Corrected.
- [x] **chen** / `index.md` — top-10 list still marked work 2 ("English Sentence
  Structure and Entity-Relationship Diagrams," 1983) as `paywalled`, though the
  work file resolved it to a self-archived LSU copy and reads `access: public`.
  Re-verified live (HTTP 200, ~5.2MB). Marker corrected.
- [ ] **cook** / `the-complexity-of-theorem-proving-procedures.md` — description
  uses the standard modern retelling: "SAT," many-one reduction, "first problem
  proven complete." The 1971 paper actually works with *tautologyhood* (the coNP
  side), reduces via query machines rather than many-one, and never uses the
  word "complete"; the NP-complete framing is Karp 1972's. Low priority —
  arguably fine as an orientation for readers — but imprecise.
- [ ] **corbato** / `multics-the-first-seven-years.md` — author order given as
  Corbató, Clingen, Saltzer; multicians.org bylines it Corbató, Saltzer,
  Clingen. Both orderings exist in the literature (the 1991 Turing lecture's own
  reference list uses ours). Cosmetic.

## B. Needs Nathan's judgment

- [?] **chuck-moore** — `the-invention-of-forth.md` and
  `forth-the-early-years.md` are **the same document**, not two works. The
  colorforth.github.io page carries the HTML title "The Invention of Forth" but
  its byline and body are "Forth — The Early Years" (1991), and the worrydream
  PDF is a reformatted copy of that identical text. So one file's description
  contrasts the document against itself. Either merge into a single work file
  listing both URLs as mirrors, or keep both and rewrite the descriptions to say
  they're one text on two hosts. All 5 lessons touching it cite both slugs, so
  either resolution works without re-extraction. Also affects the figure's
  top-10 items 2 and 3.
- [?] **cardelli** / `a-semantics-of-multiple-inheritance.md` — the `url` points
  at the 1984 conference scan, which is image-only (no text layer). The 1988
  journal version is also self-archived, has full text, and is already named in
  the Source line. Promote the journal PDF to `url`, or annotate the primary as
  image-only?
- [?] **clarke** / `design-and-synthesis-of-synchronization-skeletons...` — the
  artifact at the URL is the verbatim 2008 festschrift reprint (LNCS 5000,
  pp. 196-215), not the 1982 LNCS 131 original. Same text, so the Venue/year
  line is correct about the *paper*; worth a parenthetical that the *artifact*
  is the reprint with 2008 pagination.

## C. Phase 3 access flags now overstated

Extraction went better than Phase 3 feared for two figures; their access flags
claim more damage than actually occurred.

- [x] **abrial** — flag warned Phase 4 might come up thin on B/Event-B specifics
  because the two books are paywalled. It didn't: the 2006 talk and 2009 essay
  together carry the refinement calculus, proof-obligation discipline,
  relative-faultlessness scoping, and model-to-code pipeline. 13 lessons, 8 on
  verifiability or hardware-affinity. Softened.
- [x] **boehm** — flag says the public set is "silent on the empirical cost/risk
  data side." Too strong. What's missing is the COCOMO *estimation models*; the
  empirical data is substantially present (cost-to-fix-by-phase across IBM/GTE/
  TRW, design-vs-coding defect split, maintenance at 60-75% of life-cycle cost,
  hardware/software cost crossover, HP reuse payoff). Narrow the wording.

## D. Phase 5 tension candidates (spotted mid-extraction)

Not actionable now — recorded because these are invisible from inside a single
figure, which is exactly what Phase 5's spotting pass has to overcome.

- **Chaitin vs. Dijkstra.** Chaitin holds that formal proof of real software
  correctness is hopeless and that confidence is an empirical result, with new
  axioms adopted like physical laws. Head-on against Dijkstra's
  correctness-from-structure and proof-leads-the-program lessons already banked.
- **Cox vs. Brooks.** Brooks argues software's difficulties are essential and
  cannot be abstracted away. Cox names Brooks explicitly and argues every item
  on that list is a surmountable obstacle, adding two Brooks omitted. Cox also
  treats "programs must be provably correct" as a value-rigidity trap, which
  extends the conflict to Dijkstra and Abrial.
- **Backus vs. Hoare/Dijkstra.** Backus's algebra-of-programs argument
  explicitly holds that axiomatic and denotational semantics are the wrong
  playing field for real programs, and the Turing lecture names them.
- **Backus vs. himself** (intra-figure, already resolved by the figure). The
  FORTRAN-era lessons treat assignment and index-register mapping as the craft;
  the Turing lecture calls those constructs weak palliatives. Backus states the
  reversal himself, so this is a worked example of a tension a figure resolves
  in their own lifetime.
- **Abiteboul vs. himself** (intentional, not a contradiction to resolve away).
  "Notations are viewpoints on one class of computations" sits against "equal
  expressive power is never a licence to substitute." Reconciliation:
  equivalence licenses translation but not elimination.
- **Abiteboul vs. Codd/Dijkstra/Hoare** (likely overlap rather than conflict).
  "Restrict the language until the guarantee is a theorem" is a sharper formal
  version of both data independence and structured programming as restriction.

## E. Sourcing and tooling notes worth keeping

Operationally useful for any future pass; several would have saved an agent
real time here.

- **`pdftotext -raw` for HAL scans.** Plain `pdftotext` on the HAL Datalog scan
  emits each line word-reversed and near-unreadable; `-raw` produces correct
  prose, and also handles the two webdam textbooks' columns better.
- **Video-only figures are tractable via captions.** All four Booch works are
  video with no text source. `yt-dlp` machine-generated English captions worked
  (5.7k-14.1k words each). Caveat: ASR garbles proper names badly (Dijkstra →
  "dyra", Kruchten → "Philipe krushin"), so extract only from arguments that
  survive the noise and cite no ASR-mangled specifics.
- **Image-only PDFs that must be read visually, not text-extracted** (an empty
  extraction here is *not* a fetch failure): Brinch Hansen's RC-4000 report
  (159 pages), Chen's 1983 paper, Brooks's S/360 paper, Cardelli's 1984
  inheritance scan, Clarke's 1981 skeletons paper and 1996 survey (these two
  needed OCR via pdftoppm + tesseract), Abrial's Data Semantics (30 sheets, two
  logical pages per sheet), and Pnueli's 1977 FOCS scan.
- **Cox's three sources are all Wayback snapshots of a dead domain**
  (virtualschool.edu) — zero live-host redundancy. Worth knowing for whatever
  dead-link monitoring Phase 6 does.
- **Third-party rehost quality confirmed** for Brinch Hansen's *Operating System
  Principles* (pascal.hansotten.com): a 16MB scan, but genuinely OCR'd with
  ~723KB of usable text, so the Phase 3 "public via third-party host" call was
  sound.

## F. Cross-cutting process notes

- **Interrupted-run artifacts.** The quota-killed waves left orphaned lesson
  files in several figures (brooks, chen, cook, corbato, chuck-moore) — lessons
  written but `works/*.md` placeholders never filled and no rollup. The agents
  that later picked up those figures re-fetched every source and verified each
  inherited lesson against the real text before keeping it, rather than trusting
  it. Provenance noted here because those lessons were not authored in the
  session that completed the figure.
- **Lesson counts run above the "1-4 per work is typical" guideline** for
  long-form sources — book-length works and multi-essay Turing lectures
  (Brinch Hansen's HOPL retrospective, Brooks's *MMM*, Chaitin's books,
  Clarke's three-author Turing lecture, Cardelli's surveys). In every case the
  agent reports the inflation comes from shared `works:` arrays under the dedup
  rule rather than from duplicate lessons. Worth one deliberate decision in
  Phase 6 about whether to tighten.
- **Axis coverage is uneven per figure, honestly so.** `parallelizability` is
  thin for Cardelli, Corbató, and Backus; Clarke scores verifiability on all 14
  of his lessons. Phase 6 should decide whether per-figure axis balance is even
  a goal before treating this as a defect.

## G. Deferred: spot-check the 11 single-lesson works (grandfathered)

Open task, no action taken. Recorded here so it stays actionable if Nathan
decides he wants it.

**Background.** `extraction: complete` (schema amendment 2026-07-28) is the
per-work attestation that a source was read in full and has no lessons left in
it. It is a *forward* guarantee: the 243 works finished before that date carry
no field, and their absence must not be read as incomplete. The question the
field exists to answer — was this source exhausted, or did an agent write one
lesson and die with three left in it — cannot be answered retroactively from the
files, because a single resolving link is consistent with both.

**Why the exposure is small.** Of the 243 grandfathered works, 176 carry 4+
lessons and 56 carry 2-3. Only the 11 below carry exactly one, so they are the
entire retroactive risk surface. Several are almost certainly correct at one
lesson — Dijkstra's goto piece is a two-page letter to the editor, and Lamport's
one-idea papers genuinely yield one thinking-lesson each.

**Cost if wanted:** roughly two agents' worth. A finisher-style pass restricted
to these works, instructed to re-read each source and either add the lessons it
finds or stamp `extraction: complete` to confirm one was right.

| figure | work | pages | its single lesson |
|---|---|---|---|
| brewer | `cap-twelve-years-later` | HTML | manage-the-partition-as-an-event |
| chamberlin | `sequel-a-structured-english-query-language` | 16 | measure-a-notation-dont-defend-it |
| chamberlin | `system-r-relational-approach-to-database-management` | 41 | give-tuning-its-own-channel-that-carries-no-meaning |
| church | `an-unsolvable-problem-of-elementary-number-theory` | 20 | a-function-is-a-rule-not-a-table |
| dijkstra | `go-to-statement-considered-harmful` | HTML | shorten-the-gap-between-text-and-computation |
| dijkstra | `self-stabilizing-systems-in-spite-of-distributed-control` | HTML | make-the-legal-state-an-attractor |
| lamport | `a-new-solution-of-dijkstras-concurrent-programming-problem` | PDF | assume-the-least-from-your-primitives |
| lamport | `distributed-snapshots-determining-global-states-of-a-distributed-system` | PDF | a-consistent-snapshot-need-not-have-happened |
| lamport | `how-to-make-a-multiprocessor-computer-that-correctly-executes-multiprocess-programs` | PDF | local-correctness-does-not-compose |
| lamport | `the-byzantine-generals-problem` | PDF | make-failure-model-explicit |
| liskov | `abstraction-mechanisms-in-clu` | 1 | traversal-order-is-an-abstraction-someone-should-own |

**Highest-suspicion three**, if a partial pass is preferred over all 11:
`chamberlin/system-r-relational-approach-to-database-management` (41 pages
yielding one lesson), `church/an-unsolvable-problem-of-elementary-number-theory`
(20 pages, and Church's most consequential paper), and
`chamberlin/sequel-a-structured-english-query-language` (16 pages). The Lamport
and Dijkstra entries are the likeliest true single-lesson works.

**Also unattested: the six figures finished by the 2026-07-28 finisher run**
(knuth, landin, lampson, mccarthy, lynch, liskov — 38 works). That run was
launched minutes before `extraction: complete` was added to the prompt, so its
agents were never told to stamp the field. Their works are wired and their
lessons are real; they simply carry no attestation, same as the grandfathered
243. Attesting them is cheap if wanted, since the sources were read that day —
a pass that re-reads only these 38 and stamps or extends them.

**Regenerate this list** any time with the single-lesson query in
`scratchpad/integrity.py`'s neighbourhood — count resolving lesson links per
work, filter to exactly one, exclude OCR-HOLD and no-new-lesson markers.
