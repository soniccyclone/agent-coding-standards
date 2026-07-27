---
type: lesson
title: "Define a family's whole meaning against a handful of operations, then let specializations override only for speed — never for meaning"
figure: goldberg
works: [smalltalk-80-the-language-and-its-implementation]
axes: [primitive-count, cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Define a family's whole meaning against a handful of operations, then let specializations override only for speed — never for meaning

**Lesson:** The collection family in this book is built on a discipline worth stealing wholesale. At the top sits a general notion whose entire large repertoire — searching, counting, transforming, converting, combining — is written in terms of only three capabilities: put an element in, take an element out, and visit the elements one at a time. Everything else is derived. The consequence is that the *meaning* of every operation in the family is fixed in one place, and it is fixed once. Specializations further down do reimplement many of those operations, but the reimplementation is licensed for one reason only: the derived version does more work than a particular representation requires. The general version is the definition; the specialized version is an optimization that must agree with it. The book is willing to show what this costs at the top — the general way of answering "how many elements" walks them all, which is slow, correct, and expected to be replaced downstream.

That split does real work in two directions. Reading downward, it means a specialization can be understood as a claim about performance rather than a claim about behavior, so you never have to read a whole hierarchy to learn what an operation means. Reading upward, it means correctness has a single site: get the derived definitions right against the three operations and the family is right, then each optimization is checkable against a reference implementation that is still present in the system rather than lost to history. The alternative — where each specialization independently defines its own version of everything — has no reference, so "the same operation" gradually means slightly different things in different places, and nobody can tell which is authoritative.

The organizing decision that makes this possible is how the family is carved up in the first place. The taxonomy here is derived from the questions a user of a collection actually faces — whether the elements are ordered, whether they are reached by an external key, whether that key is a position or an arbitrary lookup value, whether ordering is imposed by the order of insertion or computed from the elements themselves — so the hierarchy reads as a decision procedure for choosing one. It is not organized by how the bits are laid out. Access semantics is what clients reason about; layout is what implementers reason about; putting the client's distinctions in the structure is what makes the structure navigable.

A programmer who adopts this writes the general, obviously-correct version first and keeps it, even when it is known to be too slow, precisely so the fast versions have something to be equivalent to. And when tempted to derive a class hierarchy from representation, the check is to ask which distinctions a caller has to make choices about — those are the ones the structure should expose.

**Source:** [Smalltalk-80: The Language and Its Implementation](../works/smalltalk-80-the-language-and-its-implementation.md) — the collection chapters, where the shared protocol is reduced to a minimal set of required operations with everything else defined in their terms and subclass reimplementation justified explicitly on efficiency grounds, together with the classification of the hierarchy by ordering and keying characteristics presented as a guide for choosing a collection.
