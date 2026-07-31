---
type: lesson
title: "Pin down the freedom a representation leaves you"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, algorithms-and-complexity]
tags: [lesson]
---
# Pin down the freedom a representation leaves you

**Lesson:** Many representations do not determine a unique value for the thing they represent. A direction is unchanged by scaling and by reversal; a rotation has multiple angle encodings; a set has many orderings; a fraction has many numerators. Whenever the defining condition is satisfied by a whole family of encodings, the family is real and the code will encounter every member of it. That is fine as long as everything downstream only asks questions the representation actually answers. It stops being fine the moment anything compares two encodings, hashes one, caches on it, diffs it, or asserts equality — because then answers depend on which member of the family showed up, and the resulting bugs are intermittent and correlated with irrelevant details like input order or library version.

The fix is to pick a canonical member and normalise to it at the boundary. Doing so has two parts, and the second one is the part people skip. First remove the continuous freedom: fix the magnitude, fix the units, fix the scale. Then remove whatever discrete freedom remains, which is usually a small residue like a sign or an ordering, by an arbitrary but stated rule — require the first nonzero component to be positive, sort the members, take the smaller representative. Handling only the continuous part feels like completion and leaves exactly the intermittent-mismatch bugs you were trying to prevent, since the two encodings now agree in magnitude and still fail equality.

Two things follow. The canonical rule must live in one place, applied at construction, rather than being reimplemented by each consumer — a normalisation that some call sites perform and others do not is worse than none, because it makes the failures rarer and therefore harder to find. And the choice of canonical form is arbitrary, which means it should be documented as a convention rather than justified, and it may be locally suspended for good reason: presenting a result in a non-canonical form because it reads better is legitimate, as long as the suspension is visible and does not reach anything that compares.

The habit worth forming is to ask, of every representation you introduce, what transformations leave the represented thing unchanged. That set is the freedom you have to pin down. It is also, incidentally, the set of transformations your tests should be invariant under, which makes the same analysis useful twice.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the definitions section of the dimensionality-reduction chapter, which observes that any scalar multiple of an eigenvector is also an eigenvector, requires unit length to remove the scale ambiguity, notes that this still leaves the sign free, adopts the convention that the first nonzero component be positive, and later deliberately violates that convention in a worked example where the opposite sign made the coordinate change easier to follow.
