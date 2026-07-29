---
type: lesson
title: "When a feature breaks a property, split the notion rather than abandon the property"
figure: strachey
works: [fundamental-concepts-in-programming-languages]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# When a feature breaks a property, split the notion rather than abandon the property

Substituting equals for equals is the property that makes ordinary mathematical reasoning possible: to understand a compound expression you need nothing about a subexpression except what it denotes. Mutable storage destroys this. Once a name can be updated, two occurrences of it need not denote the same thing, and every technique that relied on stable denotation is gone. The available responses look like a choice between keeping the mathematics and keeping the assignment statement.

Strachey's move is neither. He observes that the property fails only because one word — the value of an expression — is being made to cover two different things, and that separating them restores the property at one of the two levels. An expression on the left of an assignment stands for a place; on the right it stands for a place's current content. Contents change under assignment, but the association between a name and its place does not. So substitution still works, exactly and reliably, provided you are careful about which of the two you are substituting. The apparent conflict between imperative programming and equational reasoning was an artefact of an underspecified vocabulary, and the fix is to refine the vocabulary until the invariant reappears. He is candid that this is not free: every operation previously understood as acting on contents has to be re-examined to say which of the two it consumes, and the discipline of tracking that distinction is real work.

The generalisable habit is diagnostic. When a language feature seems to break a reasoning principle you depend on, resist both the reflex to drop the feature and the reflex to declare the principle inapplicable. Ask instead whether the principle is failing because a single concept in your description is conflating two, and try to find the finer notion under which the principle survives. This is why the same paper can note that a function's denotation is a rule paired with an environment: the intuition that a function is just its body breaks under nested scopes, so the notion of what a function denotes gets refined rather than the reasoning discarded. A designer who works this way treats a broken invariant as evidence of a coarse model, and the repair is almost always a distinction, not an amputation.

**Source:** [Fundamental Concepts in Programming Languages](../works/fundamental-concepts-in-programming-languages.md) — the analysis of assignment that introduces the two-values distinction, and the later argument that referential transparency can be preserved for the place-like value even in the presence of updating.
