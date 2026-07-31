---
type: lesson
title: "How fast the penalty grows decides who controls the answer"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# How fast the penalty grows decides who controls the answer

**Lesson:** When you fit anything by minimising total disagreement with a set of observations, the function that converts one disagreement into one penalty is not a formality — it decides how much a single observation is allowed to move the result. A penalty that grows faster than linearly gives the furthest-off observation disproportionate say, and the further off it is, the more say it gets. If some of your observations are wrong rather than merely noisy, that is a system in which the worst data is in charge. The fit is not incorrect given what you asked for; you asked for something you did not want.

The correction is to shape the penalty by region rather than to pick one formula and live with it. Near zero, fast growth is genuinely what you want: small disagreements should be distinguished from each other sharply, so the fit is decisive about the bulk of the data, and the resulting function is smooth at the point where the search will spend most of its time. Far from zero, you want the penalty's rate of increase to level off, so that an observation which is already clearly anomalous does not keep buying additional influence by being more anomalous. Switching from one growth rate to the other at a chosen distance gives you both behaviours, and the switch point is the explicit statement of where you stop believing an observation.

Two details make this work rather than merely sound reasonable. The pieces must be joined so the combined function has no kink in what the search reads — otherwise you have traded one pathology for another, and the search will chatter at the seam. And the switch point is a real parameter with a real meaning: it is the magnitude beyond which you regard a disagreement as evidence about the observation rather than evidence about the model. That is a judgement about your data source, not a tuning knob, and it should be set by what you know about how the data can be wrong.

The idea generalises past fitting. Any aggregate that sums a transformed per-item quantity — a load score, a cost function, a priority, an alert severity — has the same structure, and the transform's growth rate is what determines whether the aggregate reports the state of the population or the state of its single most extreme member. Both are legitimate things to want. The mistake is not choosing, and thereby inheriting whatever the convenient formula happened to imply.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the regression-loss section of the neural-nets chapter, which notes that mean squared error is very sensitive to outliers because the squared term lets a few points swamp all the others and make training swing wildly, and introduces the Huber loss, quadratic within a chosen distance of zero and linear beyond it, as the remedy.
