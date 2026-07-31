---
type: lesson
title: "Absorb a special parameter as an ordinary dimension"
figure: ullman
works: [mining-of-massive-datasets]
axes: [primitive-count, cognitive-load]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Absorb a special parameter as an ordinary dimension

**Lesson:** Procedures frequently carry one quantity that is structurally different from all the others — a threshold the rest of the values are compared against, an offset applied at the end, a base case the recursion is measured from. Because it is different in kind, it tends to be handled by a separate mechanism: fixed by hand, tuned in an outer loop, or given its own bespoke update rule. Each of those is a second thing to build, maintain, and reason about, and it is often unnecessary. Extend the representation by one slot, pin the corresponding input to a constant, and the odd parameter becomes an ordinary member of the vector the existing machinery already handles.

The check that makes this legitimate is a small algebraic identity: expand the extended computation and confirm it reduces exactly to the original comparison with the parameter in its old role. That takes a line, and it is worth doing explicitly, because the whole trick rests on it. Once confirmed, everything the general mechanism provides applies to the special parameter for free — it is learned rather than chosen, it is updated by the same rule, it is stored in the same structure, and every proof about the general mechanism covers it.

The cost is one dimension and one loss of specialness, and it is worth being honest that the second is sometimes a real loss. If the mechanism's update rule makes assumptions about the range or sign of its inputs, the constant you pinned may violate them, and the parameter then needs a small local adaptation — its adjustment inverted, its range clamped — which is a much smaller carve-out than a separate mechanism but not nothing. Notice that this is the price of unification, not evidence against it.

The habit generalises well past this setting. Whenever a configuration value is being managed by a path that exists only for it, ask whether the general path could carry it if the representation were one slot wider. Constant terms folded into linear systems, homogeneous coordinates that make translation a multiplication, sentinel elements that erase the empty case — all are the same move, and all pay off the same way: one mechanism instead of two, and the special case stops being special.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the section on allowing the threshold to vary in the perceptron chapter, which appends the threshold to the weight vector and a constant of minus one to every feature vector, verifies that the extended dot product being positive is exactly the original comparison against the threshold, and notes that the multiplicative variant of the training rule must treat the appended component in the opposite direction because it requires nonnegative features.
