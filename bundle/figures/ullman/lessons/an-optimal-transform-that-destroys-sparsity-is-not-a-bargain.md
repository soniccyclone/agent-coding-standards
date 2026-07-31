---
type: lesson
title: "An optimal transform that destroys sparsity is not a bargain"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, expressiveness]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# An optimal transform that destroys sparsity is not a bargain

**Lesson:** Optimality is always stated with respect to a quantity, and the quantity is rarely the one that decides whether you can run the thing. A decomposition can be provably the best possible reconstruction for a given number of components and still be unusable, because its factors do not inherit the structural property that made the original data tractable. Sparsity is the standard case: input in which almost every entry is absent can be stored in space proportional to what is present, but the factors of an exact decomposition are generally dense, so a representation advertised as smaller in its stated dimension is enormously larger in bytes. The claim was never false; it was measured in the wrong unit.

The generalisable point is that real data is almost always cheap to handle because of some property beyond its nominal size — mostly empty, mostly sorted, mostly local, mostly unchanged from last time — and any transformation you apply either preserves that property or silently spends it. Preservation is not automatic and is usually not mentioned, because the analysis of a transformation is conducted in terms of dimensions and error, where the property is invisible. So it has to be checked deliberately: take the transformation, apply it to a small structured example, and look at whether the outputs still have the shape the inputs had.

When the property is not preserved, the useful response is to look for a construction that builds its factors *out of* the original data rather than out of synthesised combinations of it. Choosing actual rows and actual columns as the basis, rather than linear mixtures of them, guarantees that the factors are exactly as sparse as the parts of the input they were taken from — and, as a side effect, keeps them interpretable, since each component is a real entity rather than a blend. The price is that such a decomposition is approximate no matter how many components you allow, where the mixture-based one becomes exact. That is the trade in its plainest form: give up exactness to keep the structural property, and the trade is worth it whenever the property is what makes the data fit in memory at all.

The habit is to add one question to the evaluation of any transformation: what does it do to the property my system depends on? Optimality in error, cost, or dimension count is the advertised axis. Structure preservation is usually the deciding one, and it is almost never on the label.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the opening of the CUR-decomposition section in the dimensionality-reduction chapter, which notes that large real matrices are typically very sparse, that the singular-value decomposition's two large factors are dense even when the input is not, and that CUR is adopted precisely because building its large factors from actual columns and rows of the input keeps them sparse — at the cost of being approximate for any number of components.
