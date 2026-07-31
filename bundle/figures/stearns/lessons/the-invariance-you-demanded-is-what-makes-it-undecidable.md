---
type: lesson
title: "The invariance you demanded is what makes the question undecidable"
figure: stearns
works: [on-the-computational-complexity-of-algorithms]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# The invariance you demanded is what makes the question undecidable

**Lesson:** A classification of computations that ignores differences in finitely many places is exactly what you want: it measures the essential shape of a thing rather than its startup quirks, and it means a bounded amount of special-casing can never move an object between categories. That insensitivity is also, immediately and unavoidably, the reason no procedure can decide which category an object falls into. Given any process whose termination is in question, you can build an object whose classification depends on nothing but whether that process ever stops — because a process that stops after some number of steps differs from one that never stops in only finitely many places, and finite differences are precisely what the classification was built to disregard. Membership therefore decides termination, which nothing does.

The important part is that this is not a defect of one particular scheme, to be fixed by a cleverer one. Any nontrivial classification with the same insensitivity property inherits the same undecidability, whatever its internal machinery. The robustness and the undecidability are the same fact seen from two sides: a category boundary that a finite perturbation cannot cross is a category boundary that an unbounded search must be run to locate. There is no design that keeps the first property and escapes the second, so the effort to find one is wasted before it starts.

The habit this installs is to derive the limits of a scheme from the properties you asked it to have, rather than discovering them empirically after years of failed attempts. Whenever you specify that a predicate must be insensitive to some class of variation — that a health check must ignore transient states, that a lint rule must ignore incidental formatting, that a policy must ignore bounded misbehaviour — ask what unbounded question that insensitivity has just made equivalent to your predicate. If the answer is a search with no termination bound, you have not built a checker, you have built a classification, and the correct engineering response is to accept a conservative approximation with known one-sided error and stop looking for the exact one. Choosing which side to err on is a real decision; pretending the decision does not exist is not.

**Source:** [On the Computational Complexity of Algorithms](../works/on-the-computational-complexity-of-algorithms.md) — the pair of results in the time-limited-computations section showing first that sequences differing in finitely many places always share a class, then that membership in a class is undecidable by encoding the stopping problem into exactly that insensitivity, together with the closing remark that the unsolvability is not peculiar to this scheme but holds for any nontrivial classification with the same finite-difference property.
