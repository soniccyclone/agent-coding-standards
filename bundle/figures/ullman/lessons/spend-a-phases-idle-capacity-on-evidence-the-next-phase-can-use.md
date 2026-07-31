---
type: lesson
title: "Spend a phase's idle capacity on evidence the next phase can use"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# Spend a phase's idle capacity on evidence the next phase can use

**Lesson:** In a multi-phase computation the phases rarely have the same resource profile, and the early phase is often the light one — it touches all the data but keeps almost nothing, leaving most of the machine idle while the later phase is the one that runs out of room. That idle capacity is free, in the strict sense that using it costs no additional passes and no additional wall time, since the data is already streaming past. The move is to spend it collecting a coarse, lossy summary of information that the expensive phase can use to rule work out. You are not trying to answer the later question early; you are trying to accumulate cheap negative evidence.

Coarseness is what makes this work, and it should be embraced rather than apologised for. Aggregate many distinct candidates into a single shared accumulator, and interpret the result asymmetrically: a large accumulator tells you nothing, because any of its contributors might be responsible, but a small one is a proof about every contributor simultaneously. One number therefore certifies the absence of a whole group. Whether that pays depends on how skewed the population is — if almost every accumulator ends up large, you have learned nothing and wasted only capacity you were not using — so it is worth estimating the expected distribution from the data volume and threshold before building it, an estimate that takes a few lines of arithmetic. The summary can then be compressed to one bit per accumulator for the next phase, which is what makes it cheap enough to carry alongside the expensive phase's own state.

The caveat is the part most people skip, and it is where this kind of optimisation actually fails. Pruning that removes an arbitrary, unpredictable subset of candidates destroys the ability to address the remaining candidates by position, which is exactly what a dense layout requires. The pruned computation is therefore forced into a sparse representation carrying several times the per-entry overhead, and it has to eliminate a large fraction of the candidates just to break even against the unpruned version using the dense layout. That break-even fraction is computable from the two representations' per-entry costs, and computing it is the difference between an optimisation and a plausible-sounding regression. An improvement that changes which representation is legal must pay for the representation it took away.

Generalised: look at each phase of a pipeline and write down which resource it leaves unused. Then ask what could be learned during that phase, at zero marginal I/O, that would shrink the phase that is actually constrained. And before adopting it, check what structural assumption the new information invalidates downstream.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the sections of the frequent-itemsets chapter on the Park-Chen-Yu algorithm, which fills the unused first-pass memory with a hash table of bucket counts, converts it to a bitmap between passes, and the accompanying argument that because the surviving pairs can no longer be stored in a triangular array, the technique must eliminate roughly two thirds of the candidate pairs before it beats the simpler algorithm.
