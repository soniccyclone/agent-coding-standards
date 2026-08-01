---
type: lesson
title: "Pass the transition when it is cheaper to realize than the state"
figure: wirth
works: [project-oberon]
axes: [hardware-affinity, expressiveness, verifiability]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Pass the transition when it is cheaper to realize than the state

**Lesson:** An operation that brings some external representation into agreement with an internal one can be told either what the new state is or what changed. Telling it the state is the safer interface and the usual default, and it is the wrong default whenever a transition has a realization far cheaper than reconstructing the target from nothing. Flipping a region between two appearances can often be done by a single bulk operation over the region, where producing that appearance from scratch means regenerating all its content; the executor can only use that shortcut if the request distinguishes "it is now selected" from "it has just become selected". So widen the request to name the transition — became-this, stopped-being-that, went-away — and the cheap realization becomes available without any caller knowing why it is cheap.

The cost of a delta interface is that it presumes agreement about the prior state, and that presumption is not always true: the representation may have been reconstructed for unrelated reasons, or a request may have been missed. The countermeasure is to keep one absolute request in the same vocabulary — render according to current state, whatever it is — and treat it as the resynchronization path. That single addition converts a fragile scheme into a robust one, because any disagreement is repairable by one absolute request rather than by unwinding history, and it costs one more value in an enumeration you were already writing.

A delta interface also imposes an ordering obligation that an absolute one does not, and it is the sort of thing that gets discovered late. A transition request has to be issued while both of its endpoints still exist: something that is about to be removed must be told to disappear *before* it is unlinked, because the executor needs the departing object in order to know what to undo. With an absolute interface the order does not matter — you mutate, then ask for a redraw. With a delta interface the mutation and the notification are ordered with respect to each other, and that ordering belongs in the contract, stated, rather than discovered as an intermittent visual artifact.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.4's `DrawMsg` mode parameter with its four values: draw according to the object's state, draw reflecting the transition from normal to selected, draw reflecting the reverse transition, and erase; the note that for captions the transitions are realized by simply inverting the rectangular area, with no rewriting of character patterns; and the observation that deleting objects requires drawing them in erase mode first and removing them from the graphic's linked list only afterwards.
