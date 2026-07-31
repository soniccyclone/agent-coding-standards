---
type: lesson
title: "Store the form that composes, and derive the form you report"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, parallelizability, primitive-count, hardware-affinity]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Store the form that composes, and derive the form you report

**Lesson:** When a summary can be written several algebraically equivalent ways, the choice between them is not cosmetic — it decides whether the summary can be updated and merged cheaply. The intuitive choice is the form a human would want to read, the interpreted quantities with meaningful units. That form is almost always the wrong thing to store, because incorporating one more observation into it requires undoing the interpretation, and combining two of them requires a weighted reconstruction that gets progressively more awkward as the summary grows richer. The right thing to store is the raw accumulation the interpreted quantities are computed from: plain running totals, closed under addition, from which every reported figure is recovered by arithmetic at the moment someone asks.

The property being bought is that the stored representation forms an additive structure. Two summaries combine by adding their components. One observation is folded in by adding its contribution. Both operations are associative, so the order of combination is irrelevant, which is exactly the condition under which the summary can be computed in parallel, computed incrementally, merged across partitions, or recomputed after a partial failure without recomputing everything. None of those capabilities is available to a representation that stores derived quantities, and none of them can be retrofitted, because they are consequences of the algebra rather than of the code around it.

The rule generalises far past statistics. Any time you are deciding what to persist about a stream of events, ask what operation you will need to apply to two persisted summaries, and choose a representation closed under that operation. Counts and sums are closed under addition; extrema are closed under maximum; sketches are designed to be closed under union precisely so this holds. Averages, ratios, percentages, and standard deviations are not closed under anything useful, and every system that stores them ends up with a special-case merge path that is subtly wrong under reordering or double-counting. Presenting a ratio is fine; persisting one is a decision to abandon composability.

The cost is trivial and the diagnostic is easy. You store a few more numbers than the report needs, and you spend a division at display time. In exchange, the summary becomes something you can distribute, resume, and recombine. If you cannot state the merge operation for your stored form in one sentence, you have chosen the reporting representation by accident.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the boxed discussion of the cluster representation in the Bradley-Fayyad-Reina section of the clustering chapter, which keeps a count, per-dimension sums, and per-dimension sums of squares rather than the centroid and standard deviations, so that adding a point or merging two summaries is componentwise addition while the reported statistics remain recoverable.
