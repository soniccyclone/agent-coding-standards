---
type: lesson
title: "A measurement set is consumed the first time you act on it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# A measurement set is consumed the first time you act on it

**Lesson:** Anything fitted to data will do better on that data than on data it has not seen, because part of what it captured is peculiar to the sample rather than to the population. So performance measured on the fitting data is not an estimate of anything useful, and everyone knows to hold some data back. The part that gets lost is that held-back data is a consumable. The moment you look at how the artefact scores on it and change the artefact in response — restrict it, tune it, pick a different one — that data has entered the fitting process, and its score has become the same kind of optimistic number you were trying to avoid. Nothing about the data changed; its role did.

That is why the discipline needs two distinct reserves with two distinct jobs, not one reserve used twice. One is for shaping: you may look at it as often as you like, and each look spends a little of its credibility, which is fine because credibility is not what it is for — it is for telling you the direction to move. The other is for measurement, and it may be consulted once, at the end, after every decision has been made. Reusing the measurement reserve for a second round of tuning is not a minor lapse; it converts your one honest number into another optimistic one, and there is no way to detect this afterwards from the number itself.

The diagnostic that matters is not the absolute score but the gap between performance on the fitting data and on the unseen data. A small gap means the artefact captured structure that generalises. A large gap means it captured the sample, and the correct response is to constrain it — fewer parameters, shallower structure, coarser granularity — rather than to keep searching for a variant that happens to score better on the reserve, which is just fitting to the reserve more slowly.

When data is too scarce to give up a large reserve, rotating the roles recovers most of the benefit: partition into equal parts, hold each out in turn while fitting on the rest, and aggregate. That reuses every observation for both jobs without any single fit ever seeing its own evaluation data. The general habit is worth stating plainly, because it applies well beyond model fitting — to benchmark suites, to canary populations, to any held-out evidence: evidence used to decide is no longer evidence to report, and a measurement kept honest requires knowing exactly how many times it has been looked at.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the machine-learning architecture section of the large-scale-machine-learning chapter, which distinguishes a validation set used to help design the model from a test set used only to determine how good it is, describes overfitting as picking up artifacts atypical of the wider population, prescribes comparing the error rate on held-out data against the error rate on the training data, and describes rotating the held-out chunk as cross-validation.
