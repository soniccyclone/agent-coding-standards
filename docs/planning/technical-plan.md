---
type: execution-plan
title: Good Programming Corpus — Technical Plan
description: Phased build pipeline for the OKF bundle. Phases 0-3 complete (95 figures, all accepted; 450 work files across all 95 figures); Phase 4 (lesson extraction) next.
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
3. **`axes/<axis>.md`** — synthesized from lessons scored on that axis, orthogonal to subdomain.
4. **`index.md`** (root) — synthesized from the nine subdomain rollups.

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

## Open before Phase 3 can start
Nothing — Phase 2 closed 2026-07-24, all 95 figures accepted and
layer-placed. Phase 3's per-figure fan-out is unblocked for the whole roster
at once, though it can still run incrementally rather than as one giant
batch. Not started autonomously alongside this Phase 2 close — it's a
separate, large fan-out task and Nathan hasn't kicked it off yet.
