---
type: lesson
title: "A series of mutually exclusive solutions degrades by construction"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# A series of mutually exclusive solutions degrades by construction

**Lesson:** Many methods produce not one answer but an ordered sequence of them, where each successive answer optimises the same criterion subject to being different from — formally, independent of — all the answers before it. Principal directions of variation, successive cuts, ranked alternative explanations, diverse recommendation slates: all have this shape. The temptation is to read the sequence as a set of coequal findings, take the first several, and combine them. They are not coequal. The first answer is optimised under one constraint; the fifth is optimised under five, and every added constraint can only make the achievable score worse. Quality decays monotonically along the sequence as a mathematical consequence of how the sequence is defined, independently of anything in your data.

That has a direct consequence for how many to take. There is no threshold in the method itself that tells you when the answers stop being worth having, because the method computes the k-th one just as dutifully as the first. The decision is yours and must be made against something outside the sequence — evaluating each answer under the original objective you cared about and watching where the score falls off a cliff, for instance. Combining several answers compounds this: crossing k of them to produce finer structure yields up to two-to-the-k groupings, most of them driven by the later, weaker answers, and the result can be far more finely divided than the data supports while looking like a richer analysis.

There is also a subtler point about what the independence constraint means. Each later answer is required to be different from the earlier ones, which is a statement about the search, not about the world. If the phenomenon genuinely has two comparably good and largely overlapping explanations, the method cannot report them both; it reports the first and then something forced to be unlike it. So the diversity in the sequence is manufactured, and treating it as evidence that the underlying structure is diverse is reading an artifact of the constraint as a finding.

The habit worth keeping is to ask, of any ranked family of results, what makes the entries different from each other. If the answer is "the method required them to be," the ranking is a decay curve and should be truncated by external judgement — not a menu whose entries can be picked from freely.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the alternative-partitioning discussion in the social-network chapter, which notes that each eigenvector after the first minimises the same quadratic form subject to orthogonality with all previous eigenvectors, that the accumulating constraints make successive cuts progressively worse, and that thresholding m eigenvectors yields 2^m groups — illustrated by a six-node graph split into four groups that the text calls too fine to be meaningful.
