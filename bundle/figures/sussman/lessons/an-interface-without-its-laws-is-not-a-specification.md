---
type: lesson
title: "An interface without its laws is not a specification"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [verifiability, expressiveness]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# An interface without its laws is not a specification

**Lesson:** Asked what data actually *is*, the authors reject the obvious answer. Saying it is whatever the given constructor and selectors implement is not enough, because plainly not every arbitrary triple of procedures would do. What completes the definition is a condition the procedures must jointly satisfy -- construct from two parts, select them back out, and the relationship between them must be preserved. A representation is valid exactly when it meets that condition, and the condition is the specification.

This is a sharper standard than an interface signature, and the difference matters. Names and argument counts constrain nothing about behaviour; any implementation typechecks. The law is what rules out the wrong ones, and it is also what tells an implementer what freedom they have -- everything the law does not pin down is theirs. An interface published without its laws has not specified a contract, it has published a vocabulary, and every property its callers actually depend on will have been inferred from the current implementation and will break silently when that changes.

The book then pushes the idea to its limit to prove the point. It implements pairs using no data structures whatsoever -- the constructor returns a procedure that selects between two captured values, and the selectors apply it. Nothing about this resembles the intuitive notion of data. It is nonetheless a completely valid representation, and the entire argument for its validity is that it satisfies the stated condition. Nothing else was ever required.

Two things follow. Whether something is data or procedure is not a fundamental distinction but a question about which laws hold, which is why the two categories keep collapsing into each other as the book proceeds. And practically: when specifying any abstraction, write the equations its operations must satisfy alongside their signatures. Those equations are what a reimplementation must preserve, what a test suite should check, and the only honest answer to a user asking what they may rely on.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.1.3, which asks what is meant by data, rejects the answer that it is whatever the given selectors and constructors implement, states the condition relating construction and selection that any valid representation must satisfy, and then exhibits a representation of pairs built entirely from procedures -- with the observation that it corresponds to nothing like the intuitive notion of data yet is perfectly adequate because it fulfils the only conditions pairs need to fulfil, and that a user accessing pairs only through the interface cannot distinguish it from one using real data structures.
