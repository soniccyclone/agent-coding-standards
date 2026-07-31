---
type: lesson
title: "Find the pigeonhole that makes a local test a complete filter for a global property"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# Find the pigeonhole that makes a local test a complete filter for a global property

**Lesson:** Distributed exactness usually looks impossible for threshold problems, because a quantity can exceed a global threshold while sitting below the threshold on every individual partition, so no worker can decide anything alone. The escape is a counting argument rather than a coordination protocol. Scale the threshold down by each partition's share of the whole, and the arithmetic forces a conclusion: if the quantity failed the scaled test on every partition, its total across all partitions is strictly below the global threshold. Contrapositively, anything genuinely above the global threshold must have passed the scaled local test somewhere. The union of every partition's local answers is therefore a superset of the true answer, with no omissions — proved, not hoped.

That single inequality is what makes the whole architecture work, and it is worth appreciating what it costs and what it buys. It costs nothing in coordination: the workers never talk to each other, never see the same data, and need no consistent view. It buys a candidate set with a hard guarantee of completeness, which is the property that approximation cannot supply and that turns a heuristic into an exact algorithm. The remaining work is mechanical — one more pass counting only the candidates, summing across partitions, and keeping those that clear the real threshold — and it is exact because the candidate set provably lost nothing.

The general shape is worth learning as a template. To make a global property decidable from local observations, look for a monotone aggregate — something where the whole is a sum, a maximum, or a union of the parts — and then find the local bound whose universal failure implies global failure. If the aggregate is a sum, the bound is the threshold divided by the number of parts. If it is a maximum, the local test is the global test unchanged. If no such bound exists, the property genuinely requires communication, and knowing that early saves you from designing a protocol that cannot be correct.

The trade being made is also clear and should be stated: local thresholds set this low admit many candidates that are locally impressive and globally irrelevant, so the second pass does real work. You are paying verification volume to buy independence between workers. That exchange is almost always favourable when the alternative is coordination, because verification parallelises trivially and coordination does not.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the Savasere-Omiecinski-Navathe section of the frequent-itemsets chapter, which runs an in-memory algorithm on each chunk at a proportionally reduced threshold, argues that anything frequent overall must be frequent in at least one chunk, and expresses the two resulting passes as a pair of map-reduce rounds.
