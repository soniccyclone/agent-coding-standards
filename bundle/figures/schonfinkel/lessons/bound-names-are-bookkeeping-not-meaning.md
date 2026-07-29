---
type: lesson
title: "Bound names are bookkeeping, not meaning"
figure: schonfinkel
works: [bausteine-der-mathematischen-logik]
axes: [cognitive-load, primitive-count, expressiveness]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Bound names are bookkeeping, not meaning

The decisive judgment in this paper is not technical, it is about what a variable actually is. Schönfinkel looks at a quantified statement and observes that the letter standing at an argument place carries no content of its own. Its entire job is to record which slots belong with which operator — a pointer scribbled in the margin so the reader can match things up. He calls it an auxiliary device, out of keeping with the fixed, unchanging thing a logical assertion is supposed to be. Once you accept that description, the conclusion is forced: something whose only role is to record a correspondence can be replaced by whatever makes the correspondence directly.

This is a general move for separating substance from notation. Ask of any construct in a formalism: does it denote something, or does it merely coordinate other parts of the text? Constructs of the second kind are candidates for elimination, because their information content is a wiring diagram, and wiring can be expressed by the connectors themselves instead of by labels on the endpoints. The result here is a calculus with no bound names anywhere, in which the plumbing that names used to describe is carried out by a handful of operators that permute, share, discard, and nest arguments.

Believing this changes what you treat as essential in a program. Names for values that flow between operations are usually coordination, not content — which is why the same computation can be written with them or without, and why a pipeline of composed operations often reads as more honest than a sequence of assignments to intermediates each mentioned twice. It also explains why capture, shadowing, and alpha-renaming are perennial sources of bugs and of fiddly implementation work: they are the maintenance cost of the label scheme, not of the computation, and a formalism that never introduces labels never pays them.

The caution attached is equally real and Schönfinkel supplies it himself. Eliminating names does not make expressions shorter or easier to read; his own worked reductions grow into long strings of operators. The labels were doing something for human comprehension even while contributing nothing to meaning. Knowing which of the two you are optimizing — the semantics or the reader — keeps you from mistaking a point-free rewrite for an improvement when only the first was at stake.

**Source:** [Über die Bausteine der mathematischen Logik](../works/bausteine-der-mathematischen-logik.md) — the passage closing the first section, where the goal of removing proposition, propositional function, and variable as primitives is justified on the grounds that a variable is only a marker linking argument places to operators.
