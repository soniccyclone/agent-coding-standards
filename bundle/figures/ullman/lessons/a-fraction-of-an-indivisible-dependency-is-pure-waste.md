---
type: lesson
title: "Half of an indivisible dependency is worth nothing at all"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Half of an indivisible dependency is worth nothing at all

**Lesson:** When you distribute a computation, the tempting mental model is that sending a worker more data always helps it a little — more inputs, more outputs it can produce, diminishing returns at worst. For a large class of problems that model is simply false. If an output depends on a whole set of inputs jointly, then a worker holding all but one of them can produce nothing. Its share of the data is not partly useful; it is exactly as useful as an empty share, and every byte of it was moved for nothing. The unit that matters is not the individual input but the smallest group that some output actually needs, and any routing scheme that splits such a group across workers has bought pure overhead.

This reframes how to think about partitioning. Before deciding who gets what, identify the indivisible bundles — a whole row, a complete key group, an entire time window, all the fields of a record a validation rule reads. Then treat those bundles, not the raw elements, as the things being placed. The immediate consequence is a much better cost estimate, because the effective capacity of a worker is measured in whole bundles, and the rounding loss from bundles that do not divide evenly is real and predictable rather than a mysterious inefficiency. The second consequence is a sharp diagnostic for a design that is going wrong: if you find yourself hoping a worker will "mostly" have what it needs, you have not identified the bundles, and the shortfall will not degrade performance gracefully — it will produce nothing.

The same observation is also the lever for proving that you cannot do better. Once you know each worker must receive complete bundles, you can bound how many outputs a worker of a given capacity could possibly cover, count how many outputs exist, and conclude a minimum total volume that must be moved no matter how clever the scheme. That is a lower bound rather than a benchmark, which is a different kind of knowledge: it tells you when to stop optimising. The recurring pattern is that these bounds are maximised by balance — a worker covers the most when its capacity is split evenly among the kinds of bundle it needs, rather than loaded up on one kind — which is worth knowing as a heuristic even when you never do the algebra.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the complexity-theory chapter's lower-bound argument for one-pass matrix multiplication, which begins by observing that a partial row of one matrix or a partial column of the other is useless to a reducer, so the best schema delivers whole rows and columns, and that coverage is maximised when their counts are equal.
