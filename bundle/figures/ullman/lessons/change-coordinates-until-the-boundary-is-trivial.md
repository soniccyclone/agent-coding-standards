---
type: lesson
title: "Change coordinates until the boundary is trivial"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Change coordinates until the boundary is trivial

**Lesson:** When a simple decision rule cannot express the distinction you need, there are two roads: build a more powerful rule, or re-express the data so the simple rule suffices. The second is routinely better and routinely skipped, because the representation arrived with the data and does not feel like a variable. It is one. A rule that can only cut along straight lines is helpless against a distinction that is really about distance from a centre — until you replace each point's coordinates with its distance and angle, at which point the distinction is a comparison against one number and the machinery you already have solves it exactly.

The reason to prefer this road is what falls out alongside. A representation chosen because it matches the structure of the phenomenon tends to make the irrelevant parts of the description visibly irrelevant: after the change of coordinates, one of the two new components does not participate in the decision at all, and can be dropped. So the same insight that made the problem easy also made the data smaller, and the resulting rule is one you can read and defend — this distinction is about how far away things are — rather than a fitted surface nobody can interpret. That interpretability is not decoration; it is what lets you predict how the rule will behave on cases you have not seen.

The alternative road has a specific hazard. It is always possible, in principle, to make any distinction expressible by moving to a sufficiently rich space, and the enrichment can be mechanical, requiring no understanding of the data at all. But a rule with enough freedom to separate any arrangement will separate the arrangement you happen to have, including the parts of it that are accidents of sampling. Power bought without understanding is bought at the price of fitting noise, and it typically shows up as excellent performance on the data you had and poor performance on everything else.

The practical reading: when a simple method is failing, spend the first effort asking what the data is really organised by — distance, ratio, time since, rank, angle, log of the amount — and re-express it in those terms. If the answer is that you do not know, then reach for the more powerful method, but reach for it knowing you are substituting capacity for understanding and inheriting the corresponding risk.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the section on transforming the training set in the perceptron chapter, where destinations classifiable only by distance from home are not linearly separable in latitude and longitude, become separable when converted to polar coordinates, and then reduce to a single-component representation once the angle is recognised as irrelevant — set against the following section's warning that transforming to a higher-dimensional space to force separability can lead to overfitting.
