---
type: lesson
title: "Look for the one tiny object that generates the entire class you care about"
figure: scott
works: [continuous-lattices]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Look for the one tiny object that generates the entire class you care about

**Lesson:** When you have identified a class of objects by an abstract property, it is worth spending real effort asking whether every member can be reached from one very small member by a couple of closure operations. The answer here is as sharp as it gets: the smallest non-trivial object, with two elements one of which is distinguished, generates the whole class under products and retracts, and nothing else is needed. That result does two independent jobs. It gives an existence proof for the class that is completely concrete, and it gives an *embedding* theorem — any object whatsoever in the surrounding universe sits inside a suitably large power of the two-element object — which means the class is not a curiosity but a place everything else can be moved into.

The reason a generator this small is possible is worth internalizing, because it tells you where to look for one. The two-element object is exactly a yes/no observation, and maps into it are precisely the observable properties of the source. Taking a product over all such properties records every observation at once, so the embedding is nothing more than the map sending each point to the record of which properties it has, and it is faithful exactly when distinct points differ in some observation. Whenever your objects are separated by their observable properties, this construction is available, and the generator is whatever object a single observation lives in. The tiny object is not chosen for smallness; it is the shape of one bit of information about a point.

Two practical consequences. First, results proved about the generator plus results about the closure operations give you the whole class, which is why the smallness pays for itself. Second, the concrete representation and the abstract characterization are useful for different things and should both be kept: Scott's own assessment is that the retract-of-a-power picture is not much help in proving theorems, while the internal characterization is, and the embedding theorem is what justifies believing the class is big enough to be worth a theory. Having a generator is not a substitute for having the axioms; it is what tells you the axioms describe something you can get your hands on.

**Source:** [Continuous Lattices](../works/continuous-lattices.md) — Section 1's chain from Proposition 1.2 (the two-point Sierpinski space is injective) through 1.3 and 1.4 (products and retracts of injective spaces are injective) to Proposition 1.5 and Corollary 1.6: every space embeds in a Cartesian power of the two-point space via the map sending a point to the record of which open sets contain it, injectivity of the source being what makes the map one-one, and the injective spaces being exactly the retracts of such powers. The discussion after 2.12 assesses that representation as of limited use for proofs relative to the internal characterization.
