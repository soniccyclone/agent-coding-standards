---
type: lesson
title: "Derive a component's tolerance from the error already present in the chain"
figure: sutherland
works: [a-head-mounted-three-dimensional-display]
axes: [hardware-affinity, verifiability, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Derive a component's tolerance from the error already present in the chain

**Lesson:** How good does a measurement need to be? The tempting answer is "as good as we can afford," which is really a refusal to answer. Sutherland answers it by reasoning outward from the rest of the system: the finest position resolution worth chasing is set by the granularity the output stage can even represent, and the accuracy worth chasing is set by the distortion the optics are already introducing downstream. Precision finer than the coarsest link in the chain buys nothing, because that link discards it before anyone perceives it. Precision much coarser than that link becomes the dominant error, and everything downstream inherits it. So the requirement is not a preference, it is a computation over the error budget of the whole path.

This holds because error composes along a path, and the total is dominated by its largest contributor. Every engineering decision about a subsystem is therefore conditional on numbers that live outside that subsystem. A team that treats each component's quality as a local virtue will systematically overbuild the cheap-to-improve parts and underbuild the expensive ones, and will have no way to tell which mistake it made, because the local view never surfaces the comparison.

The programmer who believes this changes what they do before optimizing anything. They ask what the consumer of a value can actually distinguish, and they size the producer to that. Numeric tolerances, clock precision, retry counts, cache freshness windows, floating-point widths, timestamp granularity: each of these is a question about the coarsest link downstream, not a question about the best achievable locally. And it converts vague quality debates into arithmetic, which means someone can check the answer and later revisit it when a downstream component gets better.

**Source:** [A Head-Mounted Three Dimensional Display](../works/a-head-mounted-three-dimensional-display.md) — the reasoning lives in the discussion of the head position sensor's resolution and accuracy targets, where each target is justified by an error already introduced elsewhere in the display path rather than by what the sensor could achieve.
