---
type: lesson
title: "Run the same computation under two assumptions and treat the gap as the measurement"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Run the same computation under two assumptions and treat the gap as the measurement

**Lesson:** Some quantities you badly want to measure have no direct definition — there is no field to read, no observation that reports them, and any attempt to characterise them from first principles turns into a description of surface features that will not survive contact with reality. A general escape is available whenever you have a computation whose assumptions you can vary: run it twice under two different assumptions and use the difference between the results as the quantity. The difference is meaningful precisely because everything else is held identical, so whatever changed is attributable to the assumption alone. You have converted an unmeasurable property into an ablation.

What makes this more than a trick is that the resulting number is naturally normalised and naturally interpretable. Expressing the difference as a fraction of one of the two results gives a scale-free score: near zero means the assumption made no difference to this item, near one means the item's entire value came from the assumption being relaxed. That gives you a threshold you can actually reason about rather than a raw delta you have to calibrate against nothing. It also means the score self-reports its own confidence at the extremes and honestly refuses to discriminate in the middle, which is better behaviour than a classifier that always produces a label.

The technique's dependencies are worth stating because they are where it fails. The two runs must differ in exactly one assumption; if the second run also uses a different dataset, a different convergence criterion, or a different normalisation, the difference measures a mixture and means nothing. And the assumption you vary has to be one you can justify independently, because the score inherits all of its authority from that justification — a difference against an arbitrary alternative is an arbitrary number. The corollary is that the effort should go into defending the second assumption, not into tuning the threshold on the difference.

Once you see the shape, it generalises past any one domain: the contribution of a feature is the loss with and without it, the value of a cache is the latency with and without it, the effect of an optimisation is the profile with and without it, and the dependence of an answer on a questionable input is the answer computed with and without that input trusted. In each case the thing being measured has no independent existence — it only exists as a difference — and trying to define it any other way is what makes the problem seem hard.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the spam-mass section of the link-analysis chapter, which defines a page's suspect fraction as the normalised difference between its score under a uniform restart distribution and its score under a restart distribution confined to a trusted set.
