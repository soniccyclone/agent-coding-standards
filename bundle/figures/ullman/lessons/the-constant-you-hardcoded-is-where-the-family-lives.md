---
type: lesson
title: "The constant you hardcoded is usually where the whole family of algorithms lives"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# The constant you hardcoded is usually where the whole family of algorithms lives

**Lesson:** When a computation contains a value that was chosen for neutrality — a uniform distribution, an equal weighting, an unbiased default — that value is almost never the interesting one. It is the one you picked because you had no reason to pick anything else, and that is precisely the signature of a parameter masquerading as a constant. Replacing it with an argument typically costs nothing in the implementation, because the surrounding machinery never depended on the specific value, only on its shape. What you get back is not one more configuration option but a family of distinct, separately useful algorithms, several of which you would never have thought to build from scratch.

The reason the payoff is so lopsided is that the neutral value encodes an assumption, and different substitutions correspond to different assumptions people actually hold. Bias the neutral distribution toward one subject area and the computation becomes a subject-specific ranking. Bias it toward a set you have independent reason to believe in and the same computation becomes a trust propagation. Bias it toward one participant's history and it becomes personalization. Same code, same convergence argument, same cost — three products, because the parameter names the prior and everyone has a different prior. This is a much better return on generalization than the usual kind, where you add an interface and get one alternate implementation nobody writes.

The discipline is to go looking for these deliberately rather than waiting to trip over them. Read your own computation and mark every place a value was fixed for lack of a reason. For each, ask what a non-neutral choice would mean semantically — not "what if this number were different" but "what belief would a different choice express." If the answer is a belief someone in the problem domain actually holds, you have found the seam, and exposing it is a small edit. If the answer is meaningless, the constant really is a constant and should stay one, which is also worth knowing.

The counterweight is that parameterizing a value obliges you to say where its argument comes from. A prior that nobody can supply responsibly is worse than a neutral default, because it moves a hard judgement out of the algorithm and into a caller with less context. So the seam is only worth opening when there is a real source for the argument — an existing classification, a curated set, an observed history — and identifying that source is part of the design, not a follow-up task.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the link-analysis chapter's progression from a uniform restart distribution to a restart set restricted to a topic, then to a restart set of pages believed trustworthy, where the iteration and its justification are unchanged and only the injected vector differs.
