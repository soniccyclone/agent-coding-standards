---
type: work
title: "A Methodology for Implementing Highly Concurrent Data Objects"
figure: herlihy
description: Presents a general "universal construction" - a recipe for turning any sequential object, given only a specification of its valid states and operations, into a wait-free concurrent implementation, built around compare-and-swap operating over a shared log of committed operations. Also works through smaller special-purpose techniques (small-object tricks, load-linked/store-conditional) as more efficient alternatives for particular data types. The universal construction is the constructive proof that wait-free implementations exist in general, not just for hand-picked structures like queues or counters.
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
year: 1993
url: https://cs.brown.edu/people/mph/Herlihy93/herlihy93methodology.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# A Methodology for Implementing Highly Concurrent Data Objects

**Venue/year:** ACM Transactions on Programming Languages and Systems (TOPLAS) 15(5), November 1993, pp. 745-770.
**Source:** https://cs.brown.edu/people/mph/Herlihy93/herlihy93methodology.pdf — live PDF, self-archived on Maurice Herlihy's own Brown CS page.

## Lessons
- [Let the system own correctness and the programmer own cost: write sequential code, mechanize the concurrency](../lessons/write-sequential-code-and-let-the-system-own-concurrency.md)
- [If your code may be run speculatively, it must be defined on states that could never legally occur](../lessons/speculative-execution-demands-code-that-is-total-over-nonsense.md)
- [A guarantee that is sound in the step-counting model can be the wrong engineering choice; go measure](../lessons/asymptotically-adequate-is-not-practically-adequate.md)
- [Once two primitives are both powerful enough, choose between them by what they can detect](../lessons/above-the-power-threshold-choose-primitives-by-what-they-detect.md)
