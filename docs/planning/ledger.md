---
type: figure-ledger
title: Good Programming Corpus — Figure Ledger
description: Live accept/reject/status log for candidate figures, organized by Phase 1 subdomain, plus a running tension index. This is the doc that updates continuously during execution — the four original argument docs are frozen.
tags: [ledger, figures, vetting, tensions]
---

# Figure Ledger

Live tracking doc for [technical-plan.md](technical-plan.md) Phases 1–5. Phase 1
complete as of 2026-07-24: 92 unique candidates across 9 subdomains, post-dedup,
plus 3 added out-of-band via discussion (Chuck Moore, Manfred von Thun, Jerome
Saltzer — same day). **Phase 2 (vetting) complete as of 2026-07-24: all 95
accepted** — Nathan reviewed the full candidate roster and approved every one,
no rejections. Layer placement assigned per figure below and in each stub's
`layer` field. Stub file (`bundle/figures/<slug>/index.md`) remains
authoritative for bio/why-candidate/top-10; this table is the fast-scan index.

## How to read
- **status** — `candidate` (Phase 1, unvetted) → `accepted` / `rejected` (Phase 2).
  All 95 landed on `accepted`; see stub files for the authoritative field.
- **layer** — `design-thought` / `implementation-mapping` / `both`, assigned at
  Phase 2 per the hierarchy resolution (frozen reasoning in the old
  project-state.md — cited, not re-argued here). Worked example from that
  resolution: Dijkstra, Hoare, Kernighan, Pike, Lampson land at
  implementation-mapping *despite* their formal rigor, because their subject
  is the imperative/mechanical/systems world, not Church/Lisp-style
  composition — layer tracks subject-matter lineage, not rigor level.
- Rejections get a one-line reason. Not silently dropped. (None this pass.)
- Names in **bold** were surfaced by more than one subdomain search and appear
  once in the bundle, tagged with every discovering subdomain.

## Candidates by subdomain

### 1. Foundations of Computation
**Church** (also PL&S) · Hilbert · Gödel · **Turing** · Kleene · Post ·
Schönfinkel · Curry · Péter · Kolmogorov · Chaitin

### 2. Programming Languages & Semantics
**Church** · McCarthy · Landin · Strachey · Scott · **Milner** (also Distributed)
· Reynolds · Sussman · Steele · Girard · Backus · **Liskov** (also Distributed,
Prog. Environments) · Chuck Moore (Forth, added 2026-07-24) · Manfred von Thun
(Joy, added 2026-07-24)

### 3. Formal Methods & Verification
Floyd · **Hoare** (also SW Eng, Distributed) · **Dijkstra** (also SW Eng, OS,
Distributed) · Pnueli · Manna · Clarke · Emerson · Sifakis · **Lamport** (also
Distributed) · Abrial · Jones · McMillan

### 4. Algorithms & Complexity
Knuth · Cook · Karp · Tarjan · Hartmanis · Stearns · Rabin · Edmonds · Strassen
· Yao · Valiant

### 5. Software Engineering & Architecture
**Dijkstra** · **Hoare** · Parnas · Brooks · Wirth · Naur · Boehm · Lehman ·
Royce · Booch · Gang of Four (Gamma/Helm/Johnson/Vlissides) · **Saltzer** (also
OS, added 2026-07-24)

### 6. Operating Systems & Systems Programming
**Dijkstra** · **Brinch Hansen** (also Distributed) · Ritchie · Thompson ·
Corbató · Lampson · Denning · Rashid · Cutler · Pike · Torvalds · Wilkes ·
**Saltzer** (also SW Eng, added 2026-07-24)

### 7. Distributed Systems & Concurrency
**Lamport** · **Hoare** · **Dijkstra** · **Liskov** · **Milner** · **Brinch
Hansen** · Lynch · Fischer · Herlihy · Schneider · Brewer · Dolev

### 8. Databases & Data Management
Codd · Bachman · Chamberlin · Boyce · Date · Fagin · Ullman · Abiteboul · Chen
· Stonebraker · Vardi

