---
type: work
title: "Transactional Memory: Architectural Support for Lock-Free Data Structures"
figure: herlihy
description: Proposes hardware transactional memory - extending a multiprocessor's cache-coherence protocol so a bounded sequence of loads and stores can execute as one atomic transaction that either commits as a whole or aborts and retries, without taking any lock. Argues this gives programmers the simplicity of coarse-grained locking combined with the performance of carefully hand-built lock-free code. Coined the term "transactional memory" and set off both the hardware-TM line later adopted by Intel TSX and IBM POWER, and the software-TM literature that followed.
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
year: 1993
url: https://cs.brown.edu/people/mph/HerlihyM93/herlihy93transactional.pdf
access: public
host: self-archived
tags: [work]
---

# Transactional Memory: Architectural Support for Lock-Free Data Structures

**Author(s):** Maurice Herlihy and J. Eliot B. Moss
**Venue/year:** 20th Annual International Symposium on Computer Architecture (ISCA), 1993, pp. 289-300.
**Source:** https://cs.brown.edu/people/mph/HerlihyM93/herlihy93transactional.pdf — live PDF, self-archived on Maurice Herlihy's own Brown CS page.

## Lessons
- [Before adding a mechanism, ask whether the machine already computes the predicate you need](../lessons/the-machine-may-already-be-computing-the-predicate-you-need.md)
- [Pessimistic protocols make you declare a footprint you do not yet know, and the concurrency you lose is the state-dependent kind](../lessons/pessimistic-protocols-make-you-declare-a-footprint-you-cannot-yet-know.md)
- [A mechanism with a physical limit is only usable if the limit is part of its published contract](../lessons/a-bounded-mechanism-must-publish-its-bound.md)
- [The bookkeeping a mechanism needs is a cost of the mechanism, not of the problem](../lessons/auxiliary-state-is-a-cost-of-the-mechanism-not-the-problem.md)
