---
type: lesson
title: "Encoding categories as numbers asserts distances you did not mean"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Encoding categories as numbers asserts distances you did not mean

**Lesson:** Turning a set of labels into numbers so a numeric method will accept them looks like a formatting step and is a modelling claim. Numbers carry an order and a spacing, so the moment you map three labels to one, two, and three, you have asserted that the second sits between the other two and is equally far from each — a claim the domain may flatly contradict. Any method that consumes the encoding as a magnitude will honour that claim, and the resulting errors are not visible as errors; they show up as a method that mysteriously underperforms on data that looks fine.

The constraint is worth stating precisely because it is a hard one, not a matter of care. Two mutually exclusive labels can be encoded faithfully: put them at zero and one, and the distance is zero within a label and one between them, which is exactly right. Three or more cannot. There is no assignment of three numbers to a line that leaves all three pairwise distances equal, so any encoding of three labels into a single numeric dimension necessarily makes two of them closer than the third pair. You are not choosing between a good encoding and a careless one; you are choosing which false adjacency to introduce.

The escapes are to add dimensions or to change methods. Giving each label its own dimension, with one in its own position and zero elsewhere, restores equal separation at the cost of as many dimensions as there are labels — which reintroduces the sparsity and dimensionality problems those methods have. Or use a method that never treats features as magnitudes: something that tests membership in a set of values rather than comparing against a threshold consumes labels natively and asserts nothing about their arrangement. That is a real and underweighted reason to prefer such a method when the data is genuinely categorical, independent of any argument about accuracy.

The general habit is to ask, of every encoding, what relationships it makes representable and what relationships it makes unavoidable. Encodings are not neutral transport; they are where unexamined assumptions enter a system most quietly, because the code that consumes them cannot tell an asserted relationship from a real one.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the comparison-of-learning-methods section closing the large-scale-machine-learning chapter, which notes that nearest-neighbour methods are really only useful for numerical features, that a two-valued categorical feature can be encoded as zero and one so pairs sharing a value are at distance zero and others at distance one, but that three or more values cannot be assigned numbers that are equidistant — in contrast to decision trees, which handle categorical and numerical features alike because their tests are membership tests.
