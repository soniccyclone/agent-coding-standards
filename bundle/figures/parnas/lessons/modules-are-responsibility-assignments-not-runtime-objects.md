---
type: lesson
title: "A module is an assignment of responsibility, not a unit of the running program"
figure: parnas
works: [on-the-criteria-to-be-used-in-decomposing-systems-into-modules]
axes: [hardware-affinity, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# A module is an assignment of responsibility, not a unit of the running program

**Lesson:** The word "module" invites a category error: people hear it and picture a procedure, a compilation unit, a file, something that exists at run time and can be pointed at in a memory map. Under that reading, design boundaries and execution boundaries are the same thing, and the moment a boundary looks expensive to cross the design must give way. Break the identification and the tension dissolves. Two systems can compile to byte-identical machine code and still be different designs, because a design lives in the representations used for changing, explaining, and reviewing the system — not in the one used for running it. The runnable form is only one projection, and the interesting properties are not visible in it.

Once responsibility is the unit, the hard-won boundary survives contact with performance. If crossing a boundary is realized as a call with a full linkage sequence, a fine-grained decomposition will make the program slower than a coarse one; the honest response is not to coarsen the design but to stop assuming boundaries must be realized as calls. Let the text be written as if these were procedures and let the machinery choose the realization — inline expansion, specialized transfers, whatever fits. The consequence is that in the final code the separations may be undetectable, which is fine, because the separation was never for the machine's benefit. What this does demand is tooling: if the design representation and the running representation genuinely differ, something has to maintain both and map between them, and that mapping is part of the infrastructure a serious project needs rather than an optional nicety.

This is the argument that licenses the whole modern stack of zero-cost abstraction, but the direction of reasoning matters more than the conclusion. Parnas does not argue that good abstractions happen to be free; he argues that if your abstraction boundaries are being set by call overhead, you have let the implementation layer dictate the design layer, and the fix belongs in the implementation layer. A programmer who believes this treats "that would be too many small functions" as a claim about a compiler, not a claim about a design, and goes and checks which one is actually true before conceding anything.

**Source:** [On the Criteria To Be Used in Decomposing Systems into Modules](../works/on-the-criteria-to-be-used-in-decomposing-systems-into-modules.md) — the framing note that a module is a responsibility assignment rather than a subprogram, the observation that the two decompositions could assemble to the same object, and the efficiency-and-implementation section calling for the module-as-subroutine assumption to be abandoned.
