---
type: execution-plan
title: Good Programming Corpus — Technical Plan
description: Phased build pipeline for the OKF bundle. Phases 0-3 complete (95 figures, 450 work files); Phase 4 (lesson extraction) in progress; Phase 8 is an idea backlog for making the finished bundle queryable.
tags: [execution, okf, pipeline, fan-out]
---

# Technical Plan

project-state.md, primer.md, good-programming-corpus-overview.md, and the debate
transcript are all **frozen as of 2026-07-23** — historical record of *why*
the standing rules exist, cited below but not edited further. This file (*how*
those decisions become work) and [ledger.md](ledger.md) (live figure/tension
status) are the two docs that keep changing from here on. If a phase here
seems to contradict a cited thread, the thread's reasoning still wins, but the
fix is a new dated note in this file — not an edit back into project-state.md.
The schema amendment below is the first use of that escape hatch.

**Status as of 2026-07-24:** Phase 0 done (bundle scaffolded). Phase 1 done —
95 candidate figures in `bundle/figures/`. Phase 2 done same day — Nathan
reviewed and approved the full roster, all 95 `status: accepted`, no
rejections; layer placement (`design-thought` / `implementation-mapping` /
`both`) assigned per figure per the project-state.md §2 hierarchy, logged in
[ledger.md](ledger.md#phase-2-layer-placement). Torvalds-shaped candidates
(non-publishing systems builders, shipped code instead of papers) confirmed
acceptable as Phase 3 source material — see ledger.md's Torvalds note. Phase 3
(source discovery) is in progress — pilot batch (Dijkstra, Lamport, Codd, 27
`work` files) validated the process same day; scope amended to seminal-works
verification rather than exhaustive bibliography enumeration (see Phase 3's
own section for the reasoning); remaining ~90 figures not yet started.
Tagged milestones on `main`: `author-candidates` (Phase 1 done, 92 candidates),
`author-candidates-v2` (+Chuck Moore, von Thun — Forth/Joy lineage, 94),
`author-candidates-v3` (+Jerome Saltzer — security/systems design principles,
95), `figures-accepted-v1` (Phase 2 done, all 95 accepted + layer-placed,
current HEAD).

## Schema amendments

Dated notes that supersede a frozen project-state.md thread, per the escape
hatch above. Each one stays here permanently, isn't folded back into the
frozen doc.

**2026-07-23 — `subdomain` added as a sixth type.** Supersedes project-state.md
§4 ("types fixed at five"). Reason: once figures went flat (see below),
subdomain needed to be a linkable, citable concept node — a rollup with a
definition and a backlink list — for exactly the same reason `axis` already
is one. Same many-to-many relationship to figure-owned content, same fix.
`type: subdomain`, one file per subdomain, same shape as `axis`.

**2026-07-27 — `survey_*` fields added to the `work` frontmatter.** Three
optional, mechanically-generated fields recording what it costs to actually
read a source: `survey_pages` (PDF page count), `survey_text_layer`
(`none` / `partial` / `full` — whether text can be extracted, derived from
characters recovered per page over the first ten pages), and
`survey_fetch_mb`. A failed fetch records `survey_fetch: FAILED` instead.

**2026-07-31 — a fourth `survey_text_layer` value: `ocr`.** When the OCR
quarantine was cleared, 36 works whose text layer was unusable were rasterised
and recognised locally with tesseract, and a `**Reading copy:**` line was added
to each pointing at the resulting text. Those works read `survey_text_layer: ocr`,
meaning: *the source itself has no usable text layer, but a prepared transcript
exists and an agent should read that rather than the original.* This value was
introduced in practice before it was written down here — a reynolds extraction
agent caught the omission by noticing that three work files carried a value the
schema did not define, which would silently fail any tooling that routed on the
field. Recorded now.

The caveat that travels with `ocr`: prose recognises reliably and **notation does
not**, so lessons from those works must be grounded in the prose argument and must
never transcribe or rely on a formula. Note also that `full` does not imply
born-digital text — some PDFs carry an OCR layer produced by someone else, with
the same notation-mangling property and no marker in the frontmatter.

Reason: Phase 4 lost several agent-days to sources whose cost was invisible
until an agent was already hours into one. The decisive variable turned out not
to be page count alone but page count *times* extractability — a 400-page PDF
with a text layer is one cheap `pdftotext` call, while a 30-page image-only
scan forces OCR or page-by-page visual reads, which is what kept timing agents
out. Because the answer is a fixed property of the artifact rather than of any
one pass, it belongs on the work file, where Phase 5/6 and any future re-read
get it for free instead of rediscovering it.

These are derived, not authored: they can be regenerated from the URLs at any
time (`scratchpad/survey-works.sh`), and unlike `description` or `access` they
carry no editorial judgment. Nothing downstream should treat them as
load-bearing for citation — they are routing hints.

**2026-07-28 — `extraction: complete` added to the `work` frontmatter.** A
one-line, agent-written attestation that a source has been read in full and has
no further lessons left in it. Absent means "not confirmed exhausted."

Reason: a link from a work file to a lesson proves a lesson was written; it does
not prove the source was fully mined. Phase 4 agents are killed by
infrastructure timeouts constantly, and an agent that writes one lesson and then
dies leaves a work file that looks finished while silently losing whatever else
that source contained. Link integrity (which direction points where) is a
different property from extraction completeness (was this source exhausted), and
the corpus previously had no way to express the second.

Written last, deliberately: read the source, write the lessons, link them, then
add the field. That ordering is what makes it meaningful — it is a signature on
completed work rather than a declaration of intent.

**Grandfathering:** the 243 works finished before this date carry no field, and
their absence should NOT be read as incomplete. Measured at the time: 176 of
those had 4+ lessons, 56 had 2-3, and only 11 had a single lesson — most of
those being genuinely short pieces (Dijkstra's two-page goto letter, Lamport's
Byzantine Generals). The field is a forward guarantee, not a retroactive audit.
A spot-check of the 11 single-lesson works is the proportionate follow-up if one
is ever wanted.

## Bundle target structure

```
bundle/
├── index.md                       # root rollup, synthesized from subdomains/*.md
├── log.md                         # chronological ingest audit trail, per Karpathy pattern
├── axes/
│   ├── index.md                   # nav list of the six axis files
│   └── <axis>.md                  # definition + synthesized rollup + backlinks to lessons scored here
├── subdomains/
│   ├── index.md                   # nav list of the nine subdomain files
│   └── <subdomain>.md             # definition + synthesized rollup + backlinks to tagged works/lessons
├── figures/
│   ├── index.md                   # nav list of all figures
│   └── <figure>/
│       ├── index.md               # bio, layer placement, author-level rollup of their own lessons
│       ├── works/
│       │   └── <work>.md          # type: work — subdomains: [...], links to its lesson(s)
│       └── lessons/
│           └── <lesson>.md        # type: lesson — links work + axis(es) + subdomain(s)
└── tensions/
    ├── index.md                   # full open+resolved status table
    ├── <tension>.md               # type: tension — primary content, not a rollup, see below
    └── resolutions/
        └── index.md               # curated subset: resolved tensions only, highlight-reel synthesis
```

**Figures own all primary content.** A figure's bio, works, and lessons live
in exactly one place — no subdomain nesting, no "primary subdomain" picked,
no cross-linking needed to keep a duplicate in sync. This is what kills the
multi-subdomain-author problem (McCarthy, Lamport) outright instead of
managing it.

**`axes/` and `subdomains/` are cross-cutting indexes, not owners.** Both are
structurally derived: the backlink list in each file could in principle be
rebuilt from scratch by scanning `axes`/`subdomains` frontmatter tags
elsewhere in the bundle. The definition and the synthesized rollup paragraph
are the only genuinely authored parts, and even the rollup gets
re-synthesized periodically rather than hand-maintained line by line.

**`tensions/` is the exception — primary content, not derived.** A tension
doesn't belong to one figure the way a lesson does, so there's nothing
elsewhere to rebuild it from. Delete a tension file and the resolution
reasoning is gone; delete an axis file and it's just annoying to regenerate.
Treat `tensions/` with more care than the two index directories.

## Rollup mechanics

Four tiers, each a synthesis of the level below it, each cheaper to write
than the last because it's synthesizing syntheses, not raw lessons:

1. **`figures/<figure>/index.md`** — synthesized from that figure's own lessons.
2. **`subdomains/<subdomain>.md`** — synthesized from lessons tagged with that subdomain, wherever they live.
9. **`axes/<axis>.md`** — synthesized from lessons scored on that axis, orthogonal to subdomain.
10. **`index.md`** (root) — synthesized from the nine subdomain rollups.

Root-level rollup is effectively a running draft of Phase 7's distillation
target the whole time, not something built from scratch only at the end.
Rollups get re-synthesized opportunistically as a meaningful batch of new
lessons lands underneath them — not on every single lesson, and not on a
fixed schedule. Same abstract-only, no-copy-paste rule from §3 applies to
rollup prose too — a rollup is still not allowed to smuggle in source
expression just because it's a level removed from the original work.

## Standing rules this pipeline enforces (pointers, not restatements)
- Types fixed at six: `figure`, `work`, `axis`, `subdomain`, `lesson`, `tension` — five from [project-state.md §4](project-state.md#4-okf-type-taxonomy--resolved), `subdomain` added by the schema amendment above.
- Public sources only, no paywalled/DRM'd works ingested into the bundle — [§3](project-state.md#3-scope-and-copyright-of-ingestion--resolved-publish-is-the-intent-not-a-maybe).
- Lessons are abstract (how to *think*), never technique/expression-level; zero copy-paste at any length, including in rollups — [§3](project-state.md#3-scope-and-copyright-of-ingestion--resolved-publish-is-the-intent-not-a-maybe).
- Vetting outcome is layer placement, not reject/accept — every figure lands at
  the design-thought layer or the implementation-mapping layer (or both) — [§2](project-state.md#2-does-the-primitive-count-default-license-rejecting-turing-style-figures--resolved).
- Bundle first, distilled `@`-referenceable doc second, not in parallel — [§5](project-state.md#5-final-deliverable-shape--confirmed).

## Planning/execution boundary

Everything up to and including this line happens in `docs/planning/*.md` — the
four original argument docs (now frozen) plus this plan and ledger.md (still
live). **Phase 0 is the seam.** From Phase 0 onward, work stops being "argue in
markdown about the project" and starts being "generate real OKF files in the
bundle." Nothing before Phase 0 produces a `figure`/`work`/`lesson`/`axis`/
`subdomain`/`tension` file. Status updates from Phase 0 onward (accept/reject,
layer placement, tension tracking) go into ledger.md — the four frozen docs are
never touched again, period.

Bundle root isn't pinned down yet — assuming top-level `bundle/` at the repo
root (sibling to `docs/`, not nested under `docs/planning/`), since an OKF
bundle is meant to be portable/shippable on its own rather than living inside
the argument-docs tree. Flag if that's wrong before Phase 0 runs; the tree
diagram above and everything downstream assumes it.

## Pipeline

Each phase lists a **fan-out unit** — the thing that gets split into parallel
tasks — so phases map directly onto bd/beads tickets without restructuring.

### Phase 0 — Bundle scaffolding ✅ complete (2026-07-24)
**Fan-out unit:** none, one-time setup.
**Do:** create the directory structure above; write the six `axis` files
(expressiveness, verifiability, parallelizability, hardware-affinity,
cognitive load, primitive-count) and the nine `subdomain` files (definitions
only at this point, rollups start empty) — both fixed, small, and a hard
dependency for Phase 4, so they happen before any figure work starts.
**Output:** empty bundle skeleton + populated `axes/` and `subdomains/` (definitions only).
**Depends on:** nothing.

### Phase 1 — Author discovery (fan-out by CS subdomain) ✅ complete (2026-07-24)
**Fan-out unit:** one CS subdomain per task.

**Subdomains (fixed):**
1. Foundations of Computation — logic, computability, formal systems.
2. Programming Languages & Semantics — language design, type systems.
3. Formal Methods & Verification — correctness, not just expressiveness.
4. Algorithms & Complexity — analysis, complexity theory.
5. Software Engineering & Architecture — large-system structuring, methodology.
6. Operating Systems & Systems Programming — the implementation-mapping layer's home turf.
7. Distributed Systems & Concurrency — consensus, network unreliability.
8. Databases & Data Management — relational/declarative data thinking.
9. Programming Environments & Object Systems — live environments, object-orientation as a distinct lineage.

Deliberately high-level-only — no business/applied domains (no AI/ML, crypto/security,
web, mobile, etc. as their own buckets). Figures whose real contribution is
programming-abstraction quality land under one or more of the nine above
regardless of the applied field they're best known for.

**Do:** for each subdomain, produce candidate figures and write a
`type: figure, status: candidate` stub file per candidate — bio + why they're
a candidate + which subdomain(s) surfaced them + their top 10 most influential
works (title only, best-effort, not the exhaustive Phase 3 pull) — so vetting
in Phase 2 happens by reading a file with real substance in it, not a bare
name and a guess.

Each of the ten gets a one-word accessibility flag — `public` or `paywalled` —
even though full link-pulling is still Phase 3's job. This is deliberately
decision-relevant at vetting time: if a candidate's most influential work is
locked behind a paywall and the rest of their output is minor, Nathan needs
that visible *before* accepting them, since §3 means Phase 3 will never touch
the paywalled one regardless of how central it is to their reputation.

**Dedup/merge step, after all nine fan-out tasks return:** the same person
will get surfaced by more than one subdomain pass (McCarthy from both
Foundations and Languages). Merge duplicate candidates into a single stub
tagged with every subdomain that found them, and merge their two top-10 lists
into one (dedupe overlapping titles, keep it at ten) before Phase 2 starts —
the flat `figures/` tree makes a duplicate a literal bug (two directories, one
person), not something that can silently pass.

**Output:** one `figure` stub per unique candidate, `status: candidate`,
tagged with all discovering subdomains, carrying a titles-only top-10 list
with public/paywalled flags.
**Depends on:** Phase 0 (scaffolding, not content).

**Actual result:** 92 candidates from the nine-subdomain fan-out, post-dedup
(7 figures surfaced by more than one subdomain, tagged with all of them —
Dijkstra by four). Plus 3 added out-of-band via direct discussion rather than
the fan-out itself, same output shape (stub, why-candidate, top-10 with
accessibility flags), same `status: candidate` treatment: Chuck Moore and
Manfred von Thun (Forth/Joy concatenative lineage, a gap surfaced discussing
Schönfinkel/Curry), and Jerome Saltzer (security/systems design principles,
the one real gap found scoping whether cyber/crypto/ML deserved coverage —
conclusion was no dedicated subdomains, but this one figure was missing).
95 total. Full roster and per-subdomain breakdown in [ledger.md](ledger.md).

### Phase 2 — Vetting (sequential, Nathan-in-the-loop) ✅ complete (2026-07-24)
**Fan-out unit:** one candidate figure per pass — not parallelizable the same
way as the others, since layer placement and tension-spotting need live
judgment, not independent agent runs.
**Do:** run each candidate's stub through the primer.md gate; flip `status` to
`accepted` or `rejected` in place; if accepted, assign layer placement
(design-thought / implementation-mapping / both, per §2); flag any immediately
visible tension against an already-accepted figure.
**Output:** existing stub file updated in place, not recreated — `status` and
layer placement set. Rejected stubs stay in the tree with their reason, same
"not silently dropped" principle as ledger.md. Every outcome also logged in
[ledger.md](ledger.md).
**Depends on:** Phase 1 roster (post-dedup).

**Actual result:** Nathan reviewed the full 95-figure roster directly and
approved all of it — zero rejections. Layer placement then followed
mechanically from the accept-all outcome, applying §2's hierarchy resolution
(and its own worked example: Dijkstra/Hoare/Kernighan/Pike/Lampson land
implementation-mapping despite formal rigor, because layer tracks
subject-matter lineage — Church/Lisp composition vs. Turing-lineage
mechanism — not rigor level) figure by figure against each stub's own
why-candidate content. 26 design-thought, 10 both, 59 implementation-mapping;
full breakdown and reasoning in
[ledger.md](ledger.md#phase-2-layer-placement). One immediately-visible
tension flagged per this phase's own duty: Dijkstra vs. Knuth on goto (both
now accepted), added to ledger.md's tension index for Phase 5. Also resolved
in this pass: Nathan confirmed non-publishing systems builders (Torvalds, and by the same
reasoning Cutler, Chuck Moore) can source Phase 3 material from shipped
code/documentation rather than papers — see ledger.md's Torvalds note.

### Phase 3 — Source discovery (fan-out per accepted figure) ✅ complete
**Fan-out unit:** one accepted figure per task. This is the phase Nathan named
directly — parallel per-author pull of the public-source list.

**2026-07-24 amendment — seminal works, not an exhaustive bibliography.**
Supersedes the original "enumerate every publicly accessible whitepaper,
essay, talk, interview, or repo" scope below. Lessons are abstract "how to
think about programming" extractions, and those concentrate in the works that
made a figure canonical — Dijkstra's structured-programming argument is fully
present in EWD215/EWD249, not diluted across the other ~1,300 EWDs. A true
enumerate-everything pass would multiply cost 10-20x for prolific figures
(Dijkstra, Hoare, Date) for diminishing lesson-extraction return. Verify and
formalize each figure's existing Phase 1 top-10 list into `work` files
(resolving `uncertain` flags for real, correcting `paywalled` flags where a
legitimate public copy exists) rather than launching a fresh from-scratch
bibliography search. Going beyond the top-10 is fine when a clearly-central,
clearly-public work turns up during that verification pass — the boundary is
"don't go looking for more," not "refuse more if it's sitting right there."
**The escape valve:** if a figure's lessons come up thin in Phase 4, that's
the signal to go back and pull more sources for *that specific figure* —
not a reason to over-fetch for all 95 up front.

**Do:** for each accepted figure, verify and formalize the top-10 list from
its Phase 1 stub into individually-checked `work` files. Actually fetch each
URL rather than trusting the old flag — resolve `uncertain` to public or
paywalled based on what's really there, and double check `paywalled` in case
a legitimate self-archived or institutional copy exists that the Phase 1 pass
missed. Check the Wayback Machine when an author's institutional/personal
page has moved or gone stale — a Wayback snapshot of a self-archived PDF is
exactly as public as the live version, and several of the strongest sources
here (EWD archive-style personal pages) are exactly the kind of thing that
outlives its original host. No paywalled/DRM'd sources per §3 — if a figure's
material only exists paywalled, flag it, don't substitute a summary of it.
Third-party rehosts of copyrighted (non-self-archived) material — fan
archives, course mirrors, preservation nonprofits — count as public sources
when the host looks legitimate, since these are link-only citations and the
bundle isn't redistributing anything; mark every such case with `host:
third-party-rehost` in the work file's frontmatter so a batch review can find
them later if a host turns out to be a problem.

**Flag-don't-halt:** if a work that's clearly central to a figure's "why a
candidate" case turns out to have genuinely no public copy anywhere (checked
directly, checked Wayback, confirmed), don't stop and ask mid-run — add a
`## Phase 3 access flag` note directly to that figure's own `index.md`
explaining what's missing and why it matters, then keep going with the rest
of the roster. Nathan reviews all flags in one batch after the run, not
per-figure.

**Output:** one `work` file per confirmed-public source under
`figures/<figure>/works/`, frontmatter carrying `type: work`, `figure`,
`description` (~3 sentences, own words, never copy/paste or close paraphrase
of the source), `subdomains: [...]` (the one or two that fit *this* work,
not necessarily the figure's full list), `year`, `url`, `access: public`,
and `host` (`self-archived` / `institutional` / `third-party-rehost`). Body
carries author/venue/source details and an empty `## Lessons` placeholder —
lesson extraction is Phase 4, a separate file. Per-figure agents never touch
`bundle/log.md` — the orchestrating session logs each wave itself, since
concurrent writes from a parallel batch would clobber a shared file.

**Pilot (2026-07-24):** ran Dijkstra, Lamport, Codd first to validate the
process — 27 `work` files, all independently link-verified rather than
trusting Phase 1's guesses. Caught two dead links, one wrong title, several
`uncertain`/`paywalled` flags resolved in both directions. No access flags
needed — nothing central turned out to be unavailable in this batch. Full
readout in [ledger.md](ledger.md).

**Complete (2026-07-24).** Pilot validated the process, then the remaining
92 figures ran as a rolling-queue fan-out (one subagent per figure, capped
at 20 concurrent by the harness) to a fully autonomous finish. Final tally:
450 `work` files across all 95 figures — the main run left Pnueli at zero
(all four listed works inaccessible), and a same-week follow-up pass closed
that gap via NYU's preserved copy of his self-archived homepage (see
ledger.md). 31 of 95 figures carry a `## Phase 3 access flag`. Full
per-figure breakdown, the third-party-rehost policy, and the two
corpus-wide sourcing caveats (pre-1980s papers under-covered by rehosts;
Internet-Archive-lending-only books counted as paywalled) are in
[ledger.md](ledger.md)'s Phase 3 status section.
**Depends on:** Phase 2 (can start per-figure as soon as that figure clears
vetting, doesn't need to wait for the whole roster).

### Phase 4 — Lesson extraction (fan-out per work)
**Fan-out unit:** one `work` per task (or batched per figure if a figure has
many small works).
**Do:** read the source, extract abstract lesson(s) — how it teaches someone
to *think* about programming — into `figures/<figure>/lessons/`, cited back to
the work, linked to the `axis` file(s) and `subdomain` file(s) it scores on. A
work can fan into more than one lesson if it teaches on genuinely distinct
axes. Zero reproduction of source text per §3. Append the new lesson to the
relevant `axes/<axis>.md` and `subdomains/<subdomain>.md` backlink lists.
**Output:** `lesson` files, cross-linked to figure + work + axis + subdomain. A
work with no distinct lesson beyond what's already captured gets marked
read-no-new-lesson, not skipped silently.
**Depends on:** Phase 0 (axis/subdomain files must exist to link against), Phase 3 (per-work).

### Phase 5 — Tension pass
**Fan-out unit:** loosely parallelizable for *spotting* candidate tensions
(e.g. one pass per subdomain or per pair of figures with overlapping axes);
**resolution itself is sequential and Nathan-guided**, same reasoning as Phase 2.
**Do:** scan accumulated lessons for cross-figure contradiction; open a
`tension` file (`status: open`) per real conflict found, and add a row to
ledger.md's tension index; Nathan walks through resolution per the
McCarthy→Russell pattern (cited in the frozen project-state.md §2, not
re-derived here); resolution gets written into the bundle file, `status:
resolved`, and the ledger row updated to match.
**Output:** `tension` files, increasingly `resolved` over time, mirrored in
ledger.md's index. Resolved ones get pulled into `tensions/resolutions/index.md`
as a curated highlight reel once there's enough of them to be worth reading as
a standalone piece — not urgent, build it when it earns its keep.
**Depends on:** Phase 4 (needs lessons to find contradictions between).

### Phase 6 — Lint pass
**Fan-out unit:** none, single mechanical sweep, but cheap to re-run — not a
one-time phase, a recurring check.
**Do:** Karpathy-pattern lint plus the checks this structure specifically
needs — orphaned files (no inbound links), lessons citing no axis or no
subdomain, figures with no lessons, dead source links, open tensions gone
stale, axis/subdomain backlink lists out of sync with the tags on the other
side, and duplicate figures that slipped past Phase 1's dedup step.
**Output:** punch list, not bundle content.
**Depends on:** whatever's been built so far; re-run after every batch of
Phases 3-5 work lands, not just once at the end.

### Phase 7 — Distillation
**Fan-out unit:** none, single synthesis pass.
**Do:** derive the short `@`-referenceable CLAUDE.md-replacement doc from the
full bundle — starting from the root rollup (`index.md`), which has been a
running draft since Phase 1 started, not a from-scratch synthesis. Per §5,
this replaces the current CLAUDE.md content, doesn't sit alongside it.
**Output:** the actual pluggable guidance doc — the deliverable everything else
was in service of.
**Depends on:** Phases 3-6 substantially complete, at least for the first
distillation pass; can re-run distillation as the bundle grows.

**Decided 2026-08-01, before writing:**
- **Audience is other people's CLAUDE.md files, not Nathan's.** The artifact ships
  standalone into codebases it has never seen. No reference to this project, this
  bundle, or anyone's personal preferences. Nathan's own CLAUDE.md is the thing
  this is meant to beat, not a constraint to fit inside — an earlier draft of this
  spec had that backwards.
- **Length: 1,200-1,500 words.** Not a token-cost argument; 6k tokens is noise
  against a 200k window. The binding constraint is that instruction-following
  degrades with instruction count, and this lands on top of whatever project
  instructions the user already has. Being a bad citizen of their budget is how a
  doc gets deleted.
- **Inclusion test, which is what actually sets the length.** A claim earns a slot
  only if it would change a decision AND an agent would not already make that
  decision by default. The second half does the cutting: "prefer simplicity",
  "write tests", "avoid premature abstraction" are model defaults, and spending
  words on them costs attention while buying nothing. What survives is the
  counterintuitive material.
- **Claims carry attribution.** "Name the invariant each operation protects
  (Liskov)" rather than the bare imperative. Roughly 15% word overhead. Two
  reasons: it makes every claim traceable back through the bundle, which is why
  this corpus exists rather than being a list of opinions; and per Nathan, a named
  figure activates knowledge the reading model already has, so the attribution
  does work even for a model that has never seen this bundle.

### Phase 8 — Ingestion quality of life (idea backlog, nothing implemented)

**Status: ideas only. Nothing in this phase has been built, and no file outside
this document has been touched for it.** Phase 8 exists because the bundle's
value is gated on how easily a person or an agent can actually *query* it, which
is a separate problem from building it. Ideas accumulate here as Nathan raises
them; each gets promoted to real work only on his say-so.

**Depends on:** Phase 7 substantially complete (there needs to be a corpus worth
querying), except where an idea is explicitly cheap enough to prototype earlier.

#### 8.1 — "Ask Copilot" on the GitHub repo page (Nathan, 2026-07-28)

**The idea.** A person who lands on this repository on github.com should be able
to click the Copilot chat button in GitHub's web UI and immediately start asking
substantive research questions against the OKF bundle — "what do these figures
disagree about regarding whether proof scales to real software", "which lessons
score on primitive-count and why", "who argues the opposite of Brooks on
essential complexity" — and get answers grounded in the bundle's actual lesson
files rather than in the model's own recollection of these papers.

**Why it is worth doing.** The corpus is 95 figures of abstracted thinking with
citations back to primary sources, organized along axes and subdomains. That
shape is unusually well suited to retrieval-style questioning, and the whole
point of the OKF layout (figures own content; axes and subdomains are
cross-cutting indexes) is that a traversal order exists. Nobody gets that value
from browsing markdown by hand. Making the repo self-explaining to an agent is
the difference between an archive and a usable knowledge base.

**Two audiences, two artifacts, and they are different jobs:**

1. *Agent-facing instructions* — a file telling a coding assistant how to
   traverse this bundle: that `bundle/figures/<f>/lessons/*.md` holds the
   primary content, that `axes/` and `subdomains/` are cross-cutting indexes
   into it rather than sources themselves, that `tensions/` records where
   figures genuinely disagree, that every lesson cites a `work` with a URL so
   claims can be chased to a primary source, and that lessons are deliberately
   abstract (never technique-level).
2. *Human-facing instructions* — a README section telling a visitor that this
   repo is meant to be talked to, and literally where the button is. Most
   GitHub users with a Copilot subscription have never used it as a "ask this
   repository questions" tool, so the instruction has to be explicit rather
   than assumed.

**Likely mechanism, with the part I am not sure about flagged.** GitHub supports
repository-level custom instructions at `.github/copilot-instructions.md`, which
is the natural home for the agent-facing file. What I have *not* verified is
whether the web "Ask Copilot" surface on a repo page honors that file the same
way the IDE integrations do — that needs checking against current GitHub docs
before we design around it, because if the web chat ignores it the whole idea
needs a different delivery vehicle (a prominently linked `AGENTS.md`, or
instructions embedded in the README itself where the chat will definitely see
them). Treat the mechanism as an open question, not a settled design.

**Design rule for everything in this phase: consumer surfaces do not expose
build-time bookkeeping.** `extraction: complete`, the `survey_*` fields, the
Tier 1/Tier 2 confidence split in [ledger.md](ledger.md) — none of that belongs
in an instruction file, a README, or anything else a bundle *consumer* touches.
Those exist so we can audit our own pipeline; a reader asking what these figures
thought about abstraction has no use for them, and surfacing them would only
teach a stranger to hedge on content we are confident in. Same principle the
bundle already follows internally: an abstraction layer presents a coherent
worldview and does not leak the mechanics underneath. If we later decide to
tighten the remaining loose ends, that is implementer work and stays on our side
of the line.

**Open questions to resolve before building:**
- Does GitHub's web Copilot chat read `.github/copilot-instructions.md`? If not,
  what does it read?
- How much of the bundle fits in that surface's context, and does it retrieve
  across files or only see what is linked? This determines whether the
  instruction file should teach traversal or instead point at a small number of
  pre-synthesized entry points (the root `index.md`, the axis rollups).
- Do the Phase 7 distilled doc and this instruction file want to be the same
  artifact or deliberately separate ones?

**Stretch goal Nathan named:** that this becomes worth posting to Hacker News —
"here is a knowledge base you can interrogate with a button you already have."
That reframes the deliverable slightly: the repo's front door has to be
legible to a stranger in about thirty seconds, which is a README problem more
than a corpus problem.

#### 8.2 — (next idea)

Placeholder. Nathan has more ideas beyond 8.1; they get numbered here as they
arrive so the backlog stays one list rather than scattering across the doc.

### Phase 9 — Cleanup (known-gap backlog, opened 2026-08-01)

**Fan-out unit:** per item; most are one targeted agent each.
**Do:** work the list of *known, specific* defects and deferred decisions that
accumulated while Phases 3-5 ran. This is deliberately not a lint pass — Phase 6
finds problems mechanically, Phase 9 holds problems already found and named, each
with the evidence that found it.
**Output:** corrections to bundle content, plus decisions recorded in the ledger.
**Depends on:** nothing; can run at any time. Does not gate Phase 7.

Open items, newest first. Each names how it was found, because that is usually
what tells you how to fix it.

1. **Cox's rebuttal of the essence/accident split was never extracted.**
   `cox/what-if-theres-a-silver-bullet` carries `extraction: complete` and three
   lessons, none of which is his direct answer to Brooks — that every item on the
   essential-difficulty list is a surmountable obstacle, plus the two he says
   Brooks omitted. Found by a Phase 5 spotting agent, which correctly refused to
   open a Cox-vs-Brooks tension file against a lesson that does not exist. Brooks's
   side *is* in the corpus (`complexity-that-is-the-subject-cannot-be-abstracted-away`
   among others). Fix: one targeted extraction pass at that argument, then re-run
   the tension check. **Do not write the tension first and back-fill the lesson.**

2. **Knuth's side of the goto argument was never ingested.** The oldest tension
   flagged in this project — Dijkstra's *Go To Statement Considered Harmful* vs.
   Knuth's *Structured Programming with go to Statements* (1974) — cannot be
   written, because that Knuth paper is not among his five ingested works and
   TAOCP is excluded as paywalled. Dijkstra's side is richly represented. The
   paper is freely available and was simply never queued; sourcing it is the whole
   fix. Same failure mode as item 1.

3. **Russell is not in the figure set.** The McCarthy → Russell row has said so
   since it was written. No action needed unless the tension is wanted as a file —
   the pattern itself is already doing its job as the corpus's standing
   dissolution template (project-state.md §2), and it shaped several Phase 5
   resolutions. Listed only so nobody re-discovers it as a defect.

4. **`reynolds/definitional-interpreters-for-higher-order-programming-languages`
   contradicts its own attestation.** It carries `extraction: complete` while its
   body records that the separately published *Definitional Interpreters Revisited*
   retrospective "remains unmined". Found by a reynolds extraction agent. Fix is a
   scoping call: either the retrospective is a distinct work needing its own entry,
   or the attestation is overstated. Leaning toward the former.

5. **Tier 4 attestations are unaudited.** See flags H.10. Four books
   (`jones/software-development`, `sussman/SICP`, `church/introduction-to-mathematical-logic`,
   `hoare/CSP`) are attested on the union of several passes' coverage notes, with no
   single reader having seen the whole work. Cheap mechanical audit available:
   check that the union of line spans claimed across each coverage note is
   contiguous from 1 to EOF. Would have caught the church note that recorded spans
   as both complete and unread.

6. **Tier 3 backlinks are unverified.** See flags H.8. 92 lessons across 7 figures
   had their work-file links reconstructed from their own frontmatter after the
   writing agent died. Nothing is known to be wrong; spot-checking a sample against
   the named sources is cheap and has never been done.

7. **Four works have no obtainable source.** See flags H.7 — two Kolmogorov papers
   behind abstract-only pages, Turing's *Computability and lambda-definability*,
   and a Valiant entry whose URL is a recorded talk. Decide per work: source it,
   substitute it, or drop it from the figure's list. Until then 446/450 is the
   attestation ceiling and 95/95 figures is correct only because these are marked
   `SOURCE-UNOBTAINABLE`.

8. **Chapter-offset records disagree.** `ullman/mining-of-massive-datasets`'s
   coverage note and `scratchpad/ullman/CHAPTERS.md` differ by ~30 lines on where
   chapters 6 and 7 begin. Harmless today, but resume points are read off these.

9. **The 11 single-lesson works were never spot-checked.** See flags section G.
   A work yielding exactly one lesson is either genuinely thin or a died-early
   extraction; the two are indistinguishable without opening the source.

10. **Standing questions from earlier phases:** Péter and Kleene lesson grounding,
   and the self-reported chapter gaps in Goldberg.

## Open before Phase 3 can start
Nothing — Phase 2 closed 2026-07-24, all 95 figures accepted and
layer-placed. Phase 3's per-figure fan-out is unblocked for the whole roster
at once, though it can still run incrementally rather than as one giant
batch. Not started autonomously alongside this Phase 2 close — it's a
separate, large fan-out task and Nathan hasn't kicked it off yet.
