---
type: lesson
title: "Decide what your descriptions denote, and the relations between them stop being matters of taste"
figure: cardelli
works: [on-understanding-types-data-abstraction-and-polymorphism, a-semantics-of-multiple-inheritance, structural-subtyping-and-the-notion-of-power-type]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Decide what your descriptions denote, and the relations between them stop being matters of taste

**Lesson:** Arguments about whether one interface should be accepted where another was expected can run forever while the participants trade intuitions about vehicles and cars. They terminate the moment someone commits to what a description actually denotes. Take a type to name a set of values drawn from one universe, and the questions answer themselves by set reasoning: one type is usable in place of another exactly when its values are among the other's values, having several types at once is nothing more mysterious than belonging to overlapping sets, and the hierarchy is a partial order that was already there rather than a declaration hierarchy someone drew. The relation is no longer a rule you argue for, it is a fact you compute.

The best evidence that this is more than bookkeeping is the case where the derived answer contradicts intuition and turns out to be right anyway. Ask when one function is usable where another is expected, and naive symmetry suggests both ends should move the same way. Held to the denotation, the two ends move oppositely: a replacement may accept more inputs and must promise a narrower range of results. Nobody would reliably guess that from examples, and languages that guessed have shipped unsound rules. The same discipline exposes where a proposed relation is unusable rather than merely surprising: describing a subset by an arbitrary predicate is legitimate mathematics and useless as a compatibility rule, since deciding membership becomes theorem proving, which is why the workable relations are the ones readable off the shape of a value.

The transferable habit is to stop treating a type, schema, interface, or contract as a piece of syntax that a tool happens to check, and to insist on knowing what set of things it picks out. Once that is fixed, substitutability, ambiguity, redundancy, and the question of whether two descriptions are the same become derivable rather than debatable, and any rule someone proposes can be checked against the meaning instead of against a majority intuition. Where no denotation is available, that absence is itself the important finding: it tells you the design is still being decided by folklore.

**Source:** [On Understanding Types, Data Abstraction, and Polymorphism](../works/on-understanding-types-data-abstraction-and-polymorphism.md) — the section treating types as sets of values within a single universe, and the subsequent derivation of inclusion rules for ranges, records, variants, and function spaces from that reading. Also [A Semantics of Multiple Inheritance](../works/a-semantics-of-multiple-inheritance.md) — the denotational treatment where inheritance is set inclusion, from which the reversal on function arguments is obtained rather than postulated. Also [Structural Subtyping and the Notion of Power Type](../works/structural-subtyping-and-the-notion-of-power-type.md) — the opening argument that expressive power alone would license arbitrary subsets, and that checkability is what narrows the candidates.
