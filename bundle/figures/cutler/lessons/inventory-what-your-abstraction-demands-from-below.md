---
type: lesson
title: "Enumerate the mechanisms your abstraction silently requires from the layer beneath it, then price their absence as recurring"
figure: cutler
works: [decwest-sdt-agenda-prism-vs-mips]
axes: [hardware-affinity, primitive-count, parallelizability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Enumerate the mechanisms your abstraction silently requires from the layer beneath it, then price their absence as recurring

**Lesson:** Any substantial abstraction rests on a set of specific capabilities from the layer below that its designers absorbed as ambient and never wrote down. Asked to move onto a different substrate, the useful first act is to produce that list explicitly: the atomic operations that make its locks work, the asynchronous notification mechanism that makes completion and cancellation expressible, the prioritized interrupt structure that makes scheduling and deferred work possible, the counter that makes measurement possible at all, the protection bits that make its isolation claims true, the cross-processor signalling that makes any coordination possible. Written out, the list stops being a vague sense that the port will be awkward and becomes a checkable inventory, item by item, of what has to be replaced and at what cost.

The inventory also reframes what an evaluation is measuring. A substrate's attractive properties are usually immediate and easy to quantify — it exists today, it performs well, several suppliers make it, its toolchain is mature. What it lacks is diffuse and shows up as work distributed across a system that no longer has a place to put it. Comparing the two honestly means forcing the diffuse side into the same units as the immediate side, which is what a per-item estimate does. It is the only way an argument about foundations can compete with an argument about availability, because availability speaks in weeks and foundations otherwise speak in vague unease.

The sharpest part of the reasoning is about what kind of cost absence is. A missing mechanism does not impose a one-time port cost; it imposes the port cost plus an open-ended obligation, because working around a gap in one implementation does not stop the same gap from reappearing in the next one. Distinguishing the two — the cost of coping now versus the cost of designing something implementation-independent that prevents recurrence — is what separates an estimate you can plan against from one that will be exceeded every generation. Notice, finally, the structural critique that goes with this: a capability bolted onto a substrate as a side attachment rather than integrated into its core vocabulary tends to keep costing, because everything above must know about the attachment and about the seams where it does not quite fit.

**Source:** [DECwest/SDT Agenda: PRISM vs. MIPS](../works/decwest-sdt-agenda-prism-vs-mips.md) — the section itemizing which privileged hardware features the operating system depended on and what each was used for, followed by the impact estimate that separates analysis and implementation time from the unbudgeted work of architecting solutions that would keep the same problem from recurring on the next implementation.
