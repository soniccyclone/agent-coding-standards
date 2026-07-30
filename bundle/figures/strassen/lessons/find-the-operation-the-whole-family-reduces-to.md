---
type: lesson
title: "Locate the operation an entire family of problems reduces to, and improve that one"
figure: strassen
works: [gaussian-elimination-is-not-optimal]
axes: [primitive-count, expressiveness]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Locate the operation an entire family of problems reduces to, and improve that one

**Lesson:** A cluster of problems that look independent — inverting, solving, computing a determinant — is usually held together by a single operation each of them is secretly built out of. When that is the case, the operation is the only place worth spending effort, because a bound proved there is not one result but the whole cluster's results at once: every problem that can be expressed as a bounded number of calls to it inherits the improvement automatically, with nothing to redesign at the level of each individual problem. The leverage is entirely in the reduction structure, and finding that structure is a different activity from being clever about any one member of the family.

The condition for inheritance is worth stating precisely, because it is easy to assume rather than check. A problem inherits an improvement only if it can be rewritten so its own recursive decomposition bottoms out in the improved operation, without spawning more subproblems than the improved operation itself does. That rewriting is real work — the natural formulation of a derived problem often does not call the primitive at all, and has to be reshaped into block form before the reduction exists. What follows is the discipline of asking, of each apparently new problem, not "what algorithm does this need" but "what already-improved operation can this be phrased as calls to."

The architectural consequence outlives the specific result. Effort concentrated at a genuine chokepoint compounds across everything downstream of it; the same effort spread evenly across the surface improves each thing once. So the valuable structural knowledge about a system is which of its operations are chokepoints and which are leaves, and the valuable structural work is deliberately routing more of the system through fewer of them, so that the next improvement has somewhere to propagate. A design where every problem has its own bespoke path has thrown away the multiplier before anyone starts optimizing.

**Source:** [Gaussian Elimination is not Optimal](../works/gaussian-elimination-is-not-optimal.md) — the opening claim that the multiplication algorithm induces algorithms for inversion, linear systems and determinants at the same asymptotic bound, and the later inversion construction, which is built as a block recursion whose products are handed to the fast multiplication routine.
