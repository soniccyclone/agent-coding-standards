---
type: lesson
title: "Deduplicate with a canonical order, not with a memory"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, primitive-count]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Deduplicate with a canonical order, not with a memory

**Lesson:** Whenever a structure can be discovered from several of its own parts — a group of three found by starting from any of its three members, a match found from either side — the naive enumeration produces every result several times. The reflex is to keep a record of what has already been emitted and check against it. That record costs memory proportional to the output, needs synchronisation the moment more than one worker is enumerating, and makes each emission depend on the history of every previous one. All of that is avoidable. Fix a total order on the parts and emit a result only from its least part under that order. Each result then has exactly one place it is allowed to be produced, so it is produced exactly once, and the check is a local comparison requiring no state whatsoever.

The property this buys is worth naming precisely: correctness becomes independent of what any other worker did or of what this worker did earlier. That is exactly the property that permits arbitrary partitioning, arbitrary ordering, restarts, retries, and speculative re-execution — a duplicate-suppressing memory forbids all of them or forces them through a coordination point. Trading a shared mutable set for a fixed comparison converts a stateful protocol into a stateless rule, and stateless rules parallelise for free.

The same principle applies to the partitioning itself, not just to what each worker emits. If a job is split into cells indexed by a tuple of coordinates and the underlying problem is symmetric in those coordinates, then cells whose coordinates are permutations of each other are doing redundant work. Requiring the coordinates to be non-decreasing keeps one cell from each equivalence class and discards the rest — cutting the number of cells by the number of permutations, and cutting the data that must be shipped to them by a similar factor. Symmetry in the problem is symmetry in the work, and quotienting it out is a factor you get once and keep.

The design freedom is in the choice of order, and it can be exploited. Any total order gives correctness; a well-chosen one gives correctness plus something else. Ordering by cost so that enumeration starts from the cheapest part bounds the work per result. Ordering by a hash bucket first and identity second makes the order agree with how the data is already distributed, so the canonical position and the physical location coincide. Pick the order deliberately — it is free correctness, and it may be free performance too.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the triangle-counting chapter: the ordering of nodes by degree with numeric tie-breaking used so that each triangle is counted only from the node preceding both others, and the later refinement of the parallel version where nodes are named by their hash bucket paired with their identity, so only reducers whose three bucket numbers are non-decreasing are needed and each edge is shipped to a third as many tasks.
