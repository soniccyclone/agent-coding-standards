---
type: lesson
title: "Same shape is not same meaning: keep roles distinct even when the picture collapses them"
figure: wirth
works: [algorithms-and-data-structures]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# Same shape is not same meaning: keep roles distinct even when the picture collapses them

**Lesson:** A structure with two outgoing links per element can be drawn so that it looks exactly like a familiar two-way branching structure, and the resemblance is genuine — the diagram really does map onto the other one, and every traversal that works there will run here. The temptation this creates is to conclude that it *is* that structure and to reuse the vocabulary, the operations and the mental model wholesale. Resist it, because the resemblance is at the level of shape and the difference is at the level of what the links mean. When one link says "another of the same kind, at the same level" and the other says "one level down," those two are not interchangeable, and any operation that treats them uniformly is computing something that has no interpretation in the domain — it will run, it will terminate, and its answer will be nonsense.

The diagnostic is to ask what a program would be asserting if it swapped the two links. If the swap produces a statement that is merely false, they are distinct roles and must stay distinct in the type definitions, in the names, and in the operations offered. If the swap produces a statement that is still meaningful, then the uniformity is real and the shared machinery is legitimate. Doing this check is cheap and it is the entire content of the discipline; the mistake is not that people decide wrongly but that they never pose the question, having been reassured by a picture.

The same reasoning bounds how far a general technique should be pushed. A structure with several distinct kinds of link, each meaning something different, is no longer a tree or a graph in any useful sense — it is a small model of a domain, and the operations on it are determined by what the domain says, not by what any general traversal library says. There is correspondingly little to say about it in the abstract, and the honest position is to admit that generic techniques stop applying and per-domain reasoning takes over, rather than to force the model into a shape that has known algorithms attached. Knowing where the general theory runs out is part of knowing the theory.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 4.7's treatment of multiway trees represented with a sibling link and an offspring link per element, where the figure is noted to look like a binary tree if tilted, followed by the argument that this view is misleading because the two references have entirely different meanings functionally, that one does not treat a sibling as an offspring without consequence and therefore should not do so in constructing data definitions either; and the same section's observation that adding further relationship components turns the structure into a complex relational data bank whose algorithms are intimately tied to their data definitions, so that it makes no sense to specify general rules or widely applicable techniques for them.
