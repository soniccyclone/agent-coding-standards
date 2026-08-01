---
type: lesson
title: "A weighted score cannot express a veto"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# A weighted score cannot express a veto

**Lesson:** Combining many signals into one number by weighted addition is the default architecture for any ranking or decision system, and it has a specific expressive limit that gets discovered the embarrassing way. An additive score cannot say "regardless of everything else, not this one." It can only say "this counts against you a lot", and a large enough sum of other terms always overwhelms a finite penalty. So a system built entirely out of weights will, somewhere in its input distribution, produce an output that is absurd on a criterion everyone agrees is non-negotiable, and the response will be to raise that term's weight, which fixes the observed case and leaves the structure unchanged.

The fix is not a bigger weight but a different kind of construct: a predicate evaluated before scoring that determines eligibility, with the score ranking only among the survivors. This is a genuinely different thing and it is worth being explicit that you are introducing a second mechanism. The gate is a boolean with no tuning surface, it is auditable in isolation, its behaviour does not drift when someone retunes an unrelated weight, and it makes the non-negotiable requirement legible as a requirement rather than as a large constant buried among two hundred others. Systems that have both usually have very few gates and very many weights, and that ratio is correct: the gate is expensive in expressiveness, so it should be spent only where the constraint is genuinely absolute.

Which constraints deserve one is the actual design question, and it is answered by asking what a violation costs rather than how often it occurs. A candidate that fails the gate is not merely a poor result; it is a result that damages trust in every other result, because it demonstrates the system does not understand what it is for. Relevance to the request, authorisation to view the item, legal admissibility, physical feasibility: these are not strong preferences. They are conditions on the output being an answer at all. Everything else — quality, freshness, popularity, cost — is genuinely a matter of degree and belongs in the sum, where it can be traded off, which is what a sum is for.

There is a hybrid worth recognising because it is the most common state of affairs and the most confusing to reason about. A weight set high enough that in practice nothing without the property ever surfaces behaves like a gate on all observed traffic while remaining a weight in the code. That is a real engineering choice with a real advantage: it degrades gracefully when the gate would return nothing at all. But its guarantee is empirical, valid for the input distribution you have measured, and it will be violated the first time an item accumulates unusual mass elsewhere. If you rely on that arrangement, you have not built a guarantee, you have built a very likely outcome, and the distinction should be recorded where the next person tuning weights will find it.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 5's account of how PageRank is used inside a search engine, which states that a page must contain at least one query term to be considered for ranking at all, that the weighting among the roughly two hundred and fifty page properties is arranged so that a page missing some of the terms has very little chance of reaching the top results, and that PageRank is only one component of the score computed among the qualified pages.
