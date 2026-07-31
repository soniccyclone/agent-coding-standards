---
type: lesson
title: "Insert a lossy step to declare what the answer must not depend on"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, primitive-count]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Insert a lossy step to declare what the answer must not depend on

**Lesson:** A pipeline that carries full precision from end to end is not neutral — it lets every downstream stage depend on detail you may have no intention of honouring, and it obliges every downstream stage to carry the volume that detail implies. Deliberately inserting a step that coarsens the representation between stages turns a hope into a guarantee: after that point, nothing can distinguish inputs that differ only within the granularity you collapsed, so no later stage can accidentally come to rely on the distinction. The compression is a side effect. The declaration is the point.

Two decisions define such a step and both are substantive. The granularity says how much variation you are asserting is immaterial, and it has a ceiling: coarsen too far and you have thrown away the distinctions the answer genuinely needed, which shows up as a quality loss with no obvious cause because the information disappeared several stages before the symptom. The choice of summary says what "this group of values" is supposed to mean. Taking the largest asserts that the group is interesting if any member is, and it discards how many members agreed. Taking the average asserts that the group's overall level matters and lets a single extreme member be outvoted. These encode different beliefs about what the upstream stage was reporting, and neither is a default.

The compounding payoff is what makes it worth doing early rather than late. Every stage after the coarsening operates on the smaller representation, so the saving multiplies down the chain, and the smaller representation lets the following stages be correspondingly richer for the same budget. This is why a design that alternates a stage that adds detail with a stage that removes it can go much deeper than one that only ever adds — the removal is what buys the room for the next addition.

Generalised past pipelines: whenever you find yourself hoping a consumer will ignore some aspect of the data you hand it, consider not handing it over. Rounding timestamps to the resolution your logic actually treats as simultaneous, bucketing a continuous score before it crosses a service boundary, normalising away formatting variation at ingestion — each replaces an unenforceable convention with a structural fact, and each shrinks everything downstream as a bonus rather than as the justification.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the pooling-layers section of the convolutional-networks chapter, which aggregates over small contiguous regions to shrink the spatial extent, identifies the pooling function, region size and stride as the three defining choices, notes that the maximum is usual but any aggregate such as the average could be used, observes that larger regions lose too much information in practice, and states that pooling is appropriate precisely when features are believed to be approximately invariant to small translations because relative rather than exact locations matter.
