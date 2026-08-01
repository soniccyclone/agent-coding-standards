---
type: lesson
title: "Partition the sample so its errors are forced to cancel"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Partition the sample so its errors are forced to cancel

**Lesson:** Repeating a measurement over independently drawn subsets is the reflexive way to average away sampling error, and it is not the best one available when you control which subsets are used. Independent draws overlap, leave parts of the population untouched, and let the same unlucky region be drawn repeatedly, so their errors are merely uncorrelated and cancel only in expectation. Cutting the population into disjoint blocks that together cover everything, and taking one measurement per block, produces something stronger: whatever quantity is over-represented in one block is by arithmetic under-represented somewhere else, so the deviations are negatively correlated and the average is pinned much closer to the truth. The estimator improves without any additional work, purely from how the material was divided.

The construction has a second payoff that is easy to miss. Independent repetitions usually require independent sources of randomness, one per repetition, and those sources cost something to generate, to store, and to distribute to every worker that needs them. A covering partition lets one source of randomness serve every block, because the blocks are already distinguished by which part of the population they cover. One random function and one sequential pass over the data can therefore yield as many measurements as there are blocks. Randomness stops being the per-measurement consumable it appears to be and becomes a fixed cost.

There is a real cost in the other direction and it should be stated. Each block is smaller than the whole, so an individual block-level measurement is noisier and may be entirely uninformative about some pairs of subjects, which is fine if the aggregate handles missing observations honestly and fatal if it does not. Blocks also have to be laid out so that the property being measured is not systematically aligned with the block boundaries. If the data arrives grouped by exactly the attribute you are estimating, contiguous blocks are strata that share nothing with each other, and the cancellation argument becomes an argument that you have measured different populations.

The general prompt: whenever a design says "repeat with a fresh random sample," ask whether the samples could instead be a partition of the population. Covering designs, systematic sampling every k-th record instead of k independent draws, cross-validation folds rather than repeated random splits, and sharded sweeps that each see a distinct slice are all the same manoeuvre. You give up the mathematical convenience of independence, which makes the error analysis slightly harder to write down, and you get a smaller error and less randomness to manage.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 3's treatment of computing minhash values from a restricted set of rows, which observes that using the same restricted subset for every hash function leaves the estimate at the mercy of that subset, divides the rows into groups instead so that a single hash function and a single pass produce one value per group, and argues that a group holding more than its share of one row type forces another group to hold less.
