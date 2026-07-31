---
type: lesson
title: "Algebraically equivalent formulas stop being equivalent once the values carry uncertainty"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Algebraically equivalent formulas stop being equivalent once the values carry uncertainty

**Lesson:** Two expressions that any algebra textbook would call identical, computed over quantities that carry a range rather than a point, produce different answers. Not slightly different -- one is systematically looser than the other, and the one people write first is usually the worse of the two. A user reports this as a bug and the authors treat the complaint as serious, which it is, because it means a transformation everyone regards as meaning-preserving is not.

The cause is worth understanding because it generalizes far past this example. When an uncertain quantity appears more than once in an expression, each occurrence is treated as an independent source of uncertainty, and the arithmetic has no way to know they are the same quantity and must move together. Every repeated variable therefore inflates the result's spread by accounting for combinations that cannot actually occur. Rearranging the formula changes how many times each uncertain value appears, and so changes the answer -- meaning the count of occurrences, not just the mathematical content, is part of what you are computing.

That yields a usable rule and a real limitation. The rule: among algebraically equivalent forms, prefer the one in which no uncertain variable is repeated, because it gives the tightest correct bounds. The limitation, which the authors pose as a genuinely hard open problem rather than an exercise: you cannot in general fix this inside the arithmetic, because the arithmetic sees values, not the identity relationships among them.

The generalization to carry: whenever a value is a summary of something -- an interval, a distribution, an error bound, an estimate -- operations on those summaries are not the same operations as on the underlying quantities, and identities you rely on may silently fail. Floating point breaks associativity for the same family of reasons. Before rearranging an expression for elegance or efficiency, ask whether its values are things or summaries of things, because for summaries the rewrite is a change of meaning rather than a change of form.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.1.4's extended interval-arithmetic exercise, in which two algebraically equivalent formulations of parallel resistance produce different intervals, the complaint is called a serious one, exercise 2.15 proposes that a formula gives tighter bounds when no variable representing an uncertain number is repeated, and exercise 2.16 asks in general why equivalent algebraic expressions may lead to different answers and whether a package without this shortcoming is possible -- flagged as very difficult.
