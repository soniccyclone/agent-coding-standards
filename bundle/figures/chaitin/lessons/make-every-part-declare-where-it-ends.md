---
type: lesson
title: "A part that declares its own extent can be composed; one that does not must be framed by its caller"
figure: chaitin
works: [a-theory-of-program-size-formally-identical-to-information-theory, algorithmic-information-theory, meta-math-the-quest-for-omega, an-invitation-to-algorithmic-information-theory]
axes: [expressiveness, primitive-count, parallelizability]
subdomains: [foundations-of-computation, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A part that declares its own extent can be composed; one that does not must be framed by its caller

**Lesson:** If a component's boundary is implicit in the component itself, several of them can be laid end to end and still be told apart. If the boundary has to be supplied from outside, then every act of composition costs extra information to say where the seams are, and that cost grows with the number of parts. This is a small-looking property with disproportionate consequences: it is what turns a size measure into an additive one, so that the cost of building a whole from parts is bounded by the sum of the parts plus a fixed overhead. Chaitin found that the cost of self-description was tiny, roughly what it takes to state the length in a self-describing way, and that paying it changes what can be built.

The deeper consequence is that self-delimitation is what makes a family of things summable at all. Only because programs carry their own extent does the total weight assigned to all of them stay bounded, which is exactly what lets a halting probability be a number instead of nonsense. Without it there is no way to compare programs of different sizes on one scale, and the whole edifice built on that number disappears. Composability and measurability turn out to be the same property viewed from two sides.

Chaitin is explicit that two independent properties do the work together. Syntactic self-delimitation, which in a parenthesised functional notation is free because the brackets must balance, lets expressions be concatenated. Absence of side effects lets the pieces be evaluated without regard to each other, which is why a whole list of independent computations costs a constant more than the individual costs, with the constant not growing as the list grows. Take either property away and combining n parts starts costing something that scales with n. A programmer who believes this reaches first for formats and interfaces whose fragments terminate themselves, and for components with no shared mutable state, not out of aesthetics but because those two choices are what keep the price of assembly flat.

**Source:** [A Theory of Program Size Formally Identical to Information Theory](../works/a-theory-of-program-size-formally-identical-to-information-theory.md) - the definition of the machine and the argument that prefix-freeness is equivalent to a reader that cannot overrun its input, together with the subadditivity result proved by concatenating a program for one object with a program for another. Elaborated for a general audience in [Meta Math! The Quest for Omega](../works/meta-math-the-quest-for-omega.md) (the section building headers on headers and noting the additivity that results), worked out concretely as a short glue expression in [An Invitation to Algorithmic Information Theory](../works/an-invitation-to-algorithmic-information-theory.md), and given its cleanest syntactic-plus-semantic statement in the conceptual chapter of [Algorithmic Information Theory](../works/algorithmic-information-theory.md).
