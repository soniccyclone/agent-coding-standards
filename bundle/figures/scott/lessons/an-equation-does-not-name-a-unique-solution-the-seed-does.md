---
type: lesson
title: "Solving an equation by iteration does not name a unique answer; the starting point is part of the design"
figure: scott
works: [continuous-lattices]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Solving an equation by iteration does not name a unique answer; the starting point is part of the design

**Lesson:** When a structure is obtained by iterating a construction from a seed and passing to the limit, it is easy to start describing it as *the* solution of the equation it satisfies, because the equation is what you set out to solve and the construction is deterministic once running. But the construction takes two inputs, not one: the operator and the seed, where the seed is both an initial object and the specific way that object sits inside the operator's image of it. Different seeds satisfy the same equation and give genuinely different answers. Scott's smallest case is decisive — start from the two-element lattice, notice there are exactly two ways to embed it into its own function space, and you get two limit structures that are not isomorphic, distinguishable by whether the top element is isolated.

The consequence that matters is that the differences are not confined to fine structure; they reach the operations you care about. In these two limits the fixed-point operator has different algebraic properties, so the very apparatus a semantics would be built on behaves differently depending on a choice made before the construction started. A statement like "the domain satisfying this recursive equation" therefore under-determines what you are talking about, and any property you go on to prove is a property of the pair, seed included. This is the opposite of the situation with a least fixed point inside a fixed domain, where the ordering makes the answer canonical; here there is no ambient ordering on the candidate seeds to pick one out.

The transferable habit is to look for the hidden parameter whenever a construction is described as producing "the" object with some property, and then to ask what observable behavior varies with it. Sometimes the parameter is genuinely inert and the informality is harmless. When it is not, you have found a design axis rather than an implementation detail, and the choice should be made deliberately and recorded, because everything downstream will inherit it and nothing downstream will mention it.

**Source:** [Continuous Lattices](../works/continuous-lattices.md) — the discussion following Theorem 4.4, which starts the inverse-limit construction from the two-element lattice, observes that there are exactly two projections from its function space back onto it, and shows the two resulting limit spaces differ in whether the top element is isolated, with David Park's result that the fixed-point operator of Proposition 3.14 has quite different algebraic properties in the two. Proposition 3.13 and the following remarks establish the more general point that a lattice has as many such embeddings into its function space as it has isolated elements.
