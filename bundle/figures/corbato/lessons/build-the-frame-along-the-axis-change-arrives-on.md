---
type: lesson
title: "Build the Frame Along the Axis Change Arrives On"
figure: corbato
works: [introduction-and-overview-of-the-multics-system, multics-the-first-seven-years]
axes: [expressiveness, hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Build the Frame Along the Axis Change Arrives On

**Lesson:** Multics was proposed with the explicit admission that its requirements were not knowable, which is a common enough thing to say. What makes the 1965 paper worth reading is that Corbató does not respond by trying to be general in every direction. He names the axes along which change will actually arrive and spends the abstraction budget there. Hardware generations turn over on one clock and software on another, and few organizations can afford to run both simultaneously during a transition, so writing the system in a largely machine-independent language is a way of unbinding the two schedules from each other. That is an argument about project risk, not about programmer convenience.

The same reasoning appears in the capacity dimension. Processors, memory modules and I/O controllers are pooled and anonymous, with no processor reserved for the supervisor, precisely so that a configuration can grow or shrink without either the supervisor or user programs being reorganized. The abstraction is placed at the seam where the physical world varies, and it is placed nowhere else — the paper is happy to name specific drum characteristics and page sizes where those are not expected to move underneath it. Generality has a cost in every direction you buy it, so the interesting engineering question is not whether to be flexible but where the fault line runs.

Someone reasoning this way asks, before inserting an indirection, what is going to change here and on what schedule. Indirection placed on a stable axis is pure overhead and pure reading cost; indirection placed on the moving axis is what lets the system survive a generation it was not designed for. The seven-years retrospective reports the verdict a project length later, and it is unromantic: this class of system has to evolve indefinitely because starting over is prohibitively expensive and takes years nobody will grant you, so evolvability is a hard requirement placed on the design rather than a virtue.

**Source:** [Introduction and Overview of the Multics System](../works/introduction-and-overview-of-the-multics-system.md) — the opening summary's argument for an evolutionary framework and the reasoning for a machine-independent implementation language, together with the system-requirements discussion of pooled interchangeable units. The seven-years paper's concluding claim about indefinite evolution is the retrospective form of the same position.
