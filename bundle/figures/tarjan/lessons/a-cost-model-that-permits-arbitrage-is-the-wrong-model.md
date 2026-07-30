---
type: lesson
title: "A cost model that permits arbitrage is the wrong model, and pricing it right prunes the strategy space"
figure: tarjan
works: [amortized-efficiency-of-list-update-and-paging-rules]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# A cost model that permits arbitrage is the wrong model, and pricing it right prunes the strategy space

**Lesson:** Generalizing the analysis to an arbitrary non-decreasing access cost forces a question that a fixed cost function lets you dodge: what should it cost to swap two adjacent elements? Sleator and Tarjan answer it by checking the model for arbitrage rather than by appeal to intuition. If a swap is priced below the difference in access cost between the two positions it spans, then an algorithm can pay to shuffle an element forward, read it cheaply, and shuffle it back for a net saving, obtaining a discount from a round trip that accomplished nothing. That is not a clever algorithm; it is a defect in the pricing, and any conclusion drawn under such a model measures the loophole instead of the work. Set the swap price at exactly that difference and the loophole closes.

The payoff is larger than mere consistency. Once the price is right, a whole class of moves becomes provably pointless: for any strategy that pays for reorderings, there exists an equally cheap strategy that pays for none, so voluntary rearrangement can be dropped from the search space without loss. A correctly priced model does not merely avoid lying about the strategies you compare — it eliminates strategies, shrinking what you have to reason about. The same argument reappears in the paging setting as the standard fact that moving pages before they are demanded cannot reduce faults, which turns out to be an instance of the general pricing result rather than an independent observation about memory hierarchies.

The transferable discipline is to audit any cost model, benchmark, billing scheme, or internal metric for exactly this property before trusting a comparison made under it: is there a sequence of operations that does no useful work yet scores better than doing nothing? If so, the ranking it produces is about the exploit. Two further habits follow from how the paper handles the generalization. It pushes the cost function toward greater arbitrariness until the main result breaks, and the exact structural property where it breaks — convexity, meaning the marginal cost of each step deeper into the structure never increases — is the real content of the theorem, more informative than the original special case. And when a real setting violates that property, as a two-level memory does by making all positions past the cache boundary equally expensive, the right response is to expect a different result there rather than to hope the old one still applies.

**Source:** [Amortized Efficiency of List Update and Paging Rules](../works/amortized-efficiency-of-list-update-and-paging-rules.md) — the generalized-access-cost section, which motivates the exchange price by the round-trip objection, proves that correctly priced voluntary exchanges can always be removed from a strategy, identifies convexity as the boundary of the main bound, and then treats the non-convex paging cost as a separate case for that reason.
