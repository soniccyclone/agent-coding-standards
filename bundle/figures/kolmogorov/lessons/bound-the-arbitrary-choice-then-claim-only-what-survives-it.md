---
type: lesson
title: "An arbitrary choice stops mattering once you bound its effect, and then you may only claim what the bound leaves"
figure: kolmogorov
works: [three-approaches-to-the-quantitative-definition-of-information]
axes: [verifiability, primitive-count]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# An arbitrary choice stops mattering once you bound its effect, and then you may only claim what the bound leaves

**Lesson:** Many definitions cannot be stated without fixing something arbitrary. Measure the size of a description and you have implicitly chosen a language to describe it in; a different language gives a different number, so the quantity looks like a property of your taste rather than of the thing. The usual responses are both bad: declare one choice canonical, which is arbitrariness with a crown on it, or give up on objectivity. The third move is to prove the choice only ever costs you a bounded amount. Once you show that there exists a way of describing things that is within an additive constant of every other one, and that the constant depends on the pair of conventions rather than on the object being measured, the definition becomes real. It is not choice-free; it is choice-*insensitive*, which is what was actually needed.

This buys objectivity at a specific price, and the price must be paid honestly. A quantity defined only up to an additive constant carries no information at scales comparable to that constant. Comparisons between two small values are noise, and any conclusion that would flip if the constant were different is not a conclusion. So the definition comes with a domain of validity attached: it means something when the quantities involved are large relative to the slack, and it means nothing when they are not. Knowing where your metric stops resolving is part of possessing the metric.

Both halves generalize to any engineering measure whose value depends on a convention you had to pick — the encoding, the machine model, the baseline configuration, the reference workload. The productive question is never "which one is correct," it is "how much can the answer move if I change it, and does that movement depend on what I am measuring or only on the conventions." A bounded, object-independent spread means you have a real quantity and a floor beneath which you must stop drawing conclusions. An unbounded spread, or one that grows with the thing being measured, means you have a preference dressed as a measurement, and no amount of care in applying it will fix that.

**Source:** [Three Approaches to the Quantitative Definition of Information](../works/three-approaches-to-the-quantitative-definition-of-information.md) — the fundamental theorem of §3 establishing an asymptotically optimal programming method, the consequence that any two such methods differ by a constant independent of the objects, and the accompanying insistence that the construction is aimed at quantities large enough for that constant to be negligible.
