---
type: lesson
title: "Size work units between the overhead below and the variance above"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, hardware-affinity, cognitive-load]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# Size work units between the overhead below and the variance above

**Lesson:** The instinct when parallelising is to cut the work as finely as the problem allows — one unit per independent item, one worker per unit — on the theory that maximum concurrency is maximum speed. It usually is not, and the reason is that two different costs push the right granularity in opposite directions. Below, per-unit overhead: every unit costs something to create, dispatch, track and collect, so units smaller than that overhead spend most of their life being administered. Above, variance: units are rarely equal in size, and when each unit is also a scheduling slot, the slowest unit sets the finish time for the whole phase. The workable granularity lives strictly between the two, and neither bound is discoverable from the problem statement — you have to know the dispatch cost and the spread of unit sizes.

The variance side has a specific and slightly counterintuitive remedy. Bundling several units into one scheduled task makes the task durations more alike, because a task that drew one huge unit probably drew small ones too and the sum concentrates. That argues for fewer tasks than units. But there is a second, opposing move: create more tasks than you have workers, so that a worker which lands a slow task can be left to grind on it while its neighbours run several quick tasks in sequence. That argues for more tasks than workers. Both are right, and together they pin the number of tasks into a band — comfortably more than the number of workers, comfortably fewer than the number of units — which is a far more useful design output than "parallelise it."

Notice what makes this reasoning transferable: it never mentions clusters. The same band appears when choosing batch sizes for a queue consumer, chunk sizes for a thread pool, page sizes for an I/O scheduler, or shard counts for a database. Wherever you are dividing work, ask the two questions separately. What does one unit cost to hand out, independent of doing it? And how heavy-tailed are the units? A long tail means smaller units and more of them than workers; a high dispatch cost means bigger units. If both are high you are in genuine tension and should measure rather than reason, but you will at least know what you are measuring for. The failure mode this replaces is picking a unit size from the shape of the data — one per row, one per file, one per customer — which is an accident of how the input happened to be written down rather than anything to do with how the work behaves.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the MapReduce chapter's discussion of reducers, reduce tasks and compute nodes, which argues against one task per reducer on both overhead and skew grounds and then derives the two-sided rule of thumb for how many tasks to create.
