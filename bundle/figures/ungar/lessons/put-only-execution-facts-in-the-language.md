---
type: lesson
title: "Sort every declaration by who consumes it, and let the language carry only what execution requires"
figure: ungar
works: [programming-as-an-experience]
axes: [expressiveness, verifiability, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Sort every declaration by who consumes it, and let the language carry only what execution requires

**Lesson:** Annotations in a language accumulate for two unrelated reasons. Some exist because the machine cannot proceed without them; others exist because a human reader or a checker wants a promise about intent. These grew together historically — early compiled languages needed enough type information to pick instructions, and later designers noticed the same notation also documented the program — so most languages fuse them into one syntactic category. The fusion is the problem. A single mechanism answering to both a code generator and a reasoning human gets pulled in opposite directions: strengthen it for the machine and you constrain code that would otherwise be reusable; loosen it for the human and the generator gets nothing it can act on. The visible symptom is duplicated algorithms and subverted type systems, written by people working around a promise they never wanted to make in the first place.

The alternative is to ask, for each piece of information, which consumer actually reads it, and then house it where that consumer lives. Facts the runtime needs to lay out and optimize objects can be entirely internal — invented, cached, and revised by the implementation, never named by the programmer. Facts about what the programmer intends can live above the language, in tooling that infers, records, and checks them. Neither audience is denied anything; they just stop sharing a channel. The language ends up smaller, and the descriptive vocabulary ends up extensible, because nothing about intent has been frozen into syntax that only a compiler release can change.

A programmer who takes this seriously stops treating "add a declaration form" as the default answer to a reasoning problem. When someone wants a stronger guarantee, the question becomes where the guarantee should be enforced and by whom, and often the honest answer is a checker, a linter, or an inference pass rather than a new keyword. It also means resisting the reverse temptation: if the implementation wants a representation hint, that hint should not become a thing users write, because then users own it forever and the implementation can never change its mind. Layering by consumer is what keeps both sides free to evolve.

**Source:** [Programming as an Experience: The Inspiration for Self](../works/programming-as-an-experience.md) — the language-semantics discussion of type declarations, which traces the historical merging of compiler-facing and reader-facing information and then splits it back apart into implementation-private representation knowledge versus environment-level descriptions of intent.
