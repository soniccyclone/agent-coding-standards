---
type: lesson
title: "Two resources that constrain each other need one allocator, not two good ones"
figure: denning
works: [the-working-set-model-for-program-behavior, thrashing-its-causes-and-prevention]
axes: [cognitive-load, parallelizability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Two resources that constrain each other need one allocator, not two good ones

**Lesson:** Processor scheduling and memory management had grown into separate literatures with separate techniques, each making progress on its own terms. Denning's structural claim is that they were never separate problems: a unit of work's claim on the processor and its claim on memory are two readings of one ongoing activity. A scheduler that admits work without consulting memory and a replacement rule that evicts without consulting who is runnable are each locally defensible and jointly incoherent. He forces the coupling into the open by giving every unit of work a demand expressed in both dimensions at once, and by restating allocation as the problem of holding the aggregate of those demands near a target.

The reason the split cannot survive is that whichever decision moves first constrains the other. Admitting one more unit of work than memory can hold does not slow that unit down in proportion — it degrades every unit already running, through a resource neither the scheduler nor the replacement rule was looking at. So the decision has to be made somewhere both quantities are visible. In the working-set formulation this collapses into a single rule with a hard precondition: a unit becomes eligible to run only when its memory claim is already satisfied, and its pages become removable only when it is not running. That one sentence is simultaneously a memory policy and an admission policy, which is exactly what the coupling demands.

There is a second, sharper piece of guidance for multi-dimensional allocation: the dimensions are not symmetric, so satisfy them in order of how badly overcommitment punishes you. Denning is explicit that memory must be balanced first and the processor used only to break ties, because overcommitting memory is catastrophic while overcommitting processor time is merely wasteful. Ranking the dimensions by the shape of their failure — cliff versus slope — is a general recipe for turning a vague "balance the system" goal into an ordered policy.

A programmer who believes this stops adding feedback between two independently tuned controllers and starts looking for the fault line where their local optima meet. When two subsystems each optimize a resource that gates the other, the repair is to move the decision to a place that sees both, not to make each subsystem smarter about the other's telemetry.

**Source:** [The Working Set Model for Program Behavior](../works/the-working-set-model-for-program-behavior.md) — the framing of process and working set as two manifestations of one computation, the resulting joint demand pair, and the balance policy built on it. [Thrashing: Its Causes and Prevention](../works/thrashing-its-causes-and-prevention.md) — the property that separates working-set management from the alternatives, namely the explicit link it forces between admission and memory residency.
