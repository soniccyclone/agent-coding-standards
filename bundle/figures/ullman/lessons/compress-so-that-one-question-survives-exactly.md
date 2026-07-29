---
type: lesson
title: "Compress so that one question survives exactly, not so the data gets smaller"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Compress so that one question survives exactly, not so the data gets smaller

**Lesson:** Generic compression asks how few bytes can stand in for an object. A better question, and a different one, is which single property of the object must survive intact — and then to design a reduction that preserves that property with a known statistical relationship, while destroying everything else. The reduction can be brutal: replace an object by a short vector of numbers, each of which is nothing but "which member of this set came first under one arbitrary reordering." Nothing about the original is recoverable. But because the chance that two objects produce the same number under a random reordering is exactly the similarity measure you care about, agreement counts on these vectors are an unbiased estimate of similarity, and lengthening the vector tightens the estimate on demand. You have traded the ability to answer every question for the ability to answer one question cheaply, and made the accuracy of that one answer a dial.

The same discipline governs the step before it, which is easy to overlook. Turning an object into the thing you compare — the encoding — already decides what similarity is going to mean, and it decides it more forcefully than any later algorithm. Pick a granularity too fine and every object resembles every other, because the fragments are so common that agreement carries no information; the resulting high similarity scores are real numbers computed correctly about a meaningless quantity. Pick fragments that appear in the region of the data you actually care about and rarely elsewhere, and you have biased the measure toward the signal on purpose — an encoding choice doing work no downstream tuning could do. Notice also that you can hash a large fragment down to the same number of bytes a small fragment would have occupied and be strictly better off, because what matters is not the width of the representation but how much of that width is actually used.

What a programmer does differently is stop treating representation as a preliminary and start treating it as the design. Before choosing a data structure or an algorithm, they name the one relation the pipeline exists to compute, then ask what transformation shrinks the input while keeping that relation estimable with quantifiable error. They also demand the error statement: a summary whose relationship to the truth is merely "close, usually" is not the same artefact as one whose expected agreement provably equals the target quantity, and only the second lets you reason about how much summary you need.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the similarity chapter, in its treatment of fragment-based encoding and granularity choice and then in the derivation that a minimum-under-random-permutation summary collides with probability equal to set overlap, together with the practical substitution of hash functions for real permutations.
