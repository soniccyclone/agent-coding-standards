---
type: lesson
title: "Specify by listing separate obligations, not by describing a mechanism"
figure: manna
works: [a-temporal-proof-methodology-for-reactive-systems]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Specify by listing separate obligations, not by describing a mechanism

**Lesson:** Manna and Pnueli open by defending a particular style of specification: state what a system must satisfy as a list of individually-stated requirements, and do not attempt to fuse them into a single coherent description. The first benefit they claim is the interesting one. Because the author of such a list is never asked to show how the entries fit together or how they interact, the author is never pushed into deciding a mechanism. A specification that must hang together as one artifact has to resolve the interactions between its own clauses, and resolving interactions means choosing an order of operations, a data layout, an algorithm. That choice leaks into the specification as implementation bias, and every implementer downstream inherits a constraint nobody intended to impose.

The second benefit is that independence buys editability and divisible verification at the same time. A requirement can be dropped, added, or reworded without touching the rest of the list, and an implementation can be checked against one requirement at a time, with each check standing on its own. Compare a specification written as a reference model: changing one aspect of intent means re-deriving the model, and checking conformance means relating two whole artifacts rather than discharging a set of separate claims. The list form has structure that matches how intent actually changes — in pieces.

The honest cost, which the same authors treat elsewhere as the motivating problem for their taxonomy of property kinds, is that a list has no closure condition. Nothing in the list tells you whether it says enough, and nothing forces you to notice that two entries pull against each other, because you were explicitly excused from thinking about interaction. Independence is what makes the style work and also what makes it silent about the two questions it cannot answer. The mitigation is external: keep an inventory of the kinds of obligation a component could have and walk it, treating a whole category with no entry as a finding.

A programmer holding this view writes component contracts as a set of separately-checkable claims — this never happens, this eventually happens, this happens before that — and resists the pull toward specifying by writing a simpler version of the implementation. They notice when a specification has started to describe how rather than what, and treat that as a bug in the specification rather than as helpful detail. And they accept the discipline the style demands in exchange: because no single artifact will tell them the specification is complete, they need a separate habit for asking what kinds of guarantee are missing.

**Source:** [A Temporal Proof Methodology for Reactive Systems](../works/a-temporal-proof-methodology-for-reactive-systems.md) — the introduction's case for property-list specification, where abstraction is argued for as freedom from implementation bias arising from the specifier never being required to integrate the listed requirements, and modularity is argued for both as ease of amendment and as per-property verification.
