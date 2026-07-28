---
type: lesson
title: "Define a data shape by the questions it can answer, not by how it is written or stored"
figure: landin
works: [mechanical-evaluation-of-expressions]
axes: [cognitive-load, expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Define a data shape by the questions it can answer, not by how it is written or stored

**Lesson:** Most confusion about a composite thing comes from confusing the thing with one of its inscriptions. Landin's discipline is to pin down a class of composite objects by three things only: a way to ask which of its alternative shapes an instance has, a way to get at each of its parts once the shape is known, and a way to build an instance from parts. Everything else — bracket styles, indentation, whether operators sit in front of their arguments or between them, whether the parts are contiguous words in store or scattered cells reached by addresses — is representation, and by construction none of it can affect meaning. Two texts that answer the same questions the same way are the same object; the difference between them carries no information.

This holds because the questions are exactly what any consumer of the structure can act on. If a rule for computing with the structure only ever branches on a shape test and reaches parts through selectors, then that rule is automatically insensitive to layout, and you have proved the insensitivity by construction rather than by auditing each use site. The payoff shows up twice in the same paper: he separates a program text from the tree it denotes, and then separately separates the record kept during evaluation from the linked cells that hold it in a real machine. Same move, different levels — and because it is the same move, the freedom it buys is the same. Representations can be chosen for cost (sharing, reuse of dead cells, consecutive addressing) with no argument about semantics, because there is nothing semantic left in the choice.

A programmer who takes this to heart stops arguing about surface form as though it were substance, and stops leaking form into logic. Concretely: name the interrogations your data supports and write every algorithm against those, so that changing the encoding is a local, provably meaning-free edit. It also inverts a common instinct about accessor chains — nested part-getting spelled out as one opaque compound name is worse than composing named selectors, not because it is uglier but because the compound name has smuggled a fixed internal ordering into the vocabulary. The reason to keep the interrogation layer thin is that every question you add is a commitment the representation must honor forever.

**Source:** [The Mechanical Evaluation of Expressions](../works/mechanical-evaluation-of-expressions.md) — the section introducing structure definitions in terms of predicates, selectors and constructors, and the later sections on holding a machine state as addressed cells, which apply the same separation to the implementation side.
