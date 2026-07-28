---
type: lesson
title: "What a reduction cannot derive from structure it silently borrows; keep a list of the properties you assumed twice"
figure: landin
works: [correspondence-algol-60-church-lambda-notation-part-i]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification, foundations-of-computation]
tags: [lesson]
---
# What a reduction cannot derive from structure it silently borrows; keep a list of the properties you assumed twice

**Lesson:** Explaining one system in terms of a smaller one works by converting claims about behaviour into claims about shape. A feature is genuinely explained when it stops being a rule you have to state and becomes a consequence of how the target's pieces fit together. The danger is that a reduction can appear complete while some of the original's behavioural rules were never converted at all — they were simply restated in the target and reused. The mapping still produces the right answers, so nothing looks wrong, but for those features you have explained nothing: you assumed the property twice and called the second assumption a derivation.

The tell is that the correctness of the mapping depends on the target obeying a rule of the same kind as the one you were trying to account for. If the source evaluates its parts in a particular order and your model only gets the right answer because the model evaluates its parts in a particular order too, then order was transferred, not reduced. This is a strictly weaker outcome than reduction, and worth separating out loudly, because the two look identical from the outside: both give you a translation that behaves correctly on every example you try. The difference only shows up when someone asks *why* the source behaves that way, or when they change the target's evaluation strategy and the translation quietly breaks.

Two practical habits follow. First, when you build a model of a system, keep an explicit inventory of the source's properties that your target had to be given in order for the mapping to work; that inventory is the honest boundary of your explanation, and stating it protects everyone downstream who would otherwise assume the whole thing was accounted for. Second, prefer accounts that rest on the weakest possible assumption about the target, since an explanation resting on "operands before operators" is more fragile than one resting only on "an argument is dealt with before the body that uses it" — the weaker the borrowed property, the more machines your explanation survives. Whether the residue is small or large, name it; the unexamined residue is where a model's claim to explain outruns what it actually did.

**Source:** [A Correspondence Between ALGOL 60 and Church's Lambda-Notation: Part I](../works/correspondence-algol-60-church-lambda-notation-part-i.md) — the discussion accompanying the treatment of argument lists, where Landin concedes that one of ALGOL's evaluation-order rules is not accounted for structurally by his model but relies on a matching rule in the target language, and notes the more economical assumption that would do instead.
