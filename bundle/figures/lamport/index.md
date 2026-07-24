---
type: figure
title: Leslie Lamport
description: b. 1941, Microsoft Research. Logical clocks, Byzantine Generals, Paxos, TLA+. Turing Award 2013.
status: accepted
layer: implementation-mapping
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [figure, accepted]
---

# Leslie Lamport

**Dates:** b. 1941. American computer scientist, formerly SRI International and Digital/Compaq Systems Research Center, now Microsoft Research.

## Why a candidate
- **Formal Methods & Verification:** Extended Floyd/Hoare-style assertional verification to concurrent and distributed systems, then built a full specification language and mechanized proof system (TLA+) around it — arguably the subdomain's most complete pipeline from formal primitive to industrial tool.
- **Distributed Systems & Concurrency:** Originated the formal treatment of event ordering under no-shared-clock conditions (logical clocks) and invented Paxos, the reference consensus protocol for asynchronous distributed systems with crash faults.

Nearly his entire bibliography is self-archived on his personal site — the single most accessible candidate across all nine subdomain reports.

## Top 10 most influential works
1. "Time, Clocks, and the Ordering of Events in a Distributed System" (1978) — `public` (self-archived, lamport.azurewebsites.net)
2. "The Byzantine Generals Problem" (1982, with Shostak, Pease) — `public` (self-archived)
3. "The Part-Time Parliament" (Paxos, 1998) — `public` (self-archived)
4. "Paxos Made Simple" (2001) — `public` (self-archived)
5. "Proving the Correctness of Multiprocess Programs" (1977) — `public` (self-archived)
6. "How to Make a Multiprocessor Computer That Correctly Executes Multiprocess Programs" (1979) — `public` (self-archived)
7. "The Temporal Logic of Actions" (1994, TOPLAS) — `public` (self-archived)
8. "Specifying Systems" (TLA+ book, 2002) — `public` (full free PDF, Lamport's own arrangement)
9. "A New Solution of Dijkstra's Concurrent Programming Problem" (1974, bakery algorithm) — `public` (self-archived)
10. "Distributed Snapshots: Determining Global States of Distributed Systems" (1985, with Chandy) — `public` (self-archived)

All 10 confirmed public.

## Lessons rollup

Lamport's works teach one coherent way of thinking, applied at every level from memory hardware to specification languages: state your assumptions and requirements formally before building, because in concurrency the intuitive walkthrough is worthless and the formal condition is the design. His method papers show how — correctness carved into safety and liveness, each proved by invariants over states rather than enumeration of interleavings, with system and specification written in one logic so that "implements" collapses into implication and most reasoning stays inside ordinary mathematics. His systems papers show the same reflex pointed at hidden assumptions: there is no global clock, only causal order the system can observe; no global state, only consistent states the computation could have reached; no absolute fault tolerance, only guarantees relative to an explicit failure model with a provable price; no composition of locally correct parts without a named whole-system condition; no primitive whose atomicity should be trusted rather than counted. And Paxos demonstrates the method's endpoint: derive the protocol from the invariants a proof would need, reduce all coordination to one agreed command sequence, and the algorithm arrives with its correctness argument already inside it.
