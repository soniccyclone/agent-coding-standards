---
type: lesson
title: "Replicate each item along the axes its key leaves undetermined"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, expressiveness, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, databases-and-data-management]
tags: [lesson]
---
# Replicate each item along the axes its key leaves undetermined

**Lesson:** Partitioning normally means picking one field, hashing it, and sending each item to exactly one place. That works when every item knows enough to name its destination. It stops working the moment a computation depends on several fields at once, because different inputs know different subsets of them. The move that unlocks these cases is to stop thinking of the destinations as a list and start thinking of them as a grid: hash each participating field independently, give each worker a coordinate vector, and route an item by filling in the coordinates it determines and *broadcasting it across every coordinate it does not*. Everything that must meet then meets, at exactly one worker, in one round — no cascade of pairwise stages, no intermediate result written out and read back.

The cost structure is what makes this a design decision rather than a trick. An item that pins down all coordinates is sent once; an item that leaves one axis free is sent once per bucket on that axis. So you are trading data volume for round count, and whether that trade wins depends on how large the intermediate results of the staged alternative would have been. When the intermediate is huge — when the staged plan's first step explodes before the second step filters — paying to duplicate the inputs is cheaper than materialising and shipping the explosion. When the intermediate is small, staging wins, and the grid is wasted duplication. You have to estimate both to choose, which is a good discipline in itself, because it forces you to say out loud how big the middle of your pipeline gets.

Sizing the grid is the second half, and it is not "equal shares." With a fixed total number of workers, the axes' bucket counts multiply to that total, so giving one axis more resolution takes it from another. Since each axis's bucket count is the replication factor for the data that leaves that axis free, the resolution should go where it spares the most volume: the axis whose free-riding dataset is largest gets the finest split, and the counts end up proportional to square roots of the data sizes rather than to the sizes themselves. That square-root shape is the fingerprint of a budget constrained by a product rather than a sum, and it recurs wherever you divide a multiplicative resource. The instinct to split such a budget evenly is wrong in a specific, correctable direction, and the correction is worth more the more lopsided the inputs are.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the communication-cost chapter's treatment of multiway joins in a single round, where reducers are identified with vectors of hash-bucket numbers, tuples are sent to every reducer whose unknown components could match, and the bucket counts are chosen by constrained optimisation against the relation sizes.
