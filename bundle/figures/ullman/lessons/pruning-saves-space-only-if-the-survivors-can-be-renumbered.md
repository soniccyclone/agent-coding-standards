---
type: lesson
title: "Pruning saves space only if the survivors can be renumbered densely"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# Pruning saves space only if the survivors can be renumbered densely

**Lesson:** Deciding that you no longer need to track certain elements is not the same as reclaiming the space they occupied, and the gap between the two is where a good-looking optimisation quietly fails to pay. A dense structure addresses its entries by computing a position from an identifier, which is why it needs no per-entry keys and no lookup machinery. That arithmetic assumes the identifiers form a contiguous range. Prune a scattered subset of them and the range has holes; the addressing function still maps into the same span; the memory is still allocated. You have eliminated work, not footprint.

There are two outcomes, and which one you get is decided by whether the pruning criterion lets you relabel. When survivors can be enumerated up front and assigned fresh consecutive numbers, a small renumbering table converts the logical prune into a physical one and the saving is real — and it compounds, because a structure quadratic in the identifier count returns a quadratic saving for a linear cull, so removing half the identifiers frees three-quarters of the space. When the pruning criterion is data-dependent in a way that scatters the removals unpredictably across the space, no relabelling exists: you cannot renumber to close holes whose positions you only learn as you go, and you are forced onto a sparse representation that stores an explicit key with every entry.

That forced switch is what has to be priced, and it converts a qualitative argument into an inequality anyone can evaluate. The sparse layout costs several times as much per surviving entry as the dense one, since it carries identifiers alongside the value plus whatever index makes lookup fast. So a pruning technique that forces the switch has to eliminate more than that overhead ratio's worth of entries before it breaks even — eliminate a third of the candidates and you have made things strictly worse than not pruning at all, despite the pruning being correct and the candidate count genuinely lower. The technique is not bad; it simply has a threshold below which it is a loss, and the threshold is computable from the two layouts' per-entry sizes before you implement anything.

The transferable habit is to evaluate a filter on two axes rather than one. How much does it remove is the obvious axis. What representation does the survivor set now require is the one people skip, and it can dominate. This is the same accounting that decides whether to compact a heap or leave the holes, whether a bitmap or an id list is the right set representation after a selective query, and whether a sparse matrix format earns its keep — and in each case the answer flips at an occupancy fraction rather than being uniformly one way.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 6's account of why PCY cannot use the triangular-matrix layout that A-Priori can, since the pairs it avoids counting are scattered randomly through the matrix with no way to compact around them, so PCY must use triples and gains nothing unless it eliminates at least two-thirds of the pairs of frequent items; together with the same chapter's note that A-Priori renumbers just the frequent items precisely so the triangular matrix can be sized to them.
