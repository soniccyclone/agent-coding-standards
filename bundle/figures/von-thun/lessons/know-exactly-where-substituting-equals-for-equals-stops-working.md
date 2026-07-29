---
type: lesson
title: "Know exactly where substituting equals for equals stops working"
figure: von-thun
works: [mathematical-foundations-of-joy]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Know exactly where substituting equals for equals stops working

**Lesson:** The whole practical value of reasoning about code by rewriting it rests on one permission: that a part may be swapped for an equivalent part without disturbing the whole. Von Thun makes that permission explicit rather than assumed, and in doing so isolates precisely where it fails. Two program fragments that compute the same function are freely interchangeable inside a composition. But the moment a fragment is *quoted* — turned from something that runs into something that is data — equivalence of behaviour stops being enough, because the data can be inspected. Two quotations denoting the same function can differ in length, and a program that measures length will tell them apart. Quotation creates an opaque context.

What matters is the resolution of the diagnosis. The naive conclusion would be that quoted code is simply off-limits to equational reasoning. The actual conclusion is narrower and far more useful: substitution across a quotation is licensed exactly in those contexts where the quotation is guaranteed to be run rather than examined — the contexts supplied by combinators. So the rule of inference comes in two clauses, one for composition and one for dequotation, and every law in the system is stated with an eye to which clause it needs. Reification of code as data does not destroy reasoning; it partitions contexts into transparent and opaque, and the language's job is to make the partition visible.

A programmer who has internalized this stops treating "referential transparency" as a global property a language either has or lacks, and starts locating the specific constructs that break it. Reflection, hashing a closure, comparing function identity, serializing a lambda, printing a stack trace, timing a call — each is a context that can distinguish behaviourally identical implementations, and each therefore silently invalidates a refactor that "obviously" preserves meaning. The discipline is to name those contexts up front and confine them, so that the large transparent region stays trustworthy. The alternative is a codebase where every rewrite is technically unsound and you find out which ones matter by shipping.

**Source:** [Mathematical Foundations of Joy](../works/mathematical-foundations-of-joy.md) — the statement of the prime rule of inference in the introduction, and the section on quotation and dequotation where a size-measuring program is used to show that quotation is an intensional constructor.
