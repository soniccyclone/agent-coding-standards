---
type: lesson
title: "The dependency between inputs and outputs bounds what any parallel version can cost"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, verifiability, expressiveness]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# The dependency between inputs and outputs bounds what any parallel version can cost

**Lesson:** Before writing a parallel algorithm you can characterise every algorithm you might have written, by describing the problem as nothing more than which inputs each output depends on. That bare relation is enough, because independent workers can only compute an output if some single worker was handed the whole set of inputs that output needs. From that one observation you get a definition of what it means for a decomposition to be valid at all: an assignment of inputs to workers where nobody exceeds a chosen capacity and every possible output is nevertheless fully covered by somebody. Whether such an assignment exists is a property of the problem, not of your cleverness, and it is a sharper statement of what separates problems this style of parallelism can express from ones it cannot.

The machinery then yields lower bounds, which is the part that changes how you work. Bound how many outputs any single worker of a given capacity could possibly cover; count how many outputs exist; conclude that the workers collectively must have been fed at least a certain total volume; divide by the number of inputs to get an unavoidable duplication factor. The result is a curve, not a number: duplication of input against capacity per worker, typically inverse, so more parallelism and smaller memory footprints are bought with more data movement and vice versa. You are choosing a point on a frontier rather than finding "the" algorithm, and when your candidate sits within a small constant of the proven bound you can stop optimising with justification instead of by exhaustion.

Two details in this reasoning generalise well beyond clusters. First, the dependency graph must be drawn over inputs that *could* exist, not the ones present in today's data, because an algorithm has to be correct for any subset that shows up; sparsity changes how you tune the capacity parameter, never whether the coverage requirement applies. Second, partial inputs are worthless in a way the bound must exploit — a worker holding half of what an output needs contributes nothing — and noticing which partial holdings are useless is usually the step that makes the per-worker bound provable.

A programmer who thinks in these terms treats "how do I parallelise this" as two separate questions: what does each answer depend on, and what does that dependency structure permit. The first is modelling and is cheap. The second tells you the shape of the trade-off you are stuck with, and it is answerable on paper, before any code exists and independently of which framework you eventually use.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the complexity-theory sections of the cluster-programming chapter, which introduce per-worker capacity and input-duplication as paired parameters, define coverage via a mapping schema over the input-output graph, and run the lower-bound recipe on all-pairs similarity and on matrix multiplication.
