---
type: lesson
title: "Rank by what you will actually collect, not by what was promised"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Rank by what you will actually collect, not by what was promised

**Lesson:** When candidates compete for a slot by stating what they will pay, the stated figure looks like the natural ordering key and is not. It is a conditional promise, payable only if an event occurs that the candidate does not control. Ordering by it ranks candidates by the size of a claim rather than by the value of an outcome, and the two come apart badly whenever the probability of the conditioning event varies across candidates. The correct key is the product of the promise and the observed rate at which the condition has been met historically, which is the only quantity denominated in what the ranking party actually receives.

The change is arithmetically trivial and has a large second-order effect on behaviour, which is the real reason to make it. Under the naive ranking, a candidate can capture slots by promising a lot on requests they are irrelevant to, and pays nothing when the irrelevance shows up as a non-event, so the strategy is free. Under the corrected ranking, that same irrelevance is measured, folded into the score, and quietly demotes them. No rule against irrelevant bidding has to be written or enforced, and no one has to adjudicate what counts as relevant. The candidate's own record does it, and the record is produced by the audience rather than by the candidate.

What makes this work is the split in who controls each factor. The promise is authored by the party being ranked and is therefore worth nothing as evidence on its own. The realisation rate is authored by third parties with no stake in that candidate's ranking. Multiplying them yields a score that a candidate can raise only by paying more or by actually being wanted, and the second route is the one you were trying to reward. Look for this split whenever a score combines a declared quantity with an observed one, and check that the observed factor is the one carrying the discriminating power.

The pattern recurs anywhere self-reported intent meets measurable follow-through: quoted deadlines against historical delivery, claimed capacity against observed throughput, declared priority against how often the declarer actually acts. Multiplying the claim by its historical realisation rate converts a field anyone can inflate into an estimate that costs something to move, and it does so without adding a policy, a reviewer, or an appeal process.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 8's account of how the Adwords system went beyond the earlier bid-ordered system by ordering ads not by the amount of the bid but by the expected receipts, taking the value of an ad to be the product of the bid and the observed click-through rate, and the later folding of a per-query click-through factor into the Balance score.
