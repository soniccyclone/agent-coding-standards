---
type: lesson
title: "Maximum compression and legibility pull against each other"
figure: chaitin
works: [algorithmic-information-theory, a-theory-of-program-size-formally-identical-to-information-theory, an-invitation-to-algorithmic-information-theory]
axes: [cognitive-load, primitive-count, expressiveness]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Maximum compression and legibility pull against each other

**Lesson:** A shortest description of anything is itself incompressible, because if it could be shortened it was not shortest. Chaitin draws the consequences out: large minimal programs are statistically typical, with every symbol appearing at roughly uniform frequency and no visible regularity anywhere in them, and there are essentially no alternative minimal programs to choose from, so there is no nicer variant of the same size waiting to be selected. The most compressed form of a thing is indistinguishable, on inspection, from noise.

This puts a boundary on the pursuit of minimality. A small basis of primitives is worth having because it is likely to be the actual structure of the domain, and that is a claim about correspondence, not about comfort. Expressions written at the floor of that basis are the least readable form the content can take, precisely because every remaining symbol is doing irreplaceable work and none of it is predictable from context. Redundancy is what a reader uses to check their understanding as they go, and a minimal artifact has none left to offer.

So the practical target sits deliberately above the floor. You spend symbols on names, on repetition, on structure that a machine does not need, in order to buy back predictability for the reader, and you should know that you are buying rather than wasting. Chaitin's own habit is instructive on how sharp the trade is: he shipped two copies of every program in his course, one bare and one saturated with commentary and test cases, because the bare version is unreadable for lack of context and the annotated version is unreadable for bulk. Neither single artifact serves both purposes, and pretending one does is how documentation ends up satisfying nobody.

**Source:** [Algorithmic Information Theory](../works/algorithmic-information-theory.md) - the conceptual chapter, which establishes that minimal programs are incompressible, statistically normal, and essentially unique. The randomness definition underlying this is in [A Theory of Program Size Formally Identical to Information Theory](../works/a-theory-of-program-size-formally-identical-to-information-theory.md). The two-versions-of-every-program practice is described in [An Invitation to Algorithmic Information Theory](../works/an-invitation-to-algorithmic-information-theory.md), in the aside on how the course material is presented.
