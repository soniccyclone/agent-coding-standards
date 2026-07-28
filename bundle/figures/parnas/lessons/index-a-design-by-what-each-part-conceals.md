---
type: lesson
title: "Index a design by what each part conceals, because the other indexes read more naturally and destroy it"
figure: parnas
works: [the-modular-structure-of-complex-systems]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Index a design by what each part conceals, because the other indexes read more naturally and destroy it

**Lesson:** There are three plausible ways to explain a decomposition to someone:
by the part each component plays in the system's operation, by the services it
offers callers, or by the specific piece of knowledge it exists to keep to itself.
All three describe the same code, and only the third keeps the design honest. Roles
and services are descriptions of what a component does now; concealment is a
description of what it protects you from later. Choose either of the first two as
the organizing key and the document stops being able to answer the question it was
built for — which component must change when this fact about the world changes —
because a component's role tells you nothing about which facts it depends on.

The failure mode is not intellectual but gravitational. Describing what something
provides is easier and feels more informative, so under deadline pressure that is
what gets written, and the drift is invisible at the time. Parnas's team reports
exactly this: the passages where they slipped from stating secrets to stating
interfaces or roles are the passages that produced components with no crisp
responsibility, which later had to be redone. The word choice in the document was
not documentation of the design; it *was* the design, and letting it slide changed
what got built. This is why the discipline has to be enforced on the prose, not
just intended in the architecture.

A refinement worth carrying: not everything a component hides is the same kind of
thing. Some of what it conceals was handed to it — a fact about the world, the
hardware, or the required behaviour that somebody else decided and that it has been
assigned to absorb. The rest it generated itself while figuring out how to absorb
the first kind: representations, algorithms, policies. Separating the two tells you
who can force a change and who merely benefits from one, and it lets you see when a
component's own inventions have started leaking outward. A programmer who works this
way describes each part by writing down the change it is meant to absorb, and treats
any part they cannot describe that way as a part that has not been designed yet.

**Source:** [The Modular Structure of Complex Systems](../works/the-modular-structure-of-complex-systems.md)
— the module-description section contrasting the three possible bases for describing
a structure, the distinction drawn there between primary and secondary secrets, and
the conclusion's admission about what happened when deadline pressure pulled the
writing toward interfaces and roles.
