---
type: figure
title: Danny Dolev
description: Hebrew University of Jerusalem. Core contributor to formal Byzantine agreement theory - minimal synchrony conditions, early-stopping protocols.
status: accepted
layer: implementation-mapping
subdomains: [distributed-systems-and-concurrency]
tags: [figure, accepted]
---

# Danny Dolev

**Dates:** BA Hebrew University 1971, PhD Weizmann Institute 1979; Hebrew University faculty since 1982, also IBM Almaden 1987-1993 (birth year not confirmed — omitted).

## Why a candidate
Core contributor to the formal theory of Byzantine agreement — minimal synchrony conditions, early-stopping protocols, and clock synchronization bounds — extending consensus theory from Lamport/Fischer's crash-fault model into actively adversarial fault models.

## Top 10 most influential works
1. "Polynomial Algorithms for Multiple Processor Agreement" (1982, with Strong, STOC) — `public` (self-archived, cs.huji.ac.il/~dolev)
2. "On the Minimal Synchronism Needed for Distributed Consensus" (1987, with Dwork, Stockmeyer, JACM) — `public` (self-archived, cs.huji.ac.il/~dolev)
3. "Early Stopping in Byzantine Agreement" (1990, with Reischuk, Strong, JACM) — `public` (third-party rehost — MIT 6.897 course mirror; not found on Dolev's own site)
4. "Reaching Approximate Agreement in the Presence of Faults" (1986, with Lynch, Pinter, Stark, Weihl, JACM) — `public` (self-archived, cs.huji.ac.il/~dolev)
5. "The Byzantine Generals Strike Again" (1982, J. Algorithms) — `public` (self-archived, cs.huji.ac.il/~dolev)

All 5 confirmed public — see `works/`. List was 5 items in the Phase 1/2 pass, not 10; Phase 3 stayed close to the existing list per scope (seminal-works pass, not an exhaustive bibliography sweep) and found nothing else clearly public-and-central enough to add. Dolev's personal publications page (cs.huji.ac.il/~dolev) turned out to host 4 of the 5 directly.

## Lessons
Dolev's body of work teaches that coordination under failure is governed by
resources and requirements rather than by cleverness, and that both must be
stated numerically before any mechanism is chosen. Since no participant can ever
learn which of its peers are broken, correctness has to be scoped to an explicit
budget on how many may misbehave — read as concurrent rather than lifetime
misbehaviour if the system is to survive real operations — and every combining
step should be built so that the budget itself does the filtering, converting an
unanswerable question about trust into a counting question with a definite
answer. What such a system can achieve is then capped by things the code cannot
buy: population, independent routes through the actual deployment graph, and the
granularity at which the substrate makes a step indivisible. The lever that
remains is the specification. "Everyone agrees" is a family of requirements
whose members differ discontinuously in price along the axes of exactness,
simultaneity, and universality, so the discipline is to pin the requirement at
the weakest point the application tolerates, solve that weak problem on its own
terms instead of wrapping the strong mechanism, and let the bill track the
adversity of the run at hand rather than the provisioning parameter. Running
through all of it is a way of reasoning: arguments about distributed systems are
arguments about which executions a participant can tell apart, models earn their
generality from what they refuse to look at, omnibus adjectives must be split
into independently purchasable guarantees before anything proved about them can
be believed, proofs should be mined for rules of thumb that predict without
proving, and every optimality claim should name the class of solutions it
quantifies over, since that class is where the next gain is hiding.
