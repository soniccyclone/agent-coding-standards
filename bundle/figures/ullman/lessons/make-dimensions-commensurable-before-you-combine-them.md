---
type: lesson
title: "Make dimensions commensurable before you combine them, and set the threshold in meaningful units"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Make dimensions commensurable before you combine them, and set the threshold in meaningful units

**Lesson:** Combining several measurements into one number by summing their contributions is only meaningful if the contributions are on comparable scales, and raw measurements almost never are. When they are not, the aggregate is dominated by whichever component happens to have the largest natural range, and every decision made from it is effectively a decision about that one component with the others as decoration. This is not subtle statistical error; it is a units mistake, and it survives arbitrarily careful implementation because nothing in the arithmetic complains about adding incommensurable things.

The correction is to divide each component by a measure of how much that component varies within the population you are comparing against, before combining. What this does conceptually is change every component from an absolute quantity into a question about surprise: not "how far apart on this axis" but "how unusual is being this far apart on this axis, given how this axis normally behaves here." Those are commensurable by construction. Note that the reference for the normalisation should be the specific group you are testing membership in, not the population at large — a component that is tightly controlled within the group and wildly variable overall carries a lot of information about membership, and normalising by the global spread throws exactly that information away.

The second dividend is that the composite threshold becomes interpretable. Expressed in raw units, "reject beyond distance seven" is a number with no defence. Expressed in units of the group's own variability, the same threshold corresponds to a stated probability of wrongly excluding a genuine member, so you choose it by deciding what error rate you will accept and reading off the corresponding value. That turns an unjustifiable constant into a stated policy, and it makes the constant transferable to other datasets with different scales, where a raw threshold would have to be retuned.

The precondition worth checking is that the components vary independently. Normalising each axis separately assumes the group's spread is aligned with the axes you are measuring — that knowing one component tells you nothing about another. When components move together, per-axis normalisation under-corrects and the composite is still skewed, and you either need the full correlation structure or a change of coordinates. Knowing that the technique carries this assumption, and being able to say whether your data satisfies it, is the difference between using it and cargo-culting it.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the Mahalanobis-distance discussion in the Bradley-Fayyad-Reina section of the clustering chapter, which normalises each coordinate difference by the cluster's own per-dimension standard deviation, relies on the assumption that the cluster's spread is axis-aligned, and picks the acceptance threshold by reading off the corresponding tail probability under a normal model.
