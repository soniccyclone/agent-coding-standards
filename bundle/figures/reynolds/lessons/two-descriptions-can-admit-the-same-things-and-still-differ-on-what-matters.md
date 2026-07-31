---
type: lesson
title: "Two descriptions can admit exactly the same things and still disagree about the only property that matters"
figure: reynolds
works: [the-craft-of-programming]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Two descriptions can admit exactly the same things and still disagree about the only property that matters

**Lesson:** It is easy to check a description of a language against the set of things it admits, and easy to conclude from a match that the description is right. It can still be wrong, because a description of this kind does two jobs and membership is the lesser one. The other job is decomposition: for each admitted item, saying which parts group with which. Two rule sets can agree on every string and disagree on every grouping — one making a chain of operators nest leftward, the other rightward — and if meaning is built up from the meanings of the parts, as it invariably is, then exactly one of them describes the thing you meant and the other describes a different language that happens to look identical from outside.

The practical consequence is that a description also has to be tested against structure, and structure is not visible from any single example that is accepted. Take an item where the grouping is in doubt, derive it under each candidate description, and compare the decompositions rather than the outcomes. This is also the reason ambiguity is a defect rather than a curiosity: an item admitted by two different decompositions has two meanings, and no amount of downstream care recovers the one intended, because the information was never in the text.

The technique for controlling decomposition is worth extracting from the syntax setting, since it applies to any layered description. Do not attach the grouping rules to the operators; introduce an intermediate class per level of binding strength, and let each level be defined in terms of the next tighter one. Ambiguity in a specific position is then removed by narrowing which class may appear there rather than by adding a disambiguation rule off to one side. Adding a new construct becomes the local act of inserting a level, and adding a bracketing form becomes one rule saying that a bracketed whole may stand wherever the tightest atom may stand — so the recursion re-enters at the bottom and everything nests correctly without any further coordination.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Appendix A.1, which exhibits two production sets for expressions of identifiers separated by additive operators that describe the same set of phrases but give a subtraction-then-addition expression different derivation trees, left-associating in one and right-associating in the other, and concludes that since the operators are left-associative in conventional notation only the first describes subphrase decomposition correctly; the surrounding discussion identifies ambiguity — more than one derivation tree for the same phrase — as normally a defect in a language design, removes an instance of it by restricting the phrase class permitted in one position, and builds precedence by introducing intermediate nonterminals for terms and primaries, with a parenthesized expression admitted wherever an identifier is.
