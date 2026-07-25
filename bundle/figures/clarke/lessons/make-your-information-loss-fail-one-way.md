---
type: lesson
title: "Engineer your information loss so the errors all point one way"
figure: clarke
works: [counterexample-guided-abstraction-refinement, model-checking-survey-clarke-grumberg-long]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification]
tags: [lesson]
---
# Engineer your information loss so the errors all point one way

**Lesson:** Any simplification of a system for the sake of tractability throws information away, and a naive simplification can therefore produce wrong answers in either direction: claims that hold of the simplification but not the system, and claims that fail on the simplification but hold on the system. Two-sided error is nearly worthless, because no answer can be trusted without redoing the work. The discipline that rescues abstraction is to control the *direction* of the error. Collapse concrete states into clusters and keep every transition that any member had, and the result has all the behaviours of the original plus possibly more. Nothing was removed, so nothing that must hold along all behaviours can have been created. A universal property established on the coarse model is therefore established on the real one, full stop, and the only remaining error mode is a false alarm.

That single-sidedness is what makes the coarse model usable, and it is bought by an explicit condition: the abstraction must not merge states that the specification's own atomic assertions distinguish, and the property must be restricted to the fragment with no existential path quantifiers. Both restrictions are visible, checkable, and stated as theorems rather than assumed. This is the general shape worth copying: an approximation is trustworthy exactly to the extent that you can name the class of questions it preserves and the condition under which it preserves them. Approximations whose error direction is unknown are not approximations, they are guesses.

The dual arrangement is equally legitimate and worth knowing: remove behaviours instead of adding them, and violations found on the reduced model are genuine while successes prove nothing. Choosing between over- and under-approximation is choosing which of "yes" and "no" you want to be able to believe, which in turn depends on whether you are hunting for bugs or certifying absence of them.

A programmer who works this way stops treating "close enough" as a single undifferentiated idea. Sampling, caching, static analysis, simplified test doubles, and back-of-envelope capacity models are all abstractions, and for each one the useful question is not how accurate it is but which way it lies when it lies, and what class of conclusions survives that bias. An analysis that only over-reports problems can be run automatically and triaged; one that can silently under-report cannot be trusted at all.

**Source:** [Counterexample-Guided Abstraction Refinement](../works/counterexample-guided-abstraction-refinement.md) — the abstraction section, which defines existential abstraction as clustering with transitions inherited existentially, states the appropriateness condition on the abstraction function, proves the simulation and property-preservation results for the universal fragment, and classifies related work by which side its error falls on. The 1996 survey derives the same guarantee from the simulation preorder when collapsing states by their abstract labels.
