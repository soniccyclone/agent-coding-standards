---
type: lesson
title: "Sameness and change are each defined in terms of the other, so neither can be settled by observation alone"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Sameness and change are each defined in terms of the other, so neither can be settled by observation alone

**Lesson:** Two procedures built by the same expression with the same argument, in a language without assignment, are the same in every sense that matters: either can replace the other anywhere. Add assignment and the identical construction produces two things that are not interchangeable at all, because acting on one is visible through it and not through the other. The authors then push on what "the same" could even mean and arrive at a genuine circle. The only way to establish that two apparently identical things are one thing is to modify one and see whether the other changed. But the only way to establish that something changed is to observe the same thing twice and compare. Neither notion can be reached without already having the other.

This is not a puzzle to be solved; it is a report on what mutable state costs, and the useful consequence is that identity must be *supplied* rather than discovered. No sequence of observations bottoms out in a fact about whether two references denote one object, so the answer has to come from somewhere outside the observations — a construction you can point at, an identifier you assigned, a rule of the system. That is why languages that have mutation also have a primitive identity predicate that cannot be defined in terms of the values, and why every scheme for deciding "same entity" over data that changes ends up leaning on keys, addresses, or provenance rather than on comparison.

The consequences are the ones that hurt in practice, and the example is deliberately small. Two people with a hundred dollars is a different system from two names for one account with a hundred dollars, the two are indistinguishable from the values involved, and the difference shows up only when somebody acts. Everywhere that pattern recurs — an aliased buffer, two service instances behind one cache, a record loaded twice into memory, a config object shared or copied — the bug is invisible in every static reading of the state and appears at the first mutation. Testing does not reliably catch it either, because the test also has to know which case it built.

The design instruction that falls out: any part of a system where sharing versus copying matters should say so explicitly, because nothing about the data will say it for you. Make the distinction a fact of the construction, visible at the point where the second reference comes into existence. And note the escape hatch the authors are aiming at, which is the entire reason chapters one and two avoided assignment: give up mutation and the question dissolves, since two things that can never be modified cannot be distinguished by modifying one. Identity is a problem you buy along with change.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 3 section 3.1.3's subsection on sameness and change, which contrasts two decrementers built by the same expression (interchangeable in any computation) with two simplified withdrawal procedures built the same way (not interchangeable, as shown by an interleaved sequence of calls), defines referential transparency as support for substituting equals for equals without changing a value and notes that set! violates it, argues that we cannot determine change without an a priori notion of sameness and cannot determine sameness without observing the effects of change, and works the Peter-and-Paul example of two separate accounts versus one account under two names.
