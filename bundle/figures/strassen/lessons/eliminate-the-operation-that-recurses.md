---
type: lesson
title: "In a self-applicable construction, only the operations that recurse set the growth rate — spend freely on the ones that do not"
figure: strassen
works: [gaussian-elimination-is-not-optimal]
axes: [primitive-count, hardware-affinity]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# In a self-applicable construction, only the operations that recurse set the growth rate — spend freely on the ones that do not

**Lesson:** A cost model that treats all elementary operations as interchangeable is adequate for a flat algorithm and actively misleading for a recursive one. Once a method is defined so that it invokes itself on subparts, its operations split into two populations that behave nothing alike: those whose arguments are subproblems, which turn into recursive calls and therefore compound at every level, and those that merely combine results, which stay cheap and local no matter how deep the recursion goes. Counting them together hides the only distinction that matters. The right question about any step is not "how expensive is this" but "does this step reproduce the problem at smaller scale."

That distinction converts a trade nobody would take in the flat setting into a decisive win. Restructuring a fixed, tiny case to use one fewer of the compounding operation at the price of a handful more of the cheap ones looks like a wash — until the construction is applied to itself, at which point the saved operation is a saved subtree and the extra cheap ones are a bounded surcharge per level. The branching factor of the recursion, not the total operation count of the base case, is what appears in the exponent. Small local ugliness in the base case is bought back with interest at every level of depth; local elegance that leaves the branching factor alone buys nothing at all.

Generalized: before optimizing a recursive procedure, work out which of its operations sit on the recursion's fan-out and which sit in the merge. Then apply effort strictly to the first population and stop worrying about the second. This is also a design instruction, not just an analysis one — when you are free to choose how a problem decomposes, choose the decomposition that minimizes how many subproblems you spawn, even if it makes the gluing arithmetic messier, and even if the messiness makes the base case unrecognizable to someone reading it as a standalone routine.

**Source:** [Gaussian Elimination is not Optimal](../works/gaussian-elimination-is-not-optimal.md) — the inductive definition of the multiplication algorithms, where the block-level products (which are recursive invocations) are reduced in number while the block-level additions and subtractions (which are not) are allowed to increase, and the resulting operation count where only the number of products appears raised to the recursion depth.
