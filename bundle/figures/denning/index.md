---
type: figure
title: Peter J. Denning
description: b. 1942, Princeton/Purdue/GMU/NPS. Invented the working-set model, the theoretical basis for virtual-memory page replacement.
status: accepted
layer: implementation-mapping
subdomains: [operating-systems-and-systems-programming]
tags: [figure, accepted]
---

# Peter J. Denning

**Dates:** b. 1942. American computer scientist; Princeton, Purdue, George Mason, Naval Postgraduate School.

## Why a candidate
Invented the working-set model, the theoretical and practical basis for virtual-memory page replacement and thrashing avoidance in every paging OS since.

## Top 10 most influential works
1. "The Working Set Model for Program Behavior" (1968, CACM) — `public`, confirmed (see works/the-working-set-model-for-program-behavior.md)
2. "Virtual Memory" (1970, ACM Computing Surveys) — `public`, confirmed Phase 3 (self-archived at denninginstitute.com — see works/virtual-memory.md)
3. "Thrashing: Its Causes and Prevention" (1968) — `public`, confirmed Phase 3 (self-archived at denninginstitute.com — see works/thrashing-its-causes-and-prevention.md); corrected from stub's mistaken "with Kahn" — this paper is solo-authored by Denning, confirmed against two independent hosted copies. The stub likely conflated it with Denning & Kevin C. Kahn's unrelated 1975/76 paper "An L=S Criterion for Optimal Multiprogramming".

All three of the stub's listed works verified public on Denning's own self-archive (denninginstitute.com/pjd/PUBS/); none required Wayback fallback. This trio (working-set definition, thrashing diagnosis/prevention, and the consolidating virtual-memory survey) fully covers the figure's "why a candidate" case, so Phase 3 did not go looking beyond it — no work central to the case turned out unavailable, so no Phase 3 access flag needed.

## Lessons

Denning's subject is what to do when a system's behavior is only knowable while it runs. His method starts by replacing a word everyone used loosely with the smallest definition a machine can evaluate — one window, one parameter, that parameter anchored to a physical constant of the hardware rather than fitted to a benchmark — and then insists the definition earn its keep by yielding derivations: growth curves, reentry rates, sensitivities, bounds. From there the recurring moves are about where decisions belong and which quantities they actually consume. Measure instead of predict, because modularity and data dependence destroy the foreknowledge a plan would need; refuse to speculate on that measurement when the moment you would act on it is the moment it goes stale; allocate per tenant with an admission precondition so nobody's latency is a function of who else showed up; and put the decision where both coupled resources are visible, satisfying first the one whose overcommitment fails as a cliff rather than a slope. The failure analysis is the same discipline pointed backwards: differentiate before tuning, read a symptom as evidence about the relation among behavior, policy, and hardware ratio rather than as a verdict on any single part, treat idle capacity as a report about a shortage elsewhere, and check which variable the outcome is genuinely sensitive to before spending effort on the one that is interesting to argue about. Structure carries the rest — pick the granularity so the hard sub-problem has nothing left to decide, split a parameter that two objectives are pulling to optima a hundredfold apart, and name the containment property that makes "more resource cannot hurt" a theorem instead of a hope. Underneath all of it sits a refusal that reads as modern: an automatic mechanism is worth having because it holds up across every configuration rather than winning at one, and it is never a substitute for supplying enough of the resource.
