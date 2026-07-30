---
type: lesson
title: "Evaluate mitigations in combination, and prefer ones that cover different failure modes"
figure: tarjan
works: [efficiency-of-a-good-but-not-linear-set-union-algorithm]
axes: [hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Evaluate mitigations in combination, and prefer ones that cover different failure modes

**Lesson:** The structure at the centre of this paper has two optional refinements, each a couple of lines. One decides which of two groups gets attached under the other when they merge, favouring the larger. The other flattens the chain you just walked, reattaching everything on it directly to the top. The published record on them, which Tarjan lays out as a table of prior results, is the interesting part. Without either refinement the cost is quadratic. With only the first, it drops to roughly logarithmic per operation. With only the second, also roughly logarithmic per operation. Judged one at a time, they look like interchangeable log-factor tricks, and a reasonable engineer would implement whichever was more convenient and consider the matter closed. Together they produce a bound so close to linear that the gap is a function almost nobody encounters — an improvement of a completely different order than either alone suggests.

The reason the combination outperforms the sum is that the two refinements address different mechanisms of failure. One prevents a deep chain from ever being *constructed*, by refusing merges that stack a big structure under a small one. The other repairs depth that has already been traversed, retroactively, at the moment its cost is paid anyway. An adversary trying to force expensive work has to defeat both: build depth despite the merge rule, and get value from that depth repeatedly despite the flattening. Any strategy that beats one is undone by the other. Contrast two mitigations that attack the same mechanism, where the second is nearly redundant and the measured benefit of adding it is close to zero.

The transferable habit has two parts. First, never conclude from independent measurements that two changes are comparable in value; measure the cross terms, because interaction effects between mitigations can be larger than either main effect and they are invisible to one-at-a-time evaluation. Second, when choosing what to add, classify candidates by *which failure mechanism* they close rather than by how much they helped in isolation. Two techniques that close the same mechanism are worth roughly one; two that close complementary mechanisms — prevention and repair, in this case — can leave an adversary with no move at all. That framing also tells you where to stop: once every mechanism you can identify is covered, further mitigations are buying constants.

**Source:** [Efficiency of a Good But Not Linear Set Union Algorithm](../works/efficiency-of-a-good-but-not-linear-set-union-algorithm.md) — the introduction's statement of the collapsing rule and the weighted union rule, followed by the four cited bounds for neither rule, each rule alone, and both together, with the remark that using both makes the algorithm much harder to analyze, and the paper's own near-linear bound for the combination.
