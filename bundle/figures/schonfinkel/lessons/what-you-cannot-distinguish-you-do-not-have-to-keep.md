---
type: lesson
title: "What you cannot distinguish, you do not have to keep"
figure: schonfinkel
works: [entscheidungsproblem-der-mathematischen-logik]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [formal-methods-and-verification, foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# What you cannot distinguish, you do not have to keep

The bound that turns the reduction into an algorithm comes from an observation about visibility. A formula containing some fixed number of one-place predicate symbols can only ever interrogate an element of the domain by applying those predicates to it. Two elements that answer identically to every one of them are, for the formula, the same element: nothing expressible can tell them apart. So group the domain by the pattern of answers each element produces, treat each group as a single thing, and the formula's truth is unchanged. Since there are only as many patterns as there are assignments of true and false to that many predicates, the collapsed domain cannot exceed two to the power of the predicate count, however vast the original was.

The shape of that argument is worth separating from the logic. An unbounded population plus a finite vocabulary of observations yields a finite quotient, and the size of the quotient is set by the observations, not by the population. Nothing about the domain had to be finite, small, or well behaved; the bound came entirely from how little the formula can ask. The proof that the collapse is faithful is the part that takes work, and it is done by induction over the quantifier prefix — each quantifier, having been shown to agree on representatives, agrees on the classes. That inductive obligation is the price of the collapse and you should expect to pay it every time.

Applied outside logic, this is the standard route from an unbounded state space to a checkable one, and it explains why the route ever works. States that produce identical behavior under every observation your property can make are interchangeable, so the reachable space to explore is not the space of configurations but the space of observational signatures — automaton minimization, bisimulation quotients, and abstraction in model checking are all the same trade. It is also the honest justification for a cache key, a deduplication hash, or a memoization signature: the key is legitimate exactly when it records everything the consumer can observe and nothing else, and a key that drops an observable distinction is not an optimization but a bug.

The lever it gives you is unusual, because it points the wrong way from intuition. To shrink an intractable domain, do not attack the domain. Count and narrow what the question can see. Every observation you remove from the vocabulary halves the quotient, and a property stated in terms of few observables is cheap to decide over a domain of any size — which is a reason to state properties narrowly on purpose, not merely a happy accident when they happen to be narrow.

**Source:** [Zum Entscheidungsproblem der mathematischen Logik](../works/entscheidungsproblem-der-mathematischen-logik.md) — section 2's theorem bounding the domain by two to the power of the number of predicate variables, including the partition of the domain into truth-value classes and the induction over the quantifier prefix showing the collapsed statement keeps its truth value.
