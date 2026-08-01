---
type: lesson
title: "Exhaust a shortcut's family to tell bias from noise"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Exhaust a shortcut's family to tell bias from noise

**Lesson:** Randomised estimators are routinely made cheaper by drawing from a restricted pool instead of the full one — vectors whose entries are only plus or minus one instead of arbitrary reals, integers instead of a continuum, a fixed table of values instead of a generator. The justification offered is that the restricted pool is random enough, and the evidence offered is that individual estimates look plausible. That evidence cannot distinguish the two ways such a scheme can be wrong. If the restricted pool is unbiased, more draws converge to the truth and the shortcut is free. If the restricted pool is skewed relative to the full one, more draws converge to something else, and no sample size fixes it.

There is a decisive test available whenever the restricted pool is small: enumerate all of it. Compute the estimate using every member of the restricted family rather than a random handful, and compare that value against the exact answer computed some other way. What comes back is the limit the estimator is converging to. If it differs from the truth, you have measured the bias directly, in one calculation, with no statistics involved. It is a startling test to run the first time, because a shortcut that produces respectable-looking numbers on a few draws can turn out to have a limit that is plainly wrong, and the discrepancy is invisible to any amount of averaging.

The result of running that test is not necessarily to abandon the shortcut. A known, bounded, measured bias is a very different object from an unexamined one: it can be corrected, it can be declared acceptable against the tolerance the application actually needs, or it can be confined to the regime where it is small. What is not acceptable is carrying it as an unknown. The phrase that should trigger this check is any variant of "it turns out to be sufficiently random to restrict ourselves to" — a claim about a distribution, stated without a distributional argument, in a context where the restriction was chosen for the convenience of the arithmetic.

The general form is to look for a computable limit of your approximation and evaluate it, rather than watching the approximation's variance shrink and inferring correctness. Exhausting a small family is one way. Taking the number of samples to infinity analytically is another. Running the estimator on an instance whose exact answer is known independently is a third. All three answer the question that repeated sampling structurally cannot: whether the thing you are converging on is the thing you wanted.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 3's sketch construction for cosine distance, where random vectors are restricted to entries of plus and minus one, the worked example's three-vector sketch estimates an angle far from the true one, and the text then evaluates all sixteen members of the restricted family for that dimension and finds that even the exhaustive estimate misses the true angle.
