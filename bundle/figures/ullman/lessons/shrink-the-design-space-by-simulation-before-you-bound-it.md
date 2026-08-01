---
type: lesson
title: "Shrink the space of designs by simulation before you try to bound it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Shrink the space of designs by simulation before you try to bound it

**Lesson:** Arguing about all possible implementations of something is hopeless until you cut the space down, and the cut that works is not "let us consider only the sensible ones" — that is an assumption smuggled in as taste. The legitimate cut is a simulation argument: show that any design with some extra freedom can be replaced by one without it, at no worse cost, because the freedom can be exercised somewhere else in the pipeline. Once that replacement is exhibited, the restricted class is not a subset you chose to study, it is provably as good as the whole, and everything you prove about it applies universally.

Two moves recur. The first is relocation: a stage that transforms data before handing it on can always be replaced by a stage that forwards the raw item and a downstream stage that does the transform, so you may assume without loss that nothing is transformed in transit and count raw items only. That single normalisation makes an accounting of data movement well defined, where otherwise every candidate could claim its intermediate encoding was smaller. The second is dominance: if a partial delivery is useless for producing any result, then a design that makes partial deliveries is dominated by one that does not, so you may assume every delivery is a whole unit. Both are arguments, not conventions, and the difference matters — the restricted class inherits the theorem only because the replacement was shown.

Two further tightenings usually follow, and both are worth reaching for by habit. Symmetry: if the cost is invariant under exchanging two dimensions, the extremum sits where they are equal, which collapses a two-parameter search to one. And canonicalisation of the *encoding* rather than the algorithm: fix a single representative form for anything that has multiple equivalent spellings, so no design can win the comparison by being described more cleverly. The payoff of all this is that the eventual counting argument becomes short enough to check. When a lower-bound proof is long and full of cases, the usual diagnosis is that the space was never normalised, and the effort belongs at the front rather than in the middle.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the complexity-theory chapter's development of mapping schemas, which observes that no more than one message per related input-output pair is ever needed because any transformation applied on the sending side could be applied on the receiving side instead; and the matrix-multiplication lower bound, which first argues that partial rows and partial columns are useless so whole ones may be assumed, then that coverage is maximised when their counts are equal.
