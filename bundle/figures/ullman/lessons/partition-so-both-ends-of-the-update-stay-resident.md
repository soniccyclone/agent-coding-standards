---
type: lesson
title: "Partition so that both ends of an update stay resident, and resend the cheap side"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# Partition so that both ends of an update stay resident, and resend the cheap side

**Lesson:** A decomposition that gets the operation count right can still be unusable, because the operation count says nothing about the order in which memory is touched. The characteristic failure is an update rule where each unit of work reads one location and accumulates into another: split the data by the read side alone and every unit of work lands on an unpredictable accumulator, so the accumulating structure is paged in and out continuously and the job runs orders of magnitude slower than its arithmetic suggests. The defect is not in the algorithm and not in the amount of data; it is that the partition made one side of the update resident and left the other side scattered.

The repair is to choose the partition from the residency requirement rather than from what looks like a natural split. Cut both the source and the destination into pieces, and give each unit of work one source piece paired with one destination piece, so that for the entire duration of that unit both ends of every accumulation are in fast memory and no access escapes the window. Once you frame it this way the right partition is forced: you need a two-dimensional split of whatever mediates between source and destination, because a unit of work is identified by a (source piece, destination piece) pair, not by either alone.

That partition has a price, and recognising the price as acceptable is the second half of the reasoning. Each source piece is now needed by every unit of work that owns a different destination piece, so the source has to be delivered several times over. You are deliberately paying redundant transfer of the smaller object to obtain sequential, resident access to the larger one. The trade is worth making whenever the multiplied object is the small one and the object read exactly once is the big one, which is exactly the situation when the mediating structure dwarfs the vectors it connects. The general rule underneath: duplication of the cheap side is a legitimate purchase, and refusing to duplicate anything on principle is how people end up with elegant partitions that thrash.

There is also a scheduling degree of freedom worth noticing. Grouping several units of work under one worker — all the pieces that accumulate into the same destination — lets that worker finish its destination piece completely, which collapses the subsequent merge step into concatenation. Fewer, fatter workers doing more local combining and a trivial merge is frequently better than more, thinner workers feeding a real merge, and which is better is decided by the same residency arithmetic, not by a preference for maximum parallelism.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the link-analysis chapter's sections on efficient iteration, contrasting vertical striping (which thrashes because a column can contribute to any component of the result) with square-block partitioning that keeps the relevant input and output stripes in memory together, and the variant assigning a whole row of blocks to one worker so the merge becomes concatenation.
