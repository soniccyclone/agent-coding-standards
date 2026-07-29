---
type: lesson
title: "How you combine independent estimates is part of the estimator, not a formality"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# How you combine independent estimates is part of the estimator, not a formality

**Lesson:** Running many independent copies of a randomised estimator and pooling the results feels like the trivial final step, the part where you just take the average. It is not. Averaging is only sound when the quantity being averaged has a well-behaved distribution, and estimators that read a count off an exponential scale do not: a single unlucky observation can move the estimate by a factor of two, rare observations move it by much more, and the contribution of the tail can be large enough that the expected value of the estimator is not the thing you want at all — even though every individual draw is intuitively reasonable and the estimator is intuitively unbiased. The pooling rule inherits the pathology of the individual estimator's distribution, so it must be chosen with that distribution in mind.

The obvious fix has its own defect, and noticing this is the instructive part. Taking a median discards outliers, which addresses the tail exactly — but if each individual estimate can only be a power of two, so can the median, and no number of samples will let you land between two powers of two. You have swapped an unbounded-tail problem for a resolution problem. The construction that works is a composition: average within small groups so the group results can take arbitrary values, then take the median across groups so no group's outlier dominates. Each layer fixes what the other cannot, and the sizes of the groups are set by which defect you need suppressed harder.

The transferable point is that "run it many times and combine" hides at least three separate design decisions — the pooling function, the number of samples, and the arrangement of samples into stages — and each one can be individually wrong while the code runs and produces plausible numbers. A programmer who has internalised this asks, of any Monte Carlo or sketch-based component, what the distribution of a single estimate looks like, not merely what its central tendency is. Heavy tail means do not average. Coarse support means do not take order statistics. Both means stage the combination. It is also a reminder that a correct-looking derivation of unbiasedness is not the whole story: an estimator can be unbiased and still be useless to average, and can be robust to average and still be unable to express the answer.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the stream-mining chapter's distinct-element estimation, specifically the discussion following the tail-length estimator where averaging is rejected on tail grounds, medians are rejected on granularity grounds, and medians of group averages are adopted with a size condition on the groups.
