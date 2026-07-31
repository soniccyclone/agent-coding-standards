---
type: lesson
title: "A tolerance that is fine for a final answer is not fine for a recycled one"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# A tolerance that is fine for a final answer is not fine for a recycled one

**Lesson:** Approximate methods are usually characterised by a single accuracy number, and that number is treated as a property of the method. It is not. It is a property of the method together with what consumes the result. A quantity computed to two significant figures is entirely adequate when a human reads it, or when it is used to rank things and the ranking is coarse. The same quantity, at the same accuracy, is unusable when it is subtracted from the input to produce the input for the next stage, because then its error is not observed and discarded — it is injected into the data, and every subsequent stage compounds it.

This distinction should be made before choosing a stopping criterion, not after noticing that late results look wrong. The question is whether an approximation is terminal or load-bearing. A terminal approximation's error appears once in the output. A load-bearing one's error is inherited by everything computed downstream, and in an iterative peeling scheme the inheritance is cumulative: the second extraction is corrupted by the first's error, the third by the accumulated error of both, and the degradation is often superlinear because each stage is working with a smaller true signal against a growing accumulated one. The same code, the same convergence threshold, and a completely different quality of answer depending only on whether you took one result or twenty.

The practical responses are worth having ready. Tighten the tolerance for stages whose output is fed back, and let it be loose for stages whose output is merely reported. Re-derive rather than subtract where an exact alternative exists, since the error only enters through the feedback path. Check the accumulated result against an invariant that should hold exactly — orthogonality, conservation, a total that should not have moved — because that gives you an independent measurement of drift rather than a guess. And treat the number of iterations as a range of validity: it is entirely normal for the first few extractions to be trustworthy and the later ones to be noise, and knowing where that boundary is matters more than improving the method.

The generalisation: whenever you accept an approximation, trace where its output goes. Error tolerance is a statement about a path through the system, not about a function.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the power-iteration section of the dimensionality-reduction chapter, which notes that the method introduces small errors from limited precision and from stopping before exact convergence, that these did not matter when only the principal eigenvector was wanted for ranking, but that when the found eigenpair is subtracted off to expose the next one, inaccuracies accumulate unless care is taken.
