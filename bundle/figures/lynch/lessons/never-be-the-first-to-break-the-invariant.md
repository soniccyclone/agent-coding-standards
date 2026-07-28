---
type: lesson
title: "The right obligation on an open component is never to be the first to break the invariant"
figure: lynch
works: [an-introduction-to-input-output-automata]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# The right obligation on an open component is never to be the first to break the invariant

**Lesson:** A component embedded in a larger system usually cannot guarantee a global property, because the property can be destroyed by activity it does not control. Demanding the guarantee anyway produces specifications no component can meet; dropping the demand produces specifications that guarantee nothing. The model's way out is a third obligation that sits exactly between them: a component must never be the one that first makes the property false. As long as everything it has observed so far is consistent with the property, none of its own outputs may break it. If the property is already broken when the component acts, it owes nothing.

This is a better shape for a local obligation than either alternative, for a structural reason. It is checkable entirely inside the component, against only what the component can see, with no reference to any other participant's state. And it composes: if every part of a system independently promises never to be the first violator, then in a system with no external inputs there is nobody left who could have gone first, so the property holds outright. A global guarantee has been assembled out of purely local promises, without anyone ever reasoning about the whole system's state space at once. That is the payoff — the reasoning cost stays proportional to the size of a component rather than to the size of the composition.

The same reasoning explains why the argument requires the system to be closed before it will yield the global conclusion. So long as inputs arrive from outside the scope of the analysis, the property can only be conditional, because the first violator might be out there. Drawing the boundary at which the system stops taking external input is therefore not a bookkeeping detail — it is the step that converts a stack of conditional promises into an unconditional one, and it is where you discover whether your trust assumptions actually terminate.

For a working programmer this reframes what a contract should say. The useful form is not "this module maintains ordering" but "this module never emits anything that breaks ordering, given that what it received was ordered." That version is testable locally, survives being dropped into new contexts, and makes the closure argument explicit rather than implied. It also gives a crisp read on incident analysis: the question is not which component observed the bad state, but which one was first to produce it.

**Source:** [An Introduction to Input/Output Automata](../works/an-introduction-to-input-output-automata.md) — the modular-decomposition subsection, which defines a module preserving a prefix-closed property and then shows the property holds outright for a composition with no input actions.
