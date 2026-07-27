---
type: lesson
title: "Prefer a rule a reader can apply without lookahead, even when it rejects programs another reading would have accepted"
figure: steele
works: [the-java-language-specification]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Prefer a rule a reader can apply without lookahead, even when it rejects programs another reading would have accepted

**Lesson:** When a program's text can be carved into symbols more than one way, a designer must pick between two incompatible goals: a rule that is greedy and purely local, or a rule that consults later stages of understanding to find a carving that produces a legal program. This specification chooses locality without hedging, and states the cost out loud — the greedy carving is used even in cases where it guarantees the program will be rejected while a different carving would have made it legal. The example it gives is deliberately trivial and unarguable: a pair of adjacent minus signs is read as one symbol and the program dies, even though reading them as two separate symbols would have worked.

The reasoning is about who has to hold what in their head. A local, greedy rule can be executed by a human reading the raw characters, by a syntax highlighter, by a diff tool, and by a compiler, all with identical results and none of them needing to know what a legal program looks like. A rule that reaches forward for context makes the meaning of a character sequence depend on the success or failure of an analysis that happens much later, which means no cheap tool can agree with the compiler, and a reader cannot decide what they are looking at until they have understood the whole construct. Buying a handful of extra legal programs at that price is a bad trade, and the specification treats it as one.

What makes the discipline credible is how the one unavoidable violation is handled. A later addition to the language — type arguments that nest and close with a character that is also a shift operator — creates a genuine collision with greedy reading: two closers would be eaten as a shift, three as a different shift, and at four or more the carving becomes outright ambiguous. Rather than weakening the general rule, the specification carves a single exception, scopes it precisely to one syntactic context, states the exact ambiguity that forced it, and shows the counting that makes the collision unavoidable. The exception is narrow enough that a reader can still apply the rule locally everywhere else, and the rationale is published so nobody mistakes it for a general licence.

A programmer who internalises this stops asking "can I make this input work?" and starts asking "can someone predict what this input means by looking only at it?" It changes how you design parsers, configuration formats, template syntaxes, and command-line grammars: reject the input rather than guess, since a guess that is right most of the time is a rule nobody can state. And when a genuine collision forces you off the rule, the obligation is to make the exception countable, contextually bounded, and accompanied by the demonstration that no smaller exception would do.

**Source:** [The Java Language Specification](../works/the-java-language-specification.md) — the lexical-translation section of the lexical-structure chapter, which fixes the greedy longest-match rule together with its acknowledged cost, and the single context-sensitive exception it grants for nested type arguments along with the ambiguity argument justifying it.
