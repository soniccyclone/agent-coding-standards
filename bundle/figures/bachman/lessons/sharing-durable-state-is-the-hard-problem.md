---
type: lesson
title: "Sharing durable mutable state is a different problem from sharing the machine"
figure: bachman
works: [the-programmer-as-navigator]
axes: [parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, databases-and-data-management]
tags: [lesson]
---
# Sharing durable mutable state is a different problem from sharing the machine

**Lesson:** Multiprogramming works because the resources being shared — processor time, address space — return to a neutral condition between jobs; each job can pretend it owns the machine. Bachman's insight is that shared data breaks this pretense in kind, not just in degree: a record keeps its updated value after the job that wrote it is gone, so concurrent jobs observe each other *through the data* no matter how well the OS isolates their memory. He names the two failure species this produces: one job's updates silently invalidating another's in-progress computation, and a job consuming output from a peer that later aborts, so the abort must propagate to everyone who read from it. Neither failure exists in pure compute sharing.

Two design consequences follow. First, the visibility question must be answered deliberately: how much of this turbulence should the application programmer see? Bachman describes a production system that answered "none" — automatic record blocking, deadlock detection, transparent abort-and-restart — and reports its costs honestly: roughly one job in ten aborted and retried. Second, the right efficiency metric is throughput of successfully completed work, not the absence of conflicts. He explicitly leaves open whether hiding concurrency entirely, detecting conflicts after the fact, or exposing the problem to programmers yields more finished jobs per hour, and insists the answer is workload-dependent rather than a matter of principle.

A programmer who absorbs this stops treating aborts and retries as failures to be engineered away and starts treating them as a normal, priceable cost of sharing durable state. They distinguish sharply between read-only sharing (unlimited, safe) and shared update (the entire problem), place the programmer-visibility line as an explicit design decision with its own trade-offs, and evaluate concurrency schemes by completed work under the real workload instead of by the elegance of their conflict-avoidance story.

**Source:** [The Programmer as Navigator](../works/the-programmer-as-navigator.md) — the shared-access section in the lecture's second half: the contrast with multiprogramming, the definitions of the two failure modes, and the Weyerhaeuser abort-rate discussion with its open questions.
