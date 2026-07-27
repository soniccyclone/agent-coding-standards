---
type: lesson
title: "Convert the concurrent question into a sequential one, and let the data type's meaning pay for the concurrency"
figure: herlihy
works: [linearizability-a-correctness-condition-for-concurrent-objects]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---

# Convert the concurrent question into a sequential one, and let the data type's meaning pay for the concurrency

**Lesson:** Faced with behavior too complicated to describe, there are two routes: build a formalism powerful enough to describe it, or find a restriction under which the old, simple formalism still applies. Concurrency invites the first route — a specification language that talks directly about interleavings — and the resulting specifications are as complicated as the phenomenon. The second route is to define a class of well-behaved concurrent executions as exactly those indistinguishable from some legal execution of the same object run sequentially, with each operation appearing to happen all at once somewhere inside its own invocation-to-response window. Inside that class, an object's meaning is still just pre- and postconditions on its operations, and every question about a concurrent run becomes a question about one of its sequential stand-ins. You have not made the hard formalism easier; you have declined to need it, and paid the price of being unable to describe anything outside the class.

The subtler move is the choice of what the condition is allowed to know. Earlier concurrency reasoning treated shared data as uninterpreted, focusing on control structure, and consequently had to be conservative about what interleavings to permit. Making the condition depend on the object's own semantics inverts that: what counts as acceptable overlap for a queue differs from what counts for a stack or a set, because the question "could this have happened sequentially?" is answered by the type's own axioms. Knowing what the data means is therefore not a documentation nicety, it is what licenses concurrency an uninterpreted treatment must forbid. That is why a queue built on interleaved atomic increments and swaps, with no mutual exclusion anywhere, can be judged correct against the same two-line axioms a textbook sequential queue satisfies.

Two disciplines follow for a working programmer. First, an implementation is under no obligation to realize every overlap the condition allows; it must only never produce one the condition forbids. That converts the concurrency level from a specified property into an engineering dial the implementor can move without renegotiating with callers — provided callers reason only from the contract and not from observed timing. Second, be clear about what the condition does not cover. This is a safety notion only: it says which histories cannot occur and promises nothing about what must occur, so fairness, starvation, and priority need separate tools. Mistaking a safety contract for a complete specification is exactly the error that produces informally stated correctness claims which fail to rule out items vanishing from a queue outright.

**Source:** [Linearizability: A Correctness Condition for Concurrent Objects](../works/linearizability-a-correctness-condition-for-concurrent-objects.md) — the motivating comparison of intuitively acceptable and unacceptable queue and register histories, the formal definition via extension and equivalence to a legal sequential history, the discussion contrasting the data-oriented approach with control-oriented concurrent verification, and the closing remarks on safety versus liveness and on implementation freedom.
