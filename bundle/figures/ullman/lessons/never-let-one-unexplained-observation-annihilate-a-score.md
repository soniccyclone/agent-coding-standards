---
type: lesson
title: "Never let one unexplained observation annihilate a score"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Never let one unexplained observation annihilate a score

**Lesson:** Scores that combine evidence multiplicatively have an annihilator. If any single factor is zero, the whole product is zero, and every candidate hypothesis that fails to account for even one observation scores identically with every other such hypothesis — including hypotheses that are obviously worse in every other respect. This is not a rounding problem; it is a total loss of ordering across exactly the region where most of your candidates live, because in any realistic search the early and intermediate hypotheses all leave something unexplained. The search has nothing to climb, and it will report whatever it started with.

The fix is to floor the annihilating case at a small positive value rather than zero. Doing so restores a total order over hypotheses: one that leaves three observations unexplained now scores strictly worse than one that leaves two, and the search can move between them. Nothing about the modelling assumption has been softened — you still believe such observations are essentially impossible under the hypothesis — but "essentially impossible" and "impossible" behave completely differently under multiplication, and only the first of them is usable inside a search.

It is worth being explicit that the value of the floor is a knob, not a constant, and that it encodes a real preference. The smaller you set it, the more heavily you penalise an unexplained observation relative to everything else, and the more strongly the search is pushed toward hypotheses that account for every last observation even at the cost of contorting the rest of the model. A larger floor tolerates residue and lets the model stay simple. That is a modelling judgement about how much of your data you believe is signal rather than noise, and it deserves to be chosen deliberately and written down, not left as whatever tiny number seemed safe.

The general shape recurs anywhere evidence multiplies or a rule chain conjoins: a single absolute zero, veto, or hard failure collapses a rich comparison into a binary one. Whenever you are building a scoring function you intend to search over, look for its annihilators and ask what the ranking looks like among the many candidates that hit one. If the answer is "they all tie," you have a search that cannot start, and the repair is to replace the absorbing value with a small one whose magnitude you can justify.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the affiliation-graph model in the overlapping-communities section, where a pair of individuals sharing no community is assigned a tiny nonzero edge probability rather than zero, with the explicit reasoning that a zero would prevent any assignment from receiving nonzero likelihood unless every pair shared a community, and that the smallness of the value biases the search toward assignments explaining every observed edge by joint membership.
