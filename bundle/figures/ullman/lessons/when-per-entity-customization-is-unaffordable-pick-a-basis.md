---
type: lesson
title: "When per-entity customization is unaffordable, pick a basis and store coordinates"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load, hardware-affinity]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# When per-entity customization is unaffordable, pick a basis and store coordinates

**Lesson:** The ideal version of most personalization is one full private result per participant, and it is almost always ruled out by a multiplication you can do in your head: participants times result size. When that product is impossible, the reflex is to give up on customization and serve one global result, but there is a middle construction that is usually much closer to the ideal than to the compromise. Precompute a small number of full results, each conditioned on a different assumption, and then represent each participant not by a result but by a short vector of weights over those assumptions. Storage becomes assumptions times result size, plus participants times a handful of numbers, and the second term is negligible. What was quadratic is now two separate linear costs.

The design decisions all move into choosing the basis, and that is where the thinking should go. The basis has to be small enough that precomputing every element is affordable, coarse enough that participants can be classified into it from weak evidence, and spanning enough that the blends of its elements cover the range of behaviour you actually care about. None of those are properties of the algorithm; they are claims about the population, and getting them wrong shows up as participants whose blended result is worse than the global one would have been. Notably, you do not have to assign each participant to a single element — mixing the precomputed results in proportion to inferred interest is both cheaper and more accurate than hard classification, and it degrades smoothly when the evidence is thin, since an uninformative weight vector reduces to the global result.

The pattern is the same one behind materialised aggregates, per-tenant configuration expressed as overrides on a small set of profiles, and precomputed shards of any expensive query keyed by a low-cardinality discriminator. Recognising it requires noticing that the expensive object varies over a space of much lower dimension than the number of requesters. That is an empirical claim about your workload, and it is worth testing directly: if the requesters really do vary along a hundred independent directions, the construction does not apply and you should say so rather than shipping a basis that fits none of them.

A useful side effect is that the basis becomes an artifact you can inspect and argue about, which a per-participant computation never is. You can look at a precomputed result conditioned on one assumption and ask whether it is any good, independently of any particular participant, and that separation makes debugging a personalization system tractable rather than anecdotal.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the topic-sensitive section of the link-analysis chapter, which rejects a private importance vector per user as infeasible, substitutes one vector per topic from a small fixed topic list, and suggests blending those vectors in proportion to a user's inferred interest rather than picking one.
