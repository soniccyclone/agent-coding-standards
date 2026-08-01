---
type: lesson
title: "Bound the working set with a conservation law, not a cap"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Bound the working set with a conservation law, not a cap

**Lesson:** The usual way to stop a tracking table from growing without limit is to cap its size and evict something when it is full. That works, and it imports two liabilities: the cap is a number nobody can justify, and the eviction policy becomes part of the answer, so results depend on a mechanism that was introduced for memory reasons and has no meaning in the problem. There is a better structure available whenever the quantity you track happens to have a bounded total. If every tracked score is a share of a total that arithmetic pins to some fixed value, then a threshold on the score is automatically a bound on how many scores can exist, and you get a bounded working set with no cap, no eviction policy, and no dependence on arrival order.

The reasoning is worth doing explicitly because it is short and because it is the part people skip. Total mass is bounded; every retained item holds at least the threshold; therefore the count of retained items is at most the total over the threshold. Nothing about the input matters — not its skew, not its rate, not an adversary constructing the worst case — because the bound comes from the conservation property rather than from a behavioural assumption. That robustness is the real prize. A capacity cap holds under all inputs too, but it holds by throwing away information chosen by the policy, whereas here the items that fall out are exactly the ones that failed to meet the stated relevance criterion, which is a fact about the problem and defensible to a user.

One detail in the construction is easy to get wrong and instructive. The threshold has to be set below the contribution a single fresh observation makes, or nothing can ever enter the table: an item arriving for the first time is immediately compared against the admission rule, and a rule that rejects a brand-new item rejects every item forever. An admission rule must, at minimum, admit. The wider principle is that any filter placed on a quantity that accumulates over time must be checked against the value that quantity takes at the very beginning of an item's life, not against its steady state, since the beginning is when the filter is first applied.

Look for the conservation property before reaching for a cap. Scores that are normalised to sum to one, budgets allocated from a fixed pool, tokens in a rate limiter, probabilities, decayed counters whose total converges by construction, shares of a fixed capacity — all have the property, and in each case a relevance threshold silently bounds cardinality. When there is genuinely no such property, that is information too: it tells you the working set is bounded only by policy, and that the policy is now part of your semantics and should be documented as such rather than buried in an eviction routine.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 4's decaying-window scheme for tracking currently popular items, which drops any score falling below one half and argues that since all scores sum to the reciprocal of the decay constant, no more than twice that many items can be held at once, together with its stipulation that the threshold must be below one.
