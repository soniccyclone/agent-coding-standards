---
type: lesson
title: "Reason about a concurrent system by the set of outcomes still reachable, not by the history that produced the current state"
figure: lynch
works: [impossibility-of-distributed-consensus-with-one-faulty-process]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# Reason about a concurrent system by the set of outcomes still reachable, not by the history that produced the current state

**Lesson:** The natural way to think about a running distributed system is as a trace: this message arrived, that process advanced, here is where we are. That view is useless for proving anything, because the number of traces is unbounded and no two are alike. The move that makes the reasoning tractable is to forget the history entirely and label each global state by the set of final answers still reachable from it. A state from which two different answers remain possible is genuinely undecided; a state from which only one remains is already committed, whether or not anyone has noticed yet. Once you have that labeling, the whole question becomes a question about a single step: can the system always be pushed from an undecided state to another undecided state? If yes, indecision is an invariant and the algorithm never finishes.

This reframing is worth internalizing far beyond consensus. It converts an argument about infinitely many interleavings into an argument about a one-step transition, which is the kind of thing a person can actually hold in their head and a proof assistant can actually check. It also relocates the interesting event. In the trace view, the interesting moment is when a process writes its answer. In the reachability view, the interesting moment is much earlier and usually invisible: the step at which the last alternative outcome became unreachable. Every algorithm that produces a decision must contain such a step, and adversarial scheduling is precisely the art of never letting that step be the one that runs next.

A programmer who has absorbed this stops asking "what is the system doing right now" and starts asking "what is the system still allowed to do." The second question has a bounded answer and composes; the first does not. It changes how you instrument systems, too, because the quantity you want to observe is the residual freedom of the protocol rather than its accumulated log. And it explains why so many concurrency bugs feel like they have no cause: the state where the outcome was sealed is not the state where the damage became visible, and looking only at the history will never connect them.

**Source:** [Impossibility of Distributed Consensus with One Faulty Process](../works/impossibility-of-distributed-consensus-with-one-faulty-process.md) — the classification of configurations by the set of decision values reachable from them, and the lemma showing that from any undecided configuration a pending event can always be deferred long enough to land in another undecided one.
