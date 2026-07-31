---
type: lesson
title: "Returning a collection as one value hides your fan-out from the system"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, parallelizability, primitive-count]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# Returning a collection as one value hides your fan-out from the system

**Lesson:** There is a distinction that reads as pedantic and is not: producing many outputs from one input is a different operation from producing one output that happens to be a container of many things. The results look the same when printed. They are not the same to anything that has to schedule, partition, count, or redistribute the work, because in the second case the multiplicity is inside an opaque value and the surrounding machinery sees exactly one element. Downstream, a stage that would have processed a thousand items in parallel now processes one item that is a thousand items long, and there is no seam along which it can be split.

Frameworks that take this seriously provide two separate operators — one that maps each input to exactly one output, one that maps each input to any number of them — and the second is not sugar for the first. It is the one that lets the runtime treat cardinality as public information. The general principle behind the pair is that the shape of your return type is part of the interface you offer the system, not merely a convenience for the caller. Anything you nest inside a single returned value has been removed from the system's view: it cannot be load-balanced, cannot be counted for progress, cannot be regrouped by key, and cannot be spread across machines. Anything you expose as a stream of separate elements stays schedulable.

The habit worth building is to notice, whenever you find yourself returning a list, whether the list is genuinely one thing — a record whose fields happen to be plural, a matrix, a parsed document — or whether it is really several independent things wearing a container because the function signature only had room for one slot. The second case is where hidden skew is born: one input that expands into a million outputs becomes a single unsplittable unit of work, and the whole computation waits for it. The remedy is not a bigger machine; it is choosing an interface in which the expansion is expressible, so the thing that decides where work runs can see it happen.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the chapter on cluster programming systems, in its explanation of why a one-to-one map that returns a set is not a substitute for the one-to-many operator, using the word-count pipeline where mapping each document to a set of word-count pairs produces a collection of sets rather than a collection of pairs.
