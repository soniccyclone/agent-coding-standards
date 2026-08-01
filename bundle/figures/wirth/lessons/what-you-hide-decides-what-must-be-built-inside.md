---
type: lesson
title: "What you hide decides what must be built inside"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, expressiveness, primitive-count]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# What you hide decides what must be built inside

**Lesson:** Concealing the linking fields of a structure behind a module boundary is normally justified by the freedom it preserves: clients cannot depend on the arrangement, so the arrangement can be replaced later without touching them, and a first implementation may be the simplest one that works rather than the one you expect to need. That justification is sound and the cost that accompanies it is usually left unstated. Any future facility that needs to walk the structure cannot be written outside the boundary. It must be admitted inside — so the module accumulates features that have nothing to do with its subject, and grows for a reason no one recorded. Deciding what to hide is therefore also deciding what the enclosing module will eventually contain, which is a prediction about future facilities, not merely a statement about the present ones.

Once the cost is visible the remedy is obvious and is worth building in from the start: export a traversal, not the links. An operation that applies a caller-supplied procedure to each member lets outsiders express any per-member computation without learning anything about the arrangement, and it costs one procedure in the interface. With it, the set of facilities forced inside shrinks to those needing something the traversal cannot express — reordering, structural surgery, position-dependent access — which is a small and enumerable set, and one you can then argue about honestly. Without it, everything that iterates is forced inside, and the boundary that was supposed to protect a decision ends up dictating the shape of the whole subsystem.

The general habit is to price an encapsulation by what it forbids as well as by what it protects. A boundary is not free just because it hides an implementation; it converts a class of future work from external to internal, and the size of that class depends entirely on how expressive the operations you export across it are. When you find yourself adding to a core module something that is plainly not core, that is the signal: the boundary is correct and the interface across it is too narrow.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.8.3's statement that the structures used for graphics, macros and libraries remain hidden from clients, that none of the linkage fields (`first`, `next`, `sel`) are exported from the base module, that this retains the possibility of changing the structural design decisions without affecting client modules, and that it is partly also responsible for the necessity of including macros in the base module; together with section 13.3's `Enumerate` procedure, which applies a parametric handler to all objects of a graphic.
