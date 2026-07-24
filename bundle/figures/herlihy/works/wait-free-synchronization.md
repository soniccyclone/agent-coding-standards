---
type: work
title: "Wait-Free Synchronization"
figure: herlihy
description: Introduces wait-freedom as a progress condition guaranteeing every process finishes an operation in a bounded number of its own steps regardless of other processes' speeds or failures, then uses it to rank shared-memory primitives by "consensus number" - how many processes a primitive can help solve consensus among. Shows primitives like compare-and-swap are strictly more powerful than test-and-set or plain read/write registers, giving the first rigorous hierarchy of synchronization power. This hierarchy became the standard formal yardstick for comparing hardware synchronization instructions.
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
year: 1991
url: https://cs.brown.edu/people/mph/Herlihy91/p124-herlihy.pdf
access: public
host: self-archived
tags: [work]
---

# Wait-Free Synchronization

**Venue/year:** ACM Transactions on Programming Languages and Systems (TOPLAS) 13(1), January 1991, pp. 124-149.
**Source:** https://cs.brown.edu/people/mph/Herlihy91/p124-herlihy.pdf — live PDF, self-archived on Maurice Herlihy's own Brown CS page (server redirects the older `~mph` path to `people/mph`; both resolve).

## Lessons
_(empty — lesson extraction is Phase 4)_
