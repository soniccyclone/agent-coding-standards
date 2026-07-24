---
type: lesson
title: "Design algorithms to survive the weakest primitives you can, and count every assumption you keep"
figure: lamport
works: [a-new-solution-of-dijkstras-concurrent-programming-problem]
axes: [hardware-affinity, verifiability, parallelizability]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---

# Design algorithms to survive the weakest primitives you can, and count every assumption you keep

**Lesson:** Every synchronization construct rests on assumptions about what the layer below guarantees: that reads and writes are atomic, that some test-and-set instruction exists, that a shared variable lives in memory that never fails. Those assumptions are usually inherited unexamined. The bakery algorithm demonstrates the opposite discipline: enumerate what you are assuming, then see how much of it you can throw away. It achieves mutual exclusion while tolerating a read that overlaps a write returning complete garbage, and while requiring no process to write into any memory but its own.

Two payoffs follow. First, every assumption removed is a hardware requirement removed: an algorithm that survives non-atomic reads runs correctly on machines that offer no atomic primitives at all, so weakening the algorithm's demands widens the set of physical mechanisms that can implement it. Second, every assumption removed is a shared fate removed. Prior solutions funneled all processes through one variable in one memory unit, so one component's death halted everyone; distributing the state so each process writes only locally turns central failure into an ordinary, tolerable event. Decentralization here is not an architectural taste, it falls straight out of asking which single points the correctness argument secretly leans on.

The transferable habit is to treat the assumption list as a first-class design object. Before trusting an algorithm, ask what its proof requires of the primitives; before building one, ask which of those requirements you could do without, and what each remaining one costs in hardware, in fault exposure, and in proof obligations. Sometimes the honest answer is that a weak-primitive solution needs an unbounded counter or extra complexity, and the trade is worth stating rather than hiding. The point is not that weaker is always better; it is that unexamined strength is unpriced debt.

**Source:** [A New Solution of Dijkstra's Concurrent Programming Problem](../works/a-new-solution-of-dijkstras-concurrent-programming-problem.md) — the algorithm's stated properties (overlapping read/write may return any value; each processor writes only its own memory; no central variable), the failure discussion, and the correctness assertions that explicitly avoid assuming atomic access.
