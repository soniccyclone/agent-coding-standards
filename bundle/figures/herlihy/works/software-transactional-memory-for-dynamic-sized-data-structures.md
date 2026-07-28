---
type: work
title: "Software Transactional Memory for Dynamic-Sized Data Structures"
figure: herlihy
description: Introduces DSTM, a software transactional memory system where transactions and the objects they touch can be created and sized at runtime rather than fixed in advance, built on an obstruction-free (weaker than lock-free) conflict-detection scheme. Separates the transactional mechanism itself (conflict detection, rollback) from contention-management policy (how to react when transactions collide), so different contention managers can be plugged in independently. Widely credited with moving transactional memory from a hardware-architecture proposal into a practical software technique, and it launched the STM implementation literature that followed.
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
year: 2003
url: https://cs.brown.edu/courses/cs161/papers/stm.pdf
extraction: complete
access: public
host: institutional
tags: [work]
---

# Software Transactional Memory for Dynamic-Sized Data Structures

**Author(s):** Maurice Herlihy, Victor Luchangco, Mark Moir, and William N. Scherer III
**Venue/year:** 22nd ACM Symposium on Principles of Distributed Computing (PODC), 2003, pp. 92-101.
**Source:** https://cs.brown.edu/courses/cs161/papers/stm.pdf — live PDF, hosted on Brown University's own CS course-materials site (institutional, same institution as the author, not a personal page).

## Lessons
- [Separate the part that must be correct from the part that must be tuned, and let only the tuned part be replaceable](../lessons/separate-the-mechanism-that-is-correct-from-the-policy-that-makes-progress.md)
- [Guarantees are not a ladder to climb: decompose one into its clauses and keep only the clause that is load-bearing](../lessons/decompose-a-guarantee-and-keep-only-the-clause-you-need.md)
- [When the machine's atomic unit is narrower than your invariant, restructure the data until the invariant fits behind one reference](../lessons/group-an-invariant-behind-one-reference-when-the-atomic-unit-is-too-narrow.md)
- [Shrink what you hold before getting clever about arbitrating collisions](../lessons/shrink-the-window-before-arbitrating-the-collisions.md)
- _also read as a second source for_ [If your code may be run speculatively, it must be defined on states that could never legally occur](../lessons/speculative-execution-demands-code-that-is-total-over-nonsense.md) _and_ [Let the system own correctness and the programmer own cost: write sequential code, mechanize the concurrency](../lessons/write-sequential-code-and-let-the-system-own-concurrency.md)
