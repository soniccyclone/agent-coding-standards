---
type: lesson
title: "Choose your simplifications to isolate the claim you intend to prove"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Choose your simplifications to isolate the claim you intend to prove

**Lesson:** Before analysing an allocation problem with heterogeneous prices, heterogeneous budgets, heterogeneous response rates and multiple slots per request, the authors flatten all four: one slot, equal budgets, equal response rates, all prices zero or one. What makes this worth studying is the sentence attached to it. The stated purpose of the simplification is to eventually show that a particular alternative beats the obvious approach. The assumptions were not selected because they made the algebra tractable, and not because they were realistic. They were selected because each of them is a dimension along which the two candidate procedures could differ for reasons unrelated to the claim, and stripping them leaves exactly one thing varying.

That is a different discipline from the usual reflex, which is to simplify whatever is annoying and hope the result survives. Simplifying for tractability produces a model whose relationship to the real question is unknown, and the failure mode is that the effect you demonstrate turns out to be an artifact of one of the things you removed. Simplifying to isolate a claim gives you a model where the demonstrated effect is attributable, because everything that could have caused it instead has been held constant. It also tells you what to do next, which is to restore the stripped dimensions one at a time and watch which restorations break the result.

That restoration schedule is the other half of the method, and the chapter runs it explicitly: the price dimension comes back first and destroys the guarantee outright, forcing a repaired rule; the response rate comes back next and folds into the same rule as a multiplier; the slot count and the query-frequency information come back last as practical adjustments. Each restoration is a small, checkable step with a known baseline, and any one of them that changes the conclusion identifies precisely which real-world feature the simple result depended on. Compare this to attempting the full problem at once, where a negative result tells you nothing about which of the four complications was responsible.

Applied outside analysis, this is how to design a benchmark, an ablation, or an experiment: enumerate the dimensions on which the alternatives could differ, hold constant everything that is not the hypothesis, and then unfreeze them one at a time in an order you chose in advance. The report of the simplified result should carry the purpose sentence too, because a reader who knows why a dimension was frozen can judge whether freezing it was legitimate, while a reader given only the list of assumptions cannot.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 8's four simplifying assumptions for the adwords problem, introduced with the explicit statement that their purpose is to show there is a better algorithm than the obvious greedy one, and the later sections that reintroduce arbitrary bids and budgets, then per-query click-through rates, then historical query frequency.
