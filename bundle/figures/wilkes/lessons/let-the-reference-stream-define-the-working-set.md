---
type: lesson
title: "When you cannot predict which data a computation will touch, build the mechanism that lets the touching itself decide"
figure: wilkes
works: [slave-memories-and-dynamic-storage-allocation]
axes: [cognitive-load, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, algorithms-and-complexity]
tags: [lesson]
---
# When you cannot predict which data a computation will touch, build the mechanism that lets the touching itself decide

**Lesson:** Anticipatory loading demands an answer to a question nobody is in a position to answer: of everything a computation could reach, which parts will it actually reach before it finishes or is suspended? The tempting response is to improve the forecast — profile it, annotate it, have the programmer declare it. The better response is to notice that the computation emits the answer itself, one reference at a time, at precisely the moment the answer becomes needed, and to build a mechanism that captures that emission instead of racing it. Promote nothing into the fast resource until a real reference asks for it, and the set of promoted items stops being an estimate of the working set and becomes a record of it.

The economics favour observation because a forecast has two ways to be wrong and an observation has one. Bulk anticipatory transfer charges you for everything fetched and never used, and charges you again for everything needed but not fetched. Demand-driven population deletes the first error outright — every item present was asked for — and reduces the second to a cost paid exactly once per item genuinely needed. What is left is a much smaller design problem: you no longer have to decide what to admit, only what to displace, and displacement is a decision you get to make with reference history already in hand rather than ahead of it. The hard part of the original problem has been converted from prediction into bookkeeping.

The shape recurs wherever a small fast resource fronts a large slow one — memoized results, warmed connections, lazily materialised indexes, incremental build artifacts. The signal to reach for it is someone being asked to declare up front a set that execution is about to reveal for free. One constraint travels with the pattern: the mechanism has to sit below the level that would otherwise have done the predicting, invisible to its clients. The moment a caller must cooperate to keep the population correct, the prediction problem is back, and back in a worse form — no longer one wrong guess in one place, but a guess distributed across every client who might forget to make it.

**Source:** [Slave Memories and Dynamic Storage Allocation](../works/slave-memories-and-dynamic-storage-allocation.md) — the definition of a slave store as one that automatically accumulates to itself words arriving from the slower memory and keeps them available without re-incurring the slow access, together with the large-slave section, which rejects copying an entire active block on the grounds that only a small fraction of it will be referenced before the block goes inactive, and copies each word at the moment the program calls for it instead.
