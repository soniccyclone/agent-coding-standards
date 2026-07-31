---
type: lesson
title: "Name a technique's decision points so you can search the family"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Name a technique's decision points so you can search the family

**Lesson:** Techniques arrive with names, and a name presents a whole bundle of independent choices as a single indivisible thing. That framing makes the technique easy to discuss and hard to adapt: you can adopt it or reject it, and if the version you tried performed badly the conclusion drawn is that the technique does not suit the problem. Usually the truth is that one of its embedded choices did not suit the problem and the others were fine. The remedy is to open the bundle before adopting it — enumerate the decisions the technique makes, state what each one was set to in the version you were shown, and note which alternatives exist for each.

Doing this converts one option into a space of options with independent axes. For a rule that classifies by looking at similar past cases, the axes are: what counts as similar, how many similar cases to consult, how much each consulted case should count relative to its similarity, and how to combine their answers into one. Four decisions, each with several reasonable settings, most combinations coherent. The textbook presentation fixes all four and calls the result the method; but the choice of similarity is almost entirely about your domain, the number consulted trades stability against responsiveness, and the combination rule depends on the shape of the answer. Nothing ties them together, and tuning them jointly is much more likely to help than swapping the whole technique for a different named one.

The enumeration also improves the conversation about failures. "The method did badly" is not actionable; "consulting only the single nearest case makes it fragile against noise, and consulting more requires deciding how to weight them" is. Each axis becomes a place to look, and the failure gets attributed to a decision rather than to a name. It also exposes the degenerate settings that let some choices disappear — at one extreme the weighting question does not arise, at another the combination rule is forced — which is exactly the kind of structure that tells you where the family's simple corners are.

The habit is worth applying to anything you are about to adopt wholesale: a caching strategy, a retry policy, a consensus protocol, a schema convention. Write down the decisions it embodies. You will usually find that the parts you actually need are two of five, that a third is wrong for you, and that the remaining two were never really part of the technique at all.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the framework section for nearest-neighbour calculations in the large-scale-machine-learning chapter, which enumerates the four decisions required to design such an algorithm — the distance measure, how many neighbours to consult, the kernel function weighting them by distance, and the function combining their labels — and then notes that in the single-neighbour case the weighting question disappears and the combining function has only one sensible choice.