### 9. Programming Environments & Object Systems
Kay · Ingalls · Goldberg · Dahl · Nygaard · **Liskov** · Sutherland · Reenskaug
· Ungar · Cardelli · Cox

## Phase 2 layer placement
Accepted 2026-07-24, all 95. Design-thought (26) — the Church/Lisp lineage:
Abiteboul, Backus, Cardelli, Chaitin, Church, Codd, Curry, Date, Fagin, Girard,
Gödel, Hilbert, Kleene, Kolmogorov, Landin, McCarthy, Péter, Post, Schönfinkel,
Scott, Steele, Strachey, Sussman, Ullman, Vardi, von Thun.

Both (10) — substantial work squarely in each lineage: Boyce, Chamberlin,
Chen, Chuck Moore, Dahl, Kay, Liskov, Milner, Nygaard, Reynolds.

Implementation-mapping (59) — everyone else: the full Foundations-subdomain
exception is Turing; all of Formal Methods & Verification, Algorithms &
Complexity, Software Engineering & Architecture, and Operating Systems &
Systems Programming land here in full (see the worked-example note above —
rigor doesn't move a figure into design-thought, subject matter does); plus
Bachman, Stonebraker (Databases) and Cox, Goldberg, Ingalls, Reenskaug,
Sutherland, Ungar (Programming Environments) and Brewer, Dolev, Fischer,
Herlihy, Lynch, Schneider (Distributed, non-overlapping names only).

**Torvalds note:** Nathan confirmed 2026-07-24 that a non-publishing
systems-builder's shipped code/documentation is an acceptable substitute for
papers as Phase 3 source material — this was flagged as an open question in
Phase 1 (see Cutler/Torvalds note below) and is now resolved yes, not just for
Torvalds but as the general answer for this shape of candidate (Cutler, Chuck
Moore fit the same pattern).

## Phase 3 status
**Complete as of 2026-07-24.** Scope amended same day it started: source
discovery verifies and formalizes each figure's existing Phase 1 top-10 list
into `work` files rather than an exhaustive from-scratch bibliography sweep —
reasoning and the escape valve (go deeper per-figure if Phase 4 lessons come
up thin) are in [technical-plan.md](technical-plan.md#phase-3--source-discovery-fan-out-per-accepted-figure-in-progress).

**Final tally: 450 `work` files across all 95 figures** (447 from the main
run; Pnueli's 3 backfilled by the follow-up pass below, which cleared the
sole zero-work-file gap). Executed as a pilot (3 figures) followed
by a ~89-figure rolling-queue fan-out, one subagent per figure, capped at 20
concurrent by the harness (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`); each
agent scoped to its own figure's `works/` directory and forbidden from
touching `bundle/log.md` or any other figure's files, to avoid concurrent
writes. Every completion was spot-checked (`ls` on the new `works/` dir)
before the orchestrating session refilled the freed slot.

**Pilot batch (Dijkstra, Lamport, Codd) — done first, validated the approach.**
27 `work` files, every URL independently re-fetched rather than trusting the
Phase 1 guess. Caught 2 dead links and 1 wrong title (Lamport); resolved
several `uncertain`/`paywalled` flags in both directions, including
upgrading three of Codd's IBM Research Reports from `uncertain`/`paywalled`
to `public` on finding legitimate copies. A fourth Codd item (#8, "Recent
Investigations in Relational Data Base Systems") was left `uncertain` in the
pilot and got backfilled later when the Boyce pass (they share a paper —
it's the public paper trail behind Boyce-Codd Normal Form) surfaced the same
source; Codd's `index.md` and `works/` were updated to match once noticed.

**Policy set during the pilot, held for the whole run:** third-party rehosts
of copyrighted material (fan archives, course mirrors, preservation
nonprofits — not the author's own site, not an official open-access venue,
not a Wayback snapshot of a self-archived original) count as citable public
sources when the host looks legitimate, since `work` files are link-only
citations, not redistribution. Nathan's condition: mark every such case so a
batch review can find them later if a host turns out to be a problem. Every
`work` file carries a `host` field (`self-archived` / `institutional` /
`third-party-rehost`) for exactly that review — grep `host: third-party-rehost`
across `bundle/figures/*/works/*.md` to pull the full list; it runs well
past a hundred entries across the full run and isn't reproduced here.

**31 of 95 figures carry a `## Phase 3 access flag`** in their own
`index.md` — a work named in the figure's own "why a candidate" case that
was checked directly plus a Wayback fallback and confirmed genuinely
unavailable (paywalled with no legitimate open copy, or Internet
Archive/controlled-digital-lending only), not just left unchecked. Full list:
Abrial, Bachman, Boehm, Booch, Brooks, Cardelli, Clarke, Cox, Curry, Cutler,
Date, Edmonds, Emerson, Gang of Four, Goldberg, Hilbert, Ingalls, Jones,
Kleene, Lynch, Manna, Nygaard, Parnas, Péter, Pnueli, Rabin, Sifakis, Ullman,
Ungar, Wirth, Yao. Most are non-blocking (the case survives on other public
works); the standout was **Pnueli**, where the main run found all four listed
works — including the founding "The Temporal Logic of Programs" (1977, FOCS),
the single paper his "why a candidate" case rests on — inaccessible, leaving
him the sole zero-work-file figure. A follow-up pass (2026-07-24) cleared it:
NYU Courant preserves Pnueli's complete homepage (`cs.nyu.edu/home/people/
in_memoriam/pnueli/`) including his self-archived files — the main run had
only checked a 2005 Wayback snapshot of the Weizmann copy of his
bibliography, which predates his Dec-2005 upload of the 1977 paper's scan.
Recovered: the 1977 FOCS paper (self-archived scan, render-verified), "On
the Synthesis of a Reactive Module" (1989 POPL — ACM open backfile; gold per
both Unpaywall and Semantic Scholar, though ACM's bot-check still blocks
automated end-to-end verification, the only such caveat in the corpus), plus
the 81-page Manna-Pnueli "Anchored Version of the Temporal Framework" survey
(LNCS 354, 1989, self-archived) as the public stand-in for the two
still-paywalled Springer books. Pnueli's access flag now covers only those
two books, non-blocking. Details in the figure's `index.md` and work files.

**Two corpus-wide caveats surfaced during the run**, worth carrying into
Phase 4: (1) several older foundational papers (Yao's 1977/1979 papers,
Rabin's 1980/1987 papers, Kleene's 1936 Duke Math. J. paper) predate routine
self-archiving norms and were never picked up by course-page rehosts the way
1980s+ papers were — coverage for those figures leans more on secondary
material (surveys, textbooks, retrospectives) than primary papers. (2) A
recurring pattern across ~8 figures (Abrial, Boehm, Booch, Cardelli, Clarke,
Gang of Four, Manna, Ullman) is that the flagship work is a commercial book,
and Internet Archive's copy is controlled-digital-lending (login + borrow
queue + DRM) rather than a free download — that's treated as `paywalled`
under this pass's rules, not `public`, consistently across the whole run.

## Flagged for Phase 2 attention
Pulled from the research agents' own notes — not decisions, just what to weigh.
Superseded by the accept-all outcome above; kept for the historical record of
what got weighed and the vet-together groupings (Clarke/Emerson/Sifakis,
Hartmanis/Stearns, Dahl/Nygaard, McCarthy/Moore/von Thun) since those pairings
informed the layer-placement reasoning even though every member was accepted:
- **Saltzer**, added 2026-07-24 from the cyber/crypto/ML scoping discussion. The
  identified gap once Yao/Rabin (crypto's general-abstraction content, via
  Algorithms & Complexity) and McCarthy (AI's, via Lisp not AI) turned out to
  already be covered by figures who'd earned their spot elsewhere. Saltzer's
  is genuinely general systems-architecture reasoning (End-to-End Arguments,
  protection design principles), not applied crypto/security technique — the
  conclusion from that discussion was don't add crypto or ML/AI as subdomains
  and don't chase more figures from either, but do add this one targeted gap.
  Overlaps Corbató (his doctoral advisor, Multics collaborator) and Lampson
  (adjacent security-design work already in the OS subdomain).
- **McCarthy / Chuck Moore / von Thun — a three-point spectrum on lambda-calculus fidelity**, added 2026-07-24. Forth (Moore) is independent convergent invention, zero exposure to combinatory logic. Lisp (McCarthy) is notation borrowed from Church with semantics that actually diverged (dynamic scoping broke lambda calculus's substitution semantics until Scheme fixed it decades later — McCarthy's stub corrected same day to stop overstating this as "direct translation"). Joy (von Thun) is deliberate, conscious derivation from Curry's combinatory logic. Worth vetting as a set — the contrast is more informative together than any one of them alone.
- **Church, Turing** — already accepted/placed per project-state.md §1–2 (frozen); stubs exist for bundle consistency, not open questions.
- **Schönfinkel + Curry** — combinatory logic is arguably *more* primitive-reduced than lambda calculus (no bound variables at all). Real test case for the primitive-count axis.
- **Hilbert** — antecedent/motivator (posed the Entscheidungsproblem), not a computability theorist himself. Does "posed the question" count as strongly as "answered it"?
- **Clarke / Emerson / Sifakis** — independently co-invented model checking, shared the 2007 Turing Award. Natural trio; consider vetting together.
- **Hartmanis / Stearns** — both thin individually beyond their joint 1965 paper. Consider vetting as a pair.
- **Dahl / Nygaard** — same for Simula; heavy bibliography overlap.
- **Brewer** — weakest formal fit in Distributed Systems & Concurrency (CAP was never a formal proof — that's Gilbert & Lynch, under Lynch's entry). Fold in or keep standalone?
- **Bachman, Stonebraker** (Databases) — deliberately included as mechanism-first counterweights, weighted lower per the research brief, not nominated on equal footing with Codd/Fagin/Abiteboul.
- **Boehm, Royce, Booch, Gang of Four** (SW Eng) — methodology/notation-leaning, weaker fits than Parnas/Dijkstra/Hoare/Naur/Lehman against the primitive-grounded standard.
- **Cutler, Torvalds** (OS) — non-publishing systems builders, no academic papers. Their "top 10 works" are shipped code/documentation, not papers — flagged honestly rather than forced into paper format. Worth confronting directly: real foundational systems work often never got written up.
- **Chen, Vardi** (Databases) — boundary cases, may be cuttable if the corpus needs to stay tightly primitive-first.
- **Kolmogorov, Chaitin** (Foundations) — boundary cases with Algorithms & Complexity; only a thin slice of each is squarely on-subdomain.
- **Knuth** — TAOCP itself excluded from ingestion per §3 (paywalled/DRM'd); only his freely available papers are usable sources, a real constraint on what a Knuth lesson file could actually cite.

## Tension index
Lightweight status table only — full reasoning lives in each `tension` file in
the bundle once Phase 5 runs. This table is for quick scanning, not a
duplicate of the content.

| tension | figures | status | bundle file |
|---|---|---|---|
| McCarthy → Russell | McCarthy, Russell (Russell not yet in figure set — add to queue) | open | not yet created |
| goto considered harmful, or not | Dijkstra, Knuth | open | not yet created |

Second row newly flagged at Phase 2 close (2026-07-24), now that both figures
are accepted — pre-cited as an expected case in project-state.md thread 4.
Dijkstra's "Go To Statement Considered Harmful" vs. Knuth's "Structured
Programming with go to Statements" (1974), which argues goto has legitimate
uses the pure-structured-programming line overstates. Full resolution is
Phase 5's job; flagging here per Phase 2's "note any immediately visible
tension" duty.
