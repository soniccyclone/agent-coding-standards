---
type: lesson
title: "Any translation between notations is easy; only one that preserves meaning counts, so state that test before you start"
figure: landin
works: [mechanical-evaluation-of-expressions]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Any translation between notations is easy; only one that preserves meaning counts, so state that test before you start

**Lesson:** Landin notes, almost in passing, that finding *some* correspondence between a familiar notation and a core calculus is trivial, and that the whole difficulty lies in finding one under which what the notation intuitively means matches what the core expression denotes. He gives that requirement a name and then uses it as a standing obligation on every rendering he proposes. This reframes desugaring, compilation, and refactoring as claims that can be wrong, rather than as mechanical rewriting that is right by virtue of having been performed.

The bite is in his counterexamples, and they are the kind of thing that survives translation to any era. A summation over a run of vector elements can be rewritten so that the parts line up neatly and the result is still wrong, because the rewritten form mentions only one element of the vector and so misstates what the value depends on. A two-armed conditional can be recast as picking an item out of a pair, which matches shape for shape, and yet fails precisely on the inputs the conditional existed to protect: the discarded arm now has to have a value, so an expression that was well defined becomes undefined. Both failures are invisible if you check only that the pieces correspond. They are caught immediately if your criterion is that the value, its dependencies, and its very existence must be preserved.

What follows for practice is a habit of picking the invariant first. Before rewriting a construct into a supposedly equivalent one, say out loud what equivalence you are claiming — same result on inputs where both are defined is a much weaker claim than same domain of definedness, which is weaker again than same set of things the result depends on. Then test the rewrite against the inputs that distinguish those claims, which are almost always the degenerate ones: the empty range, the divisor that is zero, the branch that must not be taken. The second-order lesson is that a notational convenience is not neutral. Sugar that quietly widens the domain a function must be defined on has changed the program's meaning while looking like it only changed its spelling.

**Source:** [The Mechanical Evaluation of Expressions](../works/mechanical-evaluation-of-expressions.md) — the criterion introduced when applicative expressions are first given values, and its two demonstrations: the misattributed dependency in a summation and the failed index-selection rendering of a conditional.
