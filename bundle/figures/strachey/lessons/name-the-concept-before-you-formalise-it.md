---
type: lesson
title: "Name the concept before you formalise it"
figure: strachey
works: [fundamental-concepts-in-programming-languages]
axes: [cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Name the concept before you formalise it

A young field's real bottleneck is not rigour, it is vocabulary. Before you can prove anything about a phenomenon you have to have noticed it, separated it from its neighbours, and given it a handle you can carry into an argument. Strachey's discipline puts insight first and axioms second: get the concepts isolated and named, accept that the names will initially be defined only loosely, and formalise once you actually know which distinctions carry weight. Formalising early does not merely waste effort; it entrenches the wrong cut, because a rigorous account of a badly chosen concept is much harder to dislodge than a vague account of one.

The naming itself is a technical act with a specific failure mode. Reaching for words that already carry meaning — address, value, name, reference, set — imports every association those words have from ordinary usage and from mathematics, and those associations quietly steer subsequent reasoning into the wrong shape. The counter-move is to coin something deliberately neutral and let the definition, not the etymology, do the work. That is why the vocabulary invented here has no metaphorical content: the terms carry only the properties actually stipulated for them, which is exactly what makes them safe to reason with. A second part of the discipline is layering: a small number of genuinely basic concepts, whose ultimate grounding may still be open, plus a much larger set of derived concepts defined precisely in terms of those. You do not have to reach bedrock to be precise one level up.

A programmer who believes this stops treating terminology arguments as bikeshedding. When a design discussion keeps circling, the diagnosis is usually that two participants are using one word for two concepts, and the fix is to split the word and name both halves. It also changes when specification happens: you write the formal model after the exploratory work has told you which distinctions are load-bearing, not before, and you tolerate a period of named-but-not-yet-defined concepts rather than forcing premature precision that will have to be retracted.

**Source:** [Fundamental Concepts in Programming Languages](../works/fundamental-concepts-in-programming-languages.md) — the opening philosophical section, where Strachey diagnoses the confusion in foundational terminology and states the methodological rule that governs the rest of the lectures.
