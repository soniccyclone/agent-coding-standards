---
type: lesson
title: "A nonnegative encoding cannot express disagreement — centre it before comparing"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# A nonnegative encoding cannot express disagreement — centre it before comparing

**Lesson:** If every observation is recorded on a scale that runs from a little to a lot, with no way to record opposition, then no comparison built on those numbers can ever say that two parties are opposed. Directionally, all the data points into the same region, and the strongest possible statement about a pair is that they overlap weakly. Opposition is not merely hard to detect in such an encoding; it is not representable in it, and no cleverness in the comparison function recovers what the representation cannot hold. This is a limit of the coordinate system, and the fix is to change the coordinate system.

Subtracting each party's own average from their observations does exactly that, and it is not a normalisation detail but a change in what the data can say. Values above a party's own baseline become positive, values below become negative, and two parties who reacted oppositely to the same things now point in opposite directions rather than merely failing to overlap. The comparison suddenly has a full range to work with: strong agreement, no relationship, and strong disagreement become three distinguishable outcomes instead of two.

The same subtraction removes a bias that otherwise contaminates everything. Parties differ systematically in how they use a scale — some record generously, some harshly — and on the raw numbers that difference dominates the genuine signal, so a generous party looks similar to every other generous party regardless of content. Centring removes the per-party offset and leaves only the relative structure, which was the actual information. It also means that when you use the comparison to predict, you must undo the transformation: estimate the deviation and add back the target party's own baseline, or you will report everyone's predictions on the wrong scale.

A pleasing side effect is that the transform makes uninformative contributors self-identify. A party whose observations are all the same value centres to all zeros, which contributes nothing to any comparison and correctly so — someone who never discriminated between anything told you nothing about their preferences, and the encoding now says so arithmetically instead of quietly injecting a constant into every calculation. Watch for that pattern generally: a good representation makes empty evidence look empty, rather than making it look like agreement with whatever is nearby.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the normalising-ratings discussion in the collaborative-filtering part of the recommendation-systems chapter, where subtracting each rater's mean turns low scores negative so opposed raters land in nearly opposite directions, where a rater who gave every item the same score reduces to all zeros, and where the prediction procedure averages the neighbours' deviations and adds back the target's own average.
