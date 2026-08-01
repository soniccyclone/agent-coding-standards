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

## H. Phase 4 blocked / deferred work — the standing backlog

Written down because it was previously living only in a session todo list and
chat scrollback, which is not a place work survives. Everything here is
regenerable from the corpus itself (see the queries at the end), but the
*decisions* are not, so they are recorded.

### H.1 OCR quarantine — RESOLVED 2026-07-29

**Nathan gave the go-ahead on 2026-07-29 and the deterministic pipeline he asked
for was built.** What follows is the original entry, kept because the reasoning
still explains the design; the resolution is recorded first.

**Resolution.** Local OCR with `tesseract` (already installed) driven by
`scratchpad/ocr-run.sh`: rasterize at 300dpi with `pdftoppm`, OCR pages 8-way
parallel, stitch to one text file per work with `=== page N ===` markers. Zero
token cost, minutes of wall time. Agents never OCR anything — they read a
prepared text file, which is exactly the cheap deterministic pipeline Nathan
asked for instead of letting each agent improvise.

Three findings from doing it, each of which changed the corpus:

1. **The quarantine was drawn at the wrong level.** A figure was quarantined if
   *any* of its works needed OCR. Of the 93 unattested works in the 21
   quarantined figures, only 37 actually needed OCR — **46 were fully readable
   with zero lessons written**. One scanned paper in Hoare's bibliography was
   blocking seven readable Hoare works. The coarseness was a deliberate choice
   (see the original reasoning below) and it was the wrong one: the correct unit
   is the work, and an agent *can* do part of a figure as long as the untouched
   works keep their deferral marker.
2. **Several `survey_text_layer: none` records were simply wrong.** Four works
   had perfectly good native text layers (`mcmillan/symbolic-model-checking`,
   98K chars, was tagged OCR-HOLD). Four more were HTML, not PDF — the surveyor
   ran `pdftotext` on HTML, got nothing, and recorded "no text layer." Kay's
   *Early History of Smalltalk* (25,133 words) and his 336-page *Reactive
   Engine* thesis were both sitting there readable the whole time.
3. **`https` vs `http` was hiding a whole thesis.** `the-reactive-engine` was
   recorded with an `https` URL; the host serves only plain `http`, so it read
   as a dead link (HTTP 000). Over `http` it returns the full text.

**The OCR quality caveat, measured not assumed.** On Hoare 1969, `pdftotext`
recovers 6 characters and tesseract recovers the whole paper cleanly. But on a
rules-of-inference page, `⊢` came out as `+`, `|` and `}` interchangeably, `⊃`
as `D`, and `Q₁; Q₂; ⋯ ; Qₙ` as `Qi; Q2; --- ; Q,`. **Prose is reliable;
notation is not.** Every OCR'd work therefore carries a `**Reading copy:**` line
warning the agent to ground lessons in the prose argument and never to rely on a
formula from the OCR text. This matters most for the notation-heavy figures
(Schönfinkel is 1924 German *and* combinator notation; Kolmogorov is measure
theory).

---

*Original entry, 2026-07-27:*

**Nathan's instruction (2026-07-27): no subagent touches an OCR source until he
gives an explicit go-ahead.** Reason: these are the expensive operations and he
wants a cheaper deterministic pipeline designed first, rather than each agent
improvising its own OCR. Not a technical blocker — a deliberate cost decision.

How it is enforced, so it cannot be forgotten:
- The gate is the committed `survey_text_layer: none` field on a work file.
- `scratchpad/next-queue.py` refuses to queue any figure with such a work. A
  figure is quarantined if *any* of its works needs OCR — deliberately coarse,
  because a per-figure agent cannot do half a figure without leaving it
  permanently unwired.
- The agent prompts forbid OCR outright (no pdftoppm, no tesseract, no
  page-image fallback). On hitting an untagged scan an agent marks that work
  `_OCR-HOLD_`, continues with the figure's other works, and flags it. Both the
  queue builder and the commit loop understand that marker, so a held figure is
  bankable rather than churning forever.

