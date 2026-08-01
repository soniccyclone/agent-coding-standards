---
type: lesson
title: "One work unit per output means shipping each input once per output"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# One work unit per output means shipping each input once per output

**Lesson:** The obvious decomposition of a job whose outputs each depend on a handful of inputs is to make one work unit per output. It reads as the maximally parallel choice and it satisfies the instinct that smaller units are better: nothing waits on anything, every unit's working set is tiny, and any worker can take any unit. The hidden term is duplication. An input that participates in many outputs must be delivered to every unit that needs it, so cutting units down to single outputs sets the copy count of each input to the number of outputs it feeds. For a job where every item must meet every other item, that is one copy per item per peer, and the transport bill lands several orders of magnitude above anything the network can carry — a plan that is perfectly parallel and cannot be run.

The constructive fix is to enlarge the unit along the dimension that causes the duplication rather than to shrink it further. Partition the items into blocks and make the unit a *pair of blocks*: one delivery of a block now services every comparison between its members and the other block's, so the copy count drops from the number of peers to the number of blocks. Nothing is lost in doing so, and this is the part worth internalising. Across the whole family of block sizes, exactly the same set of primitive comparisons gets performed exactly once each — the computation is invariant and only the placement changes. Block size is therefore a knob you may turn purely on transport and memory grounds, without ever having to trade it against how much work gets done. That is a rare and valuable shape for a design parameter to have, and it is worth checking for explicitly, because a knob that also changes the amount of computation demands a much more delicate argument.

Two edges bound the knob and neither comes from the problem statement. Bigger blocks mean less duplication but a larger working set per unit, and the moment a unit's inputs stop fitting in the memory it runs in, the accounting you did is void. Smaller blocks mean more units, which you need enough of to keep every worker busy, but past that point extra units buy nothing and cost duplication. So the range is pinned from above by the memory of one worker and from below by the count of workers, and you pick inside it. The general habit: when a decomposition looks free because every unit is independent, find what each unit had to be handed, multiply, and check whether the wire can carry it before congratulating yourself on the parallelism.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the complexity-theory chapter's similarity-join example, where keying on each pair of images gives minimal per-worker input and a replication factor equal to the collection size, yielding an exabyte of transfer and a projected runtime in the hundreds of years; and the grouped variant that keys on pairs of groups instead, together with the observation that computation cost is the same for every group size because the similarity function is applied to each pair once regardless.
