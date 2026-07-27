---
type: lesson
title: "A rule that appeals to itself is sound exactly when something strictly shrinks"
figure: manna
works: [completing-the-temporal-picture, temporal-verification-of-reactive-systems-progress]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# A rule that appeals to itself is sound exactly when something strictly shrinks

**Lesson:** One of Manna and Pnueli's rules for proving that something eventually happens has a premise of the same shape as its own conclusion. Read naively that is vicious — proving a liveness claim by assuming a liveness claim. They confront it directly, and the resolution is not a syntactic dodge: the recursive premise is discharged against a *different, strictly smaller* system, one where the fairness assumption being exploited has been removed from the pool. Since each nesting consumes one such assumption and there are finitely many, the recursion bottoms out, and the argument becomes an induction on the size of the pool rather than a loop.

What makes the discharge legitimate is an observation about the problem, not about the logic. The rule is being used to show that a certain action eventually becomes possible. That action cannot be what makes itself possible — if it ran, the goal was already reached. So the sub-obligation genuinely does not depend on the assumption it is trying to justify, and dropping that assumption from the system loses nothing. The shrinking measure is discovered by asking what the recursive appeal actually cannot use.

This generalizes past proof rules to anything that appeals to itself: recursive descent through a grammar, a cache that consults a slower layer that might consult the cache, a retry policy invoking the operation it is protecting, a scheduler that needs to schedule its own housekeeping, a spec whose refinement obligation mentions refinement. In every case the question is the same and it is answerable: name the quantity that strictly decreases at each level and the well-founded order it decreases in. If you can name it, the self-reference is induction and it is fine. If you cannot, you have not found a clever fixed point, you have written down a loop, and the fact that it typechecks or that the premise "looks provable" means nothing.

The habit this produces is small and load-bearing. Whenever a definition, rule, or protocol refers to itself, write the decreasing measure down next to it, in words, as part of the artifact rather than in the head of whoever wrote it — because the measure is the entire justification, and it is the thing a later reader will otherwise have to reconstruct or, more likely, will not.

**Source:** [Completing the Temporal Picture](../works/completing-the-temporal-picture.md) — the discussion accompanying the single-step response rule that relies on a strongly fair transition, where the apparently circular fourth premise is explained, and the completeness argument that turns it into an induction on the size of the combined fairness set. [Temporal Verification of Reactive Systems: Progress](../works/temporal-verification-of-reactive-systems-progress.md) works the same point twice more: its Response Under Fairness chapter gives an informal second measure for the same rule, where each nesting level of a multi-resource accessibility proof leaves one further process permanently blocked and therefore unable to help, so the count of processes still able to act is what shrinks; and its completeness proof formalizes the induction on the number of strong-fairness assumptions.
