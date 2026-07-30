---
type: lesson
title: "Push what the outer layer knows about access frequency down into the inner structure"
figure: tarjan
works: [a-data-structure-for-dynamic-trees]
axes: [hardware-affinity, expressiveness]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Push what the outer layer knows about access frequency down into the inner structure

**Lesson:** With an ordinary balanced structure holding each path, the overall bound came out with a squared logarithm, and the reason is instructive: a balanced structure charges the same depth for every element because it has been told nothing about which elements matter. But the outer layer knows something. It knows how much of the whole forest hangs beneath each vertex, and that quantity predicts how often the vertex will be on a path someone walks. Feeding that number down as a per-element weight, and using a structure that places heavy elements nearer the top, changes the cost of reaching an element from the logarithm of the collection's size to the logarithm of the collection's weight *divided by the element's own weight*. Heavy elements become cheap to reach. Because the traversals that matter climb from a light element toward heavier ones, the per-step costs become differences of the same monotone quantity, the sum along a whole walk telescopes, and the extra logarithm disappears.

The generalizable point is about an information flow that layering tends to block. A well-designed lower layer knows nothing about its caller, which is what makes it reusable — and also what forces it to assume the worst, namely that all accesses are equally likely. That assumption is almost never true, and the caller almost always has a cheap estimate of the truth: a size, a hit count, a recency, a fan-out. The fix is not to break the layering but to widen the interface by one parameter, so the estimate can be *passed* rather than guessed. A structure that accepts weights is still general; it simply stops pretending ignorance when the caller has knowledge. Uniform treatment of non-uniform data is a very common source of an unnecessary logarithmic factor, and it hides behind the word "balanced," which sounds like a virtue.

Two cautions come with it. The weights must be a real proxy for the access pattern, and the proxy has to be maintained as the structure changes, which is genuine bookkeeping — here the weights shift whenever the forest is re-carved, and the paper is careful to confine all weight updates to the two operations that restructure things. And the guarantee you get is about the *distribution*, not about any single access: an element that is light will be expensive to reach, and that is the point rather than a defect. If the caller's estimate is wrong, the structure faithfully optimizes for the wrong thing, which is a stronger dependency on the caller than a uniform structure has. Passing information down the stack buys performance and costs you a correctness-adjacent obligation to keep that information true.

**Source:** [A Data Structure for Dynamic Trees](../works/a-data-structure-for-dynamic-trees.md) — the theorem bounding the running time at a squared logarithm when solid paths are held in standard balanced binary trees, the substitution of biased binary trees whose external nodes carry caller-supplied weights, the definition of a vertex's weight from its descendant count in the enclosing forest, the depth bound expressed as a logarithm of the ratio of tree weight to node weight, and the telescoping of the per-splice rank differences that removes the extra logarithmic factor.
