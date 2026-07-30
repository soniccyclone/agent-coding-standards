---
type: lesson
title: "A construction closed enough to solve your equation will admit objects you did not intend"
figure: scott
works: [outline-of-a-mathematical-theory-of-computation]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# A construction closed enough to solve your equation will admit objects you did not intend

**Lesson:** Recursive definitions of structure — a list is an element or a list of these, a tree is a leaf or nodes of these — read as if they describe only the things you can finish building. Give the definition a space in which it genuinely has a solution, and the space turns out to contain more: because the construction is closed under limits and every well-behaved map on it has a fixed point, an equation like "this object is the pair of a given element with itself" has a solution, and that solution is an unending structure with no finite build order at all. Encountering this for the first time reads as a defect, evidence that the model has drifted from the intended notion. It is better read as the price of closure, and the price is usually worth paying, because the same closure is what made the recursive definition mean anything in the first place.

Two further observations turn the discovery from unsettling into useful. The unintended inhabitants are limit points: the space you got is the completion of the space you meant, containing all the finite objects you had in mind together with the limits of sequences of them. And limits of finite structures are not junk — they are streams, infinite lists, non-terminating processes, exactly the objects a language with lazy or unbounded constructs needs a home for. The construction has handed you a coherent account of a feature you might otherwise have had to bolt on. Where you do not want them, nothing forces you to use them; the extra elements sit in the space unmentioned, and a program that only ever builds finite structures only ever meets finite ones.

The habit worth carrying is to interrogate surplus before excluding it. When a model admits inhabitants outside your intent, the questions in order are: are they limits of things you do want, does anything you rely on break in their presence, and are they in fact the objects some adjacent requirement has been asking for. Only when the answers go badly is it time to reach for a restriction — and a restriction added at that point is an informed one, aimed at a specific inhabitant for a specific reason. The opposite reflex, tightening a construction the moment it produces something unfamiliar, tends to cost the closure property that made the construction work, and closure is much harder to get back than a constraint is to add.

**Source:** [Outline of a Mathematical Theory of Computation](../works/outline-of-a-mathematical-theory-of-computation.md) — the construction-of-data-types section, where the recursively defined space of lists is shown by the fixed-point theorem to contain an infinite self-referential list, the question of whether this is bad is answered in the negative, and the space is identified as the topological completion of the finite lists whose extra limit points need not be used.
