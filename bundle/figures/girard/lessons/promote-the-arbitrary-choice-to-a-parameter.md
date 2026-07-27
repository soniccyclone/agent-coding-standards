---
type: lesson
title: "If every instance of a choice is arbitrary, abstract over the choice and study what survives all of them"
figure: girard
works: [the-system-f-of-variable-types-fifteen-years-later]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# If every instance of a choice is arbitrary, abstract over the choice and study what survives all of them

**Lesson:** A recurring frustration in design is the configuration you must fix in order to proceed, where every admissible value is as defensible as every other. Modelling untyped computation is the clean example: you need a structure isomorphic to its own function space, solutions exist in abundance, and not one of them has any claim to being *the* model. The usual response is to pick one, get on with it, and quietly accept that some of your conclusions are artifacts of the pick. The better response is to notice that whatever you were computing depends on the chosen data in a *structured* way, and then to promote the choice from a fixed background to an explicit parameter — turning the arbitrary constant into a bound variable and the object of study into what is invariant across all values of it.

Two things make this more than a gesture. First, if the dependence on the parameter is uniform in the right sense, the same finite-determination machinery that tames any parameterized construction applies here, so the invariants form a small object rather than an unmanageable family — and from those invariants you can mechanically recover the answer for any particular choice you later care about. Second, this is strictly more informative than picking a representative: a single chosen model tells you about itself, while the invariants tell you about the whole class of models simultaneously, which is the class you actually cared about. The class is a natural object; any individual member of it is not.

There is a discipline attached that is easy to skip and worth honoring. The abstraction will drag in parameter values you consider degenerate — configurations whose behavior is useless or actively perverse. The temptation is to prune them, building your taste into the representation. Resist it. Keep the general object, and expose the well-behaved sub-part as a *named restriction* alongside it, because which values count as degenerate depends on the application and on who is asking, and the sub-part turns out to have the good properties anyway (here, the restricted invariants are exactly the ones that behave monotonically under evaluation). A representation that has already discarded what you didn't want cannot serve someone who wanted it.

Applied outside semantics, this is a stance on where configurability belongs. When you cannot justify a constant, do not bury it and do not vote on it — lift it into the signature, characterize the whole space of legal values, and make your claims about the space. Then offer the well-behaved subspace as a documented restriction rather than as the only thing that exists.

**Source:** [The System F of Variable Types, Fifteen Years Later](../works/the-system-f-of-variable-types-fifteen-years-later.md) — the construction of the intrinsic model, which abstracts over the domain and the two maps witnessing the self-application isomorphism instead of fixing a particular solution, together with the deliberate refusal to prune the invariants belonging to ill-behaved structures and the separately named restriction where evaluation is monotone.
