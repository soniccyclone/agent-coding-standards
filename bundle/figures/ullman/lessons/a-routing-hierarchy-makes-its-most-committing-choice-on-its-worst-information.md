---
type: lesson
title: "A routing hierarchy makes its most committing choice on its worst information"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [databases-and-data-management, distributed-systems-and-concurrency]
tags: [lesson]
---
# A routing hierarchy makes its most committing choice on its worst information

**Lesson:** Structures that direct an item to its home by descending a tree of summaries have an asymmetry that their uniform-looking code hides. Every level performs the same operation — compare the item against the digests held here, follow the best one — but the levels are not equivalent. The digest at an interior node necessarily compresses everything in its subtree, so the higher the node, the more it compresses and the less it can distinguish. Meanwhile the higher the node, the larger the region being excluded by choosing one branch over another. The consequence is that the decision with the greatest consequence is made against the least informative summary, and the decisions made against good information are the ones that barely matter because by then the alternatives are all similar anyway.

Worse, the descent is normally single-path and unbacktracked, so an early wrong turn is not corrected by any amount of care lower down. The structure will confidently deliver the item to the best home within a subtree that should never have been entered, and nothing in the result indicates that this happened. This is what separates a routing hierarchy from a search hierarchy: a search can widen and revisit, a route commits. If you have built the second while reasoning about it as the first, your error analysis is wrong in a way testing on well-separated data will never show.

Two responses follow, and they are cheap enough to be defaults. The first is to spend your fidelity budget unevenly — allow interior nodes near the root to carry richer or more numerous digests than those near the leaves, since that is where discrimination is scarce and consequential. Uniform node capacity is a storage convenience, not a correctness requirement. The second is to allow the descent to keep more than one candidate branch alive when the top choices are close, and to prune only once the summaries have become discriminating enough to justify it. That is a bounded amount of extra work, concentrated exactly where the risk is, and it converts an unrecoverable commitment into a deferred one.

The recognition generalises well past trees of summaries. Any layered dispatch has this shape: a request routed to a region, then a cell, then a host; a case triaged by category before anyone looks at the details; a query planner choosing a join order before it knows the intermediate sizes. In each, the coarsest description drives the least reversible choice. Asking which decisions in a pipeline are both early and irreversible, and then checking what evidence was available when they were made, tends to locate the real source of bad outcomes faster than examining the stages that do the visible work.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 7's description of point insertion in the GRGPF algorithm, where interior nodes hold fixed-size samples of the representatives beneath them, a point is routed by following the child with the closest sampled representative down a single path to a leaf, and the text observes that as one goes up the tree the probability of any given cluster's representative appearing in the sample diminishes.
