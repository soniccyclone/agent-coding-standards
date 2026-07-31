---
type: lesson
title: "Weaken the law only where it cannot hold"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Weaken the law only where it cannot hold

**Lesson:** Some operations are defined by a law — an inverse is the thing that composes with its argument to give the identity — and on some inputs no value satisfies the law. The usual responses are both bad. Refusing to define the operation there makes it partial, so every caller must handle a failure that is often irrelevant to them. Defining it by some plausible fallback silently breaks the law everywhere, since callers can no longer rely on it at all. There is a third option that is better than both: define the operation so that the law still holds exactly on the part of the input where it can, and fails in a completely characterised way on the rest.

Concretely, that means the composition of a thing with its generalised inverse is not the identity but is a *projection* — an operator that is the identity on the well-behaved subspace and zero on the degenerate one. That is a strictly stronger contract than "returns something reasonable," because it is a precise statement a caller can reason with: whatever survives is exactly correct, and what does not survive is identifiable. Consumers who only touch the well-behaved part get the full law; consumers who touch the rest get a documented degradation rather than a surprise.

The generalisable pattern is to look for a decomposition of the domain into the part where the ideal contract is achievable and the part where it is not, and to make the operation ideal on the first and explicitly neutral on the second. The neutral behaviour should be chosen so that composition still works — an element that annihilates rather than one that corrupts — since the whole point is that these operations get chained. Applied elsewhere: a partial parse that returns the fragments it understood and marks the rest, a merge that combines what it can and flags conflicts rather than picking a winner, a query that answers over the shards it reached and reports which it did not. All are the same move.

The discipline is naming which part of the domain is degenerate and how you can tell, since the value of the whole approach comes from that being inspectable. A generalised operation that quietly does something different on bad input, with no way to find out afterwards which inputs were bad, has given up the property that made the generalisation worth having and is just a plausible fallback with a better name.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the box in the CUR-decomposition section of the dimensionality-reduction chapter explaining why the pseudoinverse works: the inverse of a decomposed product reverses through the transposes of its orthonormal factors, the diagonal factor's inverse is elementwise except where an entry is zero, and the resulting composition is not the identity but a diagonal matrix carrying one wherever the original entry was nonzero and zero where it was not.
