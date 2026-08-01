---
type: lesson
title: "Rank the head of the distribution and lump the tail into one class"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Rank the head of the distribution and lump the tail into one class

**Lesson:** An algorithm needs items ordered by how rare they are, and the set of possible items is unbounded, so the ordering it needs cannot be computed. The resolution is not to abandon the ordering or to build machinery for maintaining frequencies over an open universe. It is to rank the most common hundred thousand or so items by measured frequency, declare every other item equally rare, and order those among themselves by an arbitrary but fixed rule. The result is a total order that is cheap to evaluate, needs a bounded table, and is wrong only in a region where being wrong costs almost nothing.

The justification is a property of the distribution rather than of the algorithm. In a skewed population the ordering decision that matters is between the heavy head and everything else; distinguishing the four-thousandth-rarest item from the four-thousand-and-first buys nothing, because both are rare and both will gate almost as well. So the accuracy of the ranking should be spent where the density is, and the rest can collapse into a single bucket. That is a general shape: when a continuous quantity feeds a decision whose sensitivity is concentrated in one region, measure precisely in that region and use a constant elsewhere, rather than trying to be uniformly accurate at uniform cost.

The second half of the compromise is the part most likely to be skipped, and it is the part that makes it correct rather than merely cheap. The fallback rule for the tail must produce a deterministic total order, not an arbitrary one, because both sides of the matching sort by this order and they must agree. Alphabetical works precisely because it needs no shared table and no coordination: two processes that have never communicated will order two unknown items identically. Choosing something like insertion order or hash order instead would be equally easy to compute and would silently break the algorithm, since the two sides would disagree on unknown items and matches would be missed with no error raised anywhere.

So the recipe has three parts and all three carry weight. Bound the table by taking the head. Assign the tail a single class rather than pretending to rank it. Order within that class by a rule that any independent party will reproduce. It is a compact answer to the recurring situation where the ideal key is a global statistic over an open set, which turns up in join ordering, sharding, priority assignment, and any conjunctive filter that wants its most selective test first.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 8's document-and-bid matching algorithm, which wants words ordered rarest-first, observes that the set of words appearing in emails is essentially unlimited, and settles on ranking the n most frequent words by frequency at the end of the order while placing every other word at the front in lexicographic order.
