---
type: lesson
title: "Your bookkeeping, not your input, sets the problem size you can handle"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# Your bookkeeping, not your input, sets the problem size you can handle

**Lesson:** For a whole class of algorithms the input is not the thing that has to fit anywhere. It arrives sequentially, is examined once, and is discarded; its size affects how long you wait but not whether the computation is possible at all. What must fit is the accumulated state — the counters, the tables, the partial aggregates that are consulted and updated in an unpredictable order as the input streams past. The moment that state exceeds fast memory, every update becomes a random access to slow storage and the algorithm does not degrade gracefully, it stops being viable. So the binding limit on problem size is a property of your bookkeeping, and it is worth computing explicitly and early.

The computation is arithmetic and takes a minute: the number of distinct things you are tracking, times the bytes per tracked thing, against available memory. Doing it produces a hard ceiling on the input's diversity — not its volume — and that ceiling is frequently much lower than intuition suggests, because the number of tracked entities is often quadratic or worse in the number of distinct elements while the input is merely linear. The result reframes the design conversation immediately: the question stops being "can we process this much data" and becomes "how do we track fewer things," which has entirely different answers, most of which involve discarding candidates before allocating state for them rather than making the state smaller.

That reframing also tells you where representation choices matter and where they do not. Squeezing the input encoding is usually pointless, since the input is streamed and bandwidth-bound rather than capacity-bound. Squeezing the state representation directly buys problem size, and there the choice between a dense layout indexed by position and a sparse layout that stores only occupied entries is a real decision with a computable crossover: the sparse form carries per-entry overhead, so it wins only below some occupancy fraction, and that fraction can be worked out from the sizes rather than argued about. Being explicit that this is where the effort belongs prevents a lot of misdirected optimisation.

The general habit is to separate, in any pipeline, the data that flows from the state that accumulates, and to size them against different resources. Flowing data is charged against time and bandwidth. Accumulated state is charged against capacity, and it is capacity that produces cliffs rather than slopes.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the memory-use sections of the frequent-itemsets chapter, which argue that passes over the basket file are the time cost while the count structure is what must be resident, work out the item-count ceiling implied by a given memory size, and compare the triangular-array layout against a triples layout with an explicit occupancy crossover.
