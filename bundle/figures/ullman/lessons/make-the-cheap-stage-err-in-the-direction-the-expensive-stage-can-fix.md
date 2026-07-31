---
type: lesson
title: "Make the cheap stage err in the direction the expensive stage can repair"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Make the cheap stage err in the direction the expensive stage can repair

**Lesson:** In a two-stage design where an approximate pass nominates candidates and an exact pass checks them, the two kinds of error are not symmetric and never can be. A wrongly nominated candidate is examined and discarded, so the exact pass removes it at no cost to correctness. A candidate that was never nominated is never examined, so no amount of exactness downstream recovers it — the verification stage only ever ranges over what the nomination stage handed it. This asymmetry is structural, not incidental, and it should determine how the cheap stage is tuned before any accuracy target is chosen.

The consequence is that the approximate stage should be deliberately mis-tuned, biased to over-nominate. Set its acceptance criterion looser than the arithmetic would suggest — noticeably looser, not marginally — because every extra candidate costs only some work in the verification pass, while every missed one costs a wrong answer that nothing downstream can detect. The price is paid in the resource the verification stage consumes, so the correct tuning is the loosest setting whose candidate volume the exact pass can still afford. That converts a question about statistical thresholds, which is hard, into a question about capacity, which is easy, and it is worth noticing that the two-stage structure is what makes the substitution legitimate.

Framing this generally: in any pipeline, identify which errors are recoverable downstream and which are absorbing, and push all the tolerance onto the recoverable side. Over-fetching and then filtering is safe; under-fetching is not. Warning on more conditions than necessary and then triaging is safe; failing to warn is not. Retrying more than needed is safe if the operation is idempotent; giving up early is not. The pattern is not "be conservative" — it is "be sloppy in exactly the direction someone else cleans up," which requires knowing who cleans up and what their budget is.

The failure mode this guards against is subtle and common: a team tunes the fast stage for its own accuracy, evaluated in isolation, treating both error types as equally bad because that is what a standard metric does. The stage then looks well-calibrated on its own and silently caps the accuracy of the whole system, and the cap is invisible because the pipeline's output contains no trace of what was never nominated.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the sampling sections of the frequent-itemsets chapter, which observe that a full verification pass eliminates every false positive from a sample-derived candidate set but leaves false negatives undiscovered, and therefore recommend running the sample with a threshold set below its proportional value so that fewer true results are missed.