| figure | OCR pages | works |
|---|---|---|
| `jones` | 665 | `software-development-a-rigorous-approach` (400pg, 89MB)<br>`development-methods-for-computer-programs-including-a-notion-of-interference` (265pg, 10MB) |
| `sussman` | 131 | `lambda-the-ultimate-declarative` (48pg)<br>`scheme-an-interpreter-for-extended-lambda-calculus` (43pg)<br>`lambda-the-ultimate-imperative` (40pg) |
| `tarjan` | 77 | `efficient-planarity-testing` (57pg)<br>`fibonacci-heaps-and-their-uses-in-improved-network-optimization-algorithms` (20pg) |
| `scott` | 58 | `a-type-theoretical-alternative-to-iswim-cuch-owhy` (30pg)<br>`toward-a-mathematical-semantics-for-computer-languages` (28pg) |
| `kolmogorov` | 54 | `grundbegriffe-der-wahrscheinlichkeitsrechnung` (47pg)<br>`three-approaches-to-the-quantitative-definition-of-information` (7pg) |
| `wirth` | 54 | `the-programming-language-pascal` (28pg)<br>`on-the-design-of-programming-languages` (8pg)<br>`program-development-by-stepwise-refinement` (7pg)<br>`from-programming-language-design-to-computer-construction` (6pg)<br>`a-plea-for-lean-software` (5pg) |
| `reynolds` | 29 | `towards-a-theory-of-type-structure` (18pg)<br>`types-abstraction-and-parametric-polymorphism` (11pg) |
| `vardi` | 25 | `on-the-semantics-of-updates-in-databases` (15pg)<br>`the-complexity-of-relational-query-languages` (10pg) |
| `sifakis` | 15 | `cesar-1982` (15pg) |
| `kay` | 14 | `user-interface-a-personal-view` (14pg) |
| `naur` | 14 | `programming-as-theory-building` (14pg) |
| `stearns` | 12 | `hierarchies-of-memory-limited-computations` (12pg) |
| `yao` | 12 | `theory-and-applications-of-trapdoor-functions` (12pg) |
| `valiant` | 10 | `np-is-as-easy-as-detecting-unique-solutions` (10pg) |
| `ingalls` | 8 | `design-principles-behind-smalltalk` (8pg) |
| `hoare` | 6 | `an-axiomatic-basis-for-computer-programming` (6pg) |
| `wilkes` | 6 | `best-way-to-design-an-automatic-calculating-machine` (4pg)<br>`slave-memories-and-dynamic-storage-allocation` (2pg) |

**Painful cases worth knowing:** Hoare is blocked on a *6-page* scan — five of
his six works are fine, and "An Axiomatic Basis for Computer Programming" is the
one holding the figure. Wirth is five small scans totalling 54 pages. Naur's
"Programming as Theory Building" is 14 pages and is arguably the single most
quoted essay in the whole roster. So the quarantine is coarse in a way that
costs real coverage cheaply — a small OCR batch would unblock a lot.

**One datapoint for pipeline design**, from the Girard agent that ran before the
hold: `pdftoppm -r 250 -gray` piped to tesseract produced clean, greppable text
from a 102-page scan, and it reported that as *far* cheaper than page-image
reads. The obvious shape is: OCR every quarantined source once, mechanically,
with no LLM involved; cache the text sidecars; then let agents read text. That
converts ~1,190 image pages from a repeated token cost into a one-time CPU cost.
Not built, not approved.

### H.2 Context-limit figures — a different problem from OCR

These have perfectly good text layers, so nothing in H.1 applies. They are
simply too long for one agent to read inside a single context.

| figure | text pages | state |
|---|---|---|
| `reenskaug` | 611 | unfinished |
| `ullman` | 603 | unfinished |
| `ungar` | 313 | unfinished |
| `mcmillan` | 284 | done |

The fix is dispatch shape, not reading policy: **one agent per work** instead of
one per figure, so a 600-page source owns an entire agent lifetime rather than
being item three on somebody's list. This has not been built. `mcmillan`
completing at 284 pages suggests the practical ceiling sits somewhere above that.

