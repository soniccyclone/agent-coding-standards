---
type: lesson
title: "An ignored factor with no bound destroys a guarantee rather than degrading it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# An ignored factor with no bound destroys a guarantee rather than degrading it

**Lesson:** Every decision rule simplifies by dropping inputs, and the usual intuition is that dropping an input costs you proportionally — a rule that ignores something mildly relevant should be mildly worse. That intuition holds only when the ignored quantity has a bounded range. If the ignored quantity can vary without limit, the loss is not proportional and not bounded: an adversary, or merely an unlucky configuration, can make the rule arbitrarily bad, and the guarantee you proved for the simplified setting collapses to nothing rather than shrinking a little. The rule does not become 20 percent worse. It becomes worthless, while still looking reasonable in every example you tried.

The mechanism is easy to see once stated. A rule that orders candidates by some secondary attribute will, whenever that attribute happens to point away from the primary one, choose the candidate whose value is lower — and if value is unbounded, the ratio between the value forgone and the value obtained is unbounded too. Repeating that choice a few times produces a total that is any fraction of optimal you care to name. This is precisely why proofs done under a simplifying assumption must be reread with the assumption removed rather than assumed to survive it: the assumption in the toy version was often the very thing supplying the bound.

The practical procedure is to enumerate the quantities your rule does not look at and ask, for each one, whether its range is bounded by the problem or merely by the instances you have seen. Bounded ones are safe to fold into a constant. Unbounded ones must appear in the rule, even crudely, and the usual repair is to multiply rather than to add — form the decision score as the product of the value at stake and a factor derived from the attribute you were tracking, so that an enormous disparity in either dimension can dominate and neither can be silently ignored. That single change is often what converts a rule with no guarantee at all into one with a good guarantee.

Beyond algorithms, this is the recurring reason that heuristics validated on the traffic you have fail catastrophically on traffic you have not: schedulers that ignore job size, caches that ignore item cost, retry policies that ignore downstream expense. The question to ask of any simplification is not "does this input usually matter" but "is there any limit on how much it could matter."

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the advertising chapter's generalisation of the Balance algorithm, with the two-bidder example where preferring the larger remaining budget while ignoring the bid amounts yields no positive guaranteed fraction at all, and the repair that multiplies the bid by a function of the fraction of budget remaining.
