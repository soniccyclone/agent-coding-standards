---
type: lesson
title: "When a construction stalls, try strengthening the maps rather than the objects"
figure: scott
works: [continuous-lattices]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# When a construction stalls, try strengthening the maps rather than the objects

**Lesson:** A structure is never just its objects; it is objects together with the maps you allow between them, and when a proof will not go through the instinct is to add hypotheses to the objects. Often the missing strength belongs on the maps instead. The instructive case is the difference between two relations that both say one object sits inside another. The weaker one asks only that going in and coming back out is the identity on the smaller object. The stronger one adds a single inequality in the other direction: going out and coming back in loses information but never invents any. That one extra condition is what makes the well-behaved theorems available — extensions become minimal rather than merely existent, limits of chains of embeddings stay inside the class, and lemmas relating successive stages become provable.

What makes this worth generalizing is that Scott could see the stronger relation was doing the work without being able to prove the weaker one insufficient. He states plainly that his proofs seem to require the stronger relationship, that he does not know whether the results hold for the weaker one, and that he suspects there may be difficulties. That is the honest and useful position: identify the property your argument actually consumed, note that you have not shown it necessary, and move on rather than either weakening the theorem or pretending the gap is closed. The general observation he draws from it — that the better-behaved relation is better behaved across the board — is the kind of judgment that guides the next construction.

The design lesson is to treat the choice of admissible map as a real parameter, tuned to the constructions you need, rather than as an afterthought fixed by whatever notion of homomorphism seemed natural first. Widening the maps buys generality and can silently destroy the closure properties everything else depended on; narrowing them costs generality and buys theorems. And when a result is reformulated in a more abstract setting, this is exactly the place the reformulation can go wrong — the objects transfer easily and the choice of maps is where the care is required, which is why Scott flags the choice of category as the thing that must be done carefully in the functorial version of his main argument.

**Source:** [Continuous Lattices](../works/continuous-lattices.md) — Definition 3.6's distinction between a retraction and a projection by the added condition that the round trip through the larger space is below the identity, Lemma 3.9 with its remark that the proof seems to require the stronger projection relationship and that projections are in general better behaved than retractions, the corresponding open question after Proposition 4.1 about inverse limits over mere retractions, and the note after the functorial restatement of Theorem 4.4 that the proper choice of category must be done with care and that projections rather than arbitrary continuous maps seem to be necessary.
