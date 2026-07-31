---
type: lesson
title: "Find the closure property that turns exhaustive search into frontier expansion"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Find the closure property that turns exhaustive search into frontier expansion

**Lesson:** Before writing any search over a combinatorial space, look for a monotonicity relation between the property you are testing and the ordering on the space. The question to ask is whether the property, holding of some object, forces it to hold of every simpler object below it. When it does — and it does far more often than people check — the entire structure of the search changes. You never have to consider an object whose simplifications have already failed the test, because failure below is a proof of failure above. What was an enumeration of an exponentially large space becomes a level-by-level expansion of a frontier, where each level's candidates are generated only from the previous level's survivors, and the expansion terminates on its own when a level comes back empty.

The property is not a footnote to the algorithm; it is the algorithm. Everything else — how you count, how you store, how many passes you make — is engineering that only pays off because the frontier stays small. This is why the check is worth doing first: if no such relation exists for your predicate, you have learned that the level-wise family of techniques is unavailable and you should be looking at sampling or approximation instead, which is a much better thing to know at the design stage than after building a pruner that prunes nothing. And if the relation exists but only approximately, that is also worth knowing precisely, because a nearly-monotone predicate can often be replaced by a monotone relaxation that over-generates candidates you then filter, which preserves the structure at a bounded cost.

The same relation pays a second time in how you report results. A family closed downward is fully described by its maximal elements: list only those, and everything else in the family is recoverable by taking subsets, while anything not below a listed element is known to be absent. That turns an output too large to read into an output whose size is the width of the frontier, with no information lost. This is the correct compression for any downward-closed answer set — supported configurations, satisfied constraints, granted capabilities — and it is available for free once you have identified the closure direction.

The habit generalises to any predicate over a partial order, not just subsets: substrings, subgraphs, prefixes, refinement of specifications, weakening of preconditions. Ask which direction your predicate is preserved in, prove it in one line if you can, and let that single fact dictate the search order. A property nobody checked for is the most common reason a combinatorial search gets written as brute force.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the monotonicity section of the frequent-itemsets chapter, which observes that every subset of a frequent set is frequent, uses that to define maximal itemsets as a compact summary of all frequent ones, and structures the level-wise algorithm as alternating construction of candidates from surviving smaller sets with filtering by an actual count.
