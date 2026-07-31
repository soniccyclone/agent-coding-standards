---
type: lesson
title: "Minimize the basis you justify things against, then refuse to make anyone work in it"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Minimize the basis you justify things against, then refuse to make anyone work in it

**Lesson:** A single selection construct is enough to define every logical connective: negation, conjunction, disjunction, implication, all of them fall out of one three-part form. Having discovered that, the tempting conclusion is to throw the connectives away and write everything in terms of the one primitive. That conclusion is wrong, and understanding why is worth more than the reduction itself. Expressions written in the minimal basis are correct and unreadable; manipulating them is drudgery, and the familiar operators come with a stock of equivalences — commutativity, distribution, the de Morgan laws — that make transformation something you can do at a glance. Discard the vocabulary and you discard the laws with it.

The right conclusion is that a system has two distinct surfaces and they should not be forced to coincide. The basis is what everything else is *justified against*: it should be as small as you can make it, because every primitive is a separate thing to be believed, and because a small basis is what makes an appeal to soundness short enough to actually follow. The working vocabulary is what people *write in*: it should be as rich as the domain wants, and its members should be exactly the concepts practitioners already reason with, so their intuition transfers instead of being retrained. The relationship between the two is a set of definitions, each individually checkable, and the redundancy of the vocabulary is not waste — it is the whole point, since every derived operator that carries useful algebraic laws pays for itself many times over in the manipulations it enables.

The design instruction is therefore twofold and the second half is the one usually skipped. Find the smallest basis, so that the number of things taken on faith is small and the definitions of everything else are checkable. Then build a deliberately redundant layer over it and make that the layer people touch, keeping the primitive form as the thing you fall back on when a question about meaning has to be settled. A language, library, or protocol that exposes only its minimal core has done half the job and shipped the half that nobody wanted; one that exposes only its convenience layer has no way to answer what anything really means when two conveniences disagree.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — the "*More on Logic" section of chapter 3, where the propositional connectives are given definitions in terms of the conditional expression and the observation follows that this one operator is therefore enough to provide a basis for all of logic, immediately qualified by the remark that manipulation in that form becomes tedious and it is far preferable to retain the familiar operators for most purposes; taken together with the list of identities for conditional expressions supplied in that same section for the same reason the propositional equivalences were supplied in chapter 2, namely that a notation is only workable if it comes with laws for transforming it.
