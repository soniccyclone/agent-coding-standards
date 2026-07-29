---
type: lesson
title: "Measure every version against the ideal, not against each other"
figure: strachey
works: [the-varieties-of-programming-language]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Measure every version against the ideal, not against each other

**Lesson:** There are usually many ways to compute the thing you want, and none of them is exactly right — each approximates the intended result, differently. The instinct when faced with two of them is to compare them to one another and ask whether they agree. That comparison is the hard one, and it gets harder combinatorially: with several candidate implementations, pairwise agreement is a mess of relationships, none of which tells you whether any of them is correct. Comparing one implementation against a stated exact specification is far easier, and doing it once per implementation is linear work that also answers the question you actually care about.

So the discipline is to write down the exact, idealised object first — the mathematical function, the reference semantics, the precise contract — while explicitly ignoring the ways reality will fail to reach it. Only then bring in the implementation and characterise the gap. This ordering feels like a detour to anyone eager to write code, but it is what makes the eventual error analysis possible at all: you cannot quantify a discrepancy without a thing to be discrepant from, and a rival implementation is a poor stand-in because its own error is unknown.

The habit generalises to any place where multiple realisations of one intent coexist: two services that should behave alike, a cache and its backing store, a fast path and a slow path, a reimplementation replacing a legacy system. Differential testing between them will find disagreements but cannot tell you which side is wrong, and it silently blesses whatever both sides get wrong together. A programmer who has internalised this writes the reference definition down as an artefact — even when no code will ever execute it — and makes every candidate answer to that, not to its siblings.

**Source:** [The Varieties of Programming Language](../works/the-varieties-of-programming-language.md) — the introduction's argument for the mathematical over the operational approach, which rests on the relative difficulty of proving a program approximates an exact function versus proving two programs approximately equivalent.
