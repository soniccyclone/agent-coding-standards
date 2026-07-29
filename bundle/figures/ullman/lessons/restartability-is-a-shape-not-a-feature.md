---
type: lesson
title: "Restartability is a shape you keep, not a feature you add"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Restartability is a shape you keep, not a feature you add

**Lesson:** Fault tolerance in a large parallel computation does not come from error-handling code; it comes from a structural property of how the computation is arranged, and that property can be lost by innocuous-looking generalisations. The property is that a unit of work publishes nothing until it has finished. If that holds, a failed unit can simply be run again somewhere else, because nobody downstream ever saw its partial output and no duplicate can arise. The entire recovery machinery is then one line of policy — mark it idle, reschedule it — rather than a distributed protocol. This is why a restricted model that only lets you write two functions can survive thousands of unreliable machines while a more expressive one cannot.

The lesson bites when you extend the model. Widen two stages into an arbitrary acyclic graph of stages and the property survives, because output still flows only after completion. Allow cycles — which you must, the moment your real problem is a fixed point, a transitive closure, or an iterative descent — and it collapses immediately, for a reason that is not an implementation detail: mutually dependent units cannot all withhold output until they finish, or none of them would ever receive input. So the question "can I add recursion to this framework" is really the question "what am I replacing the blocking property with," and the honest answers are all more expensive: retain every message you ever emitted so a restarted peer can be re-fed, snapshot global state periodically and roll everything back to the snapshot, or record how each intermediate value was derived and recompute it on demand from durable roots. Each buys back recoverability at a different price, and none is free.

That last option deserves its own note, because it inverts a default. Instead of storing intermediate results redundantly in case they are lost, store the derivation — the sequence of operations that produced them — and treat the value itself as disposable. Recovery becomes recomputation, which is more work when a failure happens but eliminates writing and shipping intermediates when one does not. The justification is a timescale argument, not an elegance argument: over hours, failure is near certain and redundancy is mandatory; over the minutes a single job runs, failure is unlikely enough that paying more in the rare bad case to pay much less in the common good case comes out ahead. Faster jobs are also less likely to be interrupted, so the optimisation partly pays for its own risk.

A programmer who has absorbed this reads a framework's restrictions as the source of its guarantees rather than as friction to route around, and asks of any workflow change whether it breaks the invariant that makes retry safe. When it does, they choose the replacement mechanism deliberately and price it, instead of discovering at scale that "just rerun the failed piece" has quietly started producing double-counted results.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the chapter on cluster programming systems, which grounds task restart in the blocking property, then shows recursion destroying it and surveys the iterated-job, lineage, and checkpoint responses, alongside its discussion of why a rediscovered path is harmless but a double-counted aggregate is not.
