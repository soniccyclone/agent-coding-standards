---
type: lesson
title: "State the weakest output that would satisfy the use, then choose the method"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, expressiveness, parallelizability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# State the weakest output that would satisfy the use, then choose the method

**Lesson:** Problems arrive stated in their strongest form because the strong form is the one that is easy to say. Fill in the whole table. Rank all the candidates. Compute the exact value for every pair. Almost none of that is ever consumed. Look at what the system actually emits and you typically find a handful of entries per requester, unranked among themselves, where being roughly right about which handful is the entire requirement. The gap between the stated problem and the delivered one is often several orders of magnitude of work, and it is invisible unless someone writes down the weak form explicitly and compares.

Three independent weakenings usually apply at once, and each unlocks different methods. You rarely need every cell, only a few per row — which converts an exhaustive computation into a per-requester search. You rarely need the values, only the identities of the leaders — which lets any monotone proxy for the value stand in, and removes calibration from the problem entirely. And you rarely need all of the leaders, only most of them — which admits sampling, pruning, and approximate neighbour search, all of which are wrong by construction on the strong form and perfectly adequate on the weak one. Committing to the strong form first forecloses all three, and no amount of later optimisation recovers them, because they are not optimisations; they are different problems.

The discipline is to write the acceptance condition before the method, in terms of what a user or downstream stage can observe. If nobody can tell the difference between the exact answer and one that omits a fifth of the top candidates, then the specification does not include those candidates, and any effort spent guaranteeing them is spent for nothing. Writing this down also has a second effect worth as much as the first: it forces the question of what happens when the output is wrong, which is how you find out whether you are building something where approximation is free or something where it is unacceptable.

The failure to watch for is a specification inherited from how a result is scored rather than from how it is used. Evaluation frameworks reward accuracy uniformly over all cells because that is easy to measure; deployment cares only about the top few. Optimising the measurable thing produces a system that is excellent at predicting the entries nobody will ever be shown.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the model section of the recommendation-systems chapter, which states that filling in every unknown entry is unnecessary, that it suffices to find some entries in each row likely to be high, and that it may not even be necessary to find all of the highest-valued ones but only a large subset of them.
