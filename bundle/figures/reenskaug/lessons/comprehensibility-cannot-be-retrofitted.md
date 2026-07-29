---
type: lesson
title: "Comprehensibility cannot be bolted on after the fact"
figure: reenskaug
works: [mvc-its-past-and-present]
axes: [cognitive-load, expressiveness]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Comprehensibility cannot be bolted on after the fact

The usual response to a system people cannot understand is to add explanatory apparatus: step-by-step guidance for the anticipated tasks, and reference material for everything else. Reenskaug rejects both on structural grounds rather than quality grounds. Guided flows only cover the paths the designers imagined, and the words they use to guide you are the system's own invented vocabulary, so a newcomer who does not know the words cannot follow the guidance and an expert who knows them finds the guidance in the way. Reference material inherits the same vocabulary problem and additionally cannot be complete. Neither mechanism creates understanding; both presuppose it.

What actually makes a system graspable is that it has a conceptual structure a person can hold, and that structure is either in the artifact from the beginning or it is not there at all. Attempting to introduce it late fails because there is nothing to introduce — you can only describe the structure the system has, and if that structure was accreted by successive feature additions then describing it faithfully produces the incoherence rather than curing it. Two further constraints follow. The conceptual vocabulary has to be assembled out of notions the person already carries, because a model cannot be built from unfamiliar parts. And since nobody's understanding of the problem is complete at the start, the model has to be a thing that can evolve across releases in step with that understanding.

That last constraint pushes toward an unusual conclusion: the model people reason with and the program that runs should be the same artifact rather than two artifacts kept in agreement. Anything maintained in parallel drifts, and when it drifts the version that stops being true is always the one that does not execute. If the conceptual description is executable, drift is impossible by construction, and the door opens to the people who own the problem reading and eventually editing the topmost layer of their own system.

A programmer who believes this treats "we will document it" as an admission of a design failure rather than a mitigation, and treats an incomprehensible system as needing its concepts reworked rather than its help text expanded. It also changes what counts as early-stage work: settling the handful of notions the system will be about, in words already meaningful to whoever owns the problem, is architecture, not preamble.

**Source:** [The Model-View-Controller (MVC): Its Past and Present](../works/mvc-its-past-and-present.md) — the mental-object-models pattern, which dismisses task wizards and help systems, argues a conceptual model must be designed in from the start and built from the user's existing vocabulary, and proposes collapsing the modeling and programming languages so the model and the program evolve as one.
