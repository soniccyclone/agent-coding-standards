---
type: lesson
title: "Concentrate the whole system's contact with hardware into a few primitives, then spend all your optimization there"
figure: ingalls
works: [design-principles-behind-smalltalk]
axes: [hardware-affinity, primitive-count, cognitive-load]
subdomains: [programming-environments-and-object-systems, operating-systems-and-systems-programming]
tags: [lesson]
---
# Concentrate the whole system's contact with hardware into a few primitives, then spend all your optimization there

**Lesson:** Decide deliberately, and early, how small a set of operations everything above them will be built from, and then route every path down to the machine through that set. The immediate payoff is that optimization stops being diffuse. When one operation underlies all of a system's graphics, its implementer has a single artifact worth studying instruction by instruction, and every fraction of a percent won there is multiplied by the whole system's use of it. The same effort scattered across dozens of near-duplicate routines would return a fraction as much and would have to be re-spent on each new platform. Concentration converts optimization from an endless chore into a bounded, high-leverage engineering task.

Naming that set is what a virtual machine specification is for, and its value is that it fixes the boundary between the parts of a system that express ideas and the parts that exploit whatever technology is currently available. Above the line, storage, computation, and display each have a single model that programs are written against. Below it, an implementation is free to be interpreted, compiled, microcoded, or cast into silicon, and each such move improves performance without asking the system above to give anything up. The choice that makes this work is where to draw the line — the set must be small enough that a determined implementer can carry all of it to new hardware, and complete enough that nothing above ever needs to reach past it.

The general principle is that the surface a system presents to its substrate should be narrow and stated, not wide and incidental. A wide surface makes performance work unbounded and portability a rewrite; a narrow one makes both finite. And because that surface is a specification rather than a piece of code, it can outlive every implementation of itself, which is what allows a design to keep benefiting from hardware progress it was not built for.

**Source:** [Design Principles Behind Smalltalk](../works/design-principles-behind-smalltalk.md) — the Leverage principle's implementer-side argument that fewer primitives let each receive careful attention amplified across the system, with all graphics performed by a single primitive operation, and the Virtual Machine principle establishing object, message and bitmap models as the framework within which microcode or hardware can raise performance without compromise elsewhere.
