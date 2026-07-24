---
type: work
title: "Time, Clocks and the Ordering of Events in a Distributed System"
figure: lamport
description: Introduces logical clocks — a way to assign consistent timestamps to events in a system of processes that have no shared clock and communicate only by message passing. Defines the "happens-before" relation as a partial order on events and shows how to extend it to a full, causally-consistent total order. Also sketches a distributed mutual-exclusion algorithm as an application of the technique.
subdomains: [distributed-systems-and-concurrency]
year: 1978
url: https://lamport.azurewebsites.net/pubs/time-clocks.pdf
access: public
host: self-archived
tags: [work]
---

# Time, Clocks and the Ordering of Events in a Distributed System

**Venue/year:** Communications of the ACM 21(7), July 1978
**Source:** https://lamport.azurewebsites.net/pubs/time-clocks.pdf — self-archived PDF on Lamport's own site, live and directly downloadable (HTTP 200).

## Lessons
- [Order events by what the system can observe, not by an imagined universal clock](../lessons/order-events-by-causality-not-clocks.md)
- [Reduce every distributed coordination problem to agreeing on one sequence of commands](../lessons/reduce-coordination-to-an-agreed-command-sequence.md)
