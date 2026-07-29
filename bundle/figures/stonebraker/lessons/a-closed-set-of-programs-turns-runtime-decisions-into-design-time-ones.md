---
type: lesson
title: "A closed set of programs turns runtime decisions into design-time ones"
figure: stonebraker
works: [the-end-of-an-architectural-era]
axes: [expressiveness, verifiability, parallelizability]
subdomains: [databases-and-data-management, distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# A closed set of programs turns runtime decisions into design-time ones

Most of a general-purpose system's machinery exists to cope with not knowing what it will be asked to do. It plans while running because the request is new. It detects conflicts while running because it cannot know which requests will collide. It guards against arbitrary durations because the next request might be enormous. Every one of those mechanisms is a runtime tax paid to purchase ignorance insurance, and the premium is charged on every request forever.

The move worth learning is to ask whether the ignorance is real. In a large class of systems, the set of programs that will ever run against the data is not open at all — it is a fixed, small catalogue, written by the same organization that owns the schema, differing between invocations only in the constants supplied. Once you make that closure an explicit requirement rather than an accident you happen to enjoy, the analyses that were impossible become possible. Which programs can touch each other's state is now a question about a finite set of pairs, answerable once. Whether a program ever needs to communicate mid-flight, or ever needs to be undone, is a property you can decide before it ever executes. The runtime shrinks to executing decisions rather than making them.

The reason this holds is that dynamic mechanisms are not fundamentally about correctness; they are about the moment at which information arrives. Locking is what you do when you learn about a conflict too late to have avoided it. If the information arrives earlier — at the time the program catalogue is registered — the same correctness can be obtained by construction, and the detection apparatus is not merely cheaper, it is absent. The trade is honest and should be stated as such: you have given up the ability to accept a request nobody anticipated, and you have made your system's speed depend on someone doing the up-front analysis, which may be hard enough that only a human can do it.

A programmer who believes this stops treating "the system must accept anything" as a free axiom and starts treating it as a priced feature. When the workload is genuinely closed, they declare the closure loudly, at the interface, and spend the resulting freedom on deleting subsystems. When it isn't, they look for the boundary inside their system where it *is* closed, and put the design-time analysis there instead of abandoning the idea.

**Source:** [The End of an Architectural Era (It's Time for a Complete Rewrite)](../works/the-end-of-an-architectural-era.md) — the requirement that every transaction class be registered ahead of time, and the section deriving schema and workload properties (single-sited, one-shot, two-phase, sterile) from that catalogue in order to justify removing concurrency control and undo logging.
