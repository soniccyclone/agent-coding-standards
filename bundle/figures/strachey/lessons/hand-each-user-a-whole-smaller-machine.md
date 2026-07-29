---
type: lesson
title: "Hand each user a whole smaller machine, not a slice of yours"
figure: strachey
works: [time-sharing-in-large-fast-computers]
axes: [expressiveness, cognitive-load, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Hand each user a whole smaller machine, not a slice of yours

**Lesson:** When a scarce resource has to serve many clients at once, there are two ways to describe what each client gets. You can expose the sharing — tell the client it has the machine for certain intervals, subject to interruption by others — or you can hide it, and tell the client it has a machine of its own that happens to be slower and smaller than the physical one. The second description costs more to implement and is worth every bit of it, because it is the only one a client can reason about without knowing who else is present. Under the first description, every program's correctness depends on facts about its neighbours; under the second, a program's behaviour is a function of its own text.

The move generalises well beyond scheduling a processor. The right abstraction over a shared thing is usually a complete, self-consistent instance of that same kind of thing, scaled down — not a partial, conditional, or intermittent view of the original. A complete-but-smaller worldview can be understood on its own terms and it composes: whoever is handed one can go on to subdivide it the same way. A partial view leaks the sharing upward forever, and every layer above must re-learn the arbitration rules.

The constraint that keeps this honest is that the illusion must not become a ceiling. The multiplexing exists because the resource is usually being wasted by one client, not because dividing it is a good in itself, so the design must retain the ability to collapse all the fictional machines back into one and give a single large job the entire real apparatus. An abstraction layer that cannot be dissolved when the workload actually wants the whole resource has stopped serving the users and started serving itself. A programmer who takes this seriously builds isolation as a presentation choice with a documented escape hatch, rather than as a hard partition baked into the substrate.

**Source:** [Time Sharing in Large Fast Computers](../works/time-sharing-in-large-fast-computers.md) — the account of normal operation, where several operators each work as though at their own machine, closes by insisting that the full machine remains available to one large problem whenever that is wanted.
