---
type: lesson
title: "A word borrowed from an ideal case carries relationships that do not survive"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# A word borrowed from an ideal case carries relationships that do not survive

**Lesson:** Technical vocabulary is routinely lifted from a clean special case and applied to messy general objects. The definitions transfer fine; the *relationships between* the definitions do not, and nobody notices, because the relationships were never written down — they were properties of the ideal case that everyone absorbed as part of the meaning of the words. Two quantities that stood in an exact ratio for the ideal object stand in no fixed relation for the general one, merely a tendency to be roughly proportional. Anyone who reasons from one to the other, or who assumes a bound on one implies a bound on the other, is applying a theorem about circles to something that is not a circle.

The compounding problem is that such words rarely name a single formula. The same term will cover a maximum in one paper, an average in another, a root-mean-square in a third, each defensible, each producing different numbers on the same data, all of them called by the identical name with a definite article as though it were canonical. This is not a documentation failure to be tidied up later; it is a live correctness hazard, because every threshold, every published constant, and every comparison against a competing method is stated in units of one particular unstated choice. Importing a constant from a paper or a neighbouring module without importing its definition is one of the more reliable ways to build something that is subtly wrong and passes review.

Two habits follow and they are cheap. First, wherever a system stores a constant expressed in such a term, keep the definition adjacent — in the name, in a comment, in the type — so that the constant cannot be moved without its meaning. Second, when introducing a general version of a familiar quantity, state explicitly which of the old relationships still hold and which do not. Saying that these two measures are no longer related by a factor of two, and giving the reason, costs one sentence and prevents a class of error that is otherwise found only by someone reconciling two numbers that should have agreed.

The same care applies to a word that has been overloaded outright, where one document uses one term for two unrelated things because both fields got there first. The correct response is not to hope context disambiguates but to flag it at the point of collision, since a reader who has resolved the ambiguity wrongly will not experience confusion — they will experience confident misunderstanding, which produces no question to answer.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 7's definitions of cluster radius and diameter, which note that the two are not directly related as they are in a circle though they tend toward proportionality, work an example where the diameter is not quite twice the radius and explain that the centroid does not lie on the line between the two extreme points, warn that several variant definitions are all referred to elsewhere as "the radius", and separately footnote that the word "cluster" carries two entirely different meanings within the parallelism section.
