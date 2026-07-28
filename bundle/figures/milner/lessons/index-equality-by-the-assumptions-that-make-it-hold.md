---
type: lesson
title: "When equality is not stable, index it by the assumptions that make it hold"
figure: milner
works: [a-calculus-of-mobile-processes]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# When equality is not stable, index it by the assumptions that make it hold

**Lesson:** A notion of sameness that survives being placed in any context is what makes substitution of equals for equals legitimate, and a candidate notion that fails this test looks broken. Here the natural notion of two processes being indistinguishable fails it outright: two systems agree as long as a pair of names is known to be different, and diverge when those names turn out to be the same, because identifying them creates an interaction that was not previously possible. The available responses are to discard the notion, or to redefine sameness as agreement under every possible identification of names. Both are taken — and then, more usefully, the space between them is filled in.

The construction is to make the assumption explicit and parameterize on it. Sameness is indexed by a stated set of pairs of names that are being taken as distinct; the fragile notion is the case where nothing may be identified, the fully substitutive notion is the case where anything may be, and in between sits a graduated family. Facts then carry their preconditions with them: an equation is not simply true, it is true relative to named assumptions, and there are laws for how those assumptions strengthen when a name becomes private (privacy already guarantees distinctness, so the assumption can be discharged) and must weaken when a name is a placeholder for whatever arrives (an incoming name might be any name, so nothing may be assumed). The whole complete axiomatization of the well-behaved relation is then obtained by adding one rule on top of the axiomatization of the fragile one — the badly-behaved relation turns out to be the better foundation because its theory is simpler.

There is a second, sharper observation in the same vicinity: how the definition of sameness orders its quantifiers changes which systems it identifies. Requiring a single matching step that works for every value that could arrive is strictly stronger than requiring, for each value, some matching step. The paper defines the operational rules so that the choice remains open, deliberately deferring the commitment rather than baking one reading into the transition relation. Definitions have design freedom in exactly the places where quantifiers meet, and those places deserve as much attention as the syntax.

The transferable habit is to stop asking whether two things are equivalent and start asking under what conditions they are. Interchangeability of two implementations, two services, two refactorings always rests on assumptions about what the environment will not do. Writing those assumptions down as part of the claim — rather than asserting an unconditional equivalence that a wider context will falsify — is what makes the claim survive contact with a real system.

**Source:** [A Calculus of Mobile Processes, I and II](../works/a-calculus-of-mobile-processes.md) — Part I's algebraic section, where ground equivalence is shown not to survive name substitution and the distinction-indexed family is introduced with laws relating it to the two binders; Part II develops the properties and derives the complete axiomatization, and its discussion of commuting a quantifier yields the late/early alternative.
