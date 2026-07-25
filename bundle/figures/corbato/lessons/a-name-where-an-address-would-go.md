---
type: lesson
title: "A Name Where an Address Would Go"
figure: corbato
works: [introduction-and-overview-of-the-multics-system, multics-the-first-seven-years]
axes: [expressiveness, cognitive-load, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, programming-languages-and-semantics, databases-and-data-management]
tags: [lesson]
---
# A Name Where an Address Would Go

**Lesson:** Multics replaces addresses with names at every level where it can afford to, and defers the binding of those names as long as possible. A program refers to another segment symbolically, and even to a location inside it symbolically; the connection is made during execution the first time it is needed, after which it runs at full speed. Stored information is reached by name rather than by device and position, so the arrangement of drums and disks underneath can be rearranged for capacity or reliability without any program knowing. A segment that is never referenced is never brought in at all, which turns an error-handling path into something that costs nothing until it fires.

The reason to accept this trade is that a name and an address are commitments to different things. An address commits you to a layout; a name commits you only to an identity, and identities change far more slowly than layouts do. So the same indirection pays out repeatedly in currencies that look unrelated: one copy of a shared pure procedure can serve many users, a segment can grow during execution without relocating anything that refers to it, a storage device can be replaced with a faster one, pages can migrate between device classes according to how recently they were touched. Each of those is a layout change that would have been a rewrite under direct addressing.

The cost discipline matters as much as the principle. Corbató is careful that the binding is paid once and then amortized to nothing, which is what makes it defensible in a system that is also trying to answer in under a second. A programmer who thinks this way puts identity in the interface and location in the implementation, and treats a one-time resolution cost as cheap rent for keeping placement decisions permanently open. The failure mode to watch for is the opposite habit: a caller that knows where something lives has silently taken a dependency on a decision you were hoping to revisit.

**Source:** [Introduction and Overview of the Multics System](../works/introduction-and-overview-of-the-multics-system.md) — the enumerated justifications for segments under hardware design features, the subroutine and linkage conventions under software features, and the file system section's argument for symbolic reference to stored information. The seven-years paper's account of the storage hierarchy mapped directly into address spaces is the implemented result.
