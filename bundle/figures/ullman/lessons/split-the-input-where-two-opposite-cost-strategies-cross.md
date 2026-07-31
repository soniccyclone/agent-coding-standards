---
type: lesson
title: "Split the input where two opposite-cost strategies cross"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Split the input where two opposite-cost strategies cross

**Lesson:** When two plausible methods for the same job have costs that move in opposite directions as some property of the input varies, the choice between them is not a choice. Neither dominates, so committing to either leaves the bad half of your input running the wrong method. The move is to run both — one on the portion where it wins, the other on the rest — and to place the boundary at the value where their costs are equal. That value is derived, not tuned: write down the two cost expressions as functions of the property, set them equal, solve. What comes out is often an unobvious quantity like a square root of the input size, which nobody would have guessed and which is optimal for a reason you can state.

Two things make the technique work rather than merely sound plausible. The first is that the partition must be exhaustive and non-overlapping, so every case is handled exactly once and the two branches can be reasoned about independently. The second, and more interesting, is that the cheap branch is usually cheap because of a conservation law, not because of an assumption. Elements above a degree threshold cannot be numerous, because total degree is fixed by the number of connections and each one contributes twice — so the count of expensive elements is bounded no matter how adversarial the input. That is what makes brute force affordable on them. Conversely the elements below the threshold have small neighbourhoods by definition, so the scan-based method is bounded there too. Both branches are bounded by construction rather than by hope, which is why the combined bound holds in the worst case and not just typically.

The habit generalises past algorithm design into ordinary system work: query plans that use an index for selective predicates and a scan for unselective ones, caches that treat hot and cold keys differently, batch versus streaming paths chosen by volume. In each case the temptation is to pick one strategy and defend it, or to tune a threshold empirically. Deriving the crossover instead gives you a number with a justification attached, tells you how the number should move when the hardware or the data shape changes, and — because you wrote both cost expressions down — tells you what the combined cost actually is.

Worth also noticing the shape of the result: the combined cost is typically worse than either method's best case and far better than either method's worst case. Hybrid strategies do not win by being brilliant on any single input; they win by not having a bad case, which is a different and usually more valuable property.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the triangle-counting algorithm in the social-network chapter, which designates nodes of degree at least the square root of the edge count as heavy hitters, bounds their number by the fact that degrees sum to twice the edge count, enumerates all triples of heavy hitters directly, handles every other triangle by scanning the neighbours of its lowest-degree node, and shows both branches cost the same order — which is also proved to be the best achievable.
