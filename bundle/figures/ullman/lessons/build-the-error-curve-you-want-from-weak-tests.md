---
type: lesson
title: "Build the error curve you want by composing tests too weak to use alone"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Build the error curve you want by composing tests too weak to use alone

**Lesson:** A test that is only slightly better than a coin flip is not useless — it is raw material. Require several such tests to agree and you push every probability down, hardest on the ones that were already low. Accept any one of several agreeing and you push every probability up, hardest on the ones that were already high. Layer the two constructions and the composite behaves nearly like the step function you wanted in the first place: almost always yes above some threshold, almost always no below it, with the location of the threshold and the steepness of the transition both set by how many components you used and how you nested them. The individual test never improves. What improves is the shape of the decision, and the shape is something you compose rather than something you find.

Two consequences matter more than the construction itself. The first is that this reframes what a useful primitive is. You do not need a good discriminator; you need one whose agreement probability is monotone in the quantity you care about, plus independence across draws. That is a far weaker requirement, which is why it can be satisfied for wildly different notions of closeness — bit disagreement, angle between directions, distance in space — by primitives as crude as "look at one randomly chosen coordinate" or "which side of a random hyperplane." Whenever you can exhibit such a primitive, the whole amplification apparatus comes along for free, and when you cannot, no amount of tuning substitutes. The second consequence is that the two kinds of error become a design choice rather than an outcome. Missing a true match and examining a false one have different costs in different applications, and shifting the threshold or reordering the layers moves cost from one to the other deliberately. That is a conversation about the application, held before the code is written, and its answer is a parameter.

There is a price the construction makes explicit and honest: sharpening the curve multiplies the number of component evaluations, so accuracy is bought in units of work with a visible exchange rate. That visibility is the point. A programmer who thinks this way stops looking for the one clever test that is right, and instead asks what cheap monotone signal they have, how they want the error split, and how much compute they are willing to spend to sharpen the boundary — three separable questions instead of one intractable one.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the similarity chapter's theory of locality-sensitive function families, where banding is generalised into conjunctive and disjunctive constructions over a sensitivity quadruple, illustrated by cascading them in both orders and by fingerprint matching where the false-positive and false-negative rates are traded against each other explicitly.
