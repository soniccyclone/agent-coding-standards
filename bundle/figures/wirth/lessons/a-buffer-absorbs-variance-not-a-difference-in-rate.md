---
type: lesson
title: "A buffer absorbs variance, not a difference in rate"
figure: wirth
works: [algorithms-and-data-structures]
axes: [hardware-affinity, parallelizability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# A buffer absorbs variance, not a difference in rate

**Lesson:** Interposing storage between a producer and a consumer is the standard answer to almost every mismatch between two stages, and it only works against one of them. What a buffer buys is the freedom for the two sides to be out of step momentarily and catch up later; what it cannot buy is a permanent difference in how fast they run. If the average rates are equal and only the instantaneous rates fluctuate, the buffer converts a hard timing constraint into a soft one and the constraint disappears from the program. If one side is genuinely slower on average, the buffer only delays the moment the difference becomes visible, and it delays it by an amount proportional to its size — which is why enlarging a buffer that is failing for the second reason is a fix that appears to work in testing and fails in production at exactly the scale where it matters. So before sizing anything, decide which of the two situations you are in, because the answers are unrelated: one is answered with storage and the other only by changing a rate.

The reason buffering is worth the trouble even in the easy case is that it removes a constraint the program was never able to satisfy. A physical device imposes timing it will not negotiate — data has to arrive at a fixed rate or the medium wastes space on restarts — and no ordinary computation can promise that. Accumulating output until there is enough of it to hand over as one unit means the program's timing stops being part of the correctness argument, and the size of that unit is dictated by the device's own structure rather than chosen for convenience. This is the general shape: a buffer is the place you convert a requirement you cannot meet into a requirement you can, and the conversion is what you are paying for, not the storage.

Two consequences worth carrying. First, the buffer's size is the amount of decoupling you have purchased, expressed in time rather than bytes, so state it that way — how long may either side stall before the other notices — because that is the number a reviewer can check against reality and a byte count is not. Second, when the two sides want to transfer in different unit sizes, the buffer is where the two units are reconciled, and its capacity should be chosen so that both divide it evenly; otherwise the reconciliation logic acquires cases that exist only because of an arbitrary number, and cases that exist for no reason are exactly the ones nobody tests.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 1.7.2's account of buffering as a way to let programs ignore the timing constraints imposed by mechanically moving devices, its statement that the decoupling between producer and consumer has an effect only if their rates are about the same on average but fluctuate at times and that the degree of decoupling grows with buffer size; together with the closing part of section 1.7.3, where producer and consumer transfer in different block sizes and the buffer's capacity is chosen as a common multiple of the two.
