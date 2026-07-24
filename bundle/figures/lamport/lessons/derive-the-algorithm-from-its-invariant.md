---
type: lesson
title: "Derive the algorithm from the conditions that make it correct, so the proof precedes the code"
figure: lamport
works: [the-part-time-parliament, paxos-made-simple]
axes: [verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---

# Derive the algorithm from the conditions that make it correct, so the proof precedes the code

**Lesson:** The usual order of work is: invent a mechanism, then try to prove it correct. For subtle problems this order is backwards. The alternative is to start from the requirements, strengthen them step by step into conditions a running system can actually maintain — each strengthening forced by asking how a proof of the previous condition would have to go — and only then read the protocol off as the operational shadow of those conditions. Done this way, the algorithm is not a clever artifact that happens to satisfy its proof; the proof skeleton existed first, and every message and rule in the protocol exists because some invariant demands it. The end product feels less invented than inevitable, which is precisely what makes it comprehensible: a reader can reconstruct why each piece must be there.

The method has a characteristic move worth naming: when maintaining an invariant would require predicting the future (what some participant might later do), do not predict — constrain. Extract a promise that narrows future behavior until the invariant becomes checkable from present state alone. That single move converts an unprovable condition into a protocol step. It also explains why the derivation-first approach finds designs that mechanism-first invention misses: the design space is navigated by proof obligations, not by analogy to existing systems. Fittingly, the conditions at the core of the consensus protocol were discovered during an attempt to prove the problem unsolvable; a failed impossibility proof, pushed honestly, hands you the requirements any solution must meet.

A programmer who works this way asks, before writing a distributed protocol: what must never be violated, what would a proof of that need, and what is the weakest promise each participant can make to carry that proof? Code that emerges from this questioning arrives with its correctness argument built in, and changes to it can be judged by whether they preserve the invariants rather than by re-simulating scenarios.

**Source:** [The Part-Time Parliament](../works/the-part-time-parliament.md) — the presentation order in which the ballot conditions are stated and proved sufficient before any protocol appears, the protocol then derived to preserve them, and the footnoted history that the conditions emerged from an attempted impossibility proof. [Paxos Made Simple](../works/paxos-made-simple.md) — the stepwise strengthening from the safety requirements through successively stronger conditions, including the pivot from predicting future acceptances to extracting promises, with the algorithm stated only after the derivation forces it.
