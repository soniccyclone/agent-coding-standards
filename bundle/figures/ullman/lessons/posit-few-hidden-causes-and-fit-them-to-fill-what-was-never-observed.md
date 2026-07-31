---
type: lesson
title: "Posit a few hidden causes and fit them, so the model fills in what was never observed"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Posit a few hidden causes and fit them, so the model fills in what was never observed

**Lesson:** Faced with a huge, mostly empty grid of observations between two populations, the neighbour-based approach reasons locally: find similar rows, borrow their values. A structurally different approach starts from a hypothesis about how the observations were produced — that behind them lies a small number of underlying factors, that each member of each population is characterised by where it stands on those few factors, and that every observation is a consequence of those two positions meeting. If the hypothesis holds, the enormous grid is not really enormous; it is a compact description that has been expanded, and the job is to recover the description.

The payoff is not compression, it is completion. A local method can say nothing about a pair with no shared context, because it has no path connecting them. A generative description assigns coordinates to both members from all their other evidence, and those coordinates yield a value for the pair whether or not any evidence about that specific pair exists. Every unobserved combination becomes computable. This is the general reason to prefer models that explain observations over models that interpolate between them: an explanation extends to cases the data never touched, and interpolation does not.

Recovering the description is a search rather than a calculation, and the search has properties you must plan for. The fit is adjusted piece by piece, each adjustment chosen to reduce total disagreement with the observed entries, with unobserved entries simply not participating — which is how the method tolerates the emptiness that defeats other approaches. But the objective has many settling points, most of them worse than the best one, and no way to tell from inside which you have landed in. The only available response is to start from many different places, or to vary the order of adjustment, and to keep the best result found — accepting explicitly that this is a heuristic with no guarantee attached. Designing that acceptance in from the start is better than discovering later that the pipeline's output depends on its seed.

The transferable habit is to ask, of any large observational dataset, what small set of underlying quantities could have generated it, and whether recovering those quantities is easier than reasoning over the observations directly. When the answer is yes, you gain the ability to answer questions about combinations that never occurred, which is usually the thing you actually wanted.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the dimensionality-reduction section of the recommendation-systems chapter, which conjectures the preference grid to be the product of two thin matrices reflecting a small number of features that determine most reactions, derives the element-wise adjustment that skips unobserved entries, and discusses the many local minima that force repeated runs from perturbed starting points with no guarantee of reaching the best one.
