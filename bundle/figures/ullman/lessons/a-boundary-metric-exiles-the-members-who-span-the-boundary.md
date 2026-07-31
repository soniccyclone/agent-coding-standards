---
type: lesson
title: "A boundary metric exiles the members who span the boundary"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# A boundary metric exiles the members who span the boundary

**Lesson:** A metric that finds boundaries by detecting which connections join otherwise-separate regions has a specific and predictable pathology: it also penalises the individuals who do the joining. The element with one tie outside its group has, by that tie, made every one of its own connections into part of a cross-region route. Its internal links inherit a high boundary score, so as you keep cutting in score order the group's own connector is severed from the group before the group's peripheral members are. Push the procedure far enough and you get partitions in which the most connected participant stands alone while everyone it introduced to each other remains together.

The general form of the problem is that these metrics score a *structural role*, not membership, and the two are only correlated. Bridging, brokering, adapting, translating — whatever you call it — is a role that legitimate members of a group perform, and any measure sensitive enough to locate the seam between groups is sensitive to the people and components sitting on that seam. This bites in ordinary engineering settings. A cohesion metric over a dependency graph will flag the adapter that is the whole point of the module. A code-ownership analysis will orphan the person who works across teams. In each case the metric is functioning exactly as designed and the interpretation laid over it is wrong.

The immediate mitigation is that the procedure's output is a nested family of partitions, and only the coarse end of it is trustworthy. The first few cuts do separate genuinely distinct regions; the later ones are dismembering the regions from the inside. Nothing in the metric marks where the transition happens, because the same quantity is being computed all the way down. So the stopping point must come from outside the method — from what you know about how many groups there should be, or from an independent quality check on the pieces — and a procedure that reports only its terminal state has thrown away the part of its output that was worth having.

The deeper habit is to ask, of any metric you plan to threshold, which legitimate participants score like the thing you are trying to exclude. There is nearly always such a class, and it is usually the class doing the most valuable work, since spanning a boundary is what makes something valuable and what makes it look anomalous, both at once. Knowing the class in advance turns an unexplained weird result into an expected one you can correct for.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the worked example in the social-network chapter where continued removal of the highest-betweenness edges past the first split leaves the two nodes joined by the removed bridge disconnected from their own communities, described in the text as those nodes being "traitors" to their groups because each has a friend outside it.
