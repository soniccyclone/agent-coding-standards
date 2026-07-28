---
type: lesson
title: "If compatibility forces two meanings on one operation, give them separate names and publish which laws each breaks"
figure: chamberlin
works: [xquery-1.0-an-xml-query-language]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [programming-languages-and-semantics, databases-and-data-management]
tags: [lesson]
---
# If compatibility forces two meanings on one operation, give them separate names and publish which laws each breaks

Comparison looks like one operation and is at least two. There is the version that relates a single value to a single value and obeys the algebra people assume — transitive, with negation and equality behaving as inverses. And there is the version that quantifies existentially over collections, which is what a path-shaped query language needs when an operand may match nothing, one thing, or many, and which cannot be transitive because two collections overlapping a third do not have to overlap each other. Once a predecessor language has shipped the second one, backward compatibility means you keep it. The temptation is to unify them behind one syntax with a rule that picks; the discipline is to keep both and name them differently, then say out loud which properties each one has and which it sacrifices.

The interesting cost is not the extra operators, it is the coercion rules, which cannot be shared. The single-value comparison has to treat unvalidated data as text, because that is the only choice that keeps it transitive across a mixture of types. The collection comparison has to coerce unvalidated data toward whatever the other operand is, because that is what its predecessor did and what users' existing numeric-looking comparisons rely on. Two conversion tables for what looks like the same operator is exactly the kind of detail a specification is tempted to gloss; publishing both, side by side, with worked examples showing the same pair of operands comparing as text under one and as numbers under the other, is what lets a reader predict their program.

The general principle: when two behaviors are both genuinely needed, distinguishing them lexically costs a few tokens of vocabulary and buys the reader locality — they can see which semantics is in force without knowing the types. Overloading one symbol saves the vocabulary and moves the cost into a rule the reader must reconstruct from context, silently, every time. And when a needed behavior violates an algebraic law users assume by default, saying so explicitly is not an admission of a defect; it is the only way the law-breaking becomes something people can reason about rather than something that bites them once a year.

A programmer who takes this seriously stops writing the clever polymorphic helper that does the right thing for scalars and for collections, and writes two functions with two names. The clever version is shorter at the call site and unpredictable everywhere else.

**Source:** [XQuery 1.0: An XML Query Language](../works/xquery-1.0-an-xml-query-language.md) — the comparison-expression sections, which define value comparisons and general comparisons as separate operator families with separate untyped-value conversion rules, and whose notes state plainly that the existential family is neither transitive nor closed under negation, with examples exhibiting both failures.
