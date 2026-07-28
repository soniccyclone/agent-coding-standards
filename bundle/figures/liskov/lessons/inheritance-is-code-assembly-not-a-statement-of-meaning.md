---
type: lesson
title: "Inheritance is code assembly; it says nothing about what a type means"
figure: liskov
works: [data-abstraction-and-hierarchy]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Inheritance is code assembly; it says nothing about what a type means

**Lesson:** Declaring one implementation to be derived from another is, in the end, an instruction for splicing code together. Whatever the language's rules for combining and overriding, the result is equivalent to having written out a single module with the merged state and merged operations, and that merged thing is what you must reason about and what you must revisit when anything changes. Nothing in the act of splicing asserts that the derived thing behaves like the thing it was spliced from. The relation is about provenance of code, and provenance of code is not a semantic claim.

Two genuinely different intentions get expressed through this one mechanism. Sometimes the intent is to reuse existing machinery because it happens to be convenient — the new abstraction is not a kind of the old one at all, merely built out of it. Sometimes the intent is the semantic claim: this really is usable wherever the other was. The first intent is achievable without the mechanism at all, by simply building the new abstraction on top of the old through its published operations, which costs a few forwarding definitions and buys back the ability to withhold operations that make no sense. The second intent is what actually adds something no other technique provides. Because both travel through the same syntax, a reader cannot tell which was meant, and neither can the language.

The overloading is not just confusing, it is functionally destructive: the two intentions want to be exercised along independent dimensions and one mechanism cannot serve both. If derivation is how you get several implementations of one abstraction, then a genuine specialization of that abstraction has to name a specific implementation as its parent — and thereby loses the freedom to pair with any of them. What you wanted was a specialization related to the abstraction, free to combine with whichever implementation suits. One mechanism carrying two meanings makes that inexpressible.

A programmer who believes this stops reading a derivation declaration as an assertion about behavior and demands the assertion be made separately, in whatever form the project can actually check. When reaching for derivation purely to reuse code, they ask whether composition through the published interface would do — it usually does, and it keeps the two ideas from collapsing into each other.

**Source:** [Data Abstraction and Hierarchy](../works/data-abstraction-and-hierarchy.md) — the sections separating implementation hierarchy from type hierarchy, and the closing discussion of multiple implementations where a specialization is forced to name one particular implementation as its parent.
