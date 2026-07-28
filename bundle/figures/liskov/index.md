---
type: figure
title: Barbara Liskov
description: b. 1939, MIT. CLU abstract data types, Liskov Substitution Principle, and PBFT - the first practical Byzantine consensus protocol. Turing Award 2008.
status: accepted
layer: both
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency, programming-environments-and-object-systems]
tags: [figure, accepted]
---

# Barbara Liskov

**Dates:** b. 1939. American computer scientist, MIT Institute Professor; first US woman to earn a PhD in computer science.

## Why a candidate
- **Programming Languages & Semantics:** Designed CLU, the first language built around abstract data types as a primitive unit of modularity, and later formalized the semantic condition for safe subtyping (the Liskov Substitution Principle).
- **Distributed Systems & Concurrency:** Co-author (with Miguel Castro) of Practical Byzantine Fault Tolerance (PBFT), the first Byzantine consensus protocol shown efficient enough for real asynchronous deployment — reasoning about correctness under active, not just crash, faults.
- **Programming Environments & Object Systems:** CLU's clusters formalized encapsulation as a design primitive independent of implementation inheritance.

## Top 10 most influential works
1. "Programming with Abstract Data Types" (1974, with Zilles) — `public` (gold open access, confirmed)
2. "A Behavioral Notion of Subtyping" (1994, with Wing, ACM TOPLAS) — `public` (self-archived on Wing's CMU page)
3. "Data Abstraction and Hierarchy" (1987, OOPSLA keynote — origin of LSP) — `public` (self-archived, cs.tufts.edu mirror)
4. "Practical Byzantine Fault Tolerance" (1999, with Castro, OSDI) — `public` (self-archived at pmg.csail.mit.edu)
5. "Abstraction Mechanisms in CLU" (1977, with Snyder, Atkinson, Schaffert) — `paywalled`/`uncertain`
6. "CLU Reference Manual" (1981, with others) — `paywalled`
7. "Guardians and Actions: Linguistic Support for Robust, Distributed Programs" (1983, Argus) — `paywalled`
8. "Distributed Programming in Argus" (1988) — `paywalled`
9. "The Power of Abstraction" (2010 Turing lecture) — `public`/`uncertain`
10. "Providing High Availability Using Lazy Replication" (1992, with Ladin, Shrira, Ghemawat) — `paywalled`

## Lessons

Liskov's work returns again and again to one move: find the promise a piece of code is really making, write it down, and then arrange the machinery so the promise is the only thing anyone can depend on. A type is its operations and nothing about its storage, which is worth nothing unless the language makes the storage unreachable; a subtype is not a matching set of names but a guarantee that everything a client could prove about the parent still holds, which is why hierarchies that satisfy the compiler routinely break correctness and why families of related types have to budget their permitted variation in advance. From that same instinct come the sharper structural claims — that derivation of code says nothing about behavior, that admitting privileged insiders creates a second contract you now owe them, that a requirement belongs at the smallest scope needing it, that interfaces should be frozen and implementations chosen late, and that a rule you cannot check mechanically should be stated as an obligation rather than approximated by a check that inspires false confidence. Carried into distributed systems, the pattern holds with the stakes raised: never let a timing guess underwrite correctness, never let an unreliable diagnosis trigger an irreversible step, never make anything visible before it is as durable as the promise attached to it, and never assume failures are independent without engineering the independence. The distributed work also supplies the constructive counterpart — collapse every failure mode into the one outcome your code already handles, make that unit of failure nestable so recovery composes, name dependencies as data instead of negotiating order through coordination, and let each operation declare the consistency it actually needs so the rare strong case does not tax the common weak one. Underneath all of it sits a working method she states outright: cut the hard problems you are not answering out of scope, embody the idea in something people must use rather than arguing for it, prefer the simple mechanism that covers most cases and can be implemented cheaply, and design for the reader, who will encounter this code long after the convenience of writing it has been forgotten.
