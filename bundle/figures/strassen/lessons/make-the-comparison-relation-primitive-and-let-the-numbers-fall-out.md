---
type: lesson
title: "Make the comparison relation the primitive object, and let the numeric measures fall out as extremes of it"
figure: strassen
works: [relative-bilinear-complexity-and-matrix-multiplication]
axes: [primitive-count, expressiveness]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Make the comparison relation the primitive object, and let the numeric measures fall out as extremes of it

**Lesson:** A numeric cost attached to an object is a lossy summary of something richer: the relation "this object can be obtained from that one." Define that relation directly — one object is below another when there is a transformation carrying the second onto the first — and you have a partial order on the whole class of objects rather than a function from objects to numbers. The number is then recoverable as an extremal fact about the order: the cost of an object is the least member of a distinguished reference family that still sits above it. Nothing is lost, and what is gained is that everything you knew about the number becomes a corollary of order properties, proved once at the level of the relation instead of separately for each measure.

The economy compounds because the order supports several measures at once. The same relation, read in the other direction, yields a second measure with a different meaning; refined into a coarser or finer relation, it yields further measures that automatically satisfy the same monotonicity, subadditivity, and behaviour under combination — none of which have to be re-derived. Facts that look like arithmetic accidents when stated about numbers turn out to be immediate: a measure is monotone because the order is transitive; it is subadditive because the order respects sums. Once the relation is the primitive, the proofs shrink to a page and the vocabulary generalizes to objects nobody had assigned a number to yet.

The general instruction is to notice when you have been reasoning about a metric and ask what relation it is a summary of. Comparability between objects is more informative than any ranking derived from it, and it is often easier to establish: showing that one thing can be built from another is a construction, whereas showing its cost is some number requires an optimization. Design your definitions so that the constructions are the primary evidence and the numbers are read off at the end. A theory phrased in orders also survives incomparability honestly, where a theory phrased in numbers is forced to invent a total ranking that the subject matter does not have.

**Source:** [Relative Bilinear Complexity and Matrix Multiplication](../works/relative-bilinear-complexity-and-matrix-multiplication.md) — sections 3 and 4, where restriction and degeneration are defined as preorders on tensor classes and rank and border rank are then characterized as the least reference object dominating a given one, after which the standard properties of both measures are obtained as properties of the orders.
