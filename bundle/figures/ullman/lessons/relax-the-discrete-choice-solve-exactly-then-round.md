---
type: lesson
title: "Relax the discrete choice, solve exactly, then round"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Relax the discrete choice, solve exactly, then round

**Lesson:** A great many hard problems are hard because of a discreteness that is incidental to what you actually want. Each element must go entirely to one side or the other; each request must be accepted or refused; each item must be in or out. The combinatorial explosion comes from that yes/no, not from the objective, which is often a perfectly smooth function. The productive response is to let the decision variables become continuous — each element gets a real number instead of a side — solve the resulting continuous problem to optimality by whatever standard machinery applies, and then recover a discrete answer by thresholding. You trade an exact answer to an intractable problem for an exact answer to a nearby tractable one, plus a rounding step whose damage you can inspect.

Doing this well is mostly a matter of getting the constraints right, because in the relaxed world the constraints are the only thing preventing collapse. Once elements are allowed real values, the objective's true minimum is usually to give everything the same value: nothing is separated from anything, every difference term is zero, and the answer is useless. Two constraints together rule it out. Fixing the overall magnitude stops everything sliding to zero, and requiring the solution to be orthogonal to the uniform assignment stops everything sliding to a common nonzero value. What remains must have both positive and negative parts, which is exactly the shape a two-way split needs. Notice that these are not technical hygiene: the orthogonality condition is where the requirement "actually divide the thing" got encoded, and if you cannot point at the constraint carrying that requirement, your relaxation is unsound.

The rounding step deserves separate attention because it is where the discreteness comes back and it is not determined by the mathematics. Splitting at zero is a convention, not a result. The continuous solution carries strictly more information than any single split of it does — magnitudes say how confidently each element belongs — and moving the threshold trades one property against another in a way you can evaluate directly by scoring each candidate split under the original discrete objective. Treat the relaxed solution as an ordering of the elements to be cut somewhere, not as an answer with a canonical reading.

The whole pattern generalises well past graphs: identify the constraint whose discreteness is causing the difficulty, ask whether the objective still makes sense when it is loosened, check what forbids the trivial relaxed answer, and keep the continuous result around so the discretisation stays a decision you can revisit rather than one baked into the solver.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the spectral-partitioning section of the social-network chapter: minimising the Laplacian quadratic form over unit-length vectors constrained to be orthogonal to the all-ones eigenvector, the argument that this forces both positive and negative components, the assignment of nodes to sides by sign, and the following section's observation that the threshold need not be zero and that other thresholds give different size/cut trade-offs.
