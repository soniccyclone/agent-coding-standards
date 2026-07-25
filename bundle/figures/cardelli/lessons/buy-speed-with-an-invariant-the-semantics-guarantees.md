---
type: lesson
title: "Buy performance with an invariant your own semantics guarantees, and quarantine the exceptions rather than generalizing"
figure: cardelli
works: [the-functional-abstract-machine]
axes: [hardware-affinity, verifiability]
subdomains: [operating-systems-and-systems-programming, programming-languages-and-semantics]
tags: [lesson]
---
# Buy performance with an invariant your own semantics guarantees, and quarantine the exceptions rather than generalizing

**Lesson:** Serious performance work rarely comes from local cleverness. It comes from finding a property that the system's own rules make true, and then designing a strategy that would be incorrect without it. In a mostly effect-free language, structures are built on top of structures that already existed, so references overwhelmingly point backwards in allocation order. That is not a hopeful assumption about workloads, it is close to a consequence of the language's semantics, and it licenses a reclamation strategy that examines only a narrow window of memory instead of all of it. The general shape is: state the property, name what it buys, and be explicit that the buying depends on the property continuing to hold.

The critical discipline is what to do about the cases where the property fails. Two constructs violate it here, mutually recursive definitions and updatable cells, and neither can be removed. The wrong response is to weaken the strategy until it is correct for everything, which surrenders the advantage for the sake of a small minority of the data. The right response is to segregate: allocate the violating objects in a separate region, treat that region conservatively by scanning it in full, keep it small, and process it on a different and less frequent schedule. The exceptions are then contained rather than allowed to set the terms for everything else, and the cost of the exceptions is proportional to how much of them you actually use.

A third element makes the arrangement pay over time. Because surviving data gets compacted towards the older end, age becomes a usable proxy for stability, so the collection schedule can be graded: attend frequently to the youngest region and rarely to the oldest. The invariant is not just exploited once, it is arranged to keep paying as the program runs.

Generalized, the recipe is: find the invariant your design already guarantees, build the aggressive strategy on it, enumerate the constructs that break it, quarantine them in a bounded region with its own conservative treatment, and grade your effort by a property that correlates with how much work is worth doing.

**Source:** [The Functional Abstract Machine](../works/the-functional-abstract-machine.md) — the garbage collection section, which identifies the directional allocation property that applicative languages make easy to verify, partitions memory into a region honouring it and a small region that may not, treats the latter by full scanning on a separate schedule, and describes the graded collection strategy that follows from stable data migrating.
