---
type: work
title: "A Semantics of Multiple Inheritance"
figure: cardelli
description: Works out a formal, type-theoretic account of inheritance and subtyping, treating multiple inheritance as a partial order on record-like types rather than as an ad hoc textual mechanism for sharing code. It identifies the width/depth subtyping issues that later languages had to reckon with when combining inheritance with static typing. Frequently cited as one of the first papers to give object-oriented inheritance a mathematical semantics rather than an implementation recipe.
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
year: 1984
url: "http://lucacardelli.name/Papers/Inheritance%20(Semantics%20of%20Data%20Types).pdf"
access: public
host: self-archived
tags: [work]
---

# A Semantics of Multiple Inheritance

**Venue/year:** Semantics of Data Types, International Symposium, Sophia-Antipolis, France, June 1984 (LNCS 173, Springer), pp. 51-67. Journal version: Information and Computation 76(2/3), February 1988, pp. 138-164.
**Source:** http://lucacardelli.name/Papers/Inheritance%20(Semantics%20of%20Data%20Types).pdf — self-archived scan of the original 1984 conference paper on Cardelli's own site (verified 200, application/pdf, ~10.9MB scan). The 1988 journal version is also self-archived there (Papers/Inheritance.pdf) if a typeset copy is preferred.

## Lessons
- [Find which feature of a paradigm is definitional by comparing the systems that claim it, then study that one alone](../lessons/isolate-the-feature-that-is-actually-definitional.md)
- [Decide what your descriptions denote, and the relations between them stop being matters of taste](../lessons/fix-what-your-types-denote-and-the-relations-follow.md)
- [Let shape decide compatibility, and seal by hiding whatever invariant the shape fails to express](../lessons/let-shape-decide-compatibility-not-names.md)
- [Make a relaxation orthogonal: every way of building a thing owes an answer in every relation you care about](../lessons/every-constructor-owes-a-rule-in-every-relation.md)
- [Reduce a whole design vocabulary to a handful of binding forms, then measure the vocabulary by what derives from them](../lessons/derive-the-vocabulary-from-a-few-binding-forms.md)
- [State the permissive rule you wish held, then spend real effort building the small program that breaks it](../lessons/attack-the-rule-you-want-to-be-true.md)
- [Write down what must be decided before deciding how to decide it, and let the algorithm be answerable to that statement](../lessons/state-the-judgment-before-writing-the-checker.md)
- [Attach substitutability to how a slot is used, not to the thing as a whole, and read protection off the same annotation](../lessons/declare-substitutability-per-direction-of-use.md)
- [Before adding a mechanism, check whether a distinction the system already maintains can carry the new job](../lessons/get-the-second-mechanism-free-from-a-distinction-you-already-keep.md)

_Read via the 1988 journal version self-archived at the same site (`Papers/Inheritance.pdf`, noted in the Source line above); the 1984 conference scan at the `url` above is an image-only PDF with no text layer._
