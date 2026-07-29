---
type: lesson
title: "Two questions fix a design: what can be named, and what can be stored"
figure: strachey
works: [the-varieties-of-programming-language]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Two questions fix a design: what can be named, and what can be stored

**Lesson:** Ask of any system two questions that sound almost the same but are not: which things can be given a name, and which things can be put somewhere and fetched back later. The answers are independent, and the pair of them determines more about how the system feels to use than any amount of surface design. Two languages can agree on their primitive operations, their notation, and their type discipline, and still be profoundly unlike each other because one lets you name almost anything while storing only numbers, and the other lets you name almost nothing while storing almost everything. Neither difference shows up in a grammar.

This is a diagnostic worth having because it is cheap and it is structural. Surface comparisons of systems tend to enumerate features, which produces lists that do not explain the felt difference between working in one and working in the other. Enumerating what inhabits each of the two spaces explains it directly: the size of the nameable set tells you how much of the language you can abstract over and pass around, and the size of the storable set tells you how much of it can be held, reorganised, and computed with at runtime. Where the two spaces overlap, and where they conspicuously do not, is where the language's characteristic awkwardness lives.

The practical consequence is a design order. Settle the inhabitants of those two spaces first, before notation, before the operator set, before the type rules — because everything downstream is constrained by them and almost nothing upstream constrains them. Design decisions of this kind are often made without being noticed at all, inherited from whatever the implementer's machine made convenient, and then they silently govern the whole result. The same question is worth asking of an API, a configuration system, or a data model: what can be referred to here, what can be persisted here, and did anyone decide that on purpose?

**Source:** [The Varieties of Programming Language](../works/the-varieties-of-programming-language.md) — the paired analyses of Algol 60 and PAL, whose contrast is drawn entirely from the relative sizes of their denotation and stored-value domains, and the closing recommendation that designers begin from this structure.
