---
type: lesson
title: "When the answers are correct but unusable, the fix belongs in the constructors, not the algorithm"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# When the answers are correct but unusable, the fix belongs in the constructors, not the algorithm

**Lesson:** A symbolic differentiator written against abstract selectors and constructors produces answers that are unarguably right and practically useless — every trivial term is left in place, so a small input yields a sprawling output. The instinct is to go back to the algorithm and add cleanup. The authors do not touch it. They change only the procedures that *build* results, so that constructing a sum of something with zero returns the something, and constructing a product with zero returns zero. The algorithm is not re-derived, not re-read, not even edited; the output collapses to the simple form anyway.

The reason this works is that quality-of-output is a property of the values, and the constructors are the only place every value is born. Any rule enforced there is enforced universally and once, including for values built by recursive calls the author of the rule never enumerated. Push the same rule into the algorithm and you have to find every site that could produce a degenerate result, keep finding them as the algorithm grows, and re-check the whole thing whenever the notion of "simple" shifts. The constructor is the chokepoint, so it is where invariants are cheap.

This generalizes past algebra to anything with a preferred form: reducing fractions, interning strings, sorting a set's internal order, normalizing a URL, collapsing an empty branch of a query tree, folding adjacent no-ops out of a generated instruction stream. In each case there is a choice of *when* to normalize — at construction or at access — and it is a real choice with a real cost profile, not a matter of taste. But there is no version of that choice in which the answer is "sprinkle it through the algorithm." An algorithm that has to know about degenerate cases of its own output has been handed a representation concern it should never have seen.

The section closes with the caveat that keeps this from being naive: what counts as simplest for one purpose may not for another, which is why algebraic simplification is genuinely hard rather than merely unfinished. That is an argument *for* the discipline, not against it. Since there is no canonical answer, the definition of "simple" is a thing you will change — and having concentrated it in the constructors is exactly what makes changing it a local edit instead of a rewrite. The test to apply to your own code: if you altered your notion of normal form today, how many places would you have to touch?

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.3.2, where the deriv procedure written against abstract sum/product selectors returns correct but unsimplified expressions; the authors note the difficulty parallels the unreduced rational numbers of section 2.1.1, state explicitly that deriv will not be changed at all, rebuild make-sum and make-product to absorb the zero and one identities and to fold constant operands, show the three examples collapsing to simple results, and close by observing that the problem of algebraic simplification is complex partly because a form simplest for one purpose may not be simplest for another.
