---
type: lesson
title: "When two summaries observe the same entities, combine them by matching"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [databases-and-data-management, distributed-systems-and-concurrency]
tags: [lesson]
---
# When two summaries observe the same entities, combine them by matching

**Lesson:** Merging two summaries is often treated as a single generic operation: pool everything and let the combining rule sort it out. That is right only when the two summaries describe disjoint things. When they are instead two independent observations of the same underlying set of entities — the same populations counted in two consecutive windows, the same services reported by two monitors, the same accounts seen by two shards — pooling is the wrong operation. The correct operation is a matching: pair each item on one side with the item on the other side that is the same entity, combine within each pair, and forbid combination within a side entirely. Forbidding it is the load-bearing part, because it is how the model's central claim gets encoded in the algorithm. If the two sides really do observe the same entities, then two items on the same side are, by construction, different entities and must never be fused.

That prohibition also tells you what the combined result should look like before you compute it, which is a rare and valuable check. The merged summary should have the same number of items as each input, not the sum. Any deviation means either the matching failed or the assumption did, and both are worth knowing about. Compare the generic pooling approach, where the result's size is whatever the combining rule happened to produce and there is nothing to compare it against. Building the expected shape into the operation converts a silent quality problem into an assertion.

The matching itself should be chosen globally rather than greedily. Pairing each item with its nearest counterpart one at a time is fast and produces conflicts and orphans; choosing the assignment that minimises total mismatch across all pairs is the operation the model actually calls for, and it is a standard assignment problem, cheap at the sizes these summaries usually have. The greedy version is a false economy that shows up as occasional badly-fused entities, which are then very hard to diagnose downstream because the resulting summary is well-formed and merely wrong.

There is a failure mode with a specific remedy. The matching is only well posed when entities move slowly enough between observations that each one's counterpart is unambiguous. When they move faster, the assignment becomes genuinely ambiguous and no better algorithm rescues it — the information needed is not present. The fix is upstream: keep finer-grained summaries than the answer requires, so that entities are represented by several items each and the pairing works at a resolution where movement is small, and defer the coarsening to the moment the answer is actually demanded. That is a real design rule with a real cost, and the parameter that sets it is not an accuracy knob but a statement about how fast you believe the underlying world changes.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 7's bucket-merging step in the BDMO stream-clustering algorithm, which finds the best matching between the k clusters of one bucket and the k of the next by minimising the total distance between matched representatives, explicitly declines to merge two clusters from the same bucket on the grounds that each bucket contains a representation of every true cluster, and recommends maintaining more than k clusters per bucket when the representatives migrate quickly enough to make the matching ambiguous.
