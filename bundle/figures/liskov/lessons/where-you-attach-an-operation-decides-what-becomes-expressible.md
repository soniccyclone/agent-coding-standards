---
type: lesson
title: "Where you attach an operation decides which programs become impossible"
figure: liskov
works: [the-power-of-abstraction]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Where you attach an operation decides which programs become impossible

**Lesson:** Two designs can agree completely on what an abstraction does and differ only in where its operations are said to live — attached to the kind of thing, or attached to each individual thing. That looks like a question of notation and is nothing of the sort. The attachment point determines what an operation can see, and what an operation can see determines whole categories of program that are natural, awkward, or unwritable.

Attach the operations to the kind, and an operation is privileged with respect to every value of that kind at once. Anything relating several values symmetrically — comparing them, combining them, merging them — falls out immediately, because the code has legitimate access to the innards of all its arguments. Attach the operations to the individual value instead, and each operation is privileged only with respect to the one value it belongs to; symmetric relations become a hunt for a way to see the other party's interior. In exchange, that arrangement makes two other things straightforward: arranging kinds into families where a more specific kind reuses a general one, and letting several different implementations of the same abstraction coexist and interoperate inside one program, since each value carries its own operations rather than deferring to a single set installed for the kind.

The lesson is not that one attachment is correct. It is that this choice is made once, usually early, usually on aesthetic grounds, and then silently prices some future programs at infinity. The strengths and the losses sit on opposite sides of a single decision, and the losses show up years later and far away, where nobody connects them back to the choice. So the decision deserves to be made with the consequences enumerated: which relations must be symmetric, whether families of related kinds are expected, whether multiple implementations of one abstraction must coexist.

A programmer who believes this stops treating the question of where behavior lives relative to data as a stylistic preference and starts asking what it makes visible to whom. When a design fights back — a comparison that cannot see both sides, an implementation that cannot be swapped in locally — they look upward at the attachment decision rather than inventing a workaround at the point of pain, because the workaround will be needed again in every similar case.

**Source:** [The Power of Abstraction](../works/the-power-of-abstraction.md) — the comparison of treating operations as belonging to the type against treating them as belonging to the object, and the tally of what each arrangement makes easy: binary operations on one side, hierarchy and multiple coexisting implementations on the other.
