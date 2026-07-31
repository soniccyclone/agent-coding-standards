---
type: lesson
title: "An approximate model needs both a repair path and a coarsening path"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# An approximate model needs both a repair path and a coarsening path

**Lesson:** A summary maintained incrementally against data you can no longer see will drift, and no amount of care in the update rule prevents it. Each update is a small approximation, the approximations compound, and eventually the summary asserts something the underlying data does not support — with no internal signal, because the summary is all you have to check against. Designs that acknowledge this are qualitatively better than designs that try to make the update rule good enough, because the drift is structural rather than a bug to be fixed.

Acknowledging it means building a repair path: the underlying data still exists somewhere slower, and the summary can be periodically recomputed from it in full. That should be designed and scheduled from the beginning rather than added after someone notices bad output, because its existence changes what the incremental rule is allowed to be. Knowing a correction is coming, you can accept a cruder and much cheaper update rule, since its errors have a bounded lifetime. Without a repair path, the incremental rule has to be right forever, which is a far more expensive requirement and usually an unachievable one.

The second path handles a different failure: the summary collection outgrowing its budget. The tempting responses are to fail, or to evict, and both are bad — failing surrenders and evicting silently loses whole regions of the model. The better response is to lower the resolution: relax whatever parameter controls how finely the data is partitioned, merge the entities that relaxation now permits to merge, and continue with a coarser but complete model. Fidelity degrades smoothly and uniformly rather than vanishing in patches, and the system reports something true at a lower resolution instead of something false at a high one. This requires that resolution be an explicit parameter with a defined merge operation attached, which is a design decision to make early; retrofitting a coarsening knob onto a model that has no notion of resolution is usually not possible.

Together these two paths make an approximate model operationally honest: accuracy is maintained against ground truth on a schedule, and memory pressure is absorbed as coarseness rather than as failure or as silent gaps. A system with neither is an approximation that gets worse in unpredictable ways and eventually falls over, which is the default outcome and the reason approximate systems have a bad reputation they do not inherently deserve.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the GRGPF sections of the clustering chapter, which acknowledge that the retained representative may cease to be the true one and prescribe periodically reloading a cluster's points from disk to recompute its features, and which respond to the summary tree exceeding memory by raising the permitted cluster radius and merging clusters rather than by failing.
