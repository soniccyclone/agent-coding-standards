---
type: figure
title: Joseph Sifakis
description: b. 1946, Verimag/CNRS Grenoble. Independently co-invented model checking in Europe (with Queille), building the CESAR tool. Turing Award 2007 (shared).
status: accepted
layer: implementation-mapping
subdomains: [formal-methods-and-verification]
tags: [figure, accepted]
---

# Joseph Sifakis

**Dates:** b. 1946. Greek-French computer scientist, Verimag/CNRS Grenoble.

## Why a candidate
Independently co-invented model checking in Europe (with Jean-Pierre Queille), building the CESAR verification tool for concurrent systems against branching-time specifications. Third of the Clarke/Emerson/Sifakis trio — consider vetting together.

## Top 10 most influential works
1. "Specification and Verification of Concurrent Systems in CESAR" (1982, with Queille) — `public` (verified Phase 3; live link dead, recovered via Wayback — see works/cesar-1982.md)
2. "An Example of Specification and Verification in CESAR" (1985, with Fernandez, Schwartz) — `paywalled` (verified Phase 3; no public copy found — see Phase 3 access flag below)
3. "Property Preserving Abstractions for the Verification of Concurrent Systems" (1995, with Loiseaux, Graf, Bouajjani, Bensalem) — `public` (verified Phase 3; corrected from stub's mistaken "1992, with Clarke, Grumberg, Long" — that trio wrote a related but different paper — see works/property-preserving-abstractions-1995.md)
4. "Model Checking: Algorithmic Verification and Debugging" (2009, shared Turing lecture) — `public` (verified Phase 3 — see works/turing-lecture-2009.md)

## Phase 3 access flag
Item 2, "An Example of Specification and Verification in CESAR" (Fernandez, Schwartz, Sifakis, 1985, in *The Analysis of Concurrent Systems*, LNCS 207) has no public copy anywhere checked: not on Sifakis's own Verimag page (which does list plenty of 1990s-2018 papers, just not this one), not on any co-author's page, not on HAL, not on ResearchGate as a free download, and no Wayback snapshot of a self-archived copy exists to fall back to. Only Springer/ACM paywalled listings turn up. This is not treated as blocking: it's a secondary worked-example companion to the 1982 CESAR paper (item 1, confirmed public) rather than an independent contribution, so the candidate case for Sifakis does not rest on it. Excluded from works/ rather than summarized.

## Lessons
Sifakis writes as someone who has to ship verification, and nearly every lesson concerns the gap between a proof and a working system. The premise is that everything you prove is about the model, so the entire guarantee rests on how the model was derived — which makes model construction, not proof search, the load-bearing step. From there the concerns are practical: give an analysis a third answer so exhausting the budget is distinguishable from a real negative; make the negative answer carry evidence, because a tool that only says no is half a tool; and prefer the algorithm that behaves well on the instances you actually get over the one with the better bound. He is unsentimental about generality, advising you to abandon the general theory and specialize the argument to one property and one architecture, and to reason at the level where structure is still visible rather than translating everything down to a single composition primitive. Approximation is treated as engineering rather than compromise: define the best possible version of what you are approximating even when you intend to ship something worse, tabulate which hypothesis buys which class of transferable answer instead of asking whether an approximation is "good," and note that possibility and necessity questions need approximations erring in opposite directions. Two organizational observations round it out — heavy reliance on after-the-fact checking is a symptom of a discipline lacking construction rules, and a method that must be practiced while building competes with building, while one that runs on the finished artifact does not.
