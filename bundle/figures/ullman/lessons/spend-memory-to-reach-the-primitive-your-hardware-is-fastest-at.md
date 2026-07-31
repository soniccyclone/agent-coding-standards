---
type: lesson
title: "Spend memory to reach the primitive your hardware is fastest at"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, primitive-count]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# Spend memory to reach the primitive your hardware is fastest at

**Lesson:** The instinct that a computation should not store the same value twice is a good default and a bad absolute. Underneath any implementation is a machine that is enormously faster at some shapes of work than others, usually because those shapes are what its parallel units are wired for. If a redundant, wasteful-looking rearrangement of the data turns your computation into one of those shapes, the rearrangement can be worth several times the memory it costs. The comparison to make is not "duplicated data versus no duplicated data" — it is total time for the tidy version against total time for the wasteful one, on the actual machine.

The move that makes this concrete is to notice when a computation consists of the same small operation applied to many overlapping windows of the input. Written naively that is a nest of loops, and each iteration reads values its neighbours also read. Written the other way, you first materialise every window as its own independent row, which duplicates each input value about as many times as there are windows covering it, and then the entire computation collapses into a single bulk multiply against one shared parameter block. The duplication is the price of removing the overlap, and removing the overlap is what makes the work uniform enough to dispatch as one operation.

What makes this a design principle rather than a trick is that it inverts the usual direction of optimisation. Ordinarily you optimise by finding shared subexpressions and computing them once. Here you deliberately un-share them, because the sharing is exactly what forced a sequential, irregular access pattern. It is worth asking of any hot loop whether its cleverness about not repeating work is buying less than the regularity it is spending — reused intermediates create dependencies, and dependencies are what keep wide hardware idle.

The reason the trade-off is stable rather than a one-off is that memory capacity and arithmetic throughput have moved apart for decades. When a machine can do enormously more operations per second than it can service distinct memory requests, the cheap resource is the one you should be wasting. Write the redundant version, measure both, and be prepared for the answer that offends your sense of economy — and keep the conversion between representations at the boundary of the operation, so callers see only the clean interface and the redundancy stays an implementation detail you can withdraw when the hardware balance changes.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the implementation-and-training section of the convolutional-networks chapter, which flattens each square region of the input into its own column so that the whole layer becomes one matrix-vector product, acknowledges that the resulting matrix is larger than the input by roughly the square of the filter size because each input entry is repeated many times, and concludes that this is nevertheless the method used in practice because matrix-vector multiplication is extremely fast on GPUs.
