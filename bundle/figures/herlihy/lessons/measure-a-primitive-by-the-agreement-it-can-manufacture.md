---
type: lesson
title: "Measure a synchronization primitive by how much agreement it can manufacture, not by how much it can compute"
figure: herlihy
works: [wait-free-synchronization]
axes: [hardware-affinity, primitive-count, parallelizability]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---

# Measure a synchronization primitive by how much agreement it can manufacture, not by how much it can compute

**Lesson:** Intuitions about the power of a machine operation are usually formed on sequential ground, where shared memory that can be read and written is enough to encode anything computable. Carry that intuition into a concurrent, fault-prone setting and it fails outright: plain reads and writes cannot support a shared queue, stack, set, or list in a way that tolerates one participant stalling — not because the algorithm hasn't been found, but because no such algorithm exists. Computational universality and coordination power are different quantities, and the second is the one that governs concurrent implementation. The right currency for it is how many participants a primitive can drive to an irreversible common decision.

Once power is measured that way, the ranking is unintuitive in useful directions. Ordinary read-modify-write operations, the family that includes most of the classical synchronization instructions, all sit at exactly two — the fatal property they share is that any two of them either commute or one wholly obliterates the other, which means a third participant can never tell which happened first, and that indistinguishability is the whole proof. A FIFO queue also sits at two, yet adding a single non-destructive inspection operation to the same queue lifts it to unbounded power, because the inspection makes the winner observable without disturbing it. Adding an operation, not adding storage or speed, is what changes the class. Meanwhile a compare-and-swap, which merely conditions its write on the value it expected to find, is at the top, because a single guarded write makes "someone already decided" a stable, readable fact. The differences that matter are about whether the order of events leaves a durable, observable trace — nothing to do with instruction cost, generality of arithmetic, or how many uses the primitive has been put to.

This reorients how one reads a hardware manual or an API. Do not ask what the operation does; ask what an uninvolved third party can subsequently learn about who got there first. A programmer with this habit stops asking whether a machine is fast enough for a concurrent structure and starts asking whether it offers any operation of sufficient coordination class at all, since below the required class no amount of ingenuity or hardware throughput helps. It also explains why message passing over ordinary channels is not a shortcut around the problem: modelled honestly, unordered channels are weak in exactly the same way shared queues are, and only ordered broadcast escapes.

**Source:** [Wait-Free Synchronization](../works/wait-free-synchronization.md) — the consensus-number definition and the hierarchy table, the theorems placing read/write at the bottom and interfering read-modify-write families at two, the contrast between a plain queue and the same queue with a non-removing inspection, and the treatment of message-passing architectures in the same currency.
