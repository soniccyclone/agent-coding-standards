---
type: work
title: "A Theory of Primitive Objects: Untyped and First-Order Systems"
figure: cardelli
description: Introduces the object calculus itself — a minimal core calculus where objects are the primitive notion (collections of labeled methods with self-reference) rather than being built up from lambda-calculus records and fixed points. Gives an untyped operational semantics and a first-order type system with subtyping directly for this calculus, showing objects can be treated as foundationally as functions. This is the paper the book *A Theory of Objects* (Abadi & Cardelli, 1996) expands into a full monograph; added here because the book itself is not available as a public full text (see Phase 3 access flag in index.md).
subdomains: [programming-environments-and-object-systems, formal-methods-and-verification]
year: 1996
url: http://lucacardelli.name/Papers/PrimObj1stOrder.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# A Theory of Primitive Objects: Untyped and First-Order Systems

**Author(s):** Martín Abadi and Luca Cardelli
**Venue/year:** Preliminary version in TACS '94 (LNCS 789, Springer), pp. 296-320; full version in Information and Computation 125(2), March 1996, pp. 78-102.
**Source:** http://lucacardelli.name/Papers/PrimObj1stOrder.pdf — self-archived on Cardelli's own site (verified 200, application/pdf). Added beyond the original top-10 list as a public stand-in for the inaccessible *A Theory of Objects* book — it's the paper that book's core theory is built from.

## Lessons
- [When every encoding of a concept drops the property you care about, the concept is a primitive](../lessons/encodings-that-lose-what-matters-mean-you-have-the-wrong-primitives.md)
- [A part that can consult the whole is no longer a part you may vary independently](../lessons/a-part-that-can-see-the-whole-cannot-vary-freely.md)
- [State the permissive rule you wish held, then spend real effort building the small program that breaks it](../lessons/attack-the-rule-you-want-to-be-true.md)
- [Find which feature of a paradigm is definitional by comparing the systems that claim it, then study that one alone](../lessons/isolate-the-feature-that-is-actually-definitional.md)
