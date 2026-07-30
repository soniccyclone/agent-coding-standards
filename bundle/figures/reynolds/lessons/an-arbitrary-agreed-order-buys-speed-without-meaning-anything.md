---
type: lesson
title: "An arbitrary order, agreed on by everybody, buys speed without meaning anything"
figure: reynolds
works: [the-craft-of-programming]
axes: [expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# An arbitrary order, agreed on by everybody, buys speed without meaning anything

**Lesson:** Keeping data sorted converts a linear search into a logarithmic one, and it is tempting to explain this by saying that the order reflects something about the data. It does not. The speedup depends only on the existence of a comparison that everyone involved computes the same way, so that a single test can be read as a statement about an entire region rather than about one item. Whether the comparison means anything is beside the point. You may therefore invent an order for the sole purpose of getting the speedup — pick any convention, so long as it is total, cheap to evaluate, and identical for the writer and the reader. Alphabetic ordering of names is exactly this: the sequence of letters carries no information about people, yet centuries of filing systems run on it, and they run fast for precisely this reason.

Once you see the property as arbitrary-but-agreed, several things stop looking like compromises. An ordering key that is a meaningless composite of fields is not a hack, it is the normal case. Two systems that disagree about the order — different collation, different tie-breaking, different treatment of case or of missing values — do not merely produce differently-arranged output; they void the reasoning that made the fast lookup correct, and the failure shows up as items that exist but cannot be found. That is why the convention, not its meaning, is the thing to specify, document, and test. The comparison function is a shared contract between whoever establishes the order and whoever exploits it, and it deserves the treatment a contract gets.

The generalized view pays off again in deciding what to maintain. Since the order need not be meaningful, you are free to choose the one that is cheapest to preserve under the updates your system actually performs, rather than the one that reads best. And since the mechanism is "one comparison excludes a whole region," it transfers beyond sorted arrays to anything with that shape: search trees, index structures, hash partitioning by an arbitrary key, range-partitioned storage, binary search over a monotone predicate that has nothing to do with sorting at all. The recurring question is never "what is the natural order here" but "is there some total, cheaply-computed, universally-agreed order I can impose, and who pays to keep it."

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — the closing paragraph of Section 2.2.10, which observes that the order-of-magnitude improvement available when data is known to be ordered has nothing to do with the meaning of the ordering relation, that it is common practice to obtain these efficiencies by ordering data according to a completely arbitrary convention, and that this is the rationale behind alphabetic ordering; together with the section's generalization of orderedness to an arbitrary relation.
