---
type: lesson
title: "Deduction moves information around; it never manufactures any"
figure: chaitin
works: [incompleteness-theorems-for-random-reals, the-limits-of-mathematics, algorithmic-information-theory]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [formal-methods-and-verification, foundations-of-computation]
tags: [lesson]
---
# Deduction moves information around; it never manufactures any

**Lesson:** Chaitin's central result is a conservation law. Treat a set of assumptions as a program that grinds out its consequences, and measure the assumptions by the size of that program. Then no conclusion whose content exceeds the assumptions' content by more than a fixed amount is reachable, no matter how long the derivation runs or how ingenious it is. Grinding does not add anything. In the extreme case he constructs, the conclusions available are so thoroughly independent of each other that each one has to be assumed separately, and a body of assumptions carrying N bits settles about N questions and no more.

This converts a familiar sort of frustration into a measurement. Before hunting for a derivation, compare budgets: how much independent content does the claim carry, and how much do the premises carry? If the claim carries more, the search is not hard, it is empty, and no amount of effort finds the argument because the argument does not exist. The striking part of Chaitin's version is that the bound is stated in terms of the size of the reasoning system itself, so it applies to a specification, a type discipline, or a proof assistant exactly as it applies to arithmetic.

The engineering reading is direct. A checking mechanism can only pin down as much behaviour as it distinguishes. A specification small enough to hold in your head does not determine a system whose behaviour carries orders of magnitude more content, and no verification technology repairs that gap, because the gap is informational rather than technological. So the two honest moves are to shrink the system's content until the specification can cover it, or to accept that the uncovered part is not going to be established by reasoning and must be handled some other way. What does not work is expecting a small set of assumptions to underwrite conclusions larger than itself.

**Source:** [Incompleteness Theorems for Random Reals](../works/incompleteness-theorems-for-random-reals.md) - the incompleteness section, where axioms are modelled as a bit string with rules of inference held fixed, and the bounds are stated in terms of the information content of those axioms. Restated with concrete numbers in place of the constants in the course outline of [The Limits of Mathematics](../works/the-limits-of-mathematics.md), and developed at book length as the single theorem the whole of [Algorithmic Information Theory](../works/algorithmic-information-theory.md) is built to prove.
