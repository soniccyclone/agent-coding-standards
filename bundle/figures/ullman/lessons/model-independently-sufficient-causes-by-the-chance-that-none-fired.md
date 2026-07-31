---
type: lesson
title: "Model independently sufficient causes by the chance that none of them fired"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, primitive-count]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Model independently sufficient causes by the chance that none of them fired

**Lesson:** When several mechanisms could each on their own produce the same effect, the natural way to write the combined chance of the effect is wrong: you cannot add the individual chances, because they exceed one as soon as there are enough of them, and you cannot take the maximum, because that makes extra mechanisms free. Compute the complement instead. Work out the chance that each mechanism *failed* to produce the effect, multiply those together on the assumption that the mechanisms act independently, and subtract from one. The formula is small, but the thinking behind it is what transfers: an effect with many sufficient causes is easiest to reason about through the single way it can be absent.

The composition rule this gives you has exactly the properties the situation demands, which is worth checking explicitly rather than trusting. Adding a mechanism can only increase the chance of the effect, never decrease it. The result stays bounded no matter how many mechanisms pile up, approaching certainty without ever exceeding it. Each additional mechanism contributes less than the last, because it can only act on the residue the others left. And a mechanism whose individual chance is zero contributes nothing at all, so it drops out cleanly. Those are the qualitative behaviours you would want from any reasonable answer, and getting all four from one expression is the sign that the decomposition is the right one.

The modelling payoff is that overlap becomes something the model predicts instead of something you have to add by hand. If two things share more than one reason to be connected, the composition rule already says they are more likely connected than either reason alone would imply — so an observed excess of connections in an overlap region is evidence about shared causes, and it can be fit rather than stipulated. Building the model out of independent per-cause contributions is what makes that inference available; a model that assigns one lumped strength to each relationship has nowhere for the excess to come from.

The independence assumption is doing real work and should be stated where it will be seen. Mechanisms that share a hidden common driver will have correlated failures, the product will understate the chance that all of them fail, and the model will systematically overpredict the effect. That is often tolerable and occasionally not, but the failure mode is at least specific and testable, which is more than can be said for a combination rule chosen because it looked reasonable.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the affiliation-graph model in the overlapping-communities chapter, in which each shared community independently induces an edge with its own probability, the edge probability for a pair is one minus the product over their shared communities of one minus each community's probability, and the motivating observation that the intersection of two communities should be denser than either community alone.
