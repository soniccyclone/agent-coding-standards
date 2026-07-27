---
type: lesson
title: "Reason about a protocol by what it has not yet ruled out, not by tracing its runs"
figure: fischer
works: [impossibility-of-distributed-consensus-with-one-faulty-process]
axes: [verifiability, parallelizability]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---

# Reason about a protocol by what it has not yet ruled out, not by tracing its runs

**Lesson:** The useful thing to know about a system state is not what it has computed so far but which outcomes are still reachable from it. Classify a state by the set of final answers that remain possible: if two different answers are still reachable, the system has committed to nothing yet, however much work it has done. That single relabelling turns an intractable question — what does this protocol do, over all interleavings, for all inputs, for all failure patterns? — into a question about how a step changes the reachable set, which is small enough to argue about exhaustively.

The reason this works is that any protocol that terminates must, somewhere, take a step that shrinks the reachable set from two possibilities to one; that step is where the decision actually gets made, and it is a specific, findable object. An argument about whether such a step can always be forced is then an argument about scheduling: can an adversary who controls only the order and timing of message delivery always keep some step of that kind postponed while still letting every process run and every message arrive? Because message delivery order is unconstrained and any step by an uninvolved process commutes with any other, the answer is yes — the adversary reaches the undecided-but-still-live state again after every stage, forever. Nothing about the protocol's cleverness enters; only the shape of its reachable-set transitions.

Naming the property this way is also what makes the known escape routes legible as escapes rather than as tuning. Randomization does not remove the region where two outcomes are still live; it removes the adversary's ability to steer reliably into it, so the chance of staying there decays instead of persisting. A timing assumption does not remove it either; it removes the guarantee that the postponing step is always available. Both are attacks on a structural property of the state space, and neither is recognizable as such until the property has a name.

A programmer who thinks this way stops reading concurrent code as a set of traces to be enumerated and starts asking what each operation forecloses. Where is the commit point? Which steps are order-sensitive because they narrow the outcome set, and which commute freely because they do not? That question is answerable by inspection, scales to systems whose trace space is infinite, and identifies the exact places where coordination is genuinely required rather than merely conventional.

**Source:** [Impossibility of Distributed Consensus with One Faulty Process](../works/impossibility-of-distributed-consensus-with-one-faulty-process.md) — the bivalent/univalent classification of configurations, the commutativity lemma for disjoint process sets, and the stage-by-stage construction of a non-deciding admissible run.
