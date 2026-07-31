---
type: lesson
title: "An invariant on the representation lets you conclude things about data you never looked at"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [cognitive-load, hardware-affinity]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# An invariant on the representation lets you conclude things about data you never looked at

**Lesson:** Represent a set as a list with no ordering and membership costs a scan; represent it as a list sorted ascending and the scan can stop the moment it passes the target. The usual reading is that sorting speeds up search. The authors are careful to point out that it does not, in the sense that matters: worst case is unchanged, average case improves by a constant factor, and the growth order is identical. The ordering has bought you almost nothing on that operation.

Then intersection drops from quadratic to linear on the same representation, and the reason is qualitatively different from a faster scan. Comparing the smallest remaining element of each set, if one is smaller than the other, it cannot appear anywhere in the other set — not because you searched and failed, but because the invariant says everything remaining there is larger still. One comparison eliminates an element against an entire collection you never touched. That is what an invariant is actually for: it converts local observations into global conclusions, and the payoff shows up where the algorithm can *discard* work rather than merely stop early.

The distinction is worth carrying around, because it predicts which operations an invariant will help. Adding order to a collection improves membership testing by a factor of two and improves pairwise combination by a factor of n. If you evaluate the change on the first operation you will conclude ordering is not worth the insertion cost; the payoff lives in the operations that relate two structures to each other, where the invariant lets each side reason about the other's untouched remainder. When you are deciding whether to maintain an invariant, ask specifically which operations can use it to rule things out, not which ones can use it to find things faster.

The same logic drives the next step to trees. Comparing against one node discharges an entire subtree, so the number of comparisons tracks the depth rather than the size — and the moment the balance assumption fails the guarantee reverts to a plain ordered list, because a degenerate tree is one whose invariant has stopped ruling anything out. That is the general risk: an invariant you assert but do not actively maintain gives you the cost of maintaining it and none of the elimination power, and the code that relied on it does not fail, it just silently becomes the naive version.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.3.3's progression through sets as unordered lists, ordered lists and binary trees, where the ordered representation is shown to leave element-of-set? at the same order of growth with only a factor-of-two average improvement, while intersection-set drops from a product of the set sizes to a sum because a smaller leading element can be immediately concluded absent from the other set; and the tree section's observation that the logarithmic claim rests on the balance assumption, with the sequential-insertion example producing a tree that has no advantage over an ordered list.
