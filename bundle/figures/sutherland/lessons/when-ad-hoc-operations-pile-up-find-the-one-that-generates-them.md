---
type: lesson
title: "When ad hoc operations pile up, find the one operation that generates them"
figure: sutherland
works: [sketchpad-a-man-machine-graphical-communication-system-afips-1963]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# When ad hoc operations pile up, find the one operation that generates them

**Lesson:** Sketchpad began the way every tool begins: one hand-written routine per command, each knowing exactly which pieces of structure to create and how to wire them together. Every new capability meant another routine and another button. The escape was not to write the routines faster or organize them better, but to notice what they all *were* — each one instantiated a fixed pattern of parts and relations, then tied that pattern into whatever the user was pointing at. Once that shape is named, a single operation that instantiates an arbitrary stored pattern and grafts it onto existing structure subsumes the whole accumulated pile, and the patterns themselves demote from code to content.

The demotion is the payoff, and it is larger than the deduplication. When an operation is code, extending the vocabulary requires someone who can build the system; when an operation is content, extending it requires only someone who can use it, and the new vocabulary items are inspectable, storable, and composable with each other in ways hand-written routines never are. Sketchpad's later capabilities — dimensioned lines, structural members carrying force values, composite relations like tangency or collinearity — arrived as saved patterns rather than as releases. That is what distinguishes a real generalization from a refactor: after a refactor the same people can do the same things with less code, whereas after a generalization a different population can do things nobody implemented.

The grafting half deserves separate attention, because it is what makes the general operation usable at all. A pattern instantiated in isolation is inert; it becomes an operation only when it can fuse with what is already there, and fusing must cascade — joining two composite parts has to force the joining of what they are each built from, or the relations carried by the pattern land on the wrong things. This is also how a system lets users name relations its representation cannot directly hold: a relation that must technically attach to lower-level parts can still be spoken about at the level the user thinks in, provided the fusion propagates downward on its own.

A programmer who believes this treats a growing switch of near-identical handlers as a diagnosis rather than a chore. The question is not how to share code between the cases but what single parameterized act all the cases are performing, and whether its parameter can be made into data the user supplies. Answering that usually shrinks the primitive count and raises the ceiling at the same time.

**Source:** [Sketchpad: A Man-Machine Graphical Communication System (AFIPS 1963)](../works/sketchpad-a-man-machine-graphical-communication-system-afips-1963.md) — the copy-function section, which narrates the shift from per-button hand-coded creation routines to one operation that instantiates any stored pattern, together with the recursive-merging discussion that supplies the cascading fusion it depends on.
