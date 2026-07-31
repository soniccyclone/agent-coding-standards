---
type: lesson
title: "A uniform probe finds the large groups first"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, cognitive-load]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# A uniform probe finds the large groups first

**Lesson:** When a population is partitioned into groups of wildly differing sizes and you want to find the large ones, the obvious approach is to compute all the groups and sort by size — which is precisely the expensive thing you were hoping to avoid. There is a much cheaper alternative that people overlook because it looks too naive to work: pick a member uniformly at random and determine which group it is in. The chance of landing in any given group is exactly that group's share of the population, so a uniform draw over members is automatically a size-weighted draw over groups. The largest group is the most likely first hit; a group holding a quarter of everything is found on the first try one time in four.

The consequence is a procedure that needs no ranking and no global pass. Sample, resolve the group you landed in, remove it, repeat. Each iteration takes out, in expectation, the largest remaining group, so the population shrinks fastest at the beginning — which is exactly the schedule you want when the goal is to get the remainder below some threshold rather than to enumerate everything. And it degrades gracefully: run it a fixed number of times, or until whatever is left is small enough, and stop. The many tiny groups you never sampled are individually negligible, which is why not finding them costs nothing.

The condition is that sampling must be uniform over members, not over groups. Sampling groups uniformly gives every group the same chance and destroys the whole effect, so any convenience that draws from a deduplicated list, an index of distinct keys, or a set of already-identified categories silently converts the good scheme into the useless one. It is worth being explicit about which population your random draw is over, because these two are easy to confuse and the difference is the entire benefit.

The pattern applies far beyond this setting. Finding hot keys by sampling requests rather than scanning key space, finding the dominant cause by sampling failures rather than enumerating causes, locating heavy files by sampling blocks — all are the same observation, that a uniform draw over the small units is a size-weighted draw over the aggregates they compose, and that size-weighted is usually the order you wanted anyway.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the graph-reduction section of the social-network chapter, which finds strongly connected components by picking nodes at random and doing two reachability calculations from each, notes that the larger a component is the more likely it is to be collapsed early, and illustrates with the web graph in which about one node in four lay in the central component so any single random pick would probably collapse it immediately.
