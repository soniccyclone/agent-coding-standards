---
type: lesson
title: "A fault-tolerance claim is meaningless until you say when the faults are allowed to happen"
figure: lynch
works: [impossibility-of-distributed-consensus-with-one-faulty-process]
axes: [verifiability, parallelizability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# A fault-tolerance claim is meaningless until you say when the faults are allowed to happen

**Lesson:** The famous negative result about asynchronous agreement is usually remembered as a statement about a quantity: one failure is enough to break everything. The same paper immediately undercuts that reading by exhibiting a working protocol that tolerates a whole minority of failed participants, provided every failure is already in place before the protocol begins. The failure count went up and the problem became solvable. What actually changed was the adversary's schedule: it lost the right to strike partway through. So the line between solvable and unsolvable was never drawn by how many components can break — it was drawn by how much of the execution timeline the adversary is permitted to choose.

This should reframe how a designer reads any resilience budget. "Tolerates f failures" is not a specification; it is half of one. The other half is the temporal quantifier, and it is where all the difficulty lives. Failures fixed before the run starts are just a smaller system with an unusual membership. Failures that may appear at any instant, chosen with knowledge of the protocol's current state, are an adversary that gets to interleave itself into your control flow. The two are not degrees of the same thing; they are different problems that happen to share a headline number.

The reason this matters practically is that real specifications drift toward the easy quantifier without anyone noticing. A system tested by killing nodes before startup, or between requests, or at a quiescent point, has been tested against the tractable adversary. The hard adversary picks the moment inside the commit path, between the two writes that were supposed to be atomic together. Reasoning about worst-case timing is unpleasant enough that teams reliably substitute the version they can imagine, and then believe they have evidence for the version they need.

A programmer who has internalized this asks a different question in design review. Not "how many replicas can we lose," but "at which points in this algorithm's execution is a loss survivable, and what forces the loss to occur only at those points?" If nothing forces it, the answer is that the algorithm is only correct against a cooperative adversary, which is another way of saying it is correct in testing and wrong in production.

**Source:** [Impossibility of Distributed Consensus with One Faulty Process](../works/impossibility-of-distributed-consensus-with-one-faulty-process.md) — read the impossibility theorem against the paper's own later section, which presents a positive protocol for the case where participants may be dead at the outset but none dies during the run.
