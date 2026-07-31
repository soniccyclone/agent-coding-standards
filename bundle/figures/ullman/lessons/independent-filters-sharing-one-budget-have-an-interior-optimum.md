---
type: lesson
title: "Independent filters sharing one budget have an interior optimum, not a monotone one"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Independent filters sharing one budget have an interior optimum, not a monotone one

**Lesson:** Requiring several independent checks to agree drives the false-acceptance rate down as a product, so the instinct is that more checks are always better and the only cost is more work. That instinct holds when each check is separately resourced. It fails, sometimes dramatically, when the checks are carved out of one fixed budget, because then adding a check makes every existing check weaker. Each one now gets a smaller share of the resource, its individual discriminating power drops, and at some point the degradation of every factor outruns the benefit of having one more factor. Past that point, adding checks makes the composite worse. The curve has an interior optimum, and the number of checks is a parameter to be solved for rather than maximised.

Getting the optimum right requires estimating each check's individual rate as a function of its share, which is usually straightforward arithmetic on the total volume and the budget: how much evidence does each check accumulate, how does that compare to the decision threshold, and therefore what fraction of its verdicts are uninformative. Multiply across checks to get the composite, then vary the count. The result is not a fine-tuning exercise — it typically tells you that a small number of checks is right and that both one and many are clearly worse, which is a decision you would not have reached by intuition in either direction.

The same reasoning also decides an architectural question that looks unrelated: whether to run several independent checks concurrently against one shared budget, or sequentially with each getting the whole budget in turn. Concurrent costs nothing in extra passes over the data but weakens each check; sequential keeps each check strong but pays another pass, and it accumulates the earlier checks' summaries in memory, which eats the budget anyway after enough rounds. Both directions therefore have their own ceiling. Framing the choice as a single trade — passes against per-check strength — makes it answerable instead of a matter of preference.

The transferable rule: whenever redundancy is supposed to improve reliability, ask whether the redundant elements are independently resourced or dividing a fixed pool. Independently resourced redundancy improves monotonically. Pooled redundancy has a peak, and systems built on the assumption that more is better sail past it — more replicas splitting the same bandwidth, more shards splitting the same cache, more sampling probes splitting the same rate limit. The failure is quiet, because each added element is individually defensible.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the multihash section of the frequent-itemsets chapter, which splits one pass's memory among several independent hash tables, works through the resulting per-table and composite false-candidate rates, and warns that beyond some number of tables the probability of an infrequent pair surviving rises rather than falls.
