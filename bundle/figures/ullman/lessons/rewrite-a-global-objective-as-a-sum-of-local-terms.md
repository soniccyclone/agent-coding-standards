---
type: lesson
title: "Rewrite a global objective as a sum of local terms to see what it rewards"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Rewrite a global objective as a sum of local terms to see what it rewards

**Lesson:** Objectives that arrive in aggregate form — a matrix expression, a norm, an accumulated score over the whole system — are opaque about their own preferences. You can evaluate one, you can hand it to an optimiser, and you still cannot say what shape of solution it favours or whether it favours the thing you care about. The remedy is almost always algebraic: expand the aggregate and regroup the terms so that each one is attached to a single local feature of the structure. When it works, the whole expression turns out to be a sum with one term per element, per pair, per edge, and each term is something you can read in plain language.

The payoff is that the objective becomes interpretable, and interpretability here is the same thing as checkability. If an expression reduces to a sum over connected pairs of their squared difference, then it is immediately clear that minimising it means giving connected things similar values, that unconnected things are unconstrained, and that the penalty grows faster than linearly so one large disagreement costs more than several small ones. Every one of those is a design decision you can now agree or disagree with. Before the regrouping, none of them was visible, and you would have been reasoning about the objective by running it on small examples and squinting — which finds gross errors and reliably misses the interesting ones.

There is a second benefit that pays off in implementation rather than understanding. A sum of independent local terms is a sum you can evaluate incrementally, distribute across partitions, and update when one part of the input changes, none of which the aggregate form makes available. So the same rewriting that explains the objective often also reveals how to compute it at scale. That is not coincidence: locality of the terms is what both properties are made of.

Worth applying in the other direction too. When you are designing rather than analysing, write down the per-element penalty you actually want first, sum it, and then look for a compact aggregate form. That way the semantics are fixed by intent and the compact form is a derived convenience — instead of adopting a standard aggregate because it is standard, and discovering later which idiosyncratic preferences you inherited with it.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the derivation in the spectral-partitioning section of the social-network chapter that expands the Laplacian quadratic form into its degree and adjacency parts, distributes each node's degree term across the pairs it participates in, and shows the whole expression collapses to a sum over graph edges of the squared difference between the two endpoints' components — which is what makes the minimisation's preference for like-signed neighbours legible.
