---
type: lesson
title: "Name the two quantities whose ratio decides it, then stop enumerating cases"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Name the two quantities whose ratio decides it, then stop enumerating cases

**Lesson:** Asked whether a heuristic always works, the reflex is to try it from every starting configuration and observe that it always did. On a small instance that is feasible and it feels like proof. It is not: it establishes the claim for that instance and transfers nothing, and worse, it leaves you unable to say what property of the instance made it work. The alternative is to identify the two quantities that actually govern the outcome and state the guarantee as a relation between them. Then a single argument covers every starting configuration, and — the part that pays for itself repeatedly — you can measure those two quantities on a new dataset and know in advance whether the heuristic will work there.

For anything that has to tell groups apart, the two quantities are almost always the same pair: how spread out a single group is, and how far apart two different groups are. Nearly every separation guarantee is a statement that the second exceeds the first by some factor. That framing is worth internalising because it relocates the difficulty from the algorithm to the data. A procedure that appears clever is often just one whose required factor is small; a dataset that defeats every procedure is one where the two quantities are comparable, and no procedure will fix that. Being able to say "this method needs the between-group gap to exceed the within-group spread" is a far more useful characterisation than a table of runs, and it is usually a short argument once you have decided to look for it.

The habit generalises past clustering. When someone claims a scheme is robust, ask what quantity it is robust with respect to, and against what other quantity that is being compared. Retry logic needs the recovery time to be short relative to the failure interval. A cache needs the reuse distance to be short relative to its capacity. A sampling estimator needs the effect size to be large relative to the noise. In each case the guarantee is a ratio, both terms are measurable on real data, and stating them converts an untestable claim of robustness into a precondition somebody can check.

The last dividend is diagnostic. When the ratio is the stated condition, a failure has a location. Either the data violated the precondition, in which case the method is not at fault and you need different data or a different method, or it satisfied it and the method still failed, in which case the implementation or the argument is wrong. Without the ratio, every failure looks the same and the debugging goes to whoever last touched the code, usually incorrectly.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 7's treatment of far-apart initialisation for k-means, which works an example from a deliberately unhelpful starting point near the centre of the data and then sets as an exercise the proof that any starting point works, explicitly steering the reader away from checking all twelve cases and toward a general theorem stated in terms of the diameters of the clusters and the minimum distance between points of different clusters.
