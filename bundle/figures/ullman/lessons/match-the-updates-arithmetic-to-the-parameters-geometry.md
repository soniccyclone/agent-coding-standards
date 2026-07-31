---
type: lesson
title: "Match the update's arithmetic to the parameter's geometry"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Match the update's arithmetic to the parameter's geometry

**Lesson:** Any procedure that adjusts a quantity in response to evidence has to decide *how* to adjust it, and the default choice — add a small amount — is a choice, not a neutral starting point. Adding treats the quantity as living on a scale where equal increments mean equal things, and where the natural neighbourhood of a value is a fixed distance around it. Multiplying treats it as living on a scale where equal ratios mean equal things, so the same correction moves a small value a little and a large one a lot. Neither is more correct in general, and which one you pick determines the reachable values, the speed of adjustment across scales, and whether certain regions of the space are ever visited.

The visible consequences are worth spelling out, because they read as separate features until you notice they all follow from the choice. A multiplicative rule applied to a positive starting value can never produce a negative one, so if the quantity is meaningfully nonnegative — a rate, a weight, a duration — the constraint is enforced by the arithmetic instead of by clamping. It reaches very large and very small magnitudes in a number of steps proportional to the logarithm of the range, so it copes with quantities of unknown scale without needing them normalised first. And a value that has been driven very small becomes very hard to revive, which is a liability if evidence may later reverse — the additive rule is more forgiving there.

The tuning parameter changes character correspondingly. For an additive rule it is a step size with the units of the quantity, and picking it requires knowing the scale in advance. For a multiplicative rule it is a dimensionless factor, and the two failure modes are the familiar ones from the other direction: too close to one and progress is glacial, too far and the value overshoots and oscillates. In both cases the sensible range is set by the same reasoning, but the numbers are not transferable between the two, which is a common source of confusion when switching.

The generalisable prompt: before writing an update rule, ask what "a little more" means for the thing being updated. If differences are what carry meaning, add. If ratios are, multiply. Getting this wrong does not produce an obviously broken system — it produces one that is unaccountably slow in some regions and unstable in others, which is a much harder thing to diagnose than a wrong answer.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the contrast in the perceptron chapter between the basic training rule, which adds a scaled multiple of the misclassified example to the weight vector and can produce components of either sign, and the Winnow rule, which doubles or halves the weights of the components present in a misclassified example, produces only positive weights, and carries the same warning about factors too close to one converging slowly and factors too large making the weights oscillate.
