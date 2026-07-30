---
type: lesson
title: "What you are actually building is a theory of the world; the program text is a by-product"
figure: naur
works: [programming-as-theory-building]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# What you are actually building is a theory of the world; the program text is a by-product

**Lesson:** Treat the output of programming as an understanding rather than an artifact. The understanding in question is a working grasp of how some slice of real-world activity corresponds to symbol manipulation a machine can perform — which parts of the world got mapped in, which got left out, and why the correspondence holds. Someone who has this grasp can do three things nobody without it can: point at any piece of the program and name the aspect of the world it answers to, go the other direction and say how a given real-world concern is represented (or deliberately isn't), and justify why each part is the way it is rather than one of the other shapes it could have taken. The program text supports none of these on its own. It records the result of the mapping without recording the mapping.

The scoping consequence is the sharp one. Deciding that some part of the world is irrelevant to the program requires understanding the part you excluded, so the boundary of the system is drawn from knowledge that by construction lives outside the system. No artifact produced inside the boundary can contain the reasoning that placed it. This is why a specification, however complete, is a record of decisions rather than the capacity to make more of them, and why a team handed a full document set can still propose changes that a team holding the grasp recognizes instantly as wrong.

Justification bottoms out in judgment, not in derivation. Design rules, quantitative comparisons, and appeals to precedent can appear in an explanation, but choosing which rule applies here is itself an act of direct assessment that no further rule licenses. Accepting this changes what you demand of a design discussion: not a chain of derivations from stated principles, but evidence that the person can situate the program in the world it serves and answer unexpected questions about the fit. If they can only recite the artifact back to you, they hold the artifact and not the theory.

**Source:** [Programming as Theory Building](../works/programming-as-theory-building.md) — the section on what the programmer's theory contains, specifically the three ways the programmer's knowledge exceeds the documented products, the argument that relevance judgments require understanding what lies outside the program, and the claim that justification finally rests on the programmer's direct estimate.
