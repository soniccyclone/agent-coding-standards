---
type: lesson
title: "Split the cost into classes with different arguments, leave the granularity free, and tune it last"
figure: tarjan
works: [efficiency-of-a-good-but-not-linear-set-union-algorithm]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Split the cost into classes with different arguments, leave the granularity free, and tune it last

**Lesson:** No single argument bounds the total work here, so Tarjan does not look for one. He groups the elements into bands by a size measure, using cut points taken from a hierarchy of extremely fast-growing functions, and then classifies every individual step the algorithm takes by *which band boundary that step crosses*. Steps within a band, steps crossing to the next band, and steps crossing all the way out are three different populations, and each is bounded by its own separate argument appealing to a different fact — one to the strictly increasing sizes along a walk, one to how few bands there are, one to how many times a given element's attachment point can be promoted before it runs out of bands. The total is the sum of these unrelated bounds. The structural idea worth taking is that a cost you cannot bound uniformly may decompose into populations that are each individually easy, and that the decomposition is a design decision you make, not something the problem hands you.

The second move is to leave the decomposition's granularity as an unbound parameter through the whole proof. How many bands there are, and therefore how coarse each one is, appears symbolically in every intermediate bound. Coarser banding makes the within-band population easier to control and the crossing population worse; finer banding does the reverse. Only at the end, with the sum in hand as a function of that parameter, does he choose the value that minimizes it — and the famously strange shape of the final answer is simply where those two opposing terms balance. Nobody chose an inverse-Ackermann-style bound as a target. It fell out. Carrying a free parameter symbolically instead of committing early is what makes that possible, and it is a habit that costs nothing but notation.

The two ideas reinforce each other and both transfer to ordinary performance work. Faced with a total you cannot characterize — total latency across a heterogeneous workload, total bytes moved by a mixed access pattern — the productive step is to find a partition of the events under which each part is separately explainable, rather than searching for one model that covers everything. And when the partition has a knob, resist filling it in with a plausible number. Keep it symbolic until the whole expression exists, then optimize. Committing early to a round number is how analyses end up proving a weaker result than the technique actually supports, and it hides the fact that the parameter's optimal value is itself informative about the system.

**Source:** [Efficiency of a Good But Not Linear Set Union Algorithm](../works/efficiency-of-a-good-but-not-linear-set-union-algorithm.md) — the upper-bound section's construction of vertex sets banded by height using levels of the Ackermann-variant hierarchy, the partition of find-path edges into the three populations bounded by the separate lemmas, the total expressed as a sum over classes with the band count left as a free parameter, and the final step choosing that parameter to minimize the resulting expression.
