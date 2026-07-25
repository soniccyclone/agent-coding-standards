---
type: lesson
title: "When a set is too large to enumerate, define it by the rules that form its members"
figure: backus
works: [syntax-and-semantics-of-the-proposed-international-algebraic-language]
axes: [primitive-count, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# When a set is too large to enumerate, define it by the rules that form its members

**Lesson:** The class of legal programs in any usable language is infinite, so it cannot be described by listing, and describing it by narration in prose produces exactly the ambiguity that makes independent implementations diverge. The remaining option is to specify the class by how its members are built: name the categories of interest, and give for each a rule saying which shapes belong to it, where the rules are permitted to refer back to the categories they define. Recursion is what buys the infinity — a handful of lines saying that a thing may be a simple token, or a thing followed by a token, or a thing juxtaposed with another thing, generates unboundedly many members with no further work.

What makes this practical rather than merely possible is how small the apparatus is. It needs three devices: a way to write a variable standing for a set of symbol strings, a connective for definition and one for alternatives, and the convention that writing two items side by side means their strings are concatenated. Everything else in the description, every mark that is not a variable or a connective, denotes itself. A notation for talking about a notation is itself a designed object, and choosing few enough primitives that its own rules fit in a paragraph is what lets a reader trust the description without a second description of it. The economy also makes the result mechanically checkable: whether a candidate text belongs to the class is a question about matching rules, not an interpretive judgment.

The transferable habit is to reach for generative rules whenever the thing being specified is an unbounded family of structures, and to keep the metalanguage's own primitive count minimal while doing it. Two further consequences are worth internalizing. Recursive formation rules give you, for free, a structure to hang meaning on later, so the same decomposition serves both the definition of legality and the eventual definition of behavior. And the reason such a description is readable at all is that the reader learns a few rules of formation instead of memorizing a catalogue of permitted shapes.

**Source:** [The Syntax and Semantics of the Proposed International Algebraic Language](../works/syntax-and-semantics-of-the-proposed-international-algebraic-language.md) — the introduction of the metalinguistic apparatus before the syntax proper, where variables, connectives, and juxtaposition are explained by a single worked example whose recursive rule generates an unbounded family of strings, followed by the rule-by-rule definition of the language's categories.
