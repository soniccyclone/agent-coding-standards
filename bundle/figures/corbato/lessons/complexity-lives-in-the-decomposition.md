---
type: lesson
title: "Complexity Lives in the Decomposition"
figure: corbato
works: [multics-the-first-seven-years]
axes: [primitive-count, cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Complexity Lives in the Decomposition

**Lesson:** When the Multics team audited why so much of their system needed redesign, they found three recurring causes and none of them was bad code. Requirements of marginal importance were contributing a disproportionate share of the total complexity. Module boundaries and the interfaces across them had been drawn awkwardly. And they had to relearn that the dominant virtue of an algorithm is simplicity rather than clever machinery for unusual cases. The performance record points the same way: replacing an over-general variable-size storage scheme with plain fixed-size allocation bought better than an order of magnitude, while dropping into machine language for speed was worth doing in only about half a dozen places out of fifteen hundred modules.

The retrospective also supplies a positive criterion for a boundary, which is rarer and more useful than the warning. Treating the segmented virtual memory *as* the file system rather than as a separate feature alongside one decoupled physical placement and data movement from naming and directory structure, and the resulting split was simple in a way nobody had to argue for. The traffic controller collected into one small module a set of duties that are conventionally smeared across the scheduler, the input/output system, the file manager, and whatever ad hoc mechanism users have for signalling each other. In both cases the signature of the right division is absorption: responsibilities converge into one place instead of leaking into four. The authors say plainly that discovering such a division is difficult and that establishing one is grounds for celebration, which tells you they regarded it as the actual intellectual work rather than preliminary bookkeeping.

A programmer carrying this forward responds to a slow or tangled subsystem by re-examining where the lines were drawn and what the low-value features are costing, before touching the code inside them. The diagnostic question when a concern shows up in four modules is not how to share code between them but which boundary, drawn differently, would make it show up in one.

**Source:** [Multics: The First Seven Years](../works/multics-the-first-seven-years.md) — the three enumerated causes of design iteration in the development-history section, and the modular-division-of-responsibility discussion under insights, covering the virtual-memory-as-file-system decision and the traffic controller.
