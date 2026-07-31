---
type: lesson
title: "Compare on the side of the relation whose entities are not mixtures"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load, parallelizability]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Compare on the side of the relation whose entities are not mixtures

**Lesson:** A table recording interactions between two populations can be read along either axis, and the machinery for finding similar rows works verbatim for finding similar columns. That symmetry is genuine and tempts you into treating the choice as arbitrary. It is not arbitrary, because the two populations usually differ in a property that decides how well similarity works at all: whether a member is one thing or several things at once. An entity that belongs to a single category has a coherent interaction profile, and two such entities in the same category will look alike. An entity that is a blend of several unrelated categories has a profile that is the union of several, and two blends that share one category still look mostly unlike each other, because each is dominated by the categories the other does not have.

The consequence is that similarity computed over the pure side is reliable and similarity computed over the mixed side is noisy, and this is a property of the domain rather than of your method. Products, documents, songs and parts tend to be pure; people, accounts, organisations and machines tend to be mixtures, since one person's activity is the superposition of every interest they have. Detecting that two items share a category is therefore easy, while detecting that two people share one interest among their several is hard — and a system that computes neighbourhoods on the mixed side will spend its life explaining why its neighbours are strange.

There is a second, opposing asymmetry to weigh against the first, which is cost and reuse. Working from the side you are serving requires one neighbourhood computation per request and directly yields everything you need for that request. Working from the other side requires the relationships among nearly the whole population to be computed before any single request can be answered. That sounds worse and often is not, because the result is shared across all requests and the underlying table changes far more slowly than it is queried — which converts the expensive direction into a batch job whose output is read many times. Rate of change against rate of query is the calculation that decides it, and it is worth doing explicitly rather than assuming that on-demand is cheaper.

Note also that the symmetry breaks at the end regardless of which side you compute on: finding similar items does not by itself produce a recommendation, since some further step must combine those similarities with the specific requester's history. Structural symmetry in the data does not imply symmetry in the task, and conflating the two produces designs that compute the right thing and then have nowhere to put it.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the duality-of-similarity section of the recommendation-systems chapter, which observes that items tend to fall in a single genre while individuals span several, that item-item similarity is therefore more reliable while user-user requires only one computation per request, that an extra step is needed either way to turn similarity into a recommendation, and that the slowly changing table justifies precomputing rather than computing on demand.
