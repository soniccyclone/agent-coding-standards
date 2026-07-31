---
type: lesson
title: "An operation belongs in the primitive set exactly when its efficiency depends on the representation"
figure: hoare
works: [notes-on-data-structuring]
axes: [primitive-count, hardware-affinity, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# An operation belongs in the primitive set exactly when its efficiency depends on the representation

**Lesson:** Deciding which operations a new abstraction should offer usually degenerates into an argument about convenience, and convenience arguments have no stopping rule — every candidate is useful to someone, so the interface grows until nobody can hold it. There is a non-arbitrary criterion available, and it is about cost rather than taste: an operation belongs in the primitive set when the way you would implement it efficiently is bound up with the choice of internal representation, and belongs outside when it can be built from the primitives without losing efficiency in the assembly. Anything a caller can compose out of what you already offer, at no penalty, is a convenience the caller can write; anything that would be badly implemented from outside because the outside cannot see the layout is yours to provide, and if you omit it your abstraction is not merely inconvenient but unusable at scale.

Two things make this criterion work where "is it useful?" does not. It is decidable — you can actually reason about whether an efficient implementation needs the representation — and it survives the representation being changed, because it is defined relative to whatever representation you pick rather than to a fixed one. It also gives the completeness test a definite shape: the set is large enough when any further operation a user wants can be defined in terms of it *and be efficient that way*. The efficiency clause is the whole content of the test; drop it and you are back to Turing-completeness arguments, which justify any interface at all.

The criterion has a companion obligation. Some operations that must be offered are, on large values, ruinous — copying a whole structure, comparing two of them in full — and offering them is still right, because their meaning is uniform across every type and a designer who cannot say "these two values are equal" has lost more than the cost of saying it. Cost is handled by making the expensive case removable: a better representation can shrink it, and the passage from an abstract program to a concrete one can eliminate it. What you must not do is delete such operations from the model because a particular representation makes them slow. The model is where meaning lives, and the price is negotiated later, in the open.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the data-manipulation section of the chapter on the concept of type, which states the guiding principle for choosing basic operators (an operator is basic when its efficient implementation depends heavily on the chosen representation, and the set is chosen so any further operation is definable in terms of it and efficient that way), and the accompanying treatment of assignment and equality as whole-value operations kept in the model despite their cost on large structures.
