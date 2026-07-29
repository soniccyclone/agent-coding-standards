---
type: lesson
title: "The browser is part of the language"
figure: reenskaug
works: [the-common-sense-of-object-oriented-programming]
axes: [cognitive-load, expressiveness]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# The browser is part of the language

A program organized along several independent concerns is not a linear object, and Reenskaug says plainly what most language designers leave implicit: presented as a single sequence of text, his own examples are probably not readable, and they become readable when read through an environment that can show one concern at a time and switch between them instantly. The paradigm and the viewer are not separable achievements. A decomposition that no tool can display is, from the reader's position, indistinguishable from no decomposition at all — the fragments are all there, and the work of assembling them has simply been moved from the machine to every person who opens the code.

This puts an obligation on notation design that is usually skipped. If you introduce a second axis of structure, you have also introduced a presentation problem, because files and lines can only express one ordering. The response in this report is a set of viewers, one per concern, sharing a window so the reader flips between coherent pictures rather than scrolling through interleaved material. Part of the structure is even edited as a diagram, since the thing being expressed — which participants exist and who can speak to whom — is a graph and gains nothing from being flattened into prose.

There is a recursive argument underneath. The obligation the application programmer has toward the end user — offer a representation that matches how they already conceive of the thing, so they feel they are handling it directly — is exactly the obligation the toolmaker has toward the programmer, one level up. The programmer's own mental model of the program and the environment's representation of it must be the same model, or the environment is something to be worked around rather than thought in.

A programmer holding this stops treating tooling as downstream of design. When a structural idea depends on being seen a certain way, shipping the idea without the viewer ships something that will be experienced as mess and blamed on the idea. It also makes the honest test of any new structure whether someone can navigate it, not whether it is well-founded.

**Source:** [The Common Sense of Object Oriented Programming](../works/the-common-sense-of-object-oriented-programming.md) — the sections presenting the per-perspective browsers arranged as overlays and the graphical editor for the participant network, together with the repeated admission that the linear document form of the same code is far harder to read than the environment's form.
