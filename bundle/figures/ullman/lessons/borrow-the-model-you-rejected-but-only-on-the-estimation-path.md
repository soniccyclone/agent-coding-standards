---
type: lesson
title: "Borrow the model you rejected, but only on the estimation path"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Borrow the model you rejected, but only on the estimation path

**Lesson:** A design will sometimes announce, correctly and for good reasons, that it cannot assume some rich structure — the data is not numeric, the objects cannot be averaged, the space has no coordinates. Having said that, the design is then free to turn around and use a property of that rejected structure anyway, provided it uses it in one specific place: to guess a number it would otherwise have to go and fetch. This looks like cheating and is not, because rejecting a model for the purposes of *definition and correctness* is a different act from borrowing it for the purposes of *estimation*. The first governs what the system is allowed to claim; the second governs how it fills in a value it cannot afford to compute. Keeping the two scopes separate is what makes the move honest rather than sloppy.

The argument that licenses the borrowing has to be made explicitly, and it is usually an argument about regime rather than about kind. The claim is not "this space is secretly the rejected one" but "in the regime we actually operate in, the two agree closely enough on the quantity we are estimating." That is a testable statement about a statistic, not a category error, and it comes with a stated failure condition: leave the regime and the estimate degrades. Anyone reading the design should be able to find that sentence. Where it is missing, what looks like a principled approximation is just an unexamined assumption inherited from whichever framework the author was trained in, and it will be silently wrong in exactly the cases the framework was rejected for.

The engineering payoff is that the borrowed law lets you derive a value from values you already hold instead of returning to the underlying data. A quantity aggregated over an entire collection can be recomputed for a new member from the aggregate plus one measured distance, because the borrowed law says how the contributions compose. That converts an operation whose cost scales with the collection into one of fixed cost, which is frequently the difference between a scheme that fits in memory and one that does not. It is worth noticing that the same law then gets reused for a second, structurally different operation — combining two collections — because a compositional law, once you have accepted it, applies wherever the composition appears.

The discipline to attach is bookkeeping about which values in the system are measured and which are inferred under the borrowed law. Inferred values are fine to act on and dangerous to accumulate, because each one carries the borrowing's error and nothing in their representation distinguishes them from measured ones. So the right companion to this technique is a path back to the ground truth — a periodic recomputation from the real data — and a clear statement of which fields it repairs.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 7's GRGPF algorithm, which is built specifically for spaces where no averaging exists, yet estimates a new point's aggregate squared distance by assuming the angle at the representative is a right angle and invoking the Pythagorean theorem, justified by the observation that non-Euclidean spaces typically behave like high-dimensional Euclidean ones where almost all angles are right angles, and which reuses the same assumption to derive aggregate distances for a merged cluster.
