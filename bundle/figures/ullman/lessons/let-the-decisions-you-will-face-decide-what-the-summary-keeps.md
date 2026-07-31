---
type: lesson
title: "Let the decisions you will face decide what the summary keeps"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# Let the decisions you will face decide what the summary keeps

**Lesson:** When data is too large to hold and you must keep a fixed-size summary instead, the instinctive approach is to keep whatever best describes the data — the central value, the count, the spread. That instinct optimises for the wrong thing. A summary is not a description, it is a substitute for the data during the decisions you will make while the data is unavailable. So the way to design it is to list those decisions first and then, for each one, ask what evidence it needs. The contents of the summary fall out of that list, and they are often surprising — including things nobody would put in a description because they are not descriptive at all.

Worked through, the discipline produces summaries with deliberately asymmetric contents. If one future decision is whether the group's representative should be replaced, you must retain the candidates most likely to replace it, which means the items closest to the current representative. If another future decision is whether two groups should be joined, and joining is judged by whether their extremities meet, you must retain the items farthest from the representative. Those two sets have nothing to do with each other and neither is what a summary of the group would naturally contain. They are there because a specific decision cannot be made without them, and that is the only justification a summary field ever needs.

Stating it that way also tells you what to leave out, which is the harder half. Any field you cannot attach to a decision is dead weight competing for the space that keeps the summary fixed-size, and fixed-size is the property that makes the whole scheme work. The discipline is symmetric: no decision, no field. It also surfaces the decisions that cannot be supported at all within your budget, which is far better discovered at design time — that is the moment to change the decision procedure or accept that it will require going back to the underlying data.

The pattern applies well beyond streaming summaries: what a log line should contain is determined by the diagnoses you will have to make from it, what an index should carry is determined by the predicates that will be pushed into it, what a cache entry should hold is determined by what the caller does next. In each case the "obviously useful" content is the content someone imagined a reader wanting, and the actually useful content is whatever a specific downstream decision cannot proceed without.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the cluster-feature representation in the GRGPF section of the clustering chapter, which retains the count, the representative, its aggregate distance measure, the nearest points because the representative may change, and the farthest points because merge decisions are made on whether distant points of two clusters are close.
