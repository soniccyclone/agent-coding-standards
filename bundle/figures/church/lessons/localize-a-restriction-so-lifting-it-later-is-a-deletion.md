---
type: lesson
title: "Put a restriction in one clause, so that generalizing later is a deletion instead of a rewrite"
figure: church
works: [introduction-to-mathematical-logic]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Put a restriction in one clause, so that generalizing later is a deletion instead of a rewrite

The second-order system is not a new system. Church introduces it by saying the symbols are the same, the formation rules are the same, and the interpretation is given by the same semantic rules — with one qualification struck out of one formation clause and the identical qualification struck out of one semantic clause. Where the first-order system said a quantifier may bind an individual variable, the second-order one says it may bind any variable. Everything else is carried over word for word, including the vocabulary of antecedents and consequents, the abbreviation conventions, and the uniqueness-of-analysis result. A jump in expressive power that changes what the logic can say about itself arrives as the removal of two adjectives.

That is only possible because the restriction had been concentrated. If the "individual variables only" condition had been sprinkled through every rule that mentions a variable — restated in the formation rules, again in each axiom, again in the definition of free occurrence, again in the semantics — then lifting it would have meant auditing every one of those sites and deciding case by case whether the condition was incidental or load-bearing there. Instead there is one place to look. The upshot for anyone laying out a system: when you impose a limitation you suspect you may someday want to relax, the question is not just whether the limitation is right, it is how many places will have to agree in order to change your mind. A restriction stated once and referred to everywhere is cheap to revisit; the same restriction inlined at forty sites is a decision you have effectively made permanent, and you will discover this only when you try to undo it.

The dividend shows up immediately afterward. Because the generalized system contains the old rules of inference outright, every theorem of the narrow system is a theorem of the wide one for free, and the whole apparatus of derived rules ports across with proofs Church can honestly describe as following the earlier ones closely and leave to the reader. That is the signature of a well-placed restriction: after it is lifted, the existing body of results does not need to be re-derived, only re-read with a wider notion of what the letters range over. When instead you find that widening a parameter forces you to reprove your existing results rather than reinterpret them, that is evidence the old scope was not a parameter at all but an assumption baked into the arguments — and the cost of the generalization is about to be much larger than the diff suggests.

**Source:** [Introduction to Mathematical Logic](../works/introduction-to-mathematical-logic.md) — §50, where the primitive basis of the second-order calculus is presented as the first-order basis with the restriction to individual variables removed from the fifth formation rule and from semantic rule f, and §51, where the first-order theorems and derived rules are inherited wholesale on that basis.
