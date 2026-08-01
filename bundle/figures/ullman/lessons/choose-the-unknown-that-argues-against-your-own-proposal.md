---
type: lesson
title: "Choose the unknown that argues against your own proposal"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Choose the unknown that argues against your own proposal

**Lesson:** Most comparisons between two designs bottom out in a quantity nobody knows. How many rows the intermediate result will have, how often the cache will hit, what fraction of requests are duplicates — the analysis is otherwise arithmetic, and the conclusion is set by whatever number gets substituted for the unknown. This is the point at which quantitative argument usually stops being quantitative, because the person doing the substituting already has a preferred answer, and any value they pick will be defensible within a range wide enough to contain the crossover. The remedy is procedural and easy: when you must guess, guess the value that makes your own preferred design look worst, and see whether it still wins.

A worked instance makes the shape clear. Comparing a one-shot multiway join against a cascade of pairwise joins turns entirely on the size of the intermediate result, which cannot be computed because it depends on the clustering structure of a social graph. The upper end of the plausible range is the fan-out squared; the estimate actually used is a tenth of that, described as conservative — and it is conservative precisely because a *smaller* intermediate result makes the cascade cheaper, which is the option being argued against. The conclusion that survives is therefore stronger than the one that would have followed from a favourable guess, and it comes with a stated direction of error: if the true value is larger, the case only improves.

Two disciplines follow. First, say which way the guess leans and why, because the reader cannot check an estimate but can check its direction. An estimate offered without that annotation is indistinguishable from motivated reasoning even when it is not. Second, when the adversarial guess flips the conclusion, that is the finding, not an inconvenience — you have learned that the answer depends on a number you do not have, and the right next move is to go measure it rather than to keep arguing. The general habit is to treat every unknown in a comparison as an adversary's choice, exactly as you would when reasoning about worst-case behaviour, with the difference that here the adversary is your own preference and it is much harder to notice.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 2's worked comparison of the three-way join against two cascaded two-way joins on a social-network friends relation, where the size of the self-join cannot be determined because friendship falls into cliques and the estimate deliberately taken is a tenth of the naive maximum, described as conservative, before deriving the number of reducers below which the multiway join still wins.
