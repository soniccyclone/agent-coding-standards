---
type: lesson
title: "A quantity can be worth defining even when nothing can compute it"
figure: kolmogorov
works: [three-approaches-to-the-quantitative-definition-of-information]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# A quantity can be worth defining even when nothing can compute it

**Lesson:** There is a reflex that says a definition is only respectable if you can evaluate it, and it quietly bends every measure toward whatever happens to be easy to compute. The shortest generator of an object is a counterexample worth internalizing: it is always finite, it is perfectly well specified, and no procedure can determine it, because deciding it would require knowing in advance which candidate programs ever halt. The quantity is real and unreachable at the same time, and it remains the right definition anyway.

What an uncomputable definition still gives you is one-sided knowledge and a fixed target. You can always exhibit a description and thereby bound the true value from above; you simply never learn that you have hit bottom. That asymmetry is not a defect, it is the shape of the situation, and pretending otherwise is how people end up optimizing a computable proxy that drifts from the thing they cared about. Better to hold the honest definition and treat every measurement as an upper bound that a cleverer description might improve, than to redefine the goal as whatever the tool reports.

The practical discipline is to keep two layers apart: what you mean, and what you can check. Formulate the concept so it says exactly what matters, then separately construct approximations, bounds, or heuristics and label them as such. A team that collapses the layers loses the ability to say that a metric has gone wrong, since the metric has become the definition and cannot disagree with itself. A team that keeps them apart can improve its estimator without renegotiating its goal, and can recognize when a comfortable number has stopped tracking the thing it was standing in for.

**Source:** [Three Approaches to the Quantitative Definition of Information](../works/three-approaches-to-the-quantitative-definition-of-information.md) — the remark in §3 that, because partially recursive functions are not defined everywhere and no fixed method decides whether a given program applied to a given object terminates, the relative complexity cannot be effectively calculated even when it is known to be finite for all arguments, together with the estimation experiments elsewhere in the paper that only ever produce upper estimates.
