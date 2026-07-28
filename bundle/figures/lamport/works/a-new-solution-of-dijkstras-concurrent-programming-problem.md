---
type: work
title: "A New Solution of Dijkstra's Concurrent Programming Problem"
figure: lamport
description: Presents the Bakery algorithm, a way for any number of processes to take turns in a critical section using only ordinary reads and writes to shared memory — no special atomic hardware instructions required. Processes take numbered "tickets" like customers at a bakery counter and are served in ticket order, which guarantees fairness (no process waits forever). Notably tolerant of processes reading each other's tickets at slightly different, even inconsistent, moments and still behaving correctly.
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
year: 1974
url: https://lamport.azurewebsites.net/pubs/bakery.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# A New Solution of Dijkstra's Concurrent Programming Problem

**Venue/year:** Communications of the ACM 17(8), August 1974
**Source:** https://lamport.azurewebsites.net/pubs/bakery.pdf — self-archived PDF on Lamport's own site, live and directly downloadable (HTTP 200).

## Lessons
- [Design algorithms to survive the weakest primitives you can, and count every assumption you keep](../lessons/assume-the-least-from-your-primitives.md)
