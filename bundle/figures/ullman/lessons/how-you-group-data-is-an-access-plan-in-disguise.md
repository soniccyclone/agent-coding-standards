---
type: lesson
title: "How you group data is a search strategy in disguise"
figure: ullman
works: [a-comparison-between-deductive-and-object-oriented-database-systems]
axes: [expressiveness, cognitive-load, hardware-affinity]
subdomains: [databases-and-data-management, programming-environments-and-object-systems]
tags: [lesson]
---
# How you group data is a search strategy in disguise

Every data model asks you to partition the world into named collections of
similar things — tables, predicates, classes — and the reason usually given is
descriptive: it tells you what a thing is. Ullman points out the function that
partition is actually performing. Before you can look for something, you must
decide where to look, and the collection name is that decision; when it can be
made statically, the cost of making it disappears entirely into compile time.
Naming your categories is not documentation, it is the first and cheapest step of
every retrieval, and it is invisible precisely because it works so well.

Which is why the scheme fails in a specific, predictable way. It holds only while
the number of meaningful categories stays small enough to name. Push toward a
domain where entities have overlapping, individually significant sets of
properties — billions of entities, thousands of possible attributes, so that
nearly every pair of entities is meaningfully different in *which* attributes
apply, not merely in their values — and the honest count of categories becomes
astronomical, with names so compound they are useless as names. The tempting
escape is to stop classifying and let each entity carry its own set of properties,
addressing things by what they respond to rather than by which bucket they sit in.
That escape is coherent at the level of meaning: existing theory already explains
how to interpret queries phrased over attributes instead of collections. What it
silently abandons is the part that made retrieval affordable. There is no longer a
static structure for a compiler to route through, indexing every attribute is
unaffordable at that width, and for any attribute that is really a computation
with effects, indexing is not even well defined.

The transferable habit is to treat any grouping — schema, class hierarchy,
namespace, shard key, directory layout, tag taxonomy — as a claim about the
queries you expect, and to check that claim against the actual breadth of the
data before adopting it. When the number of natural categories starts to approach
the number of items, that is the signal your organizing scheme has stopped
organizing, and the flexible sparse alternative is not free: it is a trade that
hands you expressiveness and hands back the retrieval plan you used to get for
nothing, leaving you to rebuild it deliberately.

**Source:** [A Comparison Between Deductive and Object-Oriented Database Systems](../works/a-comparison-between-deductive-and-object-oriented-database-systems.md) — the modelling section comparing relations, predicates and classes as embodiments of an entity set, extended through the treatment of variable component sets and the closing problems raised for "classless" data and its indexing.
