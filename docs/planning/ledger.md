---
type: figure-ledger
title: Good Programming Corpus — Figure Ledger
description: Live accept/reject/status log for candidate figures, organized by Phase 1 subdomain, plus a running tension index. This is the doc that updates continuously during execution — the four original argument docs are frozen.
tags: [ledger, figures, vetting, tensions]
---

# Figure Ledger

Live tracking doc for [technical-plan.md](technical-plan.md) Phases 1–5. Phase 1
complete as of 2026-07-24: 92 unique candidates across 9 subdomains, post-dedup.
All `status: candidate` in their stub files under `bundle/figures/<slug>/index.md`
— **nothing here is vetted yet.** This table is the fast-scan index; the stub
file is authoritative (bio, why-candidate, top-10 works with public/paywalled
flags).

## How to read
- **status** — `candidate` (Phase 1, unvetted) → `accepted` / `rejected` (Phase 2).
- **layer** — `design-thought` / `implementation-mapping` / `both`, assigned at
  Phase 2 per the hierarchy resolution (frozen reasoning in the old
  project-state.md — cited, not re-argued here).
- Rejections get a one-line reason. Not silently dropped.
- Names in **bold** were surfaced by more than one subdomain search and appear
  once in the bundle, tagged with every discovering subdomain.

## Candidates by subdomain

### 1. Foundations of Computation
**Church** (also PL&S) · Hilbert · Gödel · **Turing** · Kleene · Post ·
Schönfinkel · Curry · Péter · Kolmogorov · Chaitin

### 2. Programming Languages & Semantics
**Church** · McCarthy · Landin · Strachey · Scott · **Milner** (also Distributed)
· Reynolds · Sussman · Steele · Girard · Backus · **Liskov** (also Distributed,
Prog. Environments)

### 3. Formal Methods & Verification
Floyd · **Hoare** (also SW Eng, Distributed) · **Dijkstra** (also SW Eng, OS,
Distributed) · Pnueli · Manna · Clarke · Emerson · Sifakis · **Lamport** (also
Distributed) · Abrial · Jones · McMillan

### 4. Algorithms & Complexity
Knuth · Cook · Karp · Tarjan · Hartmanis · Stearns · Rabin · Edmonds · Strassen
· Yao · Valiant

### 5. Software Engineering & Architecture
**Dijkstra** · **Hoare** · Parnas · Brooks · Wirth · Naur · Boehm · Lehman ·
Royce · Booch · Gang of Four (Gamma/Helm/Johnson/Vlissides)

### 6. Operating Systems & Systems Programming
**Dijkstra** · **Brinch Hansen** (also Distributed) · Ritchie · Thompson ·
Corbató · Lampson · Denning · Rashid · Cutler · Pike · Torvalds · Wilkes

### 7. Distributed Systems & Concurrency
**Lamport** · **Hoare** · **Dijkstra** · **Liskov** · **Milner** · **Brinch
Hansen** · Lynch · Fischer · Herlihy · Schneider · Brewer · Dolev

### 8. Databases & Data Management
Codd · Bachman · Chamberlin · Boyce · Date · Fagin · Ullman · Abiteboul · Chen
· Stonebraker · Vardi

### 9. Programming Environments & Object Systems
Kay · Ingalls · Goldberg · Dahl · Nygaard · **Liskov** · Sutherland · Reenskaug
· Ungar · Cardelli · Cox

## Flagged for Phase 2 attention
Pulled from the research agents' own notes — not decisions, just what to weigh:
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
