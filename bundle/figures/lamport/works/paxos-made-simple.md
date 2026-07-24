---
type: work
title: "Paxos Made Simple"
figure: lamport
description: A plain, allegory-free restatement of the Paxos consensus algorithm, written because almost nobody who read "The Part-Time Parliament" actually understood it. Walks through why consensus among unreliable, asynchronous processes is hard and derives the algorithm directly from the safety requirements it has to satisfy. Ended up being the version most engineers actually read when implementing Paxos in real systems.
subdomains: [distributed-systems-and-concurrency]
year: 2001
url: https://lamport.azurewebsites.net/pubs/paxos-simple.pdf
access: public
host: self-archived
tags: [work]
---

# Paxos Made Simple

**Venue/year:** ACM SIGACT News (Distributed Computing Column) 32(4), December 2001
**Source:** https://lamport.azurewebsites.net/pubs/paxos-simple.pdf — self-archived PDF on Lamport's own site, live and directly downloadable (HTTP 200).

## Lessons
- [Derive the algorithm from the conditions that make it correct, so the proof precedes the code](../lessons/derive-the-algorithm-from-its-invariant.md)
- [Split every correctness claim into safety and liveness, and never let one pay for the other](../lessons/split-correctness-into-safety-and-liveness.md)
- [Reduce every distributed coordination problem to agreeing on one sequence of commands](../lessons/reduce-coordination-to-an-agreed-command-sequence.md)
