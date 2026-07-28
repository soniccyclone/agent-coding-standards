---
type: lesson
title: "Redundancy only helps if the redundant parts are functions: force determinism first, and the whole reliability problem collapses into agreeing on one sequence of inputs"
figure: lampson
works: [how-to-build-a-highly-available-system-using-consensus]
axes: [parallelizability, verifiability, primitive-count]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Redundancy only helps if the redundant parts are functions: force determinism first, and the whole reliability problem collapses into agreeing on one sequence of inputs

**Lesson:** Duplicating a component buys nothing by itself. Two copies of something that can each wander off in its own direction give you two opinions and no way to pick between them, so redundancy is only useful once it is coordinated — and the cheapest coordination discipline available is to make every copy do exactly the same thing. That requires the copy to be a function from state and input to new state and output, with no hidden dependence on the local clock, on the local address space, on which random numbers it happened to draw, or on the order in which its own threads got scheduled. Once that constraint holds, two copies started in the same state and fed the same input sequence are indistinguishable, and any of them can answer.

The payoff is that a hard, open-ended engineering goal is reduced to one narrow question. You no longer have to reason about what "highly available" means for your particular service, or invent per-service repair procedures; you have to agree on the values and the order of the inputs, and everything else follows mechanically. That reduction is the actual content of the idea, and it is worth noticing what kind of move it is: not a technique for making a service reliable, but a way of restructuring the problem so that a single reusable mechanism can be pointed at it. Ordering itself folds into the same question — if you can attach a sequence number to each input, the ordering problem is just more agreement, which is why real systems let one designated process hand out consecutive numbers rather than deploying an elaborate scheme for totally ordering requests by timestamp and then proving you have seen every earlier one.

The corresponding cost is honesty about generality. Identical replication is the most general form of redundancy and therefore the most expensive one; schemes that store less — erasure codes, checksums, anything that reconstructs rather than copies — are cheaper precisely because they exploit specific structure in the data or the operation. So the choice between them is a choice about how much you know about your service. If you know its algebra, buy the cheap structural redundancy. If you know nothing except that it can be made deterministic, buy the general one and stop looking for a clever shortcut.

A programmer who has internalized this treats nondeterminism inside a replicated component as a correctness bug rather than a harmless detail, and hunts it in the boring places: timestamps read from the local machine, iteration over a hash container, uninitialized memory, anything that consults the environment instead of the input. They also stop trying to make each individual service fault-tolerant on its own terms, and start asking what the input sequence is and who is allowed to extend it.

**Source:** [How to Build a Highly Available System Using Consensus](../works/how-to-build-a-highly-available-system-using-consensus.md) — the opening argument that replication requires coordination, and the section on coordinating replicas that recasts availability as agreement on an ordered input stream, including the aside on why structure-exploiting redundancy is cheaper but narrower.
