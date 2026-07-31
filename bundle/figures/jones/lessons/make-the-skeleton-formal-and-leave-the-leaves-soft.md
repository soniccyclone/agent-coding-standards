---
type: lesson
title: "Make the skeleton formal and leave the leaves soft, so precision can be bought one place at a time"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Make the skeleton formal and leave the leaves soft, so precision can be bought one place at a time

**Lesson:** The usual objection to precise description is that you cannot afford to be precise about everything, which is true and beside the point. A description has a shape and it has contents, and these can be held to different standards. Adopt the notation for the shape — what depends on what, which conditions attach to which unit, where each obligation lands — and let individual leaves stay as ordinary prose saying "the items are in the usual order" or "this is the customary rounding rule". What you get is not a half-formal document but a fully structured one whose contents are refinable, because replacing a prose leaf with a precise definition changes nothing above it. The skeleton is the load-bearing part and the skeleton is cheap; the expensive part is optional and purchasable per leaf.

The same shape works for correctness arguments, and there it pays a second time. An argument written as a rigid frame with informally discharged steps is not a weaker proof; it is a proof with known holes, and known holes are a resource. When a reviewer disbelieves one step, both parties can see exactly which step and exactly what would have to be produced to close it — so effort goes precisely where the doubt is instead of being spread uniformly over material nobody doubts. An argument with no frame cannot do this: its gaps are invisible, so disagreement about it degenerates into disagreement about everything.

Notice the inversion this performs on the usual advice. People are told to be rigorous, meaning to raise the average level of detail everywhere, which is unaffordable and therefore ignored. The productive instruction is the opposite: fix the structure absolutely, then let the level of detail vary as wildly as the material warrants. Rigour becomes a thing you spend locally, and the notation earns its keep the moment it is adopted rather than only when the description is finished — which matters, because most descriptions are never finished.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 2's argument that adopting a formal notation forces a structure onto a definition, that parts of the definition may at some level be given in natural language, that such informal parts can later be replaced by formal ones without disrupting the structure, and that this structure is the skeleton to be fleshed out where required; together with chapter 5's closing observations on the worked multiplication development, where the recorded arguments are described as no more than notes towards a proof yet adequate as a basis for constructing formal ones, so that if a step is called into doubt it is clear what must be done to complete it — explicitly likened there to a large specification being formal in structure and informal in detail.
