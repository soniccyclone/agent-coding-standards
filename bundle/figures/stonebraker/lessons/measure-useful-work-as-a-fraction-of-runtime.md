---
type: lesson
title: "Measure useful work as a fraction of runtime"
figure: stonebraker
works: [the-end-of-an-architectural-era]
axes: [hardware-affinity, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Measure useful work as a fraction of runtime

The move that makes this critique devastating is arithmetical, not architectural. Take the heaviest unit of work in the standard benchmark, count the records it actually touches, and compute how long that touching should take on the machine in front of you. The answer is a fraction of a millisecond. Then measure what the system takes. Everything between the two numbers is overhead: durability bookkeeping, lock acquisition, latch acquisition, thread scheduling, resource governing, and process-boundary crossings to get the request in and the answer out. Framing performance this way converts a vague sense that things are slow into a budget with named line items, each of which can be attacked or eliminated.

Two consequences follow that would not follow from ordinary profiling. First, the ratio tells you whether you are looking at an optimization problem or an architecture problem. When useful work is a percent or two of elapsed time, tuning the overhead is rearranging deck chairs; the only interesting question is which overheads can be made to not exist. The paper's measurement — the majority of elapsed time inside the durability subsystem alone, with the concurrency subsystem next in line, and the professional tuner unable to move it — is exactly this diagnosis. Second, the ratio identifies the *next* bottleneck before you have removed the current one, so you can predict whether a fix is worth building: with durability writes gone, the interface overhead and the locking overhead move to the front, which is why the redesign attacks all of them at once rather than shipping an improvement that would be immediately re-bounded.

The habit this produces is worth more than any specific finding. Before proposing a fix, estimate the irreducible cost of the actual work — bytes that must move, comparisons that must happen — and compare it with observed cost. If the gap is a factor of two, tune. If it is a factor of fifty, stop tuning and go find out what all that time is defending, because the answer is usually a stack of mechanisms each of which was individually reasonable and none of which was ever re-justified against the current hardware or the current workload.

**Source:** [The End of an Architectural Era (It's Time for a Complete Rewrite)](../works/the-end-of-an-architectural-era.md) — the design-considerations section's estimate of per-transaction useful work, and the results section's accounting of where the commercial system's elapsed time went.
