---
type: lesson
title: "Don't reject a measure for lacking a property your problem has no use for"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Don't reject a measure for lacking a property your problem has no use for

**Lesson:** A quantity that compares two things is habitually expected to be a distance, and a distance is expected to be symmetric: the gap from one to the other should not depend on which one you name first. That expectation is so reflexive that a comparison lacking it is often discarded as defective. Before discarding it, check whether your situation actually has the symmetry the property describes. Frequently it does not — one of the two things is the reference and the other is the candidate, one is what happened and the other is what was predicted, one is the specification and the other is the implementation. When the two roles are not interchangeable in the problem, a comparison that is not interchangeable in its arguments is a better fit, not a worse one, and insisting on symmetry means averaging away a distinction you meant to keep.

The corresponding discipline is to derive the properties you require from the use rather than from the name of the thing. Write down the operations you will actually perform on the quantity. If you will only ever compute it with the reference in a fixed position and minimise it, symmetry is simply never exercised, and neither is the triangle inequality, and neither is much else. What you do need is that it be zero when the two agree, positive otherwise, and cheap to differentiate or search over. Those are the requirements; anything else on the standard checklist is inherited from a different use case.

There is a second move in the same passage worth separating out. Once the comparison is expressed as a difference between two terms, and one of those terms depends only on the reference and not on anything you can change, that term is a constant with respect to the search and can be dropped. The simpler quantity you are left with is not an approximation — it has exactly the same minimiser, and the argument for that is one line. This is worth doing routinely, because the dropped term is often the expensive one, and because the reduced form usually turns out to be a well-known quantity with its own literature and its own efficient implementations, which the fuller form obscured.

Both moves come from the same habit: treating a definition as something to be interrogated for what your problem actually consumes, instead of adopted whole. A defensible-looking quantity carries requirements and costs that were justified elsewhere, and the reduction that survives contact with your specific use is generally smaller, cheaper, and more honest about what it is claiming.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the classification-loss section of the neural-nets chapter, which introduces the divergence between the labelled distribution and the model's output distribution, acknowledges it is not commutative and therefore not a true distance, argues this is appropriate because the labelled distribution is ground truth and the model's is a prediction, and then observes that its entropy term depends only on the input rather than the model, so minimising the divergence and minimising the cross entropy are the same problem.
