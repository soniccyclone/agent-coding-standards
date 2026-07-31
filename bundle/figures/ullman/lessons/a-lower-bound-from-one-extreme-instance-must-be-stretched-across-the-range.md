---
type: lesson
title: "A lower bound from one extreme instance must be stretched across the range"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# A lower bound from one extreme instance must be stretched across the range

**Lesson:** The cheapest way to prove that a procedure cannot be improved is to count its output. If the job is to produce a set of results, no method can finish faster than it takes to write them down, so exhibiting one input on which the number of results is large gives an immediate floor on the work — with no reference to how any algorithm might be organised. This is the most reusable form of impossibility argument available, because it depends only on the specification and not on any assumption about technique, and it is worth reaching for before spending effort trying to be cleverer.

The step people skip is the one that makes the bound mean anything. A single extreme instance proves the bound only at that instance. If the only witness is the maximally dense case, then the honest claim is "cannot be improved on maximally dense inputs," and someone will reasonably ask whether the sparse regime — the one they actually have — admits something better. The bound is not established until you can produce witnesses across the whole range of the parameter that matters. The technique for that is padding: take the extreme witness and extend it with structure that changes the parameter you are ranging over while adding nothing to the output. Attaching a long thin appendage inflates the size measure without producing new results, dragging the density ratio anywhere you like while the output count stays put, so the bound follows the family all the way down.

Reading this from the design side rather than the proof side, it is a warning about how performance claims and complexity statements are usually scoped. A result demonstrated at one corner of the input space is routinely quoted as if it held everywhere, and the corner chosen is the one that was easiest to construct or measure. Benchmarks have exactly this defect. The discipline in both cases is the same: identify the parameter your users vary, and produce evidence at several points along it rather than one, using constructions that isolate the parameter from everything else.

There is also a useful negative reading. If you cannot pad your witness to cover the range, that is informative — it may mean a better algorithm genuinely exists in the uncovered regime, and that is where to look.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the optimality argument for the triangle-counting algorithm in the social-network chapter, which uses the complete graph to show the number of triangles already forces the claimed running time, then appends a chain of arbitrary length that adds no triangles and at most doubles the edge count, so the ratio of edges to nodes can be driven as low as desired and the bound holds across the full range of densities.
