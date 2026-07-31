---
type: lesson
title: "Count your free parameters against your observations, and treat a perfect fit as a warning"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Count your free parameters against your observations, and treat a perfect fit as a warning

**Lesson:** Any procedure that tunes adjustable quantities until it reproduces a set of observations should be understood as spending a budget: the observations are the income and the adjustable quantities are the expenditure. If the quantities are as numerous as the observations, reproduction is guaranteed and carries no information — the fit has memorised rather than explained, and it will say nothing useful about anything it did not memorise. The correct configuration therefore has to be chosen so that the observations comfortably outnumber the adjustable quantities, and the consequence of choosing correctly is that you should *expect not to fit exactly*. A residual disagreement is the sign that the model was forced to generalise. Its absence is the sign that it was not.

Because this is a matter of counting rather than of statistics, it can be checked before any code runs, and it should be, because the failure it prevents is otherwise nearly undetectable. A model with excess capacity produces beautiful numbers on the data you have and mediocre ones in production, and the natural diagnosis of mediocre production numbers — the model needs to be bigger — makes it worse. The tell is the direction of the gap: improving on known data while degrading on new data means capacity, not insufficiency.

Beyond the count, three cheap habits limit the same failure and are worth knowing as a family because they attack it from different sides. Move each adjustable quantity only part of the way toward its locally best value, so that whichever ones happen to be adjusted first do not appropriate structure that belongs to the others. Stop adjusting before improvement has run out, since the last portion of the improvement is almost entirely the fitting of noise. And produce several independent fits and combine their outputs, so that the idiosyncrasies each one absorbed disagree with each other and wash out while the real structure, which all of them found, survives.

The underlying idea generalises past model fitting to anything that adapts itself to observed cases — heuristics tuned on incident history, thresholds calibrated on last quarter's traffic, rules accumulated from bug reports. In each case the question is the same: how many independent observations justified this, and how many independent decisions did I make on the strength of them. When the second number approaches the first, you have built a record of the past rather than a mechanism for the future.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the dimensionality-reduction section of the recommendation-systems chapter, which chooses its running example as the smallest case with more known entries than adjustable ones so that an exact fit should not be expected, and its overfitting discussion prescribing partial adjustment steps, stopping short of convergence, and averaging several independent decompositions.
