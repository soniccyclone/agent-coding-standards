---
type: lesson
title: "A primitive that carries no state has handed that state to every caller"
figure: thompson
works: [unix-implementation]
axes: [parallelizability, verifiability, primitive-count]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# A primitive that carries no state has handed that state to every caller

**Lesson:** The cheapest coordination primitives are the ones that remember nothing. If waiting and waking are keyed on nothing but a number, there is no registry to populate, no lifecycle to manage, no allocation before first use — the mechanism exists purely by being used, and costs a table lookup. That economy is real and worth wanting. But it comes with an exact, predictable bill: everything the primitive declined to remember still has to be remembered by somebody, and that somebody is every caller, separately, forever.

Two specific debts fall out of statelessness, and it is worth being able to name them in advance rather than discovering them under load. The first is that a signal with no memory cannot express quantity — it can only move waiters from asleep to awake, so all of them wake and contend for whatever became available, and the sizing of the thing they are waiting for is nowhere represented. The second is worse: with no record that the event occurred, the interval between deciding to wait and actually waiting becomes a window in which the wake-up can be lost entirely. The primitive is not wrong, but its correctness now depends on facts outside itself — on when control can transfer, on which code paths are allowed to interleave.

That dependence is the part to watch, because it is what determines whether the design survives a change of platform. A stateless wait is safe when transfers of control happen only at points the implementer chose, and unsafe the moment something genuinely asynchronous can signal. Scale that up and the missing state reappears as the central obstacle: the same primitive that was almost free on one processor is the first thing that breaks on several, precisely because the invariant it was leaning on was never written down anywhere.

So the working rule is to price a primitive by what it forces its callers to reconstruct, not by what it costs to invoke. When you choose the stateless version — often correctly — record in the same breath which external assumption is now load-bearing, and treat that assumption as part of the interface. The honest version of this thinking is willing to say out loud which mechanism in a system is its most suspect, and why, rather than presenting a cheap primitive as a free one.

**Source:** [UNIX Implementation](../works/unix-implementation.md) — the synchronization and scheduling discussion, which contrasts memoryless events with semaphore-style operations, then works through the resulting inability to signal quantity, the lost-wakeup race, and why this becomes the hardest part of adapting the system to multiple processors.
