---
type: lesson
title: "When the stopping rule comes from outside, return the whole trajectory"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# When the stopping rule comes from outside, return the whole trajectory

**Lesson:** Some procedures have no intrinsic finish line. They repeat a combining step until everything is one thing, and every intermediate state along the way is as legitimate an answer as any other. When you notice that the only available stopping rules are imported from outside — a count somebody told you, a quality threshold somebody chose, a heuristic about when the next step looks bad — you have learned something about the output type. The procedure does not compute an answer; it computes an ordered family of answers, and picking one of them is a separate decision belonging to whoever has the outside knowledge.

The design consequence is to change what the function returns. Emit the sequence of merges, or equivalently the nested structure they induce, and let the caller cut it wherever their criterion says. This is strictly more useful and costs nothing extra, since the procedure had to compute the whole sequence anyway. It also fixes a common workflow disaster: when the threshold is baked in, changing your mind about it means recomputing from scratch, so people avoid exploring, and the first threshold anyone guessed becomes permanent. With the trajectory in hand, re-cutting is trivial and exploring is cheap, so the parameter actually gets examined.

The structure is often more informative than any single cut, and worth returning for its own sake. The order in which things merged, and the distances at which they merged, encode relationships that survive whatever cut you eventually take — which groups are tightly bound, which are marginal, which merged only at the very end. In some applications that nesting is the actual object of interest and the flat grouping is a lossy projection of it. Any procedure that only exposes the projection is discarding evidence it already computed.

The general habit is to notice when a parameter you are about to accept as input is really a choice about how to summarise an output. Number of groups, cutoff score, confidence level, top-k, retention window — all of these frequently sit at the end of a computation that produced the full ranking or the full history anyway. Returning the richer object and letting the caller reduce it is nearly always the better factoring, and the exceptions are cases where the full object is genuinely too large to hand over, which is a size argument you should have to make rather than assume.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the hierarchical-clustering sections of the clustering chapter, which enumerate the stopping options (a known group count, an adequacy threshold on the merged group, or continuing to a single group and returning the tree of merges) and note that the tree is the meaningful answer in applications such as inferring the branching order of species.
