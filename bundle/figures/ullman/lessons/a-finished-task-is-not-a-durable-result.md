---
type: lesson
title: "A task that finished is not a result that survives"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, parallelizability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# A task that finished is not a result that survives

**Lesson:** Marking a unit of work "done" records that its code ran to completion. It says nothing about whether the value it produced is still reachable when someone comes to consume it. The two get conflated because on one machine they coincide: a function returned, so its result is in memory, and if the memory is gone so is the caller. Spread the same computation across machines and the two come apart sharply. A stage that wrote its output to the local disk of the machine that computed it has a result whose lifetime is tied to that machine, so losing the machine retroactively un-completes the work — not because the computation was wrong, but because nothing downstream can still read it. Losing a machine that was merely *running* something is the cheap case; losing one that had already finished is the expensive one, because the scheduler must reopen a task it had already retired and tell every consumer that the address it was given is now wrong.

The design consequence is that durability, not completion, is the event worth recording. Whoever tracks progress should track where each result physically lives and how many independent failure domains would have to die before it becomes unreadable, and should treat "completed" as shorthand for "completed and placed somewhere that outlives the producer." That reframing immediately raises a cost question you would otherwise never ask: publishing every intermediate into replicated shared storage makes completion mean what you want it to mean, but pays a write and a network crossing for results that will usually be consumed once, seconds later, and then discarded. Keeping them local is much faster and accepts that some finished work will be thrown away and redone. Neither is universally right; what is universally wrong is choosing one without noticing you chose.

The same confusion appears far from clusters. A build step whose artifact sits in a container that is about to exit, a cached computation held only in one process's heap, a migration that "succeeded" but wrote to a replica that has not yet been acknowledged — in each case a completion signal has been trusted as a durability claim. The habit to build is to ask, of every recorded success, which single machine or process would have to disappear to make the success meaningless. If the answer is one, the record is optimistic, and the recovery plan must include re-running things that already said they were finished.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the MapReduce node-failure discussion, where a failed map worker forces even its already-completed tasks back to idle status because their outputs lived on that worker's local disk, while a failed reduce worker costs only its in-progress work.
