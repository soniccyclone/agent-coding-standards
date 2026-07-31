---
type: lesson
title: "Whether you can synthesize a summary is a property of the space, not of your algorithm"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Whether you can synthesize a summary is a property of the space, not of your algorithm

**Lesson:** A great many algorithms are built on a step that quietly assumes you can manufacture a new object of the same type from a collection of existing ones — an average, a merge, a fused representative that stands in for the group and is itself a legal member of the space. That capability is not universal. It exists when the space carries the algebra to support it, and it simply does not exist otherwise, no matter how the algorithm is written. Where it is missing, you cannot fix it by approximating; you have to replace synthesis with selection, promoting one actual member to speak for the group. Recognising which of these two worlds you are in, early, prevents a design that is quietly impossible.

The two worlds behave differently in ways that ripple far past that one step. A synthesised representative is unconstrained by the data — it can sit anywhere, including where no member sits, so it is a genuinely compact summary whose accuracy does not depend on any member happening to be well placed. A selected representative is constrained to the observed members, so its quality depends on whether a suitable one exists, and choosing it requires its own criterion — the member that minimises the worst distance to the others, or the total, or the total of squares — each a defensible and different choice that will produce different groupings. In the synthesis world that choice does not exist, which is why moving from one world to the other adds a decision you did not previously have to make and cannot avoid.

The general form is that you should ask what operations your data type supports before choosing techniques over it, and treat the answer as a hard constraint rather than an inconvenience. Can two values be combined into a third of the same type? Is there an identity? Is the combination associative, so it can be applied in any grouping? Each of those questions gates a whole family of methods — averaging, parallel reduction, incremental maintenance, hierarchical summarisation — and the honest answer for many practical data types is no. Discovering that after choosing the algorithm produces the familiar disaster where a system works on the prototype's numeric data and cannot be made to work on the real data, which is strings or sets or sequences.

The complementary point is that when the algebra is absent you can sometimes install it rather than abandon the technique — by embedding your objects into a space that does support combination, at some cost in fidelity. That is a real option and a real trade, and it is the kind of decision that should be made deliberately and recorded, because everything downstream inherits whatever the embedding distorted.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the introductory section of the clustering chapter, which identifies the ability to summarise a group by its centroid as the key distinction between Euclidean and non-Euclidean settings and notes that without it a different means of summarising a cluster must be developed.
