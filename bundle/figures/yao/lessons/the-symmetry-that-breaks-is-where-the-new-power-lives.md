---
type: lesson
title: "When you generalize a theory, the invariant that breaks is where the new power lives"
figure: yao
works: [theory-and-applications-of-trapdoor-functions]
axes: [expressiveness, verifiability]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# When you generalize a theory, the invariant that breaks is where the new power lives

**Lesson:** Generalizing a theory is usually pitched as a gain in coverage, and the natural instinct is to inventory what the generalization preserves. The inventory worth making is the opposite one. Find the identity that the old theory guaranteed and the new one does not, because a lost identity is a degree of freedom, and a degree of freedom is something to build with. The classical relation between two coupled quantities may be perfectly symmetric — whatever one reveals about the other, the other reveals in equal measure — and that symmetry silently forecloses whole categories of mechanism. Add a resource bound to the same relation and the symmetry has no reason to hold: one direction can be effortless while the reverse direction is not, even though both directions are trivial in the unbounded account. Everything asymmetric you might want, including the possibility that a transformation can be published for anyone to apply while remaining unusable in reverse, lives exactly in that break.

The break also reorganizes how the object should be pictured. The same map, seen from the side that holds the extra knowledge, moves data faithfully; seen from the side that does not, it introduces genuine uncertainty. So the map is not one thing with a property, it is two different things depending on which end you are standing at, and the interesting engineering is the deliberate arrangement of who stands where. Notice, though, that the asymmetry disappears at the degenerate value: when one direction leaks essentially nothing, so does the other. The exploitable regime is therefore the interior, not the boundary, which is a general caution — the properties you gain by relaxing a theory tend to be invisible in exactly the extreme cases where the old theory and the new one agree, and those are the cases people check first.

Applied outside this setting, the habit is to interrogate your own generalizations for lost algebra. Adding partial failure to a computational model breaks the composition law that made two steps interchangeable; adding a time budget breaks the equivalence of two encodings of the same value; adding untrusted participants breaks the symmetry of a protocol's roles. Each break looks like damage in a proof and is actually an inventory of new constructions, and the ones nobody has spent are where the unclaimed capability is.

**Source:** [Theory and Applications of Trapdoor Functions](../works/theory-and-applications-of-trapdoor-functions.md) — the mutual-information section of Part 1, which recalls that the classical mutual information of two random variables is symmetric, states that the computational analogue is not, and identifies that asymmetry as what makes public-key cryptography possible, together with the theorem recovering near-symmetry in the vanishing case and the later "what makes the trapdoor work" analysis, which reads a single one-way map as a noiseless channel from the sender's viewpoint and a noisy one from the eavesdropper's.
