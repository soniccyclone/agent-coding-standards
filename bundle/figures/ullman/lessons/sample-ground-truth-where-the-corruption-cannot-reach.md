---
type: lesson
title: "Sample ground truth from the range the corruption cannot reach"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Sample ground truth from the range the corruption cannot reach

**Lesson:** When a signal is known to be manipulated, the reflex is to stop using it for anything, especially for choosing which items a human will examine. That reflex throws away a usable fact. Manipulation is rarely uniform across the range of a signal: it usually has a bounded budget, and a bound on how far an item can be pushed implies a region of the signal that manipulation cannot enter. If an adversary can move an item from the bottom of a distribution to the middle but not to the top, then the top of that distribution is uncorrupted, and it is a perfectly sound frame from which to draw the labelled examples everything else will be calibrated against.

This is worth spelling out because a good labelled seed set is usually the scarce resource, and the obvious sources for one are bad. Random sampling of a heavy-tailed population spends nearly all its human attention on items that matter to nobody. Sampling by a proxy that correlates with importance reintroduces whatever bias the proxy has. Using the compromised signal itself feels circular. But the circularity is only real if the corruption reaches the region you sample from, and that is a quantitative question with a quantitative answer: work out the amplification an attacker obtains as a function of their effort and your parameters, compare it against the gap between the ranks in question, and you learn which slice of the distribution is out of reach. The answer might be "none of it", which is also worth knowing, but frequently a bounded multiplier against a distribution spanning orders of magnitude leaves a clean top.

The reasoning composes with the more familiar rule that expensive human judgement should go where uncertainty is highest. These pull in opposite directions and both are right in their own regime. When you are refining a decision boundary, spend the oracle on the ambiguous cases. When you are establishing an anchor that other scores will be defined relative to, spend it where you are most confident the input is honest, because an anchor contaminated by even a few adversarial entries propagates that contamination into everything computed from it. Choosing between the two comes down to asking whether the labels are being used to draw a line or to define a reference point.

Two conditions keep this from being a trick that quietly stops working. The bound on manipulation must be derived from something structural, not from observed attacker behaviour, since observed behaviour is what changes when your defence deploys. And the bound is a function of your own tuning parameters, which means the safe region moves when you retune; a parameter change made for unrelated reasons can silently shrink the clean range that a seed set was drawn from years earlier. Both conditions argue for writing the amplification calculation down next to the sampling procedure rather than treating the seed set as a fixed asset.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 5's discussion of building a TrustRank teleport set, specifically the proposal to have humans examine the highest-PageRank pages on the theory that link spam can lift a page from the bottom to the middle of the pack but essentially cannot place one near the top, read alongside the same chapter's calculation of the amplification a spam farm obtains as a function of the taxation parameter.
