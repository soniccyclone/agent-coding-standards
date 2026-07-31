---
type: lesson
title: "If you must scan everything, shrink what you scan"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, primitive-count]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# If you must scan everything, shrink what you scan

**Lesson:** The default response to a slow lookup is to build a structure that avoids visiting most of the data. That instinct is right in the regimes it was formed in and fails in others: there are settings where the geometry guarantees that any correct answer requires examining a large fraction of the data, and in those settings every access-avoiding structure delivers negligible pruning while adding build cost, memory, maintenance, and a body of code with its own failure modes. Recognising that you are in such a regime is the whole insight, because it redirects the effort from "how do I avoid touching this data" to a different and much simpler question: "since I am going to touch all of it, how do I make each touch cheaper?"

The answer is usually precision. Most stored values carry far more resolution than a first-pass screening needs — keep the leading fraction of each value's bits and you have a companion dataset several times smaller that supports an approximate comparison. Sweep that, produce a shortlist of candidates whose approximate scores leave them possibly in contention, then consult the full-fidelity records only for the shortlist. The sweep is linear, exactly as the naive method was, but it moves a fraction of the bytes, and byte volume is what a linear sweep actually costs. No tree, no rebalancing, no structure to invalidate on update.

For this to be correct rather than merely fast, the truncation must err in one direction only: the approximate comparison has to be able to over-include but never exclude something that would have qualified at full precision. That is a property you get by bounding the error introduced by dropping the low bits and widening the shortlist threshold by that bound. Skipping the bound turns a two-stage exact method into a heuristic, which may be fine but is a different thing and should be known to be a different thing.

The transferable habit is to separate two questions that get conflated: how much data must I look at, and how expensive is each look. Indexing attacks the first. Compression, quantisation, columnar layout, and bitmap summaries attack the second, and they are the available lever precisely when the first question has the answer "all of it." Knowing which lever applies is a matter of understanding why the data is expensive, not of reaching for the structure that worked last time.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the discussion of high-dimensional data in the nearest-neighbour section of the large-scale-machine-learning chapter, which observes that for high-dimensional data little can be done to avoid searching a large portion of the data, and proposes VA files: forgo a complex structure, build a summary retaining only the high-order quarter of the bits of each component, scan that smaller file to construct a candidate list, and consult the full records only for the candidates.
