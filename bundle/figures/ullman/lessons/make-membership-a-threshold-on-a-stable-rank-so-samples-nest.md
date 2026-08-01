---
type: lesson
title: "Make membership a threshold on a stable rank so your samples nest"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [databases-and-data-management, distributed-systems-and-concurrency]
tags: [lesson]
---
# Make membership a threshold on a stable rank so your samples nest

**Lesson:** A selection rule that flips a coin per candidate and a selection rule that assigns every candidate a fixed pseudo-random rank and admits everything below a threshold produce samples with the same statistics, and they are not interchangeable. The threshold form has three properties the coin form lacks, all of which matter as soon as the selection has to survive time. The decision for any candidate is recomputable from the candidate alone, so nothing has to be remembered about who was admitted. The decision is stable across processes and machines, so independently built components agree about membership without coordinating. And the samples at different thresholds are nested, so tightening the threshold only ever removes members and never reconsiders the ones that remain.

Nesting is the property worth designing for. When the budget shrinks — storage pressure, cost limits, a retention change — you lower the threshold and discard the members above it. Nobody re-runs a selection, nothing that was in comes back later, and the smaller sample is literally a subset of the larger one, which means measurements taken before and after the change remain comparable and any trend across the boundary is real rather than an artifact of resampling. A coin-flip scheme gives none of this: shrinking it requires either a fresh draw, which breaks continuity with everything measured previously, or a stored record of past decisions, which is the state you were trying not to keep.

The general move is to replace a decision with a total order plus a cut point. Once every item has a stable position on a line, every budget is a prefix, budget changes are parameter changes, and the awkward operations become arithmetic — you can shrink continuously, shed the largest ranks first, and even index by rank so the eviction is a range scan rather than a search. It is worth noting what the rank must be a function of, since that is the whole design decision: it should depend only on the key you are sampling over and nothing else, because dependence on anything mutable turns membership into something that can change under you and destroys both stability and nesting.

The costs should be stated rather than discovered. The assignment is fixed forever, so an unlucky key stays out permanently, and there is no independence between runs to average away — repeating the experiment does not resample. Anyone who knows the function can predict who is in, which is a problem when membership is adversarially interesting. And the effective fraction depends on the rank function distributing keys evenly, so a poor one produces a sample that is biased in a way no amount of data reveals. Each of these is acceptable in most settings and disqualifying in a few, which is exactly why it should be a decision.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 4's sampling sections, which select a fraction of key values by hashing the key and comparing against a bucket boundary rather than storing per-key in/out decisions, and then handle a growing sample under a fixed storage budget by lowering a threshold on the hash value and dropping the keys that hash above it.
