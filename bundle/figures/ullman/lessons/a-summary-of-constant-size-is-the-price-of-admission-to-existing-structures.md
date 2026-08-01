---
type: lesson
title: "A summary of constant size is the price of admission to existing structures"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, primitive-count, cognitive-load]
subdomains: [databases-and-data-management, operating-systems-and-systems-programming]
tags: [lesson]
---
# A summary of constant size is the price of admission to existing structures

**Lesson:** When designing a compact stand-in for a large collection, "small" is the requirement people write down and "constant-sized" is the one that actually matters. A summary whose footprint does not depend on how much it summarises is a fixed-width record, and fixed-width records are the input assumption of a large body of existing machinery: block-oriented trees, paged indexes, slotted pages, arrays with computed offsets, anything that decides how many things fit in a page and rebalances when they do not. Meeting that assumption means you get insertion, splitting, rebalancing, and disk-block layout by adopting a structure that already exists rather than by inventing one. A summary that grows, even slowly, with the data behind it locks you out of all of it and commits you to writing storage management by hand, which is a much larger and much less pleasant project than the summarisation problem you thought you were solving.

The uniformity buys a second, subtler property. If the interior nodes of the structure carry fixed-size digests of what lies beneath them, then the branching factor is the same at every level, and the structure's depth and cost analysis follow from arithmetic rather than from the data's shape. Depth is logarithmic because the fanout is a constant, and it is a constant because somebody decided each entry would be the same size no matter what it stood for. Designs where the summary at an interior node is a union or a concatenation of what lies below lose this immediately: the fanout shrinks with height, the tree gets deep and irregular, and the neat bound quietly stops holding.

The design move, then, is to fix the summary's budget first and derive its contents second. Decide that a group will be described by a set number of fields regardless of whether it holds ten items or ten million, and then spend that budget on whatever the decisions you must make actually require. This is the opposite of the natural order, in which you list what would be useful to keep and discover afterwards that the list grows with the group. The constraint is productive: a fixed budget forces the question of what each field is for, and the answer is usually that two or three of the candidates were not earning their place.

The check to run on any proposed summary is simply to ask what happens to its size as the underlying collection grows by a factor of a thousand. If the answer is anything other than "nothing," you have a variable-length record, and you should either find a fixed-size substitute for the offending field or accept — explicitly, in the design — that you are writing your own storage layer.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 7's cluster-tree organisation in the GRGPF algorithm, which notes that a cluster's representation has a size independent of the number of points in the cluster, that leaves therefore hold as many representations as fit in a disk block, that the fixed-size samples at interior nodes make the number of children independent of level, and that the resulting structure can be split and rebalanced exactly as a B-tree is.
