---
type: lesson
title: "The shape of the tie-breaking term decides the answer's character"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# The shape of the tie-breaking term decides the answer's character

**Lesson:** When a search can end in many different places that all score about equally on what you asked for, the one you get is decided by starting conditions and the incidental path the search took. That is worth recognising as a missed opportunity rather than as noise: you have a large set of acceptable answers and no stated preference among them, so you are accepting an arbitrary member of the set when you could be specifying which member you want. The mechanism for specifying it is to add a second term to the objective, small relative to the first, that scores the property you would like the answer to have. The search then still optimises the thing you care about and, among the near-ties, prefers the one you would have chosen.

The interesting part is that the second term's *shape* determines what kind of preference you have expressed, and two penalties that both plausibly mean "keep it simple" mean very different things. Penalise the sum of squared magnitudes and you get an answer whose components are all modestly sized — nothing dominant, nothing eliminated, influence spread out. Penalise the sum of absolute magnitudes and you get an answer where many components are driven to exactly zero and the rest carry real weight — the same nominal notion of simplicity, delivered as sparsity rather than as moderation. Which you want depends on why you wanted simplicity: for robustness, the first; for a result you can prune, transmit, or explain, the second.

The weight on the second term is a real decision and it should be understood as a rate of exchange, not a tuning nuisance. You are declaring how much of the primary objective you are willing to give up to buy a unit of the secondary property. Stated that way it is an answerable question, and it also makes plain that the answer depends on how much you trust your evidence: the more likely your primary score is measuring accidents of the sample rather than the real thing, the more of it you should be willing to trade.

The general habit: whenever a procedure returns something arbitrary from among many acceptable outputs, do not treat the arbitrariness as inherent. Write down which of them you would prefer and why, turn that into a term, and the arbitrariness becomes a choice you made. Scheduling, layout, plan selection, code generation, resource assignment — all routinely have huge sets of equally valid outputs and a strong unstated preference among them.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the norm-penalties section of the regularization chapter, which observes that gradient descent settles on one of many local minima and that low-magnitude weights tend to generalise better, adds a penalty term scaled by a trade-off hyperparameter, and contrasts the squared-magnitude penalty (best for most applications) with the absolute-magnitude penalty, which is useful for model compression because it tends to drive many weights to exactly zero.
