---
type: lesson
title: "Find the order in which the best answer is a prefix"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, hardware-affinity]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Find the order in which the best answer is a prefix

**Lesson:** A search over "which subset" or "which cut point" looks combinatorial and often is not. The move that collapses it is to find a key such that, when the elements are sorted by that key, the optimal answer is guaranteed to be an initial run of the sorted list. Once that is established, an exponential search over subsets or a quadratic search over pairs of boundaries becomes a single sweep: consider each position in the order as the boundary, score it, keep the best. The hard part is never the sweep; it is identifying the key and arguing that the optimum must be a prefix under it.

That argument is usually short and is worth insisting on rather than assuming. For a criterion that improves when the two sides are made internally homogeneous, sorting elements by their propensity toward one outcome does it: any subset that is not a prefix contains an element with lower propensity while excluding one with higher, and exchanging them cannot make the split worse. The exchange argument is the standard shape, and if you cannot produce one, you do not have the reduction and the sweep may miss the optimum.

Two mechanical points make the sweep genuinely linear rather than linear-looking. The statistics for the prefix are maintained incrementally as you advance — each step adjusts a running count instead of recomputing over everything seen. And the statistics for the suffix never need their own pass: they are the totals minus the prefix, which is a subtraction. Forgetting the second turns one sweep into two or, worse, into a nested loop, which is a common way this optimisation is left half-finished. Watch also for ties in the sort key, where a boundary between equal values does not correspond to any realisable split and must be skipped.

The general prompt: when facing a choice among many subsets or thresholds, ask what quantity, if you sorted by it, would make the good answers contiguous. Sorting is cheap, it parallelises, and it converts an intractable choice into an obviously tractable one — but only if you can state why contiguity holds, which is the step that separates a sound reduction from a plausible-looking heuristic.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the two sections on selecting a decision-tree test in the large-scale-machine-learning chapter: ordering training examples by a numerical feature and sweeping the split point with cumulative per-class counts, obtaining the counts for the far side by subtracting from the totals, skipping split points where consecutive values are equal, and — for a categorical feature with two classes — ordering the feature's values by the fraction of their examples in the first class, on the argument that the lowest-impurity partition must then be a prefix of that order.
