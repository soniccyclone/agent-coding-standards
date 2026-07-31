---
type: lesson
title: "Existence without uniqueness is a construction, not the abstraction you wanted"
figure: scott
works: [data-types-as-lattices]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [foundations-of-computation, software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Existence without uniqueness is a construction, not the abstraction you wanted

**Lesson:** Scott builds two dual-looking operators for combining data types, one that pairs and one that offers a choice between alternatives, and they are presented in parallel throughout with matching theorems. Then the parallel breaks. For the pairing operator he can show that whenever two maps agree on a source, there is a map into the combination that reproduces both, and that this map is the *only* one — and he says plainly that it is the combined existence and uniqueness that identify his construct as the standard notion of product. For the alternatives operator he can show the same map exists, but not that it is unique, so he declines to call it the dual standard notion and records that he does not know a clean characterization of what he has. The whole lesson is in the refusal to round up.

Uniqueness is not a technicality appended to existence; it is where the usefulness lives. Existence tells you a thing with the right shape can be built. Uniqueness tells you that anything else with the right shape is that same thing, which is exactly what licenses the reasoning people actually want from an abstraction: recognizing a construct by its interface, substituting one implementation for another, concluding that two independently written pieces of code must agree because both satisfy the specification. Drop uniqueness and every one of those inferences silently becomes invalid while the surface description continues to look identical. So a construct that satisfies half of a universal characterization should not inherit the name of the whole, because the name is what other people will reason from.

The corresponding practice is to keep a construct honestly unnamed and explicitly flagged when it only half fits, instead of applying the familiar label with a caveat that will not survive being cited. An unnamed operator with a note saying what is known and what is not costs a reader one paragraph; a misapplied name costs them every conclusion they draw by analogy with the real thing. The same discipline applies whenever you reach for an established term — a pattern, a protocol name, an algebraic law — to describe something in your own system: find the clause of the definition you are least sure of, check that one first, and if it fails, give the thing its own name.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — Section 4's product theorem and the discussion following it, where Scott shows the mediating map into a product exists and is unique and states that this existence-and-uniqueness property is what identifies the construct as a product; contrasted with the sum theorem and its discussion, where the mediating map is shown to exist but not to be unique, leading him to conclude the operator is not the categorical coproduct and to note that he knows no neat categorical characterization of it.
