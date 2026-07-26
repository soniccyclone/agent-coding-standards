---
type: lesson
title: "When composition destroys foreknowledge, build an observer instead of a predictor"
figure: denning
works: [the-working-set-model-for-program-behavior, virtual-memory]
axes: [hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# When composition destroys foreknowledge, build an observer instead of a predictor

**Lesson:** The instinct with any resource decision is to plan it at the point where the most is known about the program — the author's head, or the compiler's symbol table. Denning's argument is that the facts such a plan would need are systematically unavailable at the moment the plan has to be made. A program assembled from independently compiled modules, bound to each other only at run time, whose control flow depends on its input and whose components were written by other people, has no compile-time description of what it will touch. Asking the author fails for a different reason: his estimate is aimed at making his own program fast, not at serving the machine's other tenants, and the overhead of consuming his advice can exceed the benefit of having it. Neither failure is a tooling gap that better static analysis closes — both are consequences of modularity and data dependence, the very properties the design is trying to support.

If a quantity is only defined at run time, the right place to compute it is at run time, from what the machine can observe for itself. A mechanism that watches actual behavior needs no cooperation from anyone, cannot be defeated by a component it has never seen, and does something sensible when the program turns out to be unusual. That is the whole case for adaptive allocation over preplanned allocation, and it generalizes far past memory: any decision whose inputs only exist after linking, after configuration, or after the first real request belongs to an instrument, not to a plan.

The comparison has to be scored honestly, and this is where the reasoning usually goes wrong. Do not measure the adaptive mechanism against the hand-tuned plan at the plan's single design point. Denning's survey does the accounting properly: the automatic scheme ran modestly worse than careful hand-built overlays at the one memory size those overlays were built for, but producing the hand version cost substantially more human effort, and the automatic one held roughly the same performance across a wide range of memory sizes where the hand plan simply did not apply at all. Point optimality at one configuration is worth less than acceptable behavior at every configuration, once the cost of producing the point solution is on the ledger.

One caveat that programmers like to skip: the adaptive mechanism relieves you of knowing the machine's parameters, not of writing code that behaves. The measured advantage depended on the programs having been written to work on one region of data at a time. Automatic management can discover a program's demand; it cannot make a program whose demand is the whole address space cheap to run.

**Source:** [The Working Set Model for Program Behavior](../works/the-working-set-model-for-program-behavior.md) — the introductory argument that neither the programmer nor the compiler can supply allocation information, which is what motivates a run-time monitoring mechanism. [Virtual Memory](../works/virtual-memory.md) — the section weighing manual against automatic storage management, including the cost-of-production and robustness-across-memory-sizes comparison.
