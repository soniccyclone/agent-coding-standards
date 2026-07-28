---
type: work
title: "Solution of a Problem in Concurrent Programming Control"
figure: dijkstra
description: A one-page communication that answers an open question from 1962 on how a set of independent, cyclic processes can guarantee that exactly one of them is ever in its critical section at a time, using only shared memory. This is the first published N-process mutual-exclusion algorithm, built from nothing but ordinary shared variables — no atomic test-and-set, no semaphores (those arrive in EWD123, Cooperating Sequential Processes, §3.2). Its solution is deliberately symmetric and makes no assumption about relative process speeds, which is what makes it a genuine mutual-exclusion result rather than a scheduling trick.
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
year: 1965
url: https://repositories.lib.utexas.edu/items/84831631-07fe-484b-a45c-3cff9f6b1f43
extraction: complete
access: public
host: institutional
tags: [work]
---

# Solution of a Problem in Concurrent Programming Control

**Venue/year:** Communications of the ACM 8(9), September 1965, p. 569.
**Source:** https://repositories.lib.utexas.edu/items/84831631-07fe-484b-a45c-3cff9f6b1f43 — live page, Texas ScholarWorks (UT Austin) repository item hosting a scanned copy of the original CACM communication (direct PDF: repositories.lib.utexas.edu/bitstreams/0f06c11e-9be7-4182-810d-4d5507f2d276/download). Not separately EWD-numbered, so it isn't on the main transcriptions archive; ACM Digital Library's copy of the same piece is paywalled.
**Host:** institutional — Texas ScholarWorks (UT Austin's official repository) — not the EWD archive itself, but the same institution.

## Lessons
- [In concurrency, proving nothing bad happens is half a proof: demand progress against an adversarial schedule](../lessons/safety-without-progress-is-not-correctness.md)
- [Make cooperating processes correct under every speed ratio, because timing assumptions are hidden coupling](../lessons/never-let-correctness-depend-on-timing.md)
