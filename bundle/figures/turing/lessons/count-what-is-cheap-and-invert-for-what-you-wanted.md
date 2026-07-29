---
type: lesson
title: "Count what your machinery finds cheap, then recover the number you actually wanted by arithmetic"
figure: turing
works: [paper-on-the-statistics-of-repetitions]
axes: [hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Count what your machinery finds cheap, then recover the number you actually wanted by arithmetic

**Lesson:** The quantity a design needs and the quantity a machine can cheaply produce are usually not the same quantity, and the instinct to close that gap by building better instrumentation is usually the expensive instinct. The better move is to find some nearby quantity the existing machinery already yields almost for free, work out the exact algebraic relation between it and the number you want, and pay for the conversion in arithmetic instead of in measurement. Here the wanted counts (how many genuine repeated runs of each length occur) are awkward to observe directly, while a sloppier family of counts — every window of a given length that looks repeated, long runs included multiply — falls out of nothing more than putting fixed-length letter groups into alphabetical order, which is exactly what the card-sorting equipment on hand did well. The two families are linked by a small triangular relation, so the wanted numbers come out of the observed ones by a couple of subtractions.

This holds because the mapping between a convenient observable and a wanted one is very often linear, or triangular, or otherwise trivially invertible, and inverting a small system of equations costs nothing compared with re-tooling a measurement path. It also composes well with the constraint you actually face: the observable is chosen to fit the mechanism, and the abstraction gap is closed on paper, where changing your mind is free. The corollary is the part people skip. An inversion consumes accuracy at its boundary — the recovery formula for a length needs the observed figures for two greater lengths — so you must collect a margin of extra input beyond the range you intend to use. Knowing exactly how much margin the derivation eats is part of designing the derivation.

A programmer who has internalized this stops asking "how do I measure X" and starts asking "what does this system already emit, and what is X's relation to it." That reframes a lot of instrumentation work into a modelling problem: derive request latency distributions from counters you already have rather than adding a tracer; get cardinality from a sketch and a correction factor rather than from a set; reconstruct the metric from the log rather than adding a metric. It also makes you honest about margins, because you now know that a derived quantity is only trustworthy over a range strictly inside the range you actually sampled.

**Source:** [Paper on Statistics of Repetitions](../works/paper-on-the-statistics-of-repetitions.md) — the middle of the paper, where Turing separates "apparent" from "actual" repeat counts, gives the relation between the two families, and then argues from it how far the collected statistics have to run past the largest length he intends to use.
