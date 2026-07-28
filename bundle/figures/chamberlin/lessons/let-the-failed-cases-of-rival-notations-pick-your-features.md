---
type: lesson
title: "Let the cases that defeat existing notations choose your features"
figure: chamberlin
works: [quilt-an-xml-query-language]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, databases-and-data-management]
tags: [lesson]
---
# Let the cases that defeat existing notations choose your features

There are two ways to arrive at a new language. You can start from a principle and derive constructs from it, or you can start from a fixed set of concrete demands, try every existing notation against all of them, and record precisely which demand breaks which notation. The second method is unglamorous and much better calibrated, because the failures are evidence rather than taste. Each construct you end up adopting has a named case behind it that nothing else could express, which means you can defend the feature list item by item — and, more usefully, refuse everything with no case behind it.

This inverts the usual relationship between borrowing and originality. Assembling proven constructs from rival designs is not a shortcut around design work; it is the design work, provided the assembly is disciplined by two things. First, coverage: the demand set has to include the cases from both camps you are trying to unify, or you will reproduce the specialization you set out to remove. Second, a single conceptual anchor: the borrowed pieces have to be reinterpreted over one data model, so that a construct taken from a document-navigation language and a construct taken from a record-matching language mean things in the same universe. Without that anchor you get a union of dialects whose interactions nobody can reason about; with it, the seams disappear and the pieces compose.

The practical discipline is also a scoping weapon. A demand-driven feature list has a natural stopping point — you stop when every case in the set is expressible — which is why this method tends to produce small implementable languages while principle-first design tends to produce maximalist ones. Note also what the approach costs: it is honest about being incomplete. Publishing a grammar with acknowledged holes and deferred decisions is the correct move when the language is still being validated against cases, and pretending to finality earlier would only make the eventual revisions more expensive.

**Source:** [Quilt: An XML Query Language for Heterogeneous Data Sources](../works/quilt-an-xml-query-language.md) — the introduction's account of how the design started from applying five or six existing query languages to a set of use cases and keeping what each one uniquely handled, together with the closing section that re-derives the feature list from the document and relational cases the paper worked through.
