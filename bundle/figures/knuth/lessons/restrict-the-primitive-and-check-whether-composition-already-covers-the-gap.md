---
type: lesson
title: "Before generalizing a primitive, check whether composing the restricted one already covers every use you actually saw"
figure: knuth
works: [literate-programming]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Before generalizing a primitive, check whether composing the restricted one already covers every use you actually saw

The obvious way to decide how powerful a facility should be is to imagine the demands users might place on it and build for the most demanding case. This work argues the opposite discipline, and argues it from having lived on the receiving end: the designer keeps the facility deliberately crippled — substitution with a single parameter, no conditional expansion, no evaluation at expansion time — and then, each time a real program seems to need more, looks for a way to get the effect by composing the crippled form with itself. The finding is that the needs kept dissolving. A two-argument abstraction falls out of two one-argument ones chained so that the first yields something the second consumes. Optional code that would seem to require conditional expansion turns out to be reachable by making the surrounding delimiters themselves redefinable, so switching a mode redefines two names rather than adding a control construct to the expander.

The reason this works is not that the restricted primitive is secretly as powerful as the general one — sometimes it isn't. The reason is that the set of demands that arise in practice is much smaller and much more structured than the set imaginable in advance, and composition reaches most of it. Generality bought speculatively is paid for permanently: every subsequent reader of the system carries the full facility in their head, every implementation of the system must reproduce it, and every error message must explain it. Generality obtained by composition costs nothing until someone needs it, and the moment of need is also the moment you learn which generality was the right one.

A programmer who takes this seriously inverts the usual order of design questions. Rather than asking what the feature should be able to express, they ask what the smallest version is that they cannot immediately work around, ship that, and treat every subsequent workaround as data rather than as a defect report. The workarounds that stay ugly after several honest attempts are the real evidence for extension, and they arrive with a concrete shape attached instead of a hypothetical one. This also produces a specific kind of humility about your own cleverness: the composition tricks that recover the missing power are frequently more interesting than the feature would have been, because they expose that the primitive was carrying more structure than its author noticed.

**Source:** [Literate Programming](../works/literate-programming.md) — the section on what was intentionally left out of the system, where the single-parameter restriction and the absence of conditional expansion are each defended by exhibiting a composition that recovers the effect, alongside the concluding remarks on refusing to build a tool for everybody.
