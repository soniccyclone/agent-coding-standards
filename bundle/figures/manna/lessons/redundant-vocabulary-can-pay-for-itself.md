---
type: lesson
title: "Expressive equivalence is not the end of the argument for adding vocabulary"
figure: manna
works: [the-anchored-version-of-the-temporal-framework]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Expressive equivalence is not the end of the argument for adding vocabulary

**Lesson:** The strongest reason to refuse a new construct is that everything it says can already be said. Manna and Pnueli take that reason seriously and then override it, deliberately and with a price tag attached. Operators that look backward in time add nothing whatever to what the logic can express — the forward-only fragment was already known to capture everything. They add them anyway, and the justification is not taste. Backward operators let the properties people actually write be written the way people actually think them: an event that had to be requested before it happened reads as a statement about its own history rather than as an implication anchored to the dawn of the execution. They also buy structure that pure expressive power does not: a normal form in which every property falls into one of a handful of syntactic shapes, which is what later makes a per-shape proof discipline and a clean correspondence with automata possible.

What makes this an honest argument rather than a plea for convenience is that the authors quantify what the enlargement costs and show the bill is small: the decision problem for the propositional fragment stays in the same complexity class, and the proof system extends by symmetry rather than by a second, independent apparatus — the backward half of the axioms mirrors the forward half almost line for line, and most of its theorems come for free by that symmetry. Redundancy that is structurally parallel to something you already have is cheap; redundancy that introduces a genuinely new mechanism is not.

So the discipline is two-sided. Minimality is the default and must be argued against, but "you can already encode it" is not a decisive counter-argument, because encodability says nothing about whether the encoding is the shape a human will reach for or whether it exposes structure a tool can exploit. The programmer who internalizes this asks three questions of any proposed addition, in order: does it change what can be said (usually no), does it change how directly the common cases are said, and what does the rest of the system pay — in checker complexity, in new inference machinery, in cases every downstream consumer must now handle. An addition that answers no, substantially, and almost nothing is worth taking even though the minimal core was already complete.

**Source:** [The Anchored Version of the Temporal Framework](../works/the-anchored-version-of-the-temporal-framework.md) — the introduction's inventory of what past operators contribute despite adding no expressive power, together with the later sections where the past half of the proof system is derived largely by mirroring the future half.
