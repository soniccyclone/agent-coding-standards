---
type: work
title: "Software Transactional Memory for Dynamic-Sized Data Structures"
figure: herlihy
description: Introduces DSTM, a software transactional memory system where transactions and the objects they touch can be created and sized at runtime rather than fixed in advance, built on an obstruction-free (weaker than lock-free) conflict-detection scheme. Separates the transactional mechanism itself (conflict detection, rollback) from contention-management policy (how to react when transactions collide), so different contention managers can be plugged in independently. Widely credited with moving transactional memory from a hardware-architecture proposal into a practical software technique, and it launched the STM implementation literature that followed.
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
year: 2003
url: https://cs.brown.edu/courses/cs161/papers/stm.pdf
access: public
host: institutional
tags: [work]
---

# Software Transactional Memory for Dynamic-Sized Data Structures

**Author(s):** Maurice Herlihy, Victor Luchangco, Mark Moir, and William N. Scherer III
**Venue/year:** 22nd ACM Symposium on Principles of Distributed Computing (PODC), 2003, pp. 92-101.
**Source:** https://cs.brown.edu/courses/cs161/papers/stm.pdf — live PDF, hosted on Brown University's own CS course-materials site (institutional, same institution as the author, not a personal page).

## Lessons
_(empty — lesson extraction is Phase 4)_