### H.3 Goldberg — complete, but with self-reported coverage gaps

`goldberg` is marked done, and its agent flagged honestly that it could not fit
both Smalltalk-80 books in context (~700 and ~500 pages, roughly 495k tokens as
text). It read *Personal Dynamic Media* in full plus most of both books, then
listed exactly what it skipped: Blue Book ch16, chs 18-20 (graphics kernel, pens,
display objects), chs 23-25 (statistics and resources in simulations), chs 28-30
(formal bytecode, primitive, and object-memory listings); and in the Orange Book
chs 1-4, 6-8, 11-13, 16-21 and Appendix 1 at full depth.

It also said plainly that judging that material "predominantly reference
listings, UI walkthroughs, and worked examples rather than new argument" is
exactly the selection judgment the spec forbids. **This is the one figure in the
corpus known to have been extracted under acknowledged sampling**, and it is a
per-work re-dispatch candidate (H.2) rather than an OCR one. Nathan has not ruled
on it.

### H.5 `survey_text_layer` had a false-positive class — fixed, methodology corrected

**Found 2026-07-28 by McMillan's agent, then audited corpus-wide.** The original
survey classified extractability by *how many characters `pdftotext` recovered
per page*. That is wrong for PDFs whose fonts are Type-3 bitmaps with a Custom
encoding and no Unicode map: extraction emits plenty of characters and every one
is garbage, a substitution cipher. Those works were recorded `full` and agents
only discovered the truth after downloading them.

**Corrected to `none` (4 works):**
- `mcmillan/symbolic-model-checking-10-20-states-and-beyond` (33 of 35 fonts Type 3)
- `mcmillan/symbolic-model-checking-an-approach-to-the-state-explosion-problem` (184 of 190)
- `stearns/an-algebraic-model-for-combinatorial-problems`
- `stearns/its-time-to-reconsider-time`

Neither figure newly enters quarantine: `stearns` was already there, and
`mcmillan` is done with one OCR-HOLD. So the corpus impact was metadata accuracy
rather than coverage — but future agents would have kept rediscovering it.

**Do NOT re-scan `mcmillan`'s thesis in an OCR batch.** Its text layer is
unusable, but the work was read in full through the sanctioned channel: archive.org
item `DTIC_ADA250924` exposes a `_djvu.txt` derivative covering all 214 pages
(DTIC ADA250924 = CMU-CS-92-131). A note to that effect is in the work file.

**Methodology, for whoever builds the OCR pipeline — font counts are the wrong
test.** A first pass using `pdffonts` flagged 13 works, and a readability check
showed **only 4 were actually unreadable**. The other 9 use Type-3 fonts for math
glyphs while the body text extracts perfectly: Parnas's program-families paper
yielded 883 common English words in four pages, Vardi's bounded-variable-queries
paper 839. Font composition tells you a document *contains* bitmap glyphs, not
that its prose is lost.

The decisive test is cheap and should be the standard:

    pdftotext -f 1 -l 4 file.pdf - | tr 'A-Z' 'a-z' | tr -s ' \n' '\n\n' \
      | grep -cxE 'the|of|and|to|is|in|that|for|with|are|this'
    # < ~10 hits over four pages => the text layer is garbage, needs OCR

Worth re-running across the whole corpus if the OCR batch is ever built, since
the original character-count survey may have mismarked in the other direction
too (a genuinely scanned page yielding stray OCR noise would score as `partial`).

### H.6 GDZ cover-only scans, and a lesson-provenance question about Péter

**Found 2026-07-29.** All 8 works in this corpus hosted by Göttingen's GDZ have
*no* extractable article text — the only embedded text is the library's German
cover sheet, and article pages yield exactly zero characters. All 8 were recorded
`partial`, which is worse than `none` would have been: it reads as "some of the
article extracts" when none of it does. My survey had been measuring the cover
boilerplate. GDZ also exposes no ALTO/OCR derivative (its IIIF manifest 404s),
so unlike McMillan's thesis there is no host-provided-text escape hatch.

