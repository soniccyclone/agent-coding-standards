---
type: lesson
title: "Derive the implementation from its defining law"
figure: von-thun
works: [recursion-theory-and-joy]
axes: [verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Derive the implementation from its defining law

Most programming is invention followed by validation: guess a construction, run it, adjust. Von Thun demonstrates a different loop for the hardest thing in his language — the combinator that supplies a program to itself so recursion needs no name. He writes down the law the thing must satisfy, which is a single equation relating the combinator's effect to its own reapplication, and then rewrites that equation line by line. Each step exchanges one form for an equal form, driven by a local dissatisfaction he states out loud: this quantity appears in two different shapes, so normalise it to one shape; these two occurrences are now identical, so a duplicating operation can produce them; the remaining argument needs moving out front, so extract it. When no unknown remains, the last line is an implementation, and it is correct because every line equalled its neighbours. He calls this a typical way of writing programs in the language, not a special trick for a special case.

The reason this works is that the notation forms an algebra whose rewrites preserve meaning, so a derivation is simultaneously a construction and a proof. Nothing gets validated afterwards because nothing was guessed. And the method is generative rather than unique: taking a different local step midway yields a second, visibly different implementation, whose equality with the first now follows from both being derived from the same law rather than from testing them against each other. Von Thun exhibits exactly that pair, and pauses to note that the obvious-looking cancellation you might use to relate them is not generally sound — the discipline includes knowing which rewrites you are actually entitled to.

The transferable habit is to write the law before the code whenever a law exists, and to treat the code as its consequence. The law is short, it is the thing stakeholders actually care about, and it is checkable by eye in a way an implementation is not. Even where a full derivation is unavailable — most real code — the ordering survives usefully: state the equation the component must satisfy, then let each line of the implementation answer to it. That converts "does it work" into "which step is unjustified," which is a question with an answer.

**Source:** [Recursion Theory and Joy](../works/recursion-theory-and-joy.md) — the step-by-step development of the recursion combinator from its defining equation, including the alternative derivation reached by taking a different intermediate step and the caution about which cancellation is legitimate.
