---
type: lesson
title: "Impose an arbitrary order on the elements and cycles stop being something you check for"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Impose an arbitrary order on the elements and cycles stop being something you check for

**Lesson:** Whenever a structure is built by making one thing point at another, the hazard is a cycle: a chain that closes on itself, at which point every traversal loops forever. The obvious defence is to check before each link, by walking the chain to see whether the destination leads back to the source. That check is correct and it is expensive — it costs a traversal on every update, and worse, it is exactly the traversal you were trying to make cheap.

The alternative is to make cycles unrepresentable rather than detectable. Fix any injective assignment of the elements to a well-ordered set — the identity of the elements themselves will do; nothing about the order needs to mean anything — and add to your structure's stated invariant that a link may only run from a smaller element to a greater-or-equal one. A cycle would require a chain of strict increases returning to its start, which the ordering forbids. Now acyclicity is not a property you verify after the fact; it is a consequence of the invariant, and the only obligation on any update is the local one that this particular link respects the order. That is a comparison instead of a walk.

The move deserves recognition as a pattern because the same trick solves a family of problems that look unrelated. The classic case outside data structures is acquiring several locks: check-then-acquire cannot prevent deadlock, but acquiring in a globally fixed order makes a cycle of waits impossible by the same argument, and the order can be arbitrary because only its consistency matters. The general form is this: when a global structural property is expensive to check, look for a cheap local quantity that changes monotonically along the structure, and put its monotonicity in the invariant. The global property then falls out for free, and every update is checked in isolation.

Two things to notice when applying it. The quantity must be genuinely cheap — the whole point is to avoid computing something like the depth of a chain, which would require the traversal you were avoiding. And the ordering is a real commitment: it constrains which links may be made, so you must confirm that every update your design needs is still expressible under it. Where it is not, you have learned something about the design rather than merely failing to apply a trick.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 13's "Cleaning up Forests" section, in the discussion of the tree-compressing variant of the equivalence-relation algorithm: the identification of the danger of creating rings when the two elements being equated are already in the same tree, the remark that the depth of the tree would be an adequate criterion but would require pre-tracing of the tree, and the resulting use of an auxiliary ordering system — a one-one mapping of the elements onto the natural numbers, with the condition that each element's order does not exceed that of the element it points to conjoined to the data type invariant, equality occurring only at roots because the mapping is injective, from which the property that reachability implies ordering follows directly.
