---
type: lesson
title: "If your code may be run speculatively, it must be defined on states that could never legally occur"
figure: herlihy
works: [a-methodology-for-implementing-highly-concurrent-data-objects, software-transactional-memory-for-dynamic-sized-data-structures]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---

# If your code may be run speculatively, it must be defined on states that could never legally occur

**Lesson:** Any mechanism that lets work proceed optimistically and discards it on conflict has a consequence people underestimate: the discarded work still ran. A slow participant can read a snapshot that was being overwritten as it was copied, obtaining a bit pattern that is not a legal state of the data structure at all, and then execute the ordinary sequential operation over that garbage. The result will certainly be thrown away, which handles correctness — but only if the doomed execution manages to finish without indexing out of range, dividing by zero, or corrupting something outside its own workspace. Being wrong is free; crashing is not, and neither is scribbling somewhere the rollback cannot reach.

Two obligations follow, and both belong to the code being transformed rather than to the transformation. The first is that operations must be total: defined for every state, returning an explicit refusal rather than faulting. This is not a stylistic convention. Even a program in which one can prove by inspection that a dequeue is never called on an empty structure will, under this machinery, execute a dequeue against an empty structure, because a participant reads the object and the pending-operations list at two different moments and the two need not agree. The second is that a speculative operation may not touch anything outside the region that gets discarded, since anything it writes elsewhere survives the abort. Notice that these two requirements together are exactly the definition of code that is safe to run and forget — which is what optimistic concurrency, transactional rollback, and hardware speculation all require of the code they run.

The generalizable habit: whenever you adopt a mechanism that may replay or abandon work, stop reasoning about which states are reachable and start asking which states are representable. Invariants that hold for all legal executions are worthless here, because the speculative execution is not a legal execution. Either make the code total over representable inputs, or interpose a validity check between reading the state and acting on it — the paper does the latter with a pair of counters bumped in opposite orders around a modification, so that a matching pair proves the copy was taken cleanly, and notes that a hardware instruction to answer the same question would be trivial to add to a machine that already implements a conditional store. Cheap detection of "the thing I read was already stale" is worth more than it looks.

**Source:** [A Methodology for Implementing Highly Concurrent Data Objects](../works/a-methodology-for-implementing-highly-concurrent-data-objects.md) — the constraints placed on sequential operations in the small-object section, the race in which a copy is taken from a block being recycled, the counter-pair consistency check and the suggested hardware validate instruction, and the later explanation of why totality is required even when the calling pattern appears to make an illegal call impossible.
