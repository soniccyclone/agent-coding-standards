---
type: lesson
title: "Be correct for the possible inputs and sized for the actual ones"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, hardware-affinity, parallelizability]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Be correct for the possible inputs and sized for the actual ones

**Lesson:** Two different questions get asked of a design, and answering both with the same input set is a reliable way to get one of them wrong. The correctness question is about the space of things that *could* arrive: if some combination is possible and your scheme has no place to handle it, the scheme is broken whether or not that combination shows up this week. The sizing question is about the things that *do* arrive: how much memory a worker needs, how deep a buffer must be, how many partitions to create. Answer sizing from the possible-input space and you provision for a density that never occurs, wasting most of your capacity. Answer correctness from the observed data and you have built something that works until the day the sparse case fills in.

The clean discipline is to derive the structure from the schema and the numbers from the statistics. Establish the covering argument — every output that could be demanded has somewhere to be computed, every case that could occur has a branch — over the full space of legal inputs, ignoring how likely any of them are. Then, holding that structure fixed, observe what fraction of the possible inputs are actually present and scale the capacity parameter by that fraction: if a twentieth of the space materialises, a structure nominally built for twenty times your memory budget will in practice hold about a budget's worth. You have not weakened the correctness argument at all; you have used a measured density to pick a parameter the correctness argument left free.

The remaining subtlety is that a density is an average, and averages have spread. A parameter set exactly at the expected occupancy will be exceeded roughly half the time, so the honest version leaves margin — trims the estimate deliberately rather than tuning to the mean and hoping. And the whole arrangement is only as good as the density estimate, which makes that estimate a monitored quantity rather than a one-time measurement. Sparsity is a property of a dataset, not a law; when it drifts, nothing about correctness changes and everything about resource use does, which is exactly the failure that looks inexplicable because the code is still right.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the complexity-theory chapter's discussion of problems where not all possible inputs are present, which insists a mapping schema must still cover every possible output while noting that the reducer-size parameter should be inflated by the reciprocal of the fraction of inputs that actually appear, and then trimmed for the randomness in that count.
