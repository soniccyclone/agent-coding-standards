---
type: lesson
title: "Fuse the two stages whose distortions cancel"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Fuse the two stages whose distortions cancel

**Lesson:** Two stages that are cleanly separable as concepts can be a poor place to put a boundary in the implementation. The tell is that one stage applies a distortion and the next applies its inverse: the first stretches a range out, the second compresses it back. Composed on paper, the two cancel and the result is well behaved. Executed as two steps with a materialised value in between, the intermediate lives in the stretched range, where the arithmetic is worst, and the cancellation happens after the damage. Nothing about either stage is wrong in isolation. The defect is entirely in the decision to make the intermediate real.

So the interesting question about a pipeline stage boundary is not whether the two sides are conceptually distinct — they usually are, that is why the boundary was drawn — but what the intermediate value looks like, and whether either neighbour would be better off never seeing it. When one stage's characteristic distortion is undone by the next, fusing them recovers precision that no amount of care on either side alone could recover, and typically also removes work: the composed operation is shorter than the two it replaces, and its rate of change with respect to the inputs, if you need that, collapses to something much simpler than the chain rule over the pieces.

Fusing does not mean abandoning the separation. The right shape is to keep both stages available individually, because they are separately meaningful and separately reusable, and additionally to provide the fused operation as a single named thing — with the fusion documented as the default for the combination, so that the pairing everyone actually uses gets the good implementation without anyone having to know why. This is the same pattern as a query planner collapsing adjacent operators, and it works for the same reason: composition is where optimisation opportunities live, and they are invisible to anyone looking at one operator at a time.

The general prompt is to look at your most common two-step sequences and ask what each step does to the range, the precision, or the size of the data flowing through. Sequences where one step expands and the next contracts, one serialises and the next parses, one sorts and the next takes a prefix, are all candidates for the same treatment. The gain is not shaving a function call; it is that the intermediate — the expensive, badly conditioned, or enormous thing in the middle — stops existing.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the classification-loss section of the neural-nets chapter, which notes that the softmax output layer saturates because one component grows past the others, that pairing it with cross entropy undoes the exponentiation in softmax's definition and thereby avoids the saturation, and that implementations such as TensorFlow therefore expose the two as a single combined operation which is both more numerically stable and simpler to differentiate than the composition of the parts.
