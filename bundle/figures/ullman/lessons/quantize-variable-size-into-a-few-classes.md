---
type: lesson
title: "Quantize variable size into a few classes, then pad within each"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, hardware-affinity]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# Quantize variable size into a few classes, then pad within each

**Lesson:** A mechanism built for a fixed size, confronted with inputs of varying size, presents two obvious escapes and both are bad at the extremes. Build it for the largest input you will ever see and pad everything else up to that: correct, uniform, and wasteful in exact proportion to how much your inputs vary, which for real distributions is most of the work. Build a separate instance per distinct size: no waste, and now you maintain, tune, warm up, and reason about as many instances as there are sizes, which for anything with a long tail is unbounded.

The resolution is to stop treating size as a continuous property and treat it as a small set of classes. Choose a handful of sizes, route each input to the smallest class that can hold it, pad within the class. The waste is now bounded by the gap between adjacent classes rather than by the distance to the global maximum, and the number of instances is a constant you chose rather than a property of your traffic. Both failure modes shrink at once, which is what makes this a genuine third option rather than a midpoint.

The class boundaries are then the design decision, and they should follow the distribution rather than be evenly spaced. Where inputs pile up, classes should be close together, because that is where padding waste is multiplied by volume. In the sparse tail, one wide class is fine, because few inputs land there and the per-input waste is paid rarely. This also gives you the diagnostic to watch afterwards: measure how much padding each class is actually carrying, and move the boundary when one class is doing most of the wasting.

The pattern recurs anywhere fixed and variable meet — size-class allocators, connection pools with a few configured capacities, batch shapes compiled ahead of time, image or buffer dimensions rounded up to a small menu. Recognising it is worth more than any individual instance, because the first two options are the ones that occur to people, and the argument between "pad to the max, it's simpler" and "handle each size exactly, it's efficient" is a false choice that both parties can lose.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the discussion of variable-length sequences in the recurrent-networks chapter, which lists zero-padding every sequence to the length of the longest and bucketing by length with a separate network per bucket as the two approaches, and then describes the combination actually used: a small number of buckets, each sequence assigned to the shortest bucket long enough to hold it, with padding applied inside the bucket.
