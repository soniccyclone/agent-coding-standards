---
type: lesson
title: "Concentrate the unrecoverable case into one named component"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Concentrate the unrecoverable case into one named component

**Lesson:** There is an instinct, when building something meant to survive failures, to spread resilience evenly — every part should tolerate the loss of every other part. That goal is expensive and usually unattainable, and pursuing it uniformly tends to produce a system where the recovery reasoning is diffuse, partially implemented everywhere, and confidently believed nowhere. The better structure is often the opposite: arrange things so that exactly one component's loss is fatal, make every other loss cheaply recoverable, and then state plainly which component that is. A coordinator that tracks the state of every unit of work and reassigns the failed ones can make thousands of unreliable workers a non-event; the coordinator itself dying restarts the job, and that is the whole of the exposure.

What makes this a design win rather than an excuse is that the fatal case becomes a single, small, inspectable object. You can compute its probability, because it is one machine rather than a distribution over thousands. You can bound its cost, because the consequence is "start over" rather than an unknown corruption. You can decide separately and later whether to buy it down — replicate the coordinator, checkpoint its bookkeeping — without touching the recovery story for anything else, because the two stories were never entangled. And crucially, a reader of the system can hold the failure model in their head: everything is retryable except this, which is a far more useful sentence than a page of per-component caveats.

The generalisable move is to stop asking "is this fault-tolerant" and start asking "what is the smallest set of losses I have not covered, and is it named." Almost every real system has such a set. The difference between a good one and a bad one is whether the set was chosen deliberately and pushed into one place, or whether it accumulated by accident and is scattered across a dozen components that each assumed someone else handled it. The former is a decision you can revisit; the latter is discovered in production, usually by observing that the recovery path itself needed the thing that was lost.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 2's section on coping with node failures, which states flatly that the failure of the node running the Master requires restarting the entire job while only that one node can bring the process down, all other failures being handled by rescheduling idle tasks.
