---
type: lesson
title: "Shrink what you hold before getting clever about arbitrating collisions"
figure: herlihy
works: [software-transactional-memory-for-dynamic-sized-data-structures]
axes: [parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---

# Shrink what you hold before getting clever about arbitrating collisions

**Lesson:** Once a system has a mechanism for resolving contention, contention starts looking like a resolution problem, and effort flows into smarter arbitration. Usually the larger win is upstream. Consider a participant walking a linked structure from the front: under a naive discipline it accumulates every node it passed, so a traversal deep into the structure is recorded as depending on the entire prefix, and two participants working on completely unrelated regions collide because both went through the front door. Nothing about the operations conflicts; the bookkeeping invented the conflict. Discarding each node's claim once it can no longer matter cuts the recorded footprint from the whole path to a couple of nodes, and the collisions simply stop happening — measurably, the version that does this survives with the crudest possible arbitration policy, while the version that does not stalls immediately under the same policy.

Two costs fall together, which is the tell that the footprint was the real variable. Every recorded dependency has to be rechecked, so the validation work is quadratic in how much you hold; holding a bounded number at a time makes the same operation's overhead linear in the structure size instead. So reducing the footprint buys both fewer conflicts and less checking, whereas better arbitration buys neither — it only distributes the losses more gracefully. The order of attack follows: first ask what the operation genuinely depends on at each moment, then arbitrate whatever irreducible overlap remains.

The honest half of this lesson is what the shrinking mechanism costs, and the paper is direct about it: releasing a dependency early means the system stops watching it, so a participant can now observe a state no serial execution would have produced, and unlike a doomed speculative execution it can commit that observation. A guarantee the machinery used to enforce becomes an obligation the programmer must discharge by argument. That trade is worth making with eyes open and worth marking loudly at the point of use, because the mistake it enables is a silent correctness violation rather than a crash or a retry. The general principle: an optimization that revokes a system-enforced property must be opt-in, local, and legible, and you should reach for it only after the free reductions in footprint have been taken.

**Source:** [Software Transactional Memory for Dynamic-Sized Data Structures](../works/software-transactional-memory-for-dynamic-sized-data-structures.md) — the conflict-reduction section on read-mode access and early release of traversed nodes, the cost analysis showing validation overhead falling with the number of simultaneously held objects, the experiment in which the reduced-footprint list tolerates the trivial arbitration policy, and the stated warning that releasing early shifts a linearizability obligation onto the programmer.
