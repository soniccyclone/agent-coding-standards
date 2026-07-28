---
type: lesson
title: "Let structure be discovered rather than committed up front"
figure: pike
works: [go-at-google]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Let structure be discovered rather than committed up front

**Lesson:** Organizing software as a classification of its types demands the most consequential decision at the moment of least knowledge. The categories, and the relationships between them, get drawn on day one — before the program has met its real inputs, before anyone knows which distinctions will earn their keep. Because that skeleton is hard to move later, the rational response to uncertainty is to over-build it: extra layers, extra abstract levels, speculative slots for uses that may never arrive. The methodology thus manufactures exactly the premature generality it was meant to discipline.

The alternative is to let the only fixed thing be small, named bundles of behavior, and to let membership in them be a consequence of what a component already does rather than a declaration made in advance. Then relatedness is computed rather than asserted, one component can belong to many groupings at once according to which slice of it you care about, and the groupings can be introduced after the fact by whoever needs them — including by code that neither side knew about. Growth becomes local: touching one such bundle reaches its immediate users and stops, because there is no descendant structure below it waiting to be repaired.

Two properties make this safe rather than merely loose. The bundles must be checked, so that decoupling does not become guessing. And they must stay small — one or two behaviors — because a small bundle is easy to satisfy accidentally-on-purpose, which is precisely what allows connections nobody planned. What you get is composability of the pipeline kind: a producer that knows nothing about its consumer, chains assembled at the call site, and wrappers that add logging, truncation, or fault injection by presenting the same shape they consume.

A programmer who believes this stops asking what the taxonomy of the domain is and starts asking what the narrowest behavior each collaboration actually requires. Interfaces get extracted at the point of use, from the consumer's need, rather than published in advance from the producer's ambition. The habit's payoff is that the way the pieces fit together is allowed to change as understanding improves, instead of being frozen when understanding was at its lowest.

**Source:** [Go at Google: Language Design in the Service of Software Engineering](../works/go-at-google.md) — the composition-over-inheritance argument, including its claim that fixing behavior sets rather than type graphs makes change linear, and the wrapper-function examples that follow it.
