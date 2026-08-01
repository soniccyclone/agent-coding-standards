---
type: lesson
title: "The restriction may be in your analysis, not in your construction"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# The restriction may be in your analysis, not in your construction

**Lesson:** When a technique comes with an awkward side condition, the reflex is to treat it as a property of the technique. Often it is a property of the argument used to justify the technique. A derivation done by explicit geometry in two dimensions, choosing convenient round numbers so the probabilities work out to nice fractions, yields a guarantee that only holds when the two regimes of interest are separated by a fixed multiplicative factor and only in the plane. Neither limitation is in the construction. The construction projects points onto a random line and buckets them; nothing about it mentions the number of dimensions or requires the two distances to be far apart. The limitation belongs to what the author could conveniently compute.

Separating the two is a specific and repeatable move: identify which claims your argument actually needs, and check whether a weaker claim would carry the same weight. Here the amplification machinery downstream needs only that the near regime has a higher agreement probability than the far regime. It never uses the values. So a purely qualitative argument — the probability of landing in the same bucket increases as points get closer, whatever the dimension — establishes everything required, and does it for all separations and all dimensions at once. The quantitative version was strictly more work and strictly less general, and it was doing no job that the qualitative version does not do.

This is worth internalising because the failure it prevents is common and expensive. A team reads the side condition as a real constraint, concludes the method is inapplicable to their setting, and either abandons it or builds something more complicated to evade a restriction that was never there. The tell is a condition whose form smells of the proof rather than of the problem: a specific small constant, a low dimension, an assumption of equal sizes, a requirement that some ratio be a power of two. Those are the fingerprints of an argument that wanted to be finishable, not of a mechanism that wanted to be constrained.

The reverse discipline matters as much. Having noticed the restriction is an artifact, say so in the write-up, and say which parts of the guarantee are now unquantified. Trading the explicit constants for generality means the parameters can no longer be computed in advance and must be found by measurement instead. That is usually a good trade, since those parameters were going to be tuned against real data anyway, but it is a trade and it should be visible rather than quietly absorbed.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 3's pair of sections on locality-sensitive families for Euclidean distance: the first derives explicit probabilities for two-dimensional space and a bucket width, yielding a guarantee tied to a fourfold gap between the two distances, and the second calls that result unsatisfying, observes that the probability of sharing a bucket necessarily grows as the distance shrinks, and concludes that a suitable family exists for any pair of distances and any number of dimensions even though its probabilities cannot be calculated.
