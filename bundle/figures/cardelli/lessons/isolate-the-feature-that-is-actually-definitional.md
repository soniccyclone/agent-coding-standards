---
type: lesson
title: "Find which feature of a paradigm is definitional by comparing the systems that claim it, then study that one alone"
figure: cardelli
works: [a-semantics-of-multiple-inheritance, a-theory-of-primitive-objects-untyped-and-first-order-systems]
axes: [cognitive-load, primitive-count]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Find which feature of a paradigm is definitional by comparing the systems that claim it, then study that one alone

**Lesson:** A paradigm arrives as a bundle of correlated features, and because they always appear together it feels as though they are one idea. Objects came with coroutines, message sending, dynamic dispatch, dynamic scoping, absence of static checking, single ancestry, and metaclasses. The way to separate the essential from the incidental is not introspection but comparison: line up the systems that everyone agrees belong to the paradigm and see which properties they disagree about. Every item on that list varies between accepted members, except the ability of one description to inherit the attributes of another. So the theory to build is a theory of that, and the rest are independent axes that may or may not be present.

The second half of the discipline is harder than the first: having identified the essential feature, refuse to study it in company. That means deliberately excluding parametric abstraction, mutable state, and recursive descriptions from a first treatment, not because they are unimportant but because their interactions would mask the thing being examined. The cost is that some perfectly reasonable programs cannot be handled yet, and the paper says so and records which ones. The benefit is that when the excluded features are added later, their interactions are visible as interactions rather than being baked into the account of the core.

The payoff is a criterion. With a clean account of the essential feature in hand, you can look at any implementation technique and say whether it is fundamental or an optimization, and you can look at any language's version of the feature and say what it added, dropped, or conflated. Without that criterion, comparing two systems degenerates into comparing their feature lists, which mostly measures marketing.

Applied outside language design, the same procedure works on any bundled methodology or architectural style. Collect the instances that claim the label, find the invariant, model it in isolation, and treat the correlated extras as separate decisions with their own justifications.

**Source:** [A Semantics of Multiple Inheritance](../works/a-semantics-of-multiple-inheritance.md) — the introduction's comparison across object-oriented languages, which concludes that inheritance is the only critically associated notion and that a theory should therefore start there, plus the conclusions where excluded features are named as deliberate omissions and the value of a clean semantics is stated as separating the fundamental from implementation accidents. Also [A Theory of Primitive Objects: Untyped and First-Order Systems](../works/a-theory-of-primitive-objects-untyped-and-first-order-systems.md) — the choices about which operations to keep primitive and which alternatives to defer, including the refusal to explain away the operation whose rules are the point.
