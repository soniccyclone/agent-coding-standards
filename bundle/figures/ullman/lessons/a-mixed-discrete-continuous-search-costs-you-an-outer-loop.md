---
type: lesson
title: "A mixed discrete/continuous search costs you an outer loop — buy it out"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, primitive-count]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# A mixed discrete/continuous search costs you an outer loop — buy it out

**Lesson:** Models often end up with two kinds of unknown: numbers you can tune smoothly, and structural choices that are yes-or-no. The smooth part has a mature optimiser waiting for it; the structural part has nothing but enumeration. The consequence is an architecture nobody chose: an outer loop that proposes structural edits and an inner solve that re-optimises the numbers from scratch for each proposal. Every candidate edit costs a full numeric optimisation, so the number of structures you can afford to examine collapses, and the structural search — the part you understand least — is the part getting the least compute.

Replacing each discrete unknown with a continuous surrogate collapses the two loops into one. Membership becomes strength of association, presence becomes weight, a choice among options becomes a distribution over them, with the far end of the continuum reproducing the discrete meaning exactly. Now a single optimiser moves everything at once, and structural change happens as a side effect of numeric movement rather than as an outer decision. That the surrogate is not literally true of the domain — one is or is not a member of a club — is a smaller cost than it appears, and often not a cost at all, since graded association frequently describes reality better than the binary it replaced.

Be clear about what this does and does not buy. It buys one mechanism instead of two, a search that can move continuously through configurations the edit-based search would have had to jump between, and gradients that carry information about which direction to move. It does not buy a global optimum. A relaxed objective over a structured domain is still full of local optima, and you will still want multiple starts from different random initialisations and will still be taking the best result you found rather than the best that exists. Anyone who sells relaxation as a fix for local optima is selling the wrong thing; the honest claim is that it makes each attempt cheaper and better-directed, so you can afford more attempts.

The general prompt is worth keeping: when a search is expensive, ask whether the expense comes from the search space itself or from an impedance mismatch between two kinds of unknown that forced a nested architecture. If it is the mismatch, converting one kind into the other is usually cheaper than optimising either loop.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the pair of sections on discrete optimisation of community assignments and on avoiding discrete membership changes, which describe hill-climbing over single-member insertions and deletions with an inner gradient-descent solve for each candidate, then replace binary membership with a nonnegative strength-of-membership parameter so a single continuous optimisation suffices, together with the accompanying sidebar's note that both formulations remain vulnerable to local optima.
