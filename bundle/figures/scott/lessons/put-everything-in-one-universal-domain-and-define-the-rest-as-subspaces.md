---
type: lesson
title: "Put everything in one universal domain and recover the specific types as subspaces of it"
figure: scott
works: [data-types-as-lattices]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Put everything in one universal domain and recover the specific types as subspaces of it

**Lesson:** Faced with many kinds of object to model, the default is a stratified construction: build each kind separately, one construction per level, with maps relating the levels. The alternative is to pick a single domain big enough to hold everything and obtain every particular kind as a distinguished part of it. The move needs two independent justifications, and both are worth demanding before committing. The structural one is that nothing is lost: every reasonable space embeds in the universal one, and every function defined on a part extends to the whole, so restricting attention to its subspaces excludes nothing you wanted. The practical one is that the subspaces you actually need are easy to pick out — cheap to define, and definable in the same language you use for ordinary values.

The choice of domain then matters more than its size. Scott's is the collection of all sets of integers, and the payoffs are specific rather than generic. It is a lattice and a topological space by inspection, needing no advanced apparatus to get started, so the machinery can be introduced later as analysis of what was already done rather than as a prerequisite. Because the ground is the integers, the connection to the existing theory of computable functions is immediate instead of requiring a translation layer. And because it is one space rather than a hierarchy, questions that would otherwise force methodological commitments up front — which category to work in, which class of maps, whether to restrict to the computable — can be deferred: you work in the universal space and define each notion as it becomes necessary, proving theorems before settling axiomatic disputes.

The cost, which should be stated rather than hidden, is that a single domain makes every element available for many uses at once, so an element is an integer, a set, a relation, a function, or a functional depending only on how the surrounding expression treats it. This is the source of the approach's power — self-application stops being paradoxical because one object is simply being used in two ways — and also of its main hazard, since nothing prevents mixing interpretations in one formula. Scott's discipline is the right one: the language permits it, but if you do it you owe an account of why it was worth doing in that case. Meaning here comes from use, which means use has to be legible.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — the Introduction's statement that the main innovation is to model everything within one universal domain, with its enumeration of the advantages; the extension and embedding theorems at the end of Section 1 and the remark that together they justify confining attention to subspaces of that domain both structurally and practically; the Section 2 discussion of what elements mean, where meaning is sought solely in terms of use and one element serves as integer, multiple integer, relation, function and functional; and the end of Section 4, which credits working in the universal space with allowing all necessary definitions and theorems without first settling axiomatic questions.
