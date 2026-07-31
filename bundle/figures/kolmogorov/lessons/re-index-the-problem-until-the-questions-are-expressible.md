---
type: lesson
title: "When the framework cannot express the question, change how the problem is indexed"
figure: kolmogorov
works: [grundbegriffe-der-wahrscheinlichkeitsrechnung]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, foundations-of-computation]
tags: [lesson]
---
# When the framework cannot express the question, change how the problem is indexed

**Lesson:** Having built probability over spaces with arbitrarily many coordinates, Kolmogorov reports a limit of his own construction rather than hiding it. When the index set is uncountable, perfectly ordinary sets fall outside the reach of the machinery — the example he picks is the set of outcomes whose every coordinate stays below a fixed bound, which simply is not in the field and therefore has no probability. His response is not to strengthen the machinery. It is a piece of methodological advice: put each problem, whenever you can, into a form where an outcome has only countably many coordinates.

The general move is that a framework's reach is fixed by how the state space was indexed, so a question you care about landing outside that reach is information about the indexing rather than a demand to extend the theory. Extending is the expensive path and frequently has no good answer, while re-indexing is often nearly free and costs you nothing you cared about — the bounded-everywhere condition over an uncountable index and over a countable one are different sentences with the same practical content whenever the process is well-behaved between sample points. What this argues for is a design-time habit: before committing to a representation, check whether the properties you will eventually need to *state* are even in the language that representation supports. That question is cheap early and expensive after everything is built on top of the answer.

The recognizable instances are everywhere once you look for them. A quantity indexed by continuous time, with a requirement that it never exceeded a threshold: that is a claim about uncountably many instants which no log can ever settle, and the fix is to define the property over the sampled index rather than to invent a semantics for the unsampled one. A state space indexed by dynamically created identities, with an invariant that must hold of all of them at once. A configuration space where the predicate you want — no two rules conflict — ranges over pairs nothing enumerates. In each case the productive question is what re-indexing would move the predicate inside the checkable region, and what that costs. Usually far less than extending the framework, and unlike extending the framework, it terminates.

**Source:** [Grundbegriffe der Wahrscheinlichkeitsrechnung](../works/grundbegriffe-der-wahrscheinlichkeitsrechnung.md) — Chapter III, §4, which notes that for a non-denumerable index set many simple and interesting subsets remain outside the Borel extension, gives the set of elements whose every coordinate stays below a fixed constant as an example, and recommends putting each problem into a form where the space of elementary events has only a denumerable set of coordinates.
