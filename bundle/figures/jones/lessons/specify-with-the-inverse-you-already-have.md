---
type: lesson
title: "Say what you want by naming the check the answer must pass, ideally using an operation you already have"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Say what you want by naming the check the answer must pass, ideally using an operation you already have

**Lesson:** There are two ways to pin down what a piece of work must produce. One is to describe a procedure that produces it. The other is to describe a test that a candidate answer would pass. These are not equally expensive. Recognizing a correct answer is often far cheaper to state than constructing one, and the gap can be enormous — square roots by successive approximation take real work to write down, while the property that distinguishes a square root from a wrong number is one line. Subtraction is defined by what adds back. Whenever that asymmetry exists, the recognizing side is where the specification should live, because it is short enough that a reader can hold all of it and check it against what they meant.

The most reliable place to find such a check is an operation you already have. If the thing you are building is the hard direction of an inverse pair, the easy direction is sitting there and it is a complete description of the hard one. This generalizes past literal inverses: any already-implemented, already-trusted operation that can distinguish a good result from a bad one is a candidate. The practical instruction is to look, before you write a description, for what you can already compute that would settle the question — and treat finding one as a substantial win rather than an accident, because it means the description is now stated in terms whose meaning is not itself in dispute.

Two consequences follow that are easy to miss. First, a check-shaped description usually admits more than one acceptable answer, and that is the feature rather than a defect: it hands the choice among them to whoever is best placed to decide, which is the implementer. Second, and this is the discipline part: the fact that the check is easy to write says nothing about whether the thing being asked for exists. A description in terms of a passing test can silently be a description of nothing at all, satisfiable by no value in the stated domain. Those cases are exactly where you have to add the assumption that makes it possible, and stating that assumption explicitly is not bureaucracy — it is the part of the specification that a procedural description would have hidden inside a branch nobody read.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 2's "Implicit Specifications" section, especially the square-root and subtraction examples given as relations that a result must satisfy rather than rules for computing it, the accompanying remark that the specification of square root is far shorter than any algorithm because a convenient inverse operation happens to exist, the observation that such a specification defines a class of acceptable functions rather than one, and the discussion of the restricted-subtraction example where a pre-condition relating the two arguments is needed to guarantee that an answer exists at all and could not be expressed by the type clause.
