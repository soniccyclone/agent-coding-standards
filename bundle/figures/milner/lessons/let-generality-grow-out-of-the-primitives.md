---
type: lesson
title: "Let generality grow out of the primitives instead of adding a feature for it"
figure: milner
works: [a-theory-of-type-polymorphism-in-programming]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics]
tags: [lesson]
---
# Let generality grow out of the primitives instead of adding a feature for it

**Lesson:** When a language needs to express "works for many kinds of thing," the obvious design is to add machinery for it — a syntax for type parameters, a declaration form for generic procedures, a place for the programmer to write down the variability. The alternative pursued here is to notice that the variability is already present, unavoidably, in the operators every language ships: applying a function, forming a pair, taking the head of a list, assigning. Those operations are indifferent to the kinds of thing they move around. If you take that indifference seriously and record it once in the operators' own descriptions, the generality of user code follows from how it uses them. No new construct is introduced, and the programmer writes nothing extra.

This works because the constraints that determine a program's generality are exactly the constraints those primitives impose, plus the requirement that repeated uses of the same bound name agree. Collect those constraints across a program fragment and solve them, and you get the most permissive description consistent with what the code actually does. The programmer's own annotations, in this framing, are not the source of generality but a redundant restatement of it — often less general than the truth, since people write the case they had in mind.

The deeper principle is about where variability should live. Contemporaries proposed making it explicit at the declaration site, which puts the burden on every author of a general routine and creates a second language of type parameters to design, teach, and get wrong. Pushing it down into a fixed handful of operators means the cost is paid once by the language implementer, the vocabulary the programmer must learn does not grow, and the generality obtained is the maximum available rather than whatever was anticipated. Fewer primitives that are honest about their own indifference beat more primitives that let you announce indifference.

A designer who thinks this way, faced with a demand for a new feature, first asks whether the capability is already latent in the existing operations and merely unrecorded. Frequently it is, and the correct change is to describe what you already have more precisely rather than to add.

**Source:** [A Theory of Type Polymorphism in Programming](../works/a-theory-of-type-polymorphism-in-programming.md) — the introduction's third characterizing feature, where the paper positions its approach against contemporaries who required explicit type variables, and the worked list-mapping example where the general description is solved for rather than declared.
