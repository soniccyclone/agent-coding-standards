---
type: lesson
title: "Build the notation for describing the thing before you describe the thing"
figure: naur
works: [revised-report-on-the-algorithmic-language-algol-60]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Build the notation for describing the thing before you describe the thing

**Lesson:** When you set out to define an artifact precisely, your first move is not to define it but to fix the language you will define it in, and to fix it in a page. A description medium needs only a few pieces: a way to write a named category, a way to say "is defined as", a way to say "or", and the convention that anything else in a rule stands for itself and that adjacency means concatenation. Everything else — infinite families of forms, nesting to arbitrary depth, mutual dependence between categories — falls out of letting a category mention itself. Introducing that medium by working one throwaway rule over a toy alphabet, rather than by theorising about it, costs a paragraph and buys the reader the ability to check every subsequent rule mechanically.

Two disciplines make the medium pay. First, name the categories with words that approximately describe what they hold, and then commit that any use of those words in the surrounding prose refers back to the formal category. That welds the two halves of the document together: the prose stops being a parallel, drift-prone description and becomes commentary anchored to named rules. Second, allow a rule to be restated at more than one place. Redundancy in a defining document is not sloppiness when the medium makes the copies checkable against each other; forcing the reader to hold a rule in memory across ten pages is the more expensive error.

The general principle is that the cost of a description is dominated by the description medium's fit to the subject, and that a medium you have designed yourself for this subject usually beats an off-the-shelf one. Two things follow. What is expressible in the medium is what the definition can say, so the medium's shape decides which properties are stated formally and which get pushed into prose and go unchecked. And a small medium is worth more than an expressive one: the reason a reader can be trusted to check a rule is that the checking procedure is short enough to hold entirely in the head.

**Source:** [Revised Report on the Algorithmic Language ALGOL 60](../works/revised-report-on-the-algorithmic-language-algol-60.md) — section 1.1, the formalism for syntactic description: the four-part metalinguistic apparatus, its introduction by example on a nonsense grammar, the deliberate choice of descriptive names for metalinguistic variables and the resulting binding of body text to formal definitions, and the licence to repeat formulae in more than one place.
