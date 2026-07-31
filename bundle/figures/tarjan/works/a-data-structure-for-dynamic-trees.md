---
type: work
title: "A Data Structure for Dynamic Trees"
figure: tarjan
description: Presents the link-cut tree, a structure for maintaining a forest of vertex-disjoint trees under edge insertion, edge deletion, and path-aggregate queries, each in O(log n) amortized time. It's built by representing paths through a dynamic tree as splay trees, so the earlier splay-tree amortized-analysis machinery gets reused as the engine underneath a strictly harder dynamic-connectivity problem. Link-cut trees became a standard building block for network-flow algorithms and later for a wide range of dynamic-graph problems.
subdomains: [algorithms-and-complexity]
year: 1983
url: https://www.cs.cmu.edu/~sleator/papers/dynamic-trees.pdf
survey_pages: 30
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: self-archived
tags: [work]
---

# A Data Structure for Dynamic Trees

**Author(s):** Daniel D. Sleator, Robert E. Tarjan
**Venue/year:** Journal of Computer and System Sciences 26(3), 1983, pp. 362-391.
**Source:** https://www.cs.cmu.edu/~sleator/papers/dynamic-trees.pdf — live page, self-archived by co-author Daniel Sleator on his CMU faculty site.

## Lessons
- [Invent the middle layer, then keep the cost a product of factors you can improve separately](../lessons/invent-the-middle-layer-and-keep-the-cost-a-product.md)
- [Promoting a concept from your analysis into the runtime buys worst-case guarantees and costs you a repair step](../lessons/promote-an-analysis-concept-into-the-runtime-only-if-you-need-worst-case.md)
- [Park a pending transformation at the top of the aggregate and resolve it on the way down](../lessons/park-a-pending-transformation-at-the-root-and-resolve-it-on-descent.md)
- [Push what the outer layer knows about access frequency down into the inner structure](../lessons/push-the-access-distribution-down-into-the-lower-layer.md)
- [Price each operation in your interface by what it forces on the implementation, and name the algebra you actually need](../lessons/price-each-operation-in-your-interface-by-what-it-forces-below.md)
- [Funnel every mutation through one operation so the invariant bookkeeping has exactly one home](../lessons/funnel-every-mutation-through-one-operation-so-bookkeeping-has-one-home.md)
- [To bound how often a step fires, find a quantity it increments and then audit everything that can decrement it](../lessons/to-bound-how-often-a-step-fires-find-what-it-increments.md)