Corrected to `none`: `kleene/general-recursive-functions-of-natural-numbers`,
`peter/uber-den-zusammenhang-...`, `peter/uber-die-mehrfache-rekursion`,
`schonfinkel/bausteine-der-mathematischen-logik`,
`schonfinkel/entscheidungsproblem-der-mathematischen-logik`, and Strassen's
three. Quarantine grows from 17 figures to 19 (adds `kleene`, `schonfinkel`).

**OCR batch priority — best value per page in the whole backlog.** Strassen's
*Gaussian Elimination is not Optimal* (1969) is **4 pages, of which only 2-3 are
article**, and it is the figure's flagship result: the entire reason Strassen is
in this corpus. Strassen currently has a rollup and **zero lessons** because all
three of its works are held. Three scanned pages unblock a whole figure. If the
batch gets prioritized at all, start here.

**NEEDS NATHAN — Péter's lesson provenance.** `peter` is marked done with 9
lessons and `extraction: complete` on both works, but both works are now
confirmed cover-only. So those 9 lessons were not derived from extracted text.
The likely explanation is benign: the extracting agent read the page images
visually, which was permitted before the OCR prohibition landed on 2026-07-28.
The finisher that later touched Péter said as much — "no OCR-HOLD marker was
left, so a prior agent evidently got enough text through. Not re-verified per
task scope." But nobody has confirmed it, and the alternative (lessons written
from model recollection of Péter's work rather than from the source) is exactly
what this project's rules exist to prevent. **This is the one place in the corpus
where lesson grounding is genuinely unverified rather than merely unattested.**
Cheapest resolution: one agent re-reads the two GDZ scans as page images and
confirms the 9 lessons are supported, or flags the ones that are not.

Same question applies more weakly to `kleene`, which has lessons against a
cover-only GDZ scan; it should be checked in the same pass.

