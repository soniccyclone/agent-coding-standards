---
type: lesson
title: "Find the floor before you climb, so you know when optimizing is finished"
figure: tarjan
works: [depth-first-search-and-linear-graph-algorithms]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Find the floor before you climb, so you know when optimizing is finished

**Lesson:** Optimization effort has no natural stopping point unless you know what the floor is. Tarjan closes by noting that the two algorithms are within a constant factor of the best achievable, and the argument for that is almost embarrassingly cheap: any correct procedure has to look at every vertex and every edge, because either could change the answer, so nothing can beat the cost of reading the input. That one sentence converts an achievement into a closed question. Further cleverness on these problems can only buy constants — worth having sometimes, but a completely different kind of pursuit from an asymptotic improvement, and worth knowing you have switched to it. The cheapest lower bound available, the one that says "you must at least examine what could matter," is usually derivable in a couple of lines and is almost never written down before the work starts.

The same reasoning does more than mark completion. Before you begin, comparing the floor with the cost of the approach you have in mind tells you how much room actually exists. A large gap says the approach is leaving something on the table and it is worth searching for structure you haven't exploited. A small gap says stop, because the remaining headroom cannot repay the complexity you would add chasing it — and complexity added there is permanent, while the speedup is bounded by a constant you already know. Practitioners routinely tune in the second situation while believing they are in the first, because they never established which one they were in.

The lower bound also disciplines what the cost is measured in. These bounds are stated in the two quantities that vary independently — how many things there are and how many connections between them — rather than collapsed into a single notion of input size. That is not fussiness. A sparse and a dense input of the same vertex count behave nothing alike, and a bound expressed in one parameter would either be loose on one of them or hide which parameter the algorithm is actually sensitive to. Whenever a problem has two dimensions that real inputs vary in separately, carrying both through the analysis is what makes the result usable for deciding anything, including where the floor is.

**Source:** [Depth-First Search and Linear Graph Algorithms](../works/depth-first-search-and-linear-graph-algorithms.md) — the closing section's observation that both algorithms are optimal to within a constant factor because every vertex and edge must be examined to answer either question, together with the abstract and theorems stating space and time bounds in vertex count and edge count as separate parameters.
