---
type: lesson
title: "Turn your subobjects into elements, and questions of existence become fixed-point equations"
figure: scott
works: [continuous-lattices]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Turn your subobjects into elements, and questions of existence become fixed-point equations

**Lesson:** Asking whether an object with a given recursive shape exists is normally a fresh construction each time: build it, or find the argument that it cannot be built. There is a way to avoid re-doing this. If the sub-objects of your structure can be identified with certain *elements* of that structure — here, each well-behaved subspace is the exact set of fixed points of a single map, so the subspace and the map are interchangeable — then the collection of sub-objects inherits whatever machinery the structure already has. Scott's collection of such maps is itself a complete lattice, closed under the relevant limits, and ordered so that one map is below another exactly when its subspace is contained in the other's.

The payoff arrives when you also lift your type constructors. Products, sums, and function spaces of subspaces correspond to operations on the maps, and those operations are continuous in the same sense everything else is. Now a recursive specification of a subspace — one built from a product of itself with itself, mapped into itself — is literally an equation between elements of a domain, in a variable ranging over those elements, with a continuous operator on the right. Its solvability is not a new theorem; it is the fixed-point theorem you already proved, applied one level up. Existence of the structure you wanted follows from computing a fixed point, and simultaneous equations in several unknowns come along for free.

The move is worth recognizing in its general form: when you find yourself repeatedly proving that things of a certain kind exist, look for a way to make those things into values inside a setting you can already compute in. The reification has to be exact rather than approximate — the map must determine its subspace and vice versa, and the lifted operations must be continuous — but when it holds, an open-ended supply of existence questions collapses into one solved problem. The same reification also pays off in ordinary reasoning, since facts about the collection of sub-objects become facts about a lattice, provable by the arguments that already work there rather than by set-theoretic bookkeeping.

**Source:** [Continuous Lattices](../works/continuous-lattices.md) — Definition 3.11 and Proposition 3.12, which make the projections of a continuous lattice into a complete lattice; the following discussion showing the ordering on projections matches containment of the subspaces they cut out, and remarking that these facts, though not deep, were much easier to prove once the projections were treated as elements; the definition of an arrow operation on projections corresponding to the function-space construction, with the observation that such operations are continuous so existence theorems about subspaces can be proved by the fixed-point theorem; and the closing discussion of the universal domain, where a solution to a recursive subspace specification is obtained by solving an equation among projections.
