---
type: lesson
title: "For coverage, greedily maximize the minimum — not the total"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# For coverage, greedily maximize the minimum — not the total

**Lesson:** When you need a small set of items that between them represent a large population, the objective people reach for first is the wrong one. Maximising total or average separation among the chosen items lets a few extreme picks dominate the score while whole regions of the population go unrepresented — the sum is happy, the coverage is terrible. The objective that produces coverage is the minimum: at each step choose the item whose distance to the nearest already-chosen item is as large as possible. That rule cannot leave a region unrepresented while an alternative was available, because an unrepresented region is precisely a place where some item's nearest chosen neighbour is far away, which is what the rule goes looking for.

This is worth holding as a general distinction between two families of objective. Sum-like objectives reward concentration, because a large contribution anywhere compensates for a zero elsewhere. Min-like objectives reward uniformity, because the score is hostage to the worst case. Which one you want is decided by whether a gap is tolerable. If you are choosing representatives, seeds, test inputs, monitoring probes, or sample points, a gap is a blind spot and the min-like objective is correct. If you are choosing where to spend a budget for aggregate return, the sum-like one is. Getting these backwards produces systems that look well optimised and have holes.

The greedy version deserves respect rather than apology. It is not a placeholder for something better: one pass, each step a scan for the item farthest from everything picked so far, and the outcome is reliably spread across the population even from a poor starting choice — starting from a point in the middle of everything still ends up with representatives in each distinct region, because the first pick's very centrality makes the extremes maximally attractive next. That robustness to initialisation is unusual and is the reason the rule is worth preferring to sampling, which can miss a small region entirely.

Its weakness is the mirror of its strength and should be stated: because it chases the farthest thing, it is attracted to genuine outliers, and a lone anomalous item will be selected early and given the standing of a representative. If your population has outliers you do not want promoted, the rule needs a guard — exclude items with too few neighbours, or run it on a lightly trimmed population. That is a small amendment, but it has to be made deliberately, because the failure it prevents looks like the algorithm working correctly.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the initialization section of the clustering chapter, which picks the first representative at random and thereafter repeatedly adds the point whose minimum distance to the already-selected points is largest, and shows that even starting from a central point the selected representatives land in different natural groups.
