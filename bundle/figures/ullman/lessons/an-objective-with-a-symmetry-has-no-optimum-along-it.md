---
type: lesson
title: "An objective with a symmetry has no optimum along it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# An objective with a symmetry has no optimum along it

**Lesson:** Before handing an objective to a solver, apply the transformations that leave the *underlying solution* unchanged and see what happens to the *score*. If some such transformation improves the score, the objective is broken: it can be improved without improving anything real, so there is no best answer, and the solver will either run forever or return whatever it had when you stopped it. The classic instance is scaling — doubling every parameter describes the same boundary, the same decision, the same behaviour, and doubles the number being maximised. Nothing is wrong with the solver. The objective is measuring the description rather than the thing described.

This is a specific and easily missed failure, distinct from an objective with a trivial optimum. There the search finds an answer you did not want; here there is no answer to find, and the symptom is unbounded growth in the parameters with no corresponding change in behaviour — which reads like a numerical problem and is a formulation problem. The check that catches it is short: list what you can change about the representation without changing the meaning, and confirm the objective is constant along each.

The repair is to fix the gauge — add a normalisation that picks one representative from each family of equivalent descriptions — and the interesting part is what happens next. Once the scale is pinned, the quantity you were maximising is usually expressible in terms of the quantity you pinned, and the problem transforms into an equivalent one with an entirely different appearance: maximising clearance becomes minimising magnitude. That reformulation is not cosmetic. The transformed problem is often the one with well-behaved derivatives, standard solvers, and an obvious connection to other formulations, and it would not have been visible without normalising first.

The habit generalises to any place where a score is computed from a representation rather than from behaviour: benchmark metrics that improve when you restate the same computation, quality scores that rise with verbosity, utilisation figures that move when you rename a resource. The test is always the same — find the transformations that preserve meaning, and check the number does not move.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the mechanics-of-an-SVM and normalizing-the-hyperplane sections, where the initial formulation of maximising the margin fails because doubling the weight vector and offset satisfies the constraints at twice the margin so no maximum exists, and the repair is to normalise the weight vector so the touching hyperplanes are at unit offset, from which the derivation shows the margin equals the reciprocal of the weight vector's magnitude and the problem becomes minimisation of that magnitude.
