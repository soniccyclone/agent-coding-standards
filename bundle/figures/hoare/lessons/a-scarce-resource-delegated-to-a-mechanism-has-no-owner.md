---
type: lesson
title: "A scarce resource delegated to an automatic mechanism has no owner, and nobody will count it"
figure: hoare
works: [the-emperors-old-clothes]
axes: [hardware-affinity, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# A scarce resource delegated to an automatic mechanism has no owner, and nobody will count it

**Lesson:** Introduce a mechanism that manages a scarce global resource — an allocator, an overlay or paging scheme, a caching layer, an autoscaler — and something quietly changes in how the people building on top of it behave. Each of them stops holding a figure for how much of the resource their part consumes, because that is now the mechanism's job. The mechanism, however, was only ever charged with *placing* consumption, not with *bounding* it, so the total is nobody's number. The characteristic failure is not that some component was extravagant; it is that the sum was never computed by anyone at all, and the project discovers only at integration that the shared budget was exhausted, with the further insult that the software's own footprint left nothing for the work the system exists to do.

The lesson is that automation of a resource does not eliminate the need for a plan for that resource; it eliminates the natural pressure that would have produced one. So a global budget has to be created deliberately and owned by a person: a stated total, an allocation per component, a running measured figure per component, and an integration check against the sum long before delivery. Note how cheap the missing step was in the failure case — nobody had added up the space their own software occupied. The most valuable measurement is usually the crude one taken early, and its absence is rarely a technical difficulty; it is a consequence of everyone reasonably assuming the responsibility lay elsewhere.

There is a corollary about the resources the mechanism cannot expand. When the easy escape exists — buy more memory, add nodes, raise the limit — a design that overruns its budget gets rescued by spending, and the underlying error is preserved rather than corrected. When a hard ceiling forbids the escape, the overrun forces a verdict on the design. The uncomfortable conclusion is that the hard ceiling is doing you a favor: it converts a slow financial leak into an early, unambiguous signal, and the users of a constrained system are protected from ambitions their supplier could not actually support. Treat the removal of a limit with suspicion, because it removes the mechanism that was catching your mistakes.

**Source:** [The Emperor's Old Clothes](../works/the-emperors-old-clothes.md) — the post-mortem of the Elliott 503 Mark II project, where no overall plan existed for allocating main storage because every programmer assumed the symbolic assembler or the automatic overlay scheme would handle it, nobody had counted the space the software itself occupied, and hardware address-length limits forbade the usual remedy of adding store; also the later observation that customers were fortunate that hardware limitations had protected them from the excesses of the software design.
