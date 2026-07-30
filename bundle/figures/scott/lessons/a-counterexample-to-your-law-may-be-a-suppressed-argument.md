---
type: lesson
title: "A counterexample to your law is often a function with an argument you forgot to declare"
figure: scott
works: [outline-of-a-mathematical-theory-of-computation]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# A counterexample to your law is often a function with an argument you forgot to declare

**Lesson:** You propose a law that every component in your system is supposed to obey, and a practitioner produces a working counterexample: here is a real, useful procedure that plainly violates it. There are three responses, and only one of them is any good. Abandoning the law concedes the field on the strength of one case. Adding an exemption keeps the law nominally but destroys its use as a filter, since anything can now be excused. The third response is to ask whether the counterexample is actually a function of the arguments you think it is. Very often it is not — some quantity it depends on has been left out of the description because it was regarded as a setting rather than an input, and once that quantity is admitted as an argument in its own right, the object satisfies the law in the variables where the law was supposed to apply.

The concrete instance is instructive because it is genuinely tempting. Monotonicity in information — better input yields no worse output — looks refuted by numerical procedures that produce a better answer from a cruder request. But such a procedure takes two things: the data, and a control parameter saying how much of an expansion to use. Adding terms can ruin an approximation while the data and the term count are both perfectly known, so nothing about *partial information* is at stake; the apparent violation was an artifact of writing one input and hiding the other. Separating them restores the law and, more usefully, makes visible that two different notions of accuracy had been conflated — the quality of a result and the completeness of what is known about an input are not the same axis at all.

The general discipline is to treat a proposed invariant as a diagnostic instrument before treating it as a rule. When something violates it, the first question is not whether the rule survives but what the violation reveals about the description: which dependency is undeclared, which two concepts are sharing a word, which state is being read rather than received. A law that keeps being violated by unremarkable cases is usually being applied to a poor model of those cases, and repairing the model is worth more than either weakening the law or arguing about it. There is a corresponding warning for the other direction: a law you can save by declaring a new argument every time it fails has stopped filtering anything, so the repair only counts when the newly declared argument is one the system genuinely supplies and could have named all along.

**Source:** [Outline of a Mathematical Theory of Computation](../works/outline-of-a-mathematical-theory-of-computation.md) — the discussion following the monotonicity axiom, where the objection from asymptotic numerical algorithms that give better answers from cruder accuracy is answered by recasting them as functions of two variables, the data and a term count, and by separating the information ordering from the numerical notion of accuracy.
