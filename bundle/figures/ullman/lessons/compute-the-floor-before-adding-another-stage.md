---
type: lesson
title: "Compute the floor before you add another stage"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Compute the floor before you add another stage

**Lesson:** Filtering pipelines invite indefinite extension. Each stage you add removes some of what the previous stages let through, the improvement is measurable, and there is always another discriminator available, so the work has no natural stopping point and teams keep going until the gains feel small. That is a bad stopping rule, because it measures the last increment rather than the remaining headroom, and the two are different numbers. The remaining headroom is knowable in advance: every stage of a sound filter is required to pass everything that genuinely qualifies, so the pipeline's output can never be smaller than the true answer. The answer's own size is the floor, and no amount of engineering goes beneath it.

Knowing the floor turns an open-ended effort into a bounded one. Measure what your pipeline currently admits, compare it against the count of things that actually qualify, and the ratio tells you the maximum improvement any further work could possibly deliver. If you are admitting three times the true answer, the best conceivable outcome from all remaining effort is a factor of three, and if the next stage costs a full pass over the data plus permanent state carried in memory, you can decide against it with an argument rather than a feeling. If you are admitting a hundred times the answer, the case for more work is strong and you know how strong. Either way the decision stops being aesthetic.

The reason this is worth making a habit of is that filter stages usually have costs that do not shrink as their benefit does. Each one's summary has to be retained through every subsequent stage, so the accumulated state grows linearly in the number of stages while it competes for the same memory that the real work needs; and if the stages are separate sweeps, each one is a fixed toll paid regardless of how much it removes. Diminishing benefit against constant cost has an optimum somewhere well short of exhaustion, and passing it means building machinery that makes the system slower while every individual stage remains individually justified.

The general form applies past filtering. Compression cannot go below the content's entropy; deduplication cannot go below the distinct set; caching cannot go below the compulsory misses; scheduling cannot go below the critical path. In each case there is an irreducible quantity that is often much easier to estimate than the optimisation is to build, and the first move on any efficiency problem should be to estimate it. The answer is either that you are close to the floor, in which case the right decision is to stop and go find a different lever, or that you are far from it, in which case you now know what the prize is worth.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 6's treatment of the Multistage algorithm, which notes that any number of extra hashing passes can be inserted between the first and the last, that each pass's bitmap must be retained through all later passes until there is no room left to count, and that no matter how many passes are used the truly frequent pairs always hash to frequent buckets and so can never be filtered away.
