---
type: lesson
title: "Hold a signal out of the score so it can tell you what the score means"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Hold a signal out of the score so it can tell you what the score means

**Lesson:** Hand-built scoring rules — points for agreement, deductions for discrepancy, penalties shaped by judgement — are unavoidable in messy matching work, and they arrive with no interpretation. Nobody knows what a score of 115 means, and there is usually no labelled ground truth to calibrate against, because if there were you would not be doing the matching. The move that dissolves this is to deliberately keep one observable *out* of the score, chosen because you expect it to behave differently for correct and incorrect matches. Measure its average behaviour among the highest-scoring pairs, which you are prepared to treat as certainly correct. Measure its average behaviour among arbitrary pairs, which you know are almost all wrong. Any intermediate score's population sits between those two poles, and the position of its average tells you what fraction of that population is genuine — a linear interpolation, no model, no training data.

The reason this works is that a quantity excluded from the scoring is not contaminated by it, so its distribution carries independent evidence about correctness. The reason it is easy to miss is that the instinct with any predictive-looking signal is to fold it into the score and improve the score. Resisting that instinct converts an uninterpretable ranking into calibrated probabilities, which is worth much more than the small accuracy the extra feature would have added. It also gives you something to argue with: a claim that pairs scoring above some cutoff are essentially all real matches becomes a measurement rather than an assertion, which is what you need when the output has to survive scrutiny by someone with an interest in disputing it.

The practical habit is to plan the held-out signal before building the scorer, and to pick it for independence rather than strength — a timestamp, a physical attribute, a provenance field, anything whose behaviour you can characterise at the extremes. It pairs naturally with a related discipline in the same setting: recall is deliberately sacrificed by only ever scoring pairs that agree exactly on at least one field, and that sacrifice is justified not by arithmetic but by the observation that a pair agreeing on nothing exactly would not have persuaded anyone anyway. Both moves come from the same stance, which is to ask what the number will be used to justify, and to design backwards from the justification.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the entity-resolution case study in the similarity chapter, where two companies' customer records are matched by a points-and-deductions score and the fraction of true matches at each score is recovered from record creation-date gaps, a field kept out of the scoring on purpose.
