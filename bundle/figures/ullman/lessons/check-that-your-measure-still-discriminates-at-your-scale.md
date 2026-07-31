---
type: lesson
title: "Check that your measure still discriminates at the scale you will use it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Check that your measure still discriminates at the scale you will use it

**Lesson:** A measure can be perfectly well defined, satisfy every axiom you would want of it, be computed correctly, and still carry no information at the scale you are applying it. This is not an approximation error or an implementation bug; it is a property of the geometry that emerges as the description of each object gets richer. When objects are described by very many independent attributes, the aggregate difference between any two of them concentrates tightly around a single value, because the aggregate is a sum of many independent contributions and sums of many independent contributions do not vary much. Everything ends up roughly the same distance from everything else. Nothing is close, so the concept of "close" stops distinguishing anything, and any procedure whose whole logic is grouping the close things has nothing to work with.

The important consequence is that this is diagnosable before you build. You do not need to run the clustering and squint at the output; you can reason about how the spread of your measure scales against its typical magnitude as the number of attributes grows, and if the ratio is collapsing, the technique is inapplicable regardless of how it is implemented or tuned. Skipping that check is how teams end up debugging a clustering that was never going to work, tuning parameters against noise, and concluding the data is bad — when in fact the measure is fine, the code is fine, and the regime is wrong. The correct responses are to reduce the description to fewer meaningful attributes, or to find a measure whose contributions are not independent, not to keep adjusting the algorithm.

The same degeneracy is also exploitable, which is the part usually missed. When a regime is degenerate, it is highly predictable, and predictability is leverage. If nearly every pair of directions is effectively unrelated, then compositions of differences obey a simple law that does not hold in the ordinary case, and you can compute a quantity from two others rather than measuring it. Extreme regimes are where cheap approximations become exact enough to build on, so the same analysis that tells you a technique is doomed often tells you which shortcut is now safe.

The habit worth forming is to treat "does this measure discriminate here" as a separate question from "is this measure correct," and to answer it with a scaling argument rather than an experiment. Correctness is about definitions. Discrimination is about the distribution of values your actual population produces, and it can fail silently while every definition holds.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the curse-of-dimensionality section of the clustering chapter, which argues that in high-dimensional spaces random pairs of points are almost all at nearly the average distance, that random vectors are almost always nearly orthogonal, that there is consequently little basis for grouping any pair rather than another, and that the orthogonality lets a third distance be inferred from two others by a rule that fails in low dimensions.
