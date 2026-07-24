---
type: lesson
title: "Split every correctness claim into safety and liveness, and never let one pay for the other"
figure: lamport
works: [proving-the-correctness-of-multiprocess-programs, the-temporal-logic-of-actions, paxos-made-simple]
axes: [verifiability, expressiveness]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---

# Split every correctness claim into safety and liveness, and never let one pay for the other

**Lesson:** "Correct" is not one property. Every requirement a program must meet decomposes into claims that nothing bad ever happens (safety) and claims that something good eventually happens (liveness), and the two have fundamentally different logical shapes. Safety is refuted by a finite prefix of an execution and proved by an invariant preserved step by step; liveness is refuted only by an infinite execution and proved with fairness assumptions and well-founded counting-down arguments. Trying to establish both with one technique produces proofs that are muddled about what they actually show. Carving the requirement first, by logical shape, decides which proof machinery each piece needs before any proving starts.

The split is also a design principle, not just a proof convenience. The two halves can, and often should, hold under different conditions: a well-designed protocol keeps its safety properties unconditionally, under any pattern of delay, restart, and message loss, while its liveness is allowed to depend on luck or timing, since known impossibility results forbid guaranteeing both in a fully asynchronous world. Consensus done right can stall forever without ever choosing two different values. Knowing which guarantee you may weaken (progress) and which you may not (agreement) is what lets a designer navigate around impossibility instead of into it.

There is a subtler discipline downstream: express liveness through fairness conditions on the system's own actions rather than as arbitrary "eventually" assertions, because a carelessly conjoined liveness formula can smuggle in new safety constraints you never intended. A programmer with this habit reads any requirements document sorting each sentence into the two bins, asks of every system "what is unconditionally safe here, and what does progress depend on?", and distrusts any design whose progress argument is tangled into its safety argument.

**Source:** [Proving the Correctness of Multiprocess Programs](../works/proving-the-correctness-of-multiprocess-programs.md) — the introduction's definition of safety and liveness as the two property types, and the paper's deliberately separate proof methods for each. [The Temporal Logic of Actions](../works/the-temporal-logic-of-actions.md) — the formalization of the split, the fairness operators, and the machine-closure discussion of liveness conditions that accidentally add safety. [Paxos Made Simple](../works/paxos-made-simple.md) — safety maintained under all asynchrony while progress requires leader election, with the impossibility result cited as the reason the asymmetry is necessary.
