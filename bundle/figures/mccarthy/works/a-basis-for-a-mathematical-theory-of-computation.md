---
type: work
title: "A Basis for a Mathematical Theory of Computation"
figure: mccarthy
description: Lays out a formal theory of conditional expressions and their recursive use, and introduces recursion induction as a method for proving properties of recursively defined functions — one of the earliest general techniques for reasoning about program correctness. The conditional-expression notation McCarthy develops here is a direct ancestor of if/cond forms in later languages. It's less a language design document than an attempt to put computation on the same rigorous footing as other branches of mathematics.
subdomains: [foundations-of-computation, formal-methods-and-verification]
year: 1963
url: https://www-formal.stanford.edu/jmc/basis1.pdf
survey_pages: 43
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# A Basis for a Mathematical Theory of Computation

**Venue/year:** Presented 1961 (Western Joint Computer Conference) and 1962 (IBM-sponsored symposium, Blaricum, Netherlands); published in P. Braffort and D. Hirschberg (eds.), "Computer Programming and Formal Systems" (North-Holland, 1963).
**Source:** https://www-formal.stanford.edu/jmc/basis1.pdf — live PDF, self-archived on McCarthy's Stanford page, confirmed 200 OK. Linked from the landing page at www-formal.stanford.edu/jmc/basis.html, which also offers .dvi and .ps versions.

## Lessons
- [The defining equation is the specification: if two programs satisfy the same recursion, they are the same program](../lessons/the-defining-equation-is-the-specification.md)
- [Build a formalism for proving things about particular programs, not for proving things about the formalism](../lessons/prove-inside-the-system-not-about-it.md)
- [Define your data spaces with an algebra of constructions, and the primitive operations arrive as consequences instead of choices](../lessons/derive-data-operations-from-the-space-definition.md)
- [Specify less than you know on purpose: prove the property for the loosest thing, and every refinement inherits it](../lessons/underspecify-on-purpose-to-prove-more.md)
- Also contributes to [Treat undefinedness as a first-class semantic outcome, and let evaluation order be part of the meaning rather than an implementation detail](../lessons/undefinedness-belongs-in-the-semantics.md) and [Two formalisms of identical power can still be unequal designs: judge a basis by which operations it makes elementary](../lessons/equal-power-is-not-equal-structure.md)
