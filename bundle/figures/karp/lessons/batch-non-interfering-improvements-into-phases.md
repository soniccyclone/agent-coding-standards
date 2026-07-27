---
type: lesson
title: "Stop optimizing the single step; find the batch of non-interfering steps and bound how many batches there are"
figure: karp
works: [an-n-5-2-algorithm-for-maximum-matchings-in-bipartite-graphs]
axes: [parallelizability, verifiability]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Stop optimizing the single step; find the batch of non-interfering steps and bound how many batches there are

**Lesson:** The natural way to write an iterative improvement loop is one improvement per pass: search, apply, search again. Hopcroft and Karp say plainly that this framing is the mistake, and that successive improvements should not be treated as independent computations at all. The unit of attention should be the phase: a whole set of improvements that do not touch each other, discovered together and applied together. Once you look for that unit, two separate questions replace the one you were asking. How much does a phase cost, and how many phases can there be? Each is attacked by a different argument, and the product is your total.

Both arguments turn on structure rather than cleverness. Within a phase the improvements are chosen to share the same length and to be disjoint, which is what makes them non-interfering: applying one does not invalidate another, so a single traversal can collect a maximal batch for essentially the cost of finding one improvement. The count of phases comes from a monotone quantity. The length of the shortest available improvement never decreases as the process runs, lengths are bounded by the size of the graph, and once the shortest available improvement has grown past a certain point there cannot be many improvements left. Put together, the number of phases lands well below the number of individual improvements, and a bound that had been the product of two large factors becomes the product of a large one and a small one.

The transferable habit has two halves and most engineers only practice the first. When you have a loop that repeatedly finds and applies one change, ask what makes two changes independent, then restructure to gather and apply all mutually independent changes per pass. This is the reasoning behind batched writes, per-pass graph rewrites in a compiler, and any traversal that collects work instead of restarting for each item. The second half is what makes it more than a micro-optimization: find the quantity that changes monotonically across passes, because without it you have merely reorganized the work, whereas with it you have a proof that the number of passes is small. A batching scheme with no monotone measure can still run for as many passes as there were original steps.

**Source:** [An n^5/2 Algorithm for Maximum Matchings in Bipartite Graphs](../works/an-n-5-2-algorithm-for-maximum-matchings-in-bipartite-graphs.md) — the paper's explicit reframing of the computation into phases, its results establishing that improvement lengths are nondecreasing and that equal-length improvements are disjoint, and the counting argument bounding the number of phases by roughly the square root of the answer's size.
