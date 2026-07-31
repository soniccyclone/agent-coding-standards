---
type: lesson
title: "Store only what an invariant cannot recompute for you"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load, primitive-count]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Store only what an invariant cannot recompute for you

**Lesson:** There are two distinct ways to make a representation smaller, and confusing them wastes both. The first is generic: drop the entries that hold a default value and record positions instead, which converts space from a function of the container's dimensions into a function of the actual content. Any sufficiently good general encoder finds this for you. The second is not generic and no encoder will find it: notice that a domain invariant already determines some of the stored values, and then store the invariant's parameter once instead of the values it implies. That second step is available only to someone who knows what the data means, and it is usually where the remaining factor of several lives.

The move is worth stating in a form you can apply elsewhere. Look at the values you are about to persist and ask which of them are functions of other values you are also persisting. If a whole group of entries shares a value that is derivable from a single per-group fact, keep the group's membership and the one fact, and let the reader reconstruct. What you have done is shifted a small amount of work to read time in exchange for a large amount of space and, more importantly, a large amount of bandwidth — since the same representation is what crosses the network and the cache line, not just what sits on disk. This is the opposite of the usual denormalisation reflex, and it wins whenever the bottleneck is movement rather than arithmetic.

The catch is that the derived value stops being derivable if you later partition the data in a way that separates a group from the fact it depends on. Splitting the representation into pieces forces the per-group fact to be repeated in every piece that holds any of the group, and suddenly the compression you earned is partly given back. The right response is not to abandon either the compression or the partition, but to bound the damage: the repetition can only occur once per piece a group actually appears in, which caps the blow-up by a factor you can compute in advance from the partitioning parameter. Deciding whether a representation and a partition compose is arithmetic, done on paper, before either is built.

The general habit is to treat a data layout as a claim about which facts are primitive and which are consequences. Every derived value you materialise is a bet that recomputation is more expensive than storage and transmission, and at scale that bet is usually wrong. Making the claim explicit — writing down what determines what — also gives you the check that catches the partitioning interaction, because you can see immediately which dependencies a proposed split would cut.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the link-analysis chapter's sections on representing the transition matrix, where the general sparse encoding is followed by the observation that every nonzero in a column is fixed by that column's out-degree, and by the analysis bounding the extra space that block partitioning costs.
