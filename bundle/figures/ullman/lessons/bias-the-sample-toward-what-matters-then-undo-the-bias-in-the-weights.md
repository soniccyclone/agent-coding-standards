---
type: lesson
title: "Bias the sample toward what matters, then undo the bias in the weights"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Bias the sample toward what matters, then undo the bias in the weights

**Lesson:** Sampling uniformly is the safe default because it is obviously fair, and it is often badly wasteful. When the elements of a population contribute wildly unequally to whatever you are estimating, a uniform sample spends almost all its draws on elements that contribute nearly nothing, and the estimate is dominated by whether you happened to catch one of the few that matter. The alternative is to sample deliberately unfairly — draw each element with probability proportional to its contribution — and then compensate by scaling whatever you kept by the inverse of the probability with which you kept it. The unfairness in selection and the unfairness in weighting cancel, so the estimate remains centred on the truth while its variance collapses, because you are now almost certain to have captured the elements that dominate the answer.

The compensation step is not bookkeeping and cannot be skipped or approximated. Without it you have simply built a summary of the largest elements, which is a different and usually wrong answer; with the wrong exponent on the correction you have an estimator that is subtly biased in a direction nobody will notice. The correct factor follows from requiring that the expected contribution of each element be what it would have been under exhaustive treatment, and it is worth re-deriving for your specific setting rather than copying, because it depends on how the sampled elements are combined — a rule that squares its inputs needs a different correction from one that adds them.

Choosing the proportionality measure is the design decision. It should be as close as you can get to each element's actual contribution to the final quantity, and when the exact contribution is unknown a computable proxy is usually available and usually good enough — total magnitude, size, frequency, past cost. A proxy that is roughly right still concentrates the sample where the mass is; a proxy that is uncorrelated with contribution gives you uniform sampling with extra steps and worse variance.

Two details show up every time. Drawing independently means the same element can be selected repeatedly, which is not an error — either keep the duplicates or merge them, with a corresponding adjustment to the weight, and both are correct as long as the adjustment matches. And the guarantee this buys is that the estimate is right in expectation and converges as you take more draws; it is not a bound on any single run. Choosing the sample size by what accuracy you need, not by what looked reasonable, is the part that keeps that guarantee meaningful.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the CUR-decomposition sections of the dimensionality-reduction chapter, which choose rows and columns with probability proportional to their squared magnitude relative to the whole matrix, scale each chosen row or column by the reciprocal of the square root of its expected selection count, and describe merging repeated selections into a single vector scaled by the square root of the number of times it was drawn.
