---
type: lesson
title: "When a construction repeats at every level, make the pattern the artifact and let instantiation cover the infinite family"
figure: church
works: [a-formulation-of-the-simple-theory-of-types]
axes: [cognitive-load, primitive-count, expressiveness]
subdomains: [programming-languages-and-semantics, foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# When a construction repeats at every level, make the pattern the artifact and let instantiation cover the infinite family

Church's type hierarchy is infinite, so most of what he wants to say has infinitely many instances: the axioms, the rules, and the theorems about arithmetic all recur once per level, differing only in which type subscripts appear. He does not enumerate. He states each one as a single schema with the level left indeterminate, and observes that the same device condenses not just the infinite list of statements but the infinite list of proofs — one schematic derivation stands in for all of its instances. He is explicit that no stage of building the system ever arrives at which all instances have been proved, and equally explicit that this does not matter, because the schema is an argument that any instance you actually need is derivable.

The move is to treat the level as an argument rather than as a case. Once the pattern is the object of study, the size of the family it covers stops being a cost you pay per member. This is the same trade a generic function or a parametric proof makes, and Church's version is worth attention because he separates the two things people usually conflate: having a uniform notation for the family, and having warrant that every member behaves. The schema gives both, but the warrant is a metamathematical claim about the schema, made in the surrounding language, not a theorem inside the system. The parametric artifact and the argument that parameterization is sound live at different levels, and confusing them is how people convince themselves that a generic abstraction is correct because it typechecks.

Church is disciplined about where the uniformity breaks, which is what makes the schema trustworthy. Several of his numbered results are flatly not theorems at certain levels of the hierarchy — the ones built without individuals — and he says which and why rather than letting the schematic notation paper over the exception. The schema is a claim about a range, and stating the range precisely is part of stating the schema.

A programmer who works this way, on meeting the third near-copy of a construction, stops writing copies and asks what varies; then writes the varying thing as a parameter and the argument for correctness once, over the parameter. They also keep two facts distinct in their head: what the generic code says, and what they actually know about all its instantiations — and they document the levels where the generic claim stops holding instead of trusting that no one will instantiate it there.

**Source:** [A Formulation of the Simple Theory of Types](../works/a-formulation-of-the-simple-theory-of-types.md) — the footnote on typical ambiguity that defends schematic statements and schematic proofs over an infinite hierarchy, together with the sections on Peano's postulates where certain schemata are shown to fail at specific types.
