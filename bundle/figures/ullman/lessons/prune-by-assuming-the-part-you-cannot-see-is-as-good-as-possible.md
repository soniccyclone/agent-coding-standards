---
type: lesson
title: "Prune by assuming the part you cannot see is as good as possible"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Prune by assuming the part you cannot see is as good as possible

**Lesson:** To discard a candidate without examining it, you need a bound that holds no matter what the unexamined part contains, and there is a mechanical way to get one. Take whatever coarse facts you do have, imagine the most favourable possible completion consistent with those facts, and evaluate the criterion against that fiction. If even the fiction fails to clear the threshold, the real candidate cannot clear it either, and you may drop it with a proof rather than a guess. The bound is computed from an instance that will never occur, which is what makes the reasoning feel illegitimate the first time and what makes it sound.

The method is uniform in a way that is easy to miss when the individual filters are presented separately, because each one looks like a different clever observation. Knowing only two sizes, the best case is that the smaller collection sits entirely inside the larger, which caps their agreement at the ratio of the sizes and immediately excludes everything outside a narrow window. Knowing additionally that the elements agree from some position onward, the best case is that they are identical from there to the end, which caps agreement by how much was left behind. Knowing additionally how much material follows the indexed position on each side, the best case shifts again and the cap tightens. Each additional fact placed into the key admits a stronger optimistic completion and therefore a tighter bound. The filters are not four inventions; they are one technique applied to four increasingly informative summaries.

That framing tells you where to spend design effort. Every extra attribute folded into the key multiplies the number of buckets, so the question is which attribute most constrains the optimistic completion per bit of key it costs. Cheap scalars that bound the ratio directly, such as sizes and counts, tend to be the best value. It also tells you when to stop: when the optimistic completion is already so constrained that tightening it further excludes almost nothing, additional key material buys nothing but buckets.

The wider practice is to notice that bounds computed against impossible best cases are the engine underneath a great deal of practical search — the admissible heuristic that keeps a shortest-path search from expanding a node, the branch-and-bound cutoff, the query optimiser rejecting a plan on an optimistic cost estimate, the sizing filter that precedes an expensive comparison. In each case correctness comes from a single obligation: the estimate must never be pessimistic about the unseen part. Get that direction wrong by even one case and the pruning silently deletes real answers, which is why the direction deserves an explicit argument every time rather than an appeal to how the filter is meant to behave.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 3's sequence of exact filters for high-similarity matching, which bounds similarity by the ratio of the two string lengths, then bounds it by supposing the shorter string is exactly the tail of the longer beyond the indexed prefix, then bounds it by supposing the two strings agree exactly beyond the positions at which they share a symbol, and finally refines that with the number of symbols following the indexed position on each side.
