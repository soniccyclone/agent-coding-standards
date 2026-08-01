---
type: lesson
title: "Know which property of a quantity you consume before you break the rest"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [formal-methods-and-verification, databases-and-data-management]
tags: [lesson]
---
# Know which property of a quantity you consume before you break the rest

**Lesson:** A computed quantity typically satisfies several properties at once: it sums to something, it lies in a range, it obeys a conservation law, it induces an ordering, it has an interpretation in the domain the model came from. Downstream code consumes some subset of these, usually a small one. When a repair or an extension is proposed, the question that decides whether it is acceptable is not "does the quantity still mean what it meant" but "which of these properties does anything actually depend on, and does the repair preserve those." Skipping that question produces both errors: refusing a cheap fix because it breaks an invariant nobody uses, and shipping one that breaks the single invariant something quietly relied on.

The sharp version of this appears when a procedure is extended to cases the original derivation excluded. Removing the awkward parts of the input, solving the clean remainder, and then imputing values back onto the removed parts in reverse order of removal is a good pattern, and it does not preserve the global invariant. The imputed values are computed by the same local rule as the rest but are not competing for a fixed budget, so the totals no longer add up and the quantity is no longer a distribution over anything. That is a genuine loss and it should be stated plainly rather than glossed. It is also, for a consumer who only ever sorts by the value and takes the top few, no loss at all. The relative ordering is preserved, and the ordering was the entire product.

What makes this dangerous rather than merely subtle is that the abandoned property is usually the one that carried the intuition. The model was explained as a distribution, and the explanation is what people remember; the fact that the shipped numbers stopped being one is a detail in a paragraph. Later, someone writes code that assumes normalisation — thresholding on an absolute value, comparing across two runs, treating a component as a probability in a downstream expectation — and it works on the examples they tried, because the violation is small on well-behaved inputs and grows with exactly the structures the repair was introduced to handle. The failure surfaces on the inputs where the fix is doing the most work.

So the discipline has two halves and both are cheap. When you build the quantity, enumerate its properties and mark which ones the consumers use, treating the unmarked ones as explicitly not guaranteed. When you change how it is produced, re-derive that list rather than checking a spot value. The list is short, it takes minutes, and it is the difference between a documented approximation and a latent assumption. It also frees you: an invariant nobody depends on is not a constraint on your design, and knowing which ones those are is where most of the room to manoeuvre turns out to be.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 5's method for restoring recursively deleted dead ends, which computes each restored node's score from its already-computed predecessors in reverse deletion order and then notes that the resulting values sum to more than one and no longer represent the distribution of a random surfer, while still serving as decent estimates of relative importance; the same chapter also observes that with dead ends present the iterated vector's components may sum to less than one.
