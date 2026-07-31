---
type: figure
title: Robert E. Tarjan
description: b. 1948, Princeton. Formalized depth-first search with provable linear-time bounds; foundational amortized-analysis work.
status: accepted
layer: implementation-mapping
subdomains: [algorithms-and-complexity]
tags: [figure, accepted]
---

# Robert E. Tarjan

**Dates:** b. 1948. American computer scientist, Princeton University.

## Why a candidate
Formalized depth-first search as a rigorous algorithmic technique with provable linear-time bounds, and did foundational amortized-analysis work on data structures (splay trees, Fibonacci heaps) — cost-as-formal-property is essentially his research program.

## Top 10 most influential works
Phase 3 recheck resolved every entry to a public copy — none of the original `paywalled`/`uncertain` flags held up once each paper was checked directly. Formal-publisher links (SIAM/JACM/JCSS/CACM) stayed behind paywalls throughout; every entry below is a self-archived, institutional, or course-mirror copy instead. See `works/` for full citations:
1. "Depth-First Search and Linear Graph Algorithms" (1972, SIAM J. Comput.) — `public` (course-mirror scan, UCSB)
2. "Efficiency of a Good But Not Linear Set Union Algorithm" (1974 UCB tech report / 1975 JACM) — `public` (UC Berkeley EECS tech-report archive)
3. "Self-Adjusting Binary Search Trees" (1985, with Sleator, splay trees) — `public` (self-archived, Sleator's CMU site)
4. "Fibonacci Heaps and Their Uses in Improved Network Optimization Algorithms" (1987, with Fredman) — `public` (course-mirror scan, Princeton)
5. "A Data Structure for Dynamic Trees" (1983, with Sleator) — `public` (self-archived, Sleator's CMU site)
6. "Amortized Efficiency of List Update and Paging Rules" (1985, with Sleator) — `public` (self-archived, Sleator's CMU site)
7. "Efficient Planarity Testing" (1973 Cornell TR / 1974 JACM, with Hopcroft) — `public` (Cornell eCommons TR repository, via Wayback snapshot — live item page currently 202s to automated fetches)

## Lessons
Tarjan's discipline begins before any algorithm exists: choose the cost measure first, because the measure decides the answer, and price each interface operation by what it forces on the implementation rather than by what it looks like from outside. A model that permits arbitrage is simply the wrong model, and getting the prices right prunes the strategy space for free. Much of his thinking is about where to put bookkeeping so the analysis collapses. Funnel every mutation through one operation so invariant maintenance has exactly one home; order the work so items nest and the bookkeeping becomes a stack; speed a method up by re-hosting its bookkeeping rather than rewriting its logic. Rather than making repair cheaper he prefers ordering the work so nothing needs repairing, and where damage is unavoidable he tolerates a bounded amount of it and lets the accounting choose the threshold. His amortized arguments come with a warning he states plainly: interchangeable at the interface is not interchangeable at the guarantee, since an amortized component cannot hold up a per-operation promise. Two proof habits generalize well beyond algorithms — to bound how often a step fires, find a quantity it increments and then audit everything that can decrement it; and to prove you beat every rival, run the rival inside the proof and make the disagreement itself the ledger. He is equally firm about honesty in results: measure improvement against inputs that actually occur, and publish the outcome even when it goes against you.
