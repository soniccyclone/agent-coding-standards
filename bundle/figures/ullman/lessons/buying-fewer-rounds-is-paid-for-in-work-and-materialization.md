---
type: lesson
title: "Buying fewer rounds is paid for in work and in what you must hold"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# Buying fewer rounds is paid for in work and in what you must hold

**Lesson:** In any system where a round of computation carries a fixed coordination cost — a synchronisation barrier, a shuffle, a scheduling latency — the number of rounds is a first-class cost independent of the work inside them. A procedure that follows one step of structure per round takes as many rounds as the structure is deep. You can nearly always cut that: if the relation being built is transitive, composing what you know with itself doubles the reach per round, so depth drops from linear in the structure to logarithmic. On something a thousand steps deep that is a hundredfold reduction in coordination, and it is the difference between a job that finishes and one that does not.

The exchange rate is what makes this a design decision rather than an improvement. Advancing one step at a time lets you drive each round from only the newly discovered facts, and each fact meets only its immediate successors, so total work stays proportional to the size of the data. Composing the accumulated relation with itself means facts meet facts, and the work becomes proportional to a much larger product. The same table can therefore be read two ways: fewest rounds and most work at one end, most rounds and least work at the other, with nothing dominating. Which end you want depends entirely on whether your per-round overhead or your per-unit work is the binding constraint, and that is a property of the platform, not of the problem.

The third column is the one most often left out. Doubling tricks work by computing the general relation between all pairs, so even when you only wanted the answer for a single starting point, you must materialise the general result and discard most of it at the end — and you cannot discard early, because any pair might turn out to be a link in a chain you need. Specialising to one starting point keeps the working set small but reimposes the step-at-a-time depth. So the choice is genuinely three-way between rounds, work, and peak state, and a system can be infeasible on the third axis while looking excellent on the first.

The habit to carry: when a distributed or staged computation is slow, establish first whether it is slow because each round is expensive or because there are many rounds, since the two have opposite remedies. And when you reach for a depth-reducing restructuring, compute the peak intermediate size before committing to it — that is where these techniques usually fail in practice, not in the arithmetic.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the comparison of transitive-closure methods in the social-network chapter, whose table sets reachability at work proportional to the arc count over a number of rounds equal to the diameter, linear transitive closure at node-count times arc-count over the same rounds, and both recursive-doubling variants at cubic work over the logarithm of the diameter; together with the sidebar warning that obtaining a single node's reachable set by doubling requires storing all pair facts, which may be infeasible even where the reachable set is not.
