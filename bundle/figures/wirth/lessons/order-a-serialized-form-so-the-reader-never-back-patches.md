---
type: lesson
title: "Order a serialized form so the reader never has to back-patch"
figure: wirth
works: [project-oberon]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Order a serialized form so the reader never has to back-patch

**Lesson:** Turning a linked structure into a flat sequence requires replacing every internal pointer with something position-independent — a number that stands for a node. The interesting decision is not the numbering scheme but the emission order, and it should be settled by asking which side of the exchange happens more often. A form written once and read many times should be arranged for the reader, and the arrangement that helps a reader most is the one where every reference is backward: each node's definition appears before anything that mentions it. Then a reader can consume the sequence in a single forward sweep, resolving each reference the moment it appears against a table of what it has already built, holding nothing pending and needing no second pass.

The cost lands on the writer, and it is a real cost, not a bookkeeping detail. Emitting in this order means the writer cannot simply walk its structure in whatever order is natural; before emitting anything that mentions a node, it must check whether that node has been emitted and, if not, emit it first. That check needs a per-node marker recording "already written," which is state the writer would not otherwise carry. Paying it once at write time in exchange for removing pending-reference machinery from every read is straightforwardly the right trade when reads outnumber writes, and stating the asymmetry explicitly is what makes the decision reviewable rather than accidental.

Genuine cycles cannot be ordered away, and the honest response is not to abandon the discipline but to confine the exception. Emit an explicit repair instruction for exactly the references that could not be made backward — a small, separately tagged element saying which reference to complete once both ends exist. The reader then keeps its single forward sweep for the overwhelming majority of the structure and handles a short, enumerable list of repairs. What makes this better than general back-patching is that the exceptions are visible in the form itself: you can count them, and a growth in their number is a signal that something about the structure has changed, rather than a cost silently absorbed by a mechanism that was always running.

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.6's account of symbol-file generation, which states that the problem is representing pointers in a form free of absolute addresses, that the solution assigns a unique reference number to each occurring type, that because the efficiency of importing has priority over that of exporting these reference numbers should never constitute forward references so a definition must precede its occurrence, that a type's reference field starts at zero to signal not-yet-exported so the export of a type precedes the export of any identifier of that type, and that the Fixup specifier mirrors a forward reference in a pointer type declaration and triggers repair of the base type when the file is read.
