---
type: lesson
title: "A cost model is a claim about which resource runs out first"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# A cost model is a claim about which resource runs out first

**Lesson:** Counting operations is a habit, not a law. The right thing to count is whatever the machine you are actually running on exhausts first, and on a cluster of commodity nodes that is not arithmetic — it is the movement of bytes between nodes. Once you accept that, a startlingly coarse accounting becomes the useful one: add up the sizes of the inputs handed to every stage, ignore how long each stage computes, and ignore outputs entirely. The omissions are defensible on physical grounds rather than mathematical ones. Per-item work in these jobs is usually linear and trivial; interconnect bandwidth is orders of magnitude below what a processor can chew through, and contended besides; every intermediate output is some other stage's input and so already counted; and a genuinely huge final output is unusable anyway, which means something downstream is aggregating it and that aggregation's input cost stands in for it.

The discipline that makes this worth having is that you must state the model's escape hatches with it. A metric you can drive to zero by cheating is not a metric — total data movement is minimised by giving all the work to a single node, which is obviously wrong, so the model only ranks designs that already spread work evenly and must be read alongside elapsed time. The same care applies to the accounting of memory: a stage whose working set spills to disk pays a cost the model does not name, so the model's advice is only valid inside the region where each unit's input fits in memory. A cost model with its domain of validity attached is a tool; the same model quoted without it produces confident nonsense.

The payoff is that decisions which look like matters of taste become calculable. Whether to join three relations pairwise or all at once stops being a stylistic preference and becomes an inequality whose terms are relation sizes, join selectivity, and the number of parallel units — and the answer flips depending on those numbers, so neither approach is simply better. Whether one pass or two passes is cheaper likewise turns on the arithmetic and can favour the extra pass by a wide margin, which contradicts the instinct that fewer stages must be faster. A programmer who thinks this way stops arguing about architecture in the abstract, writes down the cost expression for each candidate, and lets the sizes decide — while remembering that they have chosen what to count, and that on different hardware they would have to choose again.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the chapter on cluster programming, in its communication-cost sections: the justification for counting input sizes only, the elapsed-time caveat against concentrating work, and the worked comparisons of cascaded two-way joins against a single multiway join and of one-pass against two-pass matrix multiplication.
