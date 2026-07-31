---
type: lesson
title: "Repairing a shared lemma is not done until every use of it has been rechecked individually"
figure: scott
works: [continuous-lattices]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture, foundations-of-computation]
tags: [lesson]
---
# Repairing a shared lemma is not done until every use of it has been rechecked individually

**Lesson:** A convenient intermediate claim gets stated once and then leaned on in several later arguments, which is exactly what it is for. When it turns out to be false, the repair has two halves and only the first is obvious. The first is fixing the claim: find the missing hypothesis, restate it, and confirm that the corrected version is true — usually a small edit, because the claim was nearly right. The second is going to every place the old version was used and showing, separately at each one, that the added hypothesis actually holds there. Skipping the second half leaves a document or a system that is locally correct everywhere and globally unsound, because a downstream argument that quietly needed the false version is indistinguishable, from the outside, from one that did not.

The rechecking is not a formality, and the reason is that the added hypothesis will not hold uniformly. In Scott's correction the same repaired remark is used at three sites and each requires a different argument: at one it follows immediately from the shape of a basis, at another the relevant inequalities point the wrong way and the repair has to be routed through a retraction and a different class of open sets, and at the third the hypothesis is free because the relevant limits are computed pointwise. Three uses, three distinct verifications, one of them genuinely more delicate than the original claim. Had the author only patched the statement, one of those three would have been left with no justification at all, and nothing in the text would have shown it.

This is the same discipline as fixing a bug in a shared function rather than at the one call site that reported it, with the second half made explicit: after you tighten the shared thing's contract, every caller inherits a new obligation, and each one has to be examined on its own terms because each satisfies the new precondition for a different reason, or fails to. The published correction is also a model of how to record this — the false remark, the counterexamples, the added hypothesis, and then a site-by-site walk through the affected proofs, so a reader can verify the repair is complete rather than take it on trust.

**Source:** [Continuous Lattices](../works/continuous-lattices.md) — the Correction added March 1972 after Robin Milner pointed out that the remark preceding Proposition 2.5 was false, which supplies counterexamples, adds the hypothesis that the given topology be contained in the induced lattice topology, and then re-establishes each of the three propositions (2.9, 2.10, and the function-space theorem) that had used it, with a separate argument for each and an explicit note that in one case the inequalities run the wrong way.
