---
type: lesson
title: "Decline to model what your layer does not need to know"
figure: thompson
works: [the-unix-time-sharing-system]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Decline to model what your layer does not need to know

**Lesson:** The strongest decisions in a foundational layer are usually refusals. Refusing to give stored data any structure beyond an addressable run of bytes, refusing to distinguish sequential from random access, refusing to require that a size be declared in advance, refusing to keep any structured bookkeeping objects inside the caller's own memory that the layer then depends on — each of these is a thing the layer chose not to know. Interpretation is left entirely to whoever wrote the program that reads the bytes, and because the layer holds no opinion, it also cannot hold a wrong one.

The reason this is a thinking discipline rather than mere minimalism is that each refusal has to be argued on its own terms, and sometimes the argument is that the problem is real but the layer is the wrong place to solve it. The refusal to provide user-visible file locking is the sharp case: the reasoning offered is not that concurrent writers are harmless but that locks would be both unnecessary for the workload actually present and insufficient against the way editors really behave, since a tool that works on a private copy defeats any lock the layer could have offered. Internal invariants are still defended — the layer keeps its own structures consistent under concurrent use — but a mechanism that would look like a solution while failing at the level users actually collide is declined. That distinction, between protecting your own invariants and pretending to solve someone else's coordination problem, is the substance.

Notice what the refusals buy. Because a file has no imposed record structure, one set of read and write operations serves text, executables, directories, and devices alike. Because there is no elaborate access-method machinery to insulate callers, programs can talk to the layer directly instead of through a library that reimplements what the layer already does. Every concept the layer declines to define is a concept that never has to be learned, versioned, or worked around — and the count of concepts, not the count of lines, is what determines whether people can hold the system in their heads.

A programmer who has absorbed this asks, before adding a feature to a base layer, who is actually going to be hurt by its absence and whether that party is better positioned to solve the problem themselves. When the honest answer is that the layer's version would be approximate, they leave it out and say why, rather than shipping a facility whose real function is to look complete.

**Source:** [The UNIX Time-Sharing System](../works/the-unix-time-sharing-system.md) — the treatment of ordinary files as unstructured byte sequences, the I/O call section's explanation of why user-visible locks were rejected while internal interlocks were kept, and the retrospective remarks on avoiding access-method layers and caller-held control blocks.
