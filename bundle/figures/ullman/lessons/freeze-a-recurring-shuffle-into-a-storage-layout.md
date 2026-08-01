---
type: lesson
title: "Freeze a recurring shuffle into a storage layout"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, parallelizability, cognitive-load]
subdomains: [databases-and-data-management, distributed-systems-and-concurrency]
tags: [lesson]
---
# Freeze a recurring shuffle into a storage layout

**Lesson:** When a computation is analysed as a one-off, the movement of data to the workers that need it is a cost of the run. When the same computation runs every day against the same population of participants, that movement is being paid over and over to produce the same arrangement — and at that point it stops being a runtime cost and becomes a question about where things should live. If the optimal plan for a query would replicate the small reference data across the workers in a particular pattern, and every query of that family wants the same pattern, then store it that way permanently. The plan's communication step becomes a no-op, and the recurring cost collapses to the storage of a few extra copies of the small tables.

The condition that makes this legitimate is worth naming, because it is what distinguishes the move from ordinary caching. It is not that the data is hot; it is that the *shape* of the demand is stable. Something large is joined against several somethings small, the large thing dominates by orders of magnitude, and the identity of the small things does not change from query to query even though the predicates do. Under those conditions the layout is derivable from the schema rather than from a workload trace, and it does not need invalidation logic, because nothing about it depends on which particular query arrives. The sizing falls out of the same analysis that would have sized the one-off plan: how finely to partition on each join key is set by the size of the reference data attached to that key, so the layout inherits the optimisation rather than guessing at it.

The habit is to look at your recurring jobs and ask which part of each run is re-establishing an arrangement that the previous run already had. Repeated sorting into the same order, repeated broadcasting of the same lookup tables, repeated co-location of the same pairs — each is a runtime cost that a placement decision could have absorbed once. The general form of the question is: of everything this job does, what depends on the request and what depends only on the schema? The second category has no business being recomputed per request, and moving it into how the data is stored is usually a smaller change than any of the alternatives people reach for first.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 2's sidebar on star joins, which suggests distributing the fact table across the available compute nodes and replicating the dimension tables permanently in exactly the pattern the multiway join would have produced, with the number of buckets for each key attribute proportional to the size of its dimension table.
