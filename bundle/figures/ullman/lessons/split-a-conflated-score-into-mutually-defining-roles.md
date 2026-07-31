---
type: lesson
title: "When one score conflates two kinds of value, define them by mutual reference"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# When one score conflates two kinds of value, define them by mutual reference

**Lesson:** A single ranking number forces every participant onto one line, and that is a modelling commitment, not a neutral summary. It is wrong whenever the population contains items that are valuable in genuinely different ways — one because it answers the question, another because it reliably tells you where the answers are. Collapsing those into one number means the two kinds trade off against each other for no reason, and the collapse is invisible in the output, because a single number always looks like it means something. The remedy is to notice the distinction up front and give each kind its own score.

The interesting part is how the two scores get defined, because defining each independently just gives you two unrelated heuristics. Instead, define each in terms of the other: a good pointer is one that points at good answers, and a good answer is one that good pointers point at. Neither definition stands alone and neither is circular in the harmful sense, because the pair has a computable joint solution reached by alternating between them. This is the same trick as a single self-referential score, applied across two populations instead of within one, and it buys the same thing — the quality standard is defined by the structure rather than imposed from outside, so it needs no curated list to bootstrap and no manual upkeep as the population changes.

There is a practical dividend that is easy to miss. Because the two quantities are recomputed from each other and renormalised at every step rather than conserving a fixed total, the pathologies that plague a single conserved score simply do not arise: an item that points nowhere gets a pointer-score of zero and that is the correct answer rather than a divergence, and a closed clump cannot hoard anything because nothing is being distributed. Choosing the right formulation can dissolve whole categories of correction machinery you would otherwise have to build, which is worth more than the correction machinery being clever.

Generalised: whenever you catch yourself ranking heterogeneous things on one axis, ask whether the population actually contains two roles that serve each other. Index versus content, producer versus consumer, generator versus validator, curator versus creator — all of these are pairs where each side's quality is best evidenced by its relationship to good instances of the other. If the pair exists, two mutually defined scores are more honest and often cheaper than one blended score plus a pile of heuristics to un-blend it later.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the hubs-and-authorities section of the link-analysis chapter, which contrasts the one-dimensional importance model with a pair of mutually recursive scores, and observes that the alternating scaled iteration converges without needing the corrections that dead ends and closed clumps force on the single-score computation.
