---
type: lesson
title: "A model you reason in need not be a model you can build"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# A model you reason in need not be a model you can build

**Lesson:** There is a habit of treating the object you explain an algorithm with as a commitment to construct that object. It is not, and refusing to separate the two costs you the clearest available explanation. A dense table indexed by every possible element, with a mark in every cell where an element belongs to a collection, is the ideal picture for stating what a summary preserves and why the arithmetic works. It is also a catastrophic thing to store, since almost every cell is empty, and the underlying facts are already sitting in some transactional record kept for entirely unrelated reasons. Both statements are true at once. The picture earns its place by making a proof short, and it is never allocated.

The stronger version of the same move is when the object is not merely wasteful but impossible. An algorithm can be defined in terms of shuffling billions of rows into a random order and reading down the shuffled list, while everyone involved knows that generating and materialising such an order is out of the question. What gets implemented is a cheap function that assigns each row a pseudo-random position, with collisions that a true shuffle would not have. The correctness argument is still conducted entirely in the language of the shuffle, and the implementation is justified by the claim that the difference does not matter at the scale in question. Keeping the fiction is what lets the proof stay simple; discharging it is a separate, small argument about collision rates.

What makes this disciplined rather than sloppy is that the gap between the fiction and the mechanism gets named and bounded, not hidden. Say plainly which properties of the ideal object the implementation reproduces exactly, which it reproduces approximately, and what governs the error. Then a reader can check the proof against the ideal and check the substitution separately, instead of having to hold a smeared combination of both. The failure mode on the other side is equally real: an explanation given directly in terms of the mechanism, with the pseudo-random positions and the collisions baked in from the first line, is much harder to verify and hides the reason the thing works at all.

The general practice is to keep at least two descriptions of any nontrivial system and to be explicit about the role each one plays. One is chosen so that the invariants are obvious. The other is chosen so that it fits in memory and runs. Design pressure that forces these to be the same description degrades both, and the instinct that a specification must be executable to be respectable throws away the main thing specifications are for.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 3's introduction of the characteristic matrix and of minhashing, where the matrix is offered as a way to visualise the data while the text notes it is almost never how the data is stored and is nearly all zeros, and where the minhash is defined by a random permutation of the rows that the following section declares infeasible to construct and replaces with a hash function that merely maintains the fiction of permuting.