### H.4 Regenerating all of the above

    # OCR quarantine list + page counts
    grep -l 'survey_text_layer: none' bundle/figures/*/works/*.md

    # full status incl. quarantine and hand-inspect sets
    python3 scratchpad/next-queue.py --status

    # per-figure total text pages (context-limit risk)
    #   sum survey_pages across a figure's works

### H.7 Four works with no obtainable source — needs Nathan's decision

Found 2026-07-29 while clearing the OCR quarantine. These are not OCR problems
and not fixable by a better fetch; the text is not reachable from a URL we have.
Each blocks its figure from full attestation, so each needs either a source
Nathan can supply or an explicit decision to drop the work from the figure's list.

| figure | work | what is actually at the URL | why it is not fixable here |
|---|---|---|---|
| `turing` | `computability-and-lambda-definability` | Turing Digital Archive landing page (26KB, no full text) | See the misattribution note below. Turing is otherwise 7/8 attested with 27 lessons. |
| `kolmogorov` | `logical-basis-for-information-theory-and-probability-theory` | mathnet.ru abstract page (24KB) | Guessed mirrors on `alexander.shen.free.fr` return 404. |
| `kolmogorov` | `on-the-definition-of-an-algorithm` | mathnet.ru abstract page (23KB) | Same. |
| `valiant` | `the-extent-and-limitations-of-mechanistic-explanations-of-nature` | a YouTube video | It is a recorded talk, not a text. Needs a transcript or substitution with a written work. |

**A near-miss worth recording, because it would have corrupted the corpus
silently.** Searching for the Turing paper surfaced
`baklaniv.at.ua/CPP/fp.pdf`, a real PDF titled "Computability and
λ-Definability" — the exact title of Turing's 1937 JSL paper. It is a **2013 book
chapter by Barendregt, Plasmeijer and others** that merely shares the title.
Fetching it and reading the first page caught it; accepting it on title match
would have attributed another author's work to Turing and produced lessons
grounded in the wrong paper, with nothing downstream able to detect the error.

The rule this earns: **a recovered URL is not verified until its first page has
been read and the author and venue confirmed.** Title match is not identity —
titles are reused, especially for survey and textbook treatments of a famous
result. The existing `url-sweep.sh` classifies by HTTP status and byte count,
which would have passed this file as `OK`.


### H.8 92 lessons were adopted by backlink repair, not by verification

Commit `c51d354` repaired work files whose `## Lessons` sections did not reference
lesson files that existed on disk — the second failure direction from killed
agents. The repair was mechanical and correct in what it did, but it created a
class of lesson worth flagging, and **its own commit message gets the numbers
wrong**, which is why this entry exists.

**Corrected counts, read from the diff rather than the message:**

| | commit message claims | diff actually shows |
|---|---|---|
| work files touched | 16 | **30** |
| distinct lessons adopted | 36 | **92** |
| link lines added | — | 101 |

(101 links across 92 distinct lessons because nine lessons are cited by more than
one work.) All 92 still exist on disk. The seven figures are `chamberlin`,
`church`, `lampson`, `landin`, `liskov`, `lynch`, `mccarthy`. Regenerate the exact
list with:

```
git show c51d354 -- 'bundle/figures/*/works/*.md' | grep -E '^\+\- \[' \
  | grep -oE '\.\./lessons/[a-z0-9-]+\.md' | sed 's|../lessons/||;s|\.md||' | sort -u
```

Per Nathan's standing instruction the message is **not** being amended — history
rewriting is his call. The correction lives here instead.

**The epistemic caveat, which is the actual point.** Each link was reconstructed
from the lesson's own `works: [...]` frontmatter. That is deterministic and
reproducible, but it is the *lesson's own testimony* about which work it came
from. Nobody re-opened the source to confirm it. If a dying agent wrote a lesson
with a wrong `works:` value, the repair propagated that error faithfully and the
result looks identical to a correct link. So these 92 sit in a third tier,
distinct from both agent-attested and bulk-stamped work:

- Tier 1 — agent read the source and wrote the link in the same pass.
- Tier 2 — bulk-stamped `extraction: complete` at commit `443703b`, unverified.
- **Tier 3 — link adopted from lesson frontmatter after the writing agent died.**

Nothing here is known to be wrong, and spot-checking is cheap: for any of the 92,
open the named work and confirm the lesson's Source line describes a passage that
is actually in it. Worth doing for a sample during the Phase 6 lint pass rather
than as a blocking task now.


### H.9 Findings from the final agent waves (2026-07-31)

Resolved in place, recorded because each names a failure mode worth recognising.

**A work can quarantine itself.** `mcmillan/symbolic-model-checking` bounced
between `survey_text_layer: full` and `none` three times. The PDF has an embedded
text layer and `pdftotext` returns ~103k characters, so my OCR enumeration scored
it readable and I set `full` — and told Nathan it had been held behind an OCR
marker over "98K characters of perfectly extractable text." Wrong. The characters
are a Type-3 bitmap substitution cipher (Ghostscript 6.01 out of DVI, no ToUnicode
map) and read as `!#"%$&')(*'+-,`. **This is the exact false-positive class already
written up in H.5, and the enumeration script used the very character-count
heuristic H.5 warns against.** An extraction agent opened the file, saw nonsense,
and correctly reverted the field to `none` — after which every later agent skipped
it by rule, including one dispatched straight at it, which returned after seven
tool calls having done nothing. It looked like an agent failure and was a
self-inflicted quarantine. Now genuinely OCR'd (33pp, 10,922 words, 0.326
common-word ratio) with a reading-copy note that spells out the trap.

The general rule: **an agent's downgrade of a survey field is evidence, not
vandalism.** It is the only signal in the system produced by something that
actually opened the document. When a field flips back, believe the flip and go
look.

**A correcting note is not a correction.** `kay/the-early-history-of-smalltalk`
claimed its source carried "full text ... through the closing section and
references." False — the worrydream HTML stops after the Coda; references and
Appendices I-V are linked but absent. The agent found this and appended an
accurate coverage note while leaving the false claim in place, so the file
contradicted itself and whichever a reader hit first decided what they believed.
Fixed at the source. Worth telling agents explicitly: correct the wrong statement,
do not merely annotate around it.

**`survey_text_layer: full` does not mean born-digital.**
`scott/data-types-as-lattices` extracts cleanly enough to need no OCR pass, but its
text layer is itself an OCR layer over a scan of the SIAM reprint: prose reliable,
notation mangled. The field was accurate and the file still misled, because `full`
answers "can I extract this?" and not "can I trust a formula I read from it?" A
caution line now says so. Any work whose PDF predates about 1995 deserves the same
question asked.

**Coverage-note discipline is not reliably followed.**
`kay/steps-toward-the-reinvention-of-programming` carried one lesson and no
coverage note — a prior agent wrote a lesson and died without recording where it
stopped, which is indistinguishable from a work that yielded exactly one lesson.
The re-reading agent had to redo it from the start to be safe. Cheap to prevent,
expensive to detect.

**Two lessons were deliberately not written**, and the reasoning is worth keeping.
Reading Kay's *Reactive Engine*, the agent judged its prefix-versus-postfix
evaluation-order argument to reduce to the same claim as the existing
`replace-assignment-with-goals`, and its files-as-frozen-globals material to be
covered by `collapse-system-categories-into-one-concept`. Both would have been
duplicates under new names. The open item: those two existing lessons arguably
should cite `the-reactive-engine` in their `works:` arrays, which the agent could
not do because editing existing lesson files was forbidden. A human should decide.


### H.10 A fourth confidence tier: works attested across passes, not read end to end

Raised by the church extraction agent on 2026-07-31, unprompted, about its own
attestation. It should not stay buried in a workflow result.

Closing out `church/introduction-to-mathematical-logic`, the agent wrote
`extraction: complete` and then said plainly that it had personally read only two
short spans; the rest of the exhaustion claim rested on coverage notes left by
three earlier passes. It verified those notes' internal consistency — spot-checking
five line spans the notes never explicitly listed, confirming each fell inside a
section a prior pass recorded as read — then posed the question directly: **if
`extraction: complete` asserts that one agent read the work end to end, this file
does not meet that bar; under the coverage-note convention, it does.**

That ambiguity is not confined to church. The books finished in these waves were
each read across several agent sessions, stitched together by resume notes:

| work | pass markers |
|---|---|
| `jones/software-development-a-rigorous-approach` | 14 |
| `sussman/structure-and-interpretation-of-computer-programs` | 8 |
| `church/introduction-to-mathematical-logic` | 4 |
| `hoare/communicating-sequential-processes-book` | 4 |

So H.8's tiers need a fourth entry, and it is *not* strictly weaker than Tier 2 —
it is a different kind of claim:

- Tier 1 — one agent read the source and attested in the same pass.
- Tier 2 — bulk-stamped at `443703b`, unverified.
- Tier 3 — backlink adopted from lesson frontmatter after the writing agent died.
- **Tier 4 — attested on the union of several passes' coverage notes. No single
  reader saw the whole work. The claim is only as good as the notes, and the notes
  are written by agents that then die.**

Two findings argue for watching Tier 4 rather than trusting it. The church agent
found that file's coverage note *contradicting itself* — one paragraph recording
spans as complete while the next still listed those same sections as unread,
because prior passes advanced the resume line without revising the gap list. And
the hoare agent found its note's line number was a **floor rather than a fact**:
lesson Source lines proved the previous pass had read ~400 lines further than its
own note claimed. Both errors ran in the safe direction; nothing guarantees that.

**Recommendation, not applied.** Either re-scope `extraction: complete` to mean
"the union of recorded passes covers this work" and say so in the technical plan,
or keep the stronger meaning and re-read the four works above end to end. The cheap
middle option is a mechanical audit: for each Tier 4 work, check that the union of
line spans claimed across its coverage note is contiguous from 1 to EOF with no
gaps. Checkable in seconds, and it would have caught the church contradiction.

**Note-format rule earned here:** a coverage note must carry exactly one
authoritative statement of coverage — a position log — never a progress line plus a
separately maintained gap list. Two records of the same fact drift, and the drift
is invisible because each looks plausible alone.

