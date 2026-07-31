---
type: lesson
title: "Claim only the structure your problem actually has: unasserted properties are freedom the implementer gets to spend"
figure: hoare
works: [notes-on-data-structuring]
axes: [expressiveness, hardware-affinity, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Claim only the structure your problem actually has: unasserted properties are freedom the implementer gets to spend

**Lesson:** Most representations carry properties the problem never asked for. Anything you write down in a list is ordered whether or not order means anything; anything encoded as a number is comparable whether or not comparison means anything. The temptation is to shrug and let the incidental properties ride, since they cost nothing to have. They cost plenty. Every property a client can observe is a property some client will come to depend on, and once depended on it constrains every future representation and every future scheduling decision. Freedom, in a design, is exactly the set of properties you declined to promise; it is spent silently the moment it becomes observable.

So make the optional properties opt-in, and make claiming one an explicit act in the text rather than a side effect of how the thing happens to be built. Then a design that leaves ordering unasserted has recorded a decision, not an omission, and the implementer downstream is licensed to choose whatever layout, traversal order, or evaluation strategy suits the machine — none of which is available to him once callers can see an order and start assuming it. This is why the same discipline shows up as both a modelling rule and a notational one: the notation has to have a way of saying "unordered" that is shorter and more natural than saying "ordered," or the default drifts back toward over-promising.

The reciprocal obligation is that when you do assert a property, you must give programs a way to use it that does not smuggle in more. If a type is ordered, callers need to name its extremes and step between its values through the ordering itself, rather than by mentioning the particular constants that happen to sit at the ends today — otherwise every program that uses the ordering is also silently bound to the enumeration's current membership, and the property you meant to grant has dragged a second, unintended one along behind it. Grant the property; supply the vocabulary for consuming it abstractly; and refuse everything you were not asked for.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the representations and data-manipulation discussion in the chapter on the concept of type, which notes that types with no meaningful ordering are better treated as unordered because this leaves greater freedom in later choice of representation and sequencing strategy; and the treatment of enumerated types, where ordering is a separate opt-in qualifier on the declaration and the extremes and successor/predecessor functions exist so programs and proofs can be stated independently of the constants' actual names.
