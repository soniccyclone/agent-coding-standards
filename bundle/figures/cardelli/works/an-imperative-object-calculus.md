---
type: work
title: "An Imperative Object Calculus"
figure: cardelli
description: Extends the functional object calculus to a setting with mutable state, giving objects with updatable fields a small-step operational semantics and a type system with soundness guarantees. This is the branch of the object calculus work that maps most directly onto mainstream imperative OO languages, where fields are assigned to rather than only rebound functionally. It's a direct precursor to the fuller treatment later published as the book *A Theory of Objects*.
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
year: 1995
url: http://lucacardelli.name/Papers/PrimObjImp.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# An Imperative Object Calculus

**Author(s):** Martín Abadi and Luca Cardelli
**Venue/year:** Preliminary version in TAPSOFT'95 (LNCS 915, Springer), pp. 471-485; full version in Theory and Practice of Object Systems 1(3), 1995, pp. 151-166.
**Source:** http://lucacardelli.name/Papers/PrimObjImp.pdf — self-archived on Cardelli's own site (verified 200, application/pdf). Note: the Phase 1/2 stub listed this as "1996" — the author's own bibliography dates both the preliminary and journal versions to 1995; corrected here.

## Lessons
- [Attach substitutability to how a slot is used, not to the thing as a whole, and read protection off the same annotation](../lessons/declare-substitutability-per-direction-of-use.md)
- [State the semantics over the mechanism you will actually run, so the theorem covers the thing you ship](../lessons/prove-it-about-the-machine-you-will-actually-run.md)
- [Derive the organizing construct from what you already have, and its preconditions become visible instead of built in](../lessons/derive-the-organizing-construct-instead-of-building-it-in.md)
- [Reduce a whole design vocabulary to a handful of binding forms, then measure the vocabulary by what derives from them](../lessons/derive-the-vocabulary-from-a-few-binding-forms.md)
- [When every encoding of a concept drops the property you care about, the concept is a primitive](../lessons/encodings-that-lose-what-matters-mean-you-have-the-wrong-primitives.md)
- [A part that can consult the whole is no longer a part you may vary independently](../lessons/a-part-that-can-see-the-whole-cannot-vary-freely.md)
- [Minimality is owed by the layer you reason in, speed by the layer you run on, and neither should be asked of the other](../lessons/each-layer-owes-a-different-virtue.md)
