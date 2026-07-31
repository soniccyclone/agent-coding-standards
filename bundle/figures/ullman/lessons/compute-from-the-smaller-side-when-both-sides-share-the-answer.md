---
type: lesson
title: "Compute from the smaller side when both sides share the answer"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Compute from the smaller side when both sides share the answer

**Lesson:** A relation between two populations can be summarised from either end — by how the members of one population relate to each other through the second, or the reverse. These two summaries are different sizes: one is square in the number of entities on the left, the other square in the number on the right, and in real data those counts often differ by orders of magnitude. Before doing any work, it is worth asking whether the thing you actually want is recoverable from either summary, because if it is, you have a free choice and one of the options may be thousands of times cheaper to form and to analyse.

The case where this is exact rather than approximate is more common than it looks, and the argument for it is short enough to reconstruct rather than memorise. If a quantity characterises one summary, applying the relation to it produces a quantity characterising the other, with the same magnitude attached; the derivation runs in both directions, so the two summaries carry the same set of magnitudes. The only difference is that the larger summary has extra slots to fill, and they are filled with zeros — degenerate entries that certify emptiness and carry no information. Nothing was lost by choosing the smaller side; the surplus in the larger one was always vacuous.

Two things follow for practice. First, when you find yourself forming a summary whose size is quadratic in the larger of two dimensions, treat that as a smell and check for the transposed formulation. This is one of the few optimisations that is simultaneously a large asymptotic win and a provably exact rewrite, which makes it strictly better than the approximations people usually reach for at that point. Second, the correspondence gives you a cheap consistency check: compute on the small side and confirm that the magnitudes you get are the ones the large side would have produced, with the remainder accounted for as degenerate. An identity that must hold exactly is the best kind of test to have for numerical code.

More broadly, this is the habit of noticing when two apparently different computations are two views of the same underlying object. The tell is that a derivation converts one into the other with nothing thrown away. When that holds, the choice between them is pure cost, and cost is the only thing that should decide it.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the matrix-of-distances section in the dimensionality-reduction chapter, which observes that forming the product of the data matrix with its transpose in either order gives a symmetric matrix of different size, derives that an eigenvector of one yields an eigenvector of the other with the same eigenvalue by multiplying through, handles the degenerate case, and concludes that the larger product's spectrum is the smaller one's plus additional zeros.
