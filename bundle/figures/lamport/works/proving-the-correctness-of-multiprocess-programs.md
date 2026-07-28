---
type: work
title: "Proving the Correctness of Multiprocess Programs"
figure: lamport
description: Extends Floyd/Hoare-style assertional verification — proving programs correct via invariants attached to program points — from sequential programs to concurrent ones. Separates out safety (nothing bad ever happens) and liveness (something good eventually happens) as two distinct properties that need their own proof techniques. Lays groundwork that later feeds directly into Lamport's temporal-logic approach to specification.
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
year: 1977
url: https://lamport.azurewebsites.net/pubs/proving.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# Proving the Correctness of Multiprocess Programs

**Venue/year:** IEEE Transactions on Software Engineering SE-3(2), March 1977
**Source:** https://lamport.azurewebsites.net/pubs/proving.pdf — self-archived PDF on Lamport's own site, live and directly downloadable (HTTP 200).

## Lessons
- [Reason about concurrent programs through invariants over states, never by enumerating interleavings](../lessons/prove-concurrent-programs-with-invariants-not-interleavings.md)
- [Split every correctness claim into safety and liveness, and never let one pay for the other](../lessons/split-correctness-into-safety-and-liveness.md)
