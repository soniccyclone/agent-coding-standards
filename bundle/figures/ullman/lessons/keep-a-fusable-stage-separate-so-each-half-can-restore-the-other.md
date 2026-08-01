---
type: lesson
title: "Keep a fusable stage separate so each half can restore the other"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, verifiability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Keep a fusable stage separate so each half can restore the other

**Lesson:** Fusing two stages that could be one is the obvious efficiency: the second stage's job is already possible in the first, the intermediate hop disappears, and the code gets shorter. There is a reason to refuse that gets missed, and it has nothing to do with modularity or clean layering. Two separated stages that each retain what they have sent are mutually reconstructive. If either side is lost, everything it needs to be rebuilt is sitting on the other side, because the other side is precisely the place all its inputs came from and all its outputs went. Fuse them and that property evaporates — a restarted unit now needs history that only it held.

The construction is worth stating carefully because it composes with placement. Put the two kinds of stage in different failure domains, have each keep the output files it has produced, and a loss anywhere on one side is repaired from the other side, which is intact by construction. You have bought recovery from any single-domain failure without a replication protocol, without a consensus layer, and without storing anything twice; the second copy of every message is not a copy at all, it is the sender's record of what it sent, which had to exist anyway if the stage is to be replayable. The cost is one extra network crossing per round and the discipline of not deleting sent output. That is a remarkably cheap price for a recovery story in a computation that is cyclic and therefore cannot use the ordinary retry-the-failed-unit trick at all.

The general principle: a decomposition boundary is also a place where the state of the computation exists in two independent locations, and that duplication is usable. Before collapsing a pipeline stage, ask what the boundary is currently giving you besides separation of concerns — the answer is sometimes a checkpoint you did not know you had. The inverse question is as useful: when a system needs recovery and has none, look for a stage that was fused for efficiency and consider un-fusing it, because reintroducing the boundary may be a smaller change than adding a durability mechanism. Efficiency arguments that only count hops are systematically blind to this, since the hop is exactly what was doing the work.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 2's transitive-closure example under recursive extensions, which observes that the duplicate-elimination tasks are not essential because the join tasks could remove duplicates themselves, and then argues for keeping them separate: with every task storing all output files it has created and the two kinds of task placed on different racks, a restarted task of either kind can obtain all its previously generated inputs from the other kind.
