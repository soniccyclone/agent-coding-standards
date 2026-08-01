---
type: lesson
title: "Start the search from the point where the trivial answer already holds"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Start the search from the point where the trivial answer already holds

**Lesson:** Iterative fitting procedures need somewhere to begin, and the starting point is usually treated as arbitrary: zeros, ones, small random values, whatever the library defaults to. It is not arbitrary if you have a trivial predictor lying around, because you can choose the initial parameters to be exactly the ones that reproduce it. Solve the small algebra problem of which constant value, spread over your parameters, makes the model output the overall mean of the observed data, and start there. From that moment the search has a floor: every subsequent step is measured against a baseline you already understood, and any run that ends worse than where it began is unambiguously a bug rather than a bad draw.

The second thing this buys is a sanity check on your representation. If the initialisation that expresses the trivial predictor turns out to be inexpressible, or requires strange values, that is early evidence the parameterisation is awkward. Conversely the check often reveals that a preprocessing step has already done the job: when the data has been centred so that the mean of the observations is zero, the initialisation that reproduces the mean is simply all zeros, and the two conventions agree. Two independent lines of reasoning arriving at the same starting point is worth noticing, because it means the transform and the initialisation share a common description of what "no information yet" looks like.

Then perturb outward from there rather than sampling from nowhere. Diversity in the starting points is needed anyway to escape local optima, but diversity around a known-good centre is different in kind from diversity across an arbitrary region: the spread is a deliberate knob, you can reason about how far a run has wandered from baseline, and a distribution of outcomes is interpretable as improvement over a fixed reference. The general habit is that any procedure whose answer must beat a simple alternative should be constructed so it starts holding that alternative in its hand, instead of being asked to rediscover it.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 9's initialization discussion in the section on building a complete UV-decomposition algorithm, which recommends giving every element of the two factor matrices the value whose product equals the average of the non-blank entries of the utility matrix, notes that this value is necessarily zero once the matrix has been normalized, and then perturbs each element randomly to obtain many starting points.
