---
type: lesson
title: "A pure safety condition can quietly forbid progress; audit what your consistency contract makes impossible"
figure: herlihy
works: [linearizability-a-correctness-condition-for-concurrent-objects]
axes: [verifiability, parallelizability]
subdomains: [distributed-systems-and-concurrency, databases-and-data-management, formal-methods-and-verification]
tags: [lesson]
---

# A pure safety condition can quietly forbid progress; audit what your consistency contract makes impossible

**Lesson:** A correctness condition looks like a constraint on outcomes, so it seems it could only rule out bad answers, never prevent an answer from being produced. That intuition is wrong, and the failure is easy to miss because it happens one level below the implementation. Consider two participants that each read one object and then attempt to write the other; under a condition whose unit of atomicity spans both objects, there is no way to let both of them finish without violating the condition. No concurrency-control mechanism is at fault, and switching mechanisms does not help — the deadlock is a consequence of the contract itself, which is why systems built on such contracts must also ship rollback and retry machinery as a structural necessity rather than an optimization. The same audit applied to a per-operation, per-object condition comes out the other way: a participant with an outstanding invocation of a fully defined operation can always be given some response consistent with the condition, so the contract never forces anyone to wait.

The right way to read this is that safety and liveness constraints are not as separable as their names suggest. Choosing a consistency contract silently sets a floor on the coordination and recovery apparatus you will need, so the question to ask of any contract — an isolation level, a memory model, a module invariant — is not only which outcomes it forbids but which pending requests it can leave with no legal answer. If the answer is "some," you have signed up for abort-and-retry, or timeouts, or a scheduler with the authority to sacrifice a participant, whether or not you noticed.

Where a caller does want to wait, the discipline is to put the waiting in the specification rather than in the consistency machinery. Leave the operation undefined for the states in which waiting is intended, and the natural concurrent reading of that gap is precisely "wait until the state permits." The distinction that matters is between blocking that a caller asked for by writing a partial specification, and blocking that the correctness condition imposed on everyone by accident. The first is visible at the interface and can be reasoned about; the second is invisible until it deadlocks in production.

**Source:** [Linearizability: A Correctness Condition for Concurrent Objects](../works/linearizability-a-correctness-condition-for-concurrent-objects.md) — the nonblocking theorem for pending invocations of total operations, the two-register two-transaction history establishing that serializability is inherently blocking independent of mechanism, the accompanying note on failure atomicity having no counterpart here, and the treatment of partial specifications as the intended way to express deliberate waiting.
