---
type: lesson
title: "How much the answers can tell you is a property of the question you asked"
figure: chaitin
works: [algorithmic-information-theory, incompleteness-theorems-for-random-reals]
axes: [expressiveness, verifiability]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# How much the answers can tell you is a property of the question you asked

**Lesson:** Chaitin makes this vivid with one family of equations and two questions about it. Ask, for each of N settings of a parameter, whether a solution exists, and the N answers turn out to carry only about the logarithm of N in independent content, because the solvable cases can be enumerated and knowing how many are solvable is enough to recover which. Ask instead whether the number of solutions is finite or infinite, and the N answers can be fully independent, N bits with no shortcut between them. Same equations, same arithmetic, same objects. The predicate is what decides whether the answers compress.

The general point is that information content belongs to the query rather than to the subject matter, and choosing what to observe is therefore the most consequential modelling step, taken before any algorithm exists. Two properties that look equally natural in prose can differ enormously in how much structure their answers have. When the answers to a family of questions are cheap to summarise, there is a mechanism in there to exploit, usually some form of enumerability, monotonicity, or a counting identity that collapses the family. When they are not, no ingenuity compresses them and you are looking at a genuine per-case cost.

The habit that follows is to interrogate the predicate before attacking the problem. Given a large matrix of cases to decide, ask whether the answers are related, and look for the reformulation whose answers are related. That reframing is where the leverage lives, and it comes earlier than any choice of technique. It also cuts the other way as a warning: a small change in what you ask, such as moving from existence to cardinality or from eventually to always, can silently convert a tractable question into one whose answers are irreducibly many.

**Source:** [Algorithmic Information Theory](../works/algorithmic-information-theory.md) - the preface and introduction, which explain the choice to ask about infinitude of solutions rather than existence, and give the counting argument for why existence answers are highly redundant. The construction that realises the independent version is the equation built in [Incompleteness Theorems for Random Reals](../works/incompleteness-theorems-for-random-reals.md), whose finite-or-infinite answers track independent coin tosses.
