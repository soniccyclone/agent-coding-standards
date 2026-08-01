---
type: lesson
title: "A bound and an accurate estimate are not interchangeable"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# A bound and an accurate estimate are not interchangeable

**Lesson:** Two approximations of the same quantity can look equally reasonable, cost the same, and differ in a way that decides whether the system built on them is safe. One of them is guaranteed to err in a known direction — it never comes out below the truth, say, because the derivation goes through an inequality that only ever adds. The other has no such guarantee but is typically much closer, because the derivation goes through an assumption that happens to hold well in the regime you operate in. Neither is better in the abstract. Which one you want is determined by what happens downstream, and the mistake is to compare them on average error alone, since that comparison is blind to the property that actually matters.

The rule follows from how the value gets used. Compared against a threshold that gates an irreversible action — admit this into the group, allocate this much space, declare this within budget — a one-sided approximation gives you a real guarantee on one class of error, at the price of being conservative and rejecting things it needn't have. You will never overrun the budget; you will sometimes refuse a legitimate case. The accurate-but-unbounded version gives you neither guarantee and will occasionally cross the line in the direction that hurts. Conversely, when the value is reported, ranked, or fed into a further estimate, a tight estimate that is wrong in both directions is worth much more than a loose bound, because the systematic slack in a bound compounds through every subsequent stage and drifts steadily further from the truth.

The practical habit is to make each approximation in a system carry its character alongside its value: is this a bound, and in which direction, or is this an estimate, and under what assumption. That information exists at the moment the formula is derived — you know whether you invoked an inequality or an approximation — and it is almost always discarded immediately, leaving a later reader with a number and no way to recover whether it is safe to compare against a limit. Recording it costs a comment; reconstructing it costs re-deriving somebody else's algebra.

There is a design consequence too. When a quantity will be tested against a limit, look for the variant of the derivation that yields a bound, even if it is loose, and prefer it over the sharper one. When several such approximations feed a decision together, check that their directions agree, since a mixture of an upper bound on one term and an unbounded estimate of another produces an aggregate with no guarantee at all — the weakest link governs, and the guarantee is quietly lost in the combination rather than in any single step.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 7's stream-clustering examples, which estimate a merged cluster's summed distances by routing each point through the old centroid and note that the triangle inequality makes the result an upper bound, then give the sum-of-squares variant of the same formula and describe it instead as close to correct in high dimensions by the curse of dimensionality.
