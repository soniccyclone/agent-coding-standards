---
type: lesson
title: "Correct parts do not make a correct whole; name the composition condition and price it"
figure: lamport
works: [how-to-make-a-multiprocessor-computer-that-correctly-executes-multiprocess-programs]
axes: [hardware-affinity, parallelizability, verifiability]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---

# Correct parts do not make a correct whole; name the composition condition and price it

**Lesson:** A component can satisfy its own specification perfectly and still break the system it is placed into, because the component's spec was stated relative to that component alone. A processor that reorders operations while preserving its own sequential semantics is flawless in isolation; put two of them against a shared memory and a two-line mutual-exclusion protocol that is provably correct on paper fails, since correctness of the protocol assumed an ordering property no individual part promised. The lesson is that whole-system correctness needs its own explicitly stated condition — here, that the execution be equivalent to some interleaving respecting each program's order — and that condition belongs to the system boundary, not to any part.

Once the condition is named, it becomes something you can implement, verify against, or knowingly trade away. Working out what sequential consistency demands of hardware yields concrete, checkable requirements on request ordering and memory servicing; and it also reveals the price, since meeting the condition forbids specific optimizations that make individual parts faster. That trade is legitimate, but only as a visible decision: a system that abandons the condition for speed must accept that ordinary reasoning about its programs is no longer sound, and that synchronization must then be reasoned about at the level of raw machine behavior, where verification costs explode.

The way of thinking transfers far beyond memory models. Whenever components compose, ask: what property does the composition need that no component individually asserts? State it as precisely as the components' own specs, and treat any performance trick that weakens it as changing the contract, not merely the implementation. Programmers who skip this step end up debugging emergent failures that no unit test could catch, because every unit was, in fact, correct.

**Source:** [How to Make a Multiprocessor Computer That Correctly Executes Multiprocess Programs](../works/how-to-make-a-multiprocessor-computer-that-correctly-executes-multiprocess-programs.md) — the definition of sequential consistency as a whole-machine condition distinct from per-processor sequentiality, the mutual-exclusion counterexample, the derived requirements R1 and R2, and the closing observation on the cost of giving the condition up.
