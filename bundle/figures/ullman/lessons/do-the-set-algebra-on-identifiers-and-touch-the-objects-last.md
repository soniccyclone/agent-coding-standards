---
type: lesson
title: "Do the set algebra on identifiers and touch the objects last"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, parallelizability, cognitive-load]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Do the set algebra on identifiers and touch the objects last

**Lesson:** A pipeline that combines several filters has two very different kinds of work in it, and conflating them is what makes such pipelines slow. There is the bookkeeping — forming unions of candidate groups, intersecting the results of two independent screens, deduplicating — and there is the actual examination of the objects, which involves loading them, decoding them, and running a comparison whose cost dwarfs everything else. The bookkeeping can be done entirely on integer handles. Nothing about a union or an intersection needs the payload. So the combination logic should manipulate identifiers only, and the objects should be fetched exactly once, at the end, for the small set that survives every stage.

The reason this is worth stating as a principle rather than an optimisation is that the natural way to write the code does the opposite. Each filter is implemented as a function that returns matching objects, the combining code takes unions and intersections of those collections, and the result is correct and reads well. It also loads every object that any single stage admits, which is a far larger population than the intersection, and it loads some of them repeatedly. The expense is invisible in the structure of the program because it is hidden inside the type flowing between stages. Changing that type to a handle is a small edit with a large effect, and it also makes the stages composable in ways they were not before, since handles are uniform while payloads are not.

Once the boundary is drawn, the arithmetic of a composite filter can be reasoned about honestly. Two independent screens, each admitting a few percent of the population, intersect to something a few parts in ten thousand, and it is that final number, not either intermediate, that determines how much real comparison work there is. The intermediate sets may be large without embarrassment, because a large set of integers is cheap. That decoupling is what makes an aggressive multi-stage design affordable, and it is unavailable to a pipeline whose intermediates are objects.

The pattern is old and shows up wherever selection is separable from retrieval: index intersection before row fetch in a database, identifier lists in a search engine's posting-list merge, sorting an array of pointers rather than an array of records, marking before sweeping in a collector. The general instruction is to find the smallest token that fully determines an object, run all the logic on tokens, and treat dereferencing as an expensive operation that happens once, as late as possible, on as few tokens as possible.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 3's fingerprint-matching case study, which improves on a single large disjunction of hash functions by splitting them into two groups, taking the union of the buckets a probe falls into within each group and then the intersection of the two unions, with the explicit note that the unions and intersections are computed over database indices while only the intersection's members are ever compared as fingerprints, since the comparison is what dominates the running time.
