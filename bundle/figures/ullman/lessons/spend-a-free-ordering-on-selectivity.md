---
type: lesson
title: "Spend a free ordering on selectivity"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Spend a free ordering on selectivity

**Lesson:** Algorithms frequently require that some universe of elements be arranged in a fixed order, without caring which order it is. The requirement is real — the order is what makes an unordered collection into a sequence, so that prefixes, positions and suffixes become meaningful — but it constrains nothing beyond consistency. Everyone then reaches for whichever order is nearest to hand: alphabetical, numeric, insertion, whatever the identifiers happen to sort by. Correctness is unaffected by that choice, which is exactly why it deserves a second look. A parameter that cannot make the answer wrong can still make the runtime terrible, and one that cannot make the answer wrong is also completely safe to optimise.

The optimisation here is to order the universe by frequency, rarest first. Anything that indexes on a prefix of the sequence then indexes on the least common elements, so the resulting buckets are small and a lookup returns few candidates to examine. Order by frequency the other way, or arbitrarily, and prefixes fill up with the commonest elements, every object lands in a handful of enormous buckets, and the index degenerates into a scan while remaining perfectly correct. The gap between the two configurations can be orders of magnitude and there is no error message; the system just runs slowly in a way that looks like the workload being hard.

Extracting this requires knowing the frequencies, which means a preliminary pass over the collection to count occurrences. That pass is a real cost, and it introduces a dependency: the order is now derived from the data, so it must be recomputed or at least revisited as the data drifts, and it must be recorded because every object's representation depends on it. Those are the honest prices. They are usually small compared with what they buy, and the decision of whether to pay them is a straightforward comparison rather than a matter of taste.

The transferable habit is to hunt for degrees of freedom that a correctness argument has already declared irrelevant, and then to ask what cost model would like them set to. Any statement of the form "fix an arbitrary order," "choose any representative," "pick a starting point," or "select any tie-breaking rule" is such a degree of freedom. Left arbitrary, it is decided by whatever was convenient to write; decided deliberately, it is free performance. The distinguishing feature of this class of tuning is that it carries no risk, since the argument for correctness never mentioned the choice at all.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 3's aside on a better ordering for symbols, which notes that the obvious lexicographic order over the universal set can be replaced by an order that counts how often each element occurs across all the sets and places the rarest first, so that the indexed prefixes contain rare symbols and land in index buckets with few members, leaving fewer strings to compare.
