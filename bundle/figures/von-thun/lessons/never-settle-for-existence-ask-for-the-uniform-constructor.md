---
type: lesson
title: "Never settle for existence — ask for the uniform constructor"
figure: von-thun
works: [recursion-theory-and-joy]
axes: [expressiveness, verifiability]
subdomains: [foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# Never settle for existence — ask for the uniform constructor

Von Thun states each of his theorems twice. The first version is the ordinary one: for every program of some kind, a program with the desired property exists. He then immediately strengthens it to a form with the quantifiers rearranged — there is one fixed program which, given any input program, produces the desired one. He does this for parameterisation, for diagonalisation, for the fixpoint theorem, and for the self-reproducing variants, every time, and the strengthened version is always the one he goes on to use. The fixpoint case is the clearest payoff: the uniform constructor gets a name and becomes an ordinary operator in the language, and from it the recursion combinator follows in one further step. The weak form could not have been used that way, because a construction that exists case by case is not a thing you can invoke.

The difference between the two forms is exactly the difference between a fact and a tool. Existence per case licenses you to build the object whenever you need it; a single uniform constructor is the object, available at the same level as everything else in the system, composable with the rest. Moving the quantifier outward also raises the bar in a productive way: it forbids constructions that secretly inspect the input and branch on what they find, forcing you to discover the one mechanism that handles all cases the same way. That mechanism is usually simpler than any of the per-case constructions, and it is what you actually wanted.

For a programmer the discipline is to notice when you have proved something only pointwise. You have a procedure for migrating this schema, a recipe for wiring up this handler, a documented sequence for adding a case to this dispatcher, a known-good pattern people copy. Each of those is an existence result carried around by hand, and each instance is an opportunity for the pattern to be applied slightly wrong. The question to keep asking is whether the recipe can be replaced by one thing you call. Sometimes the answer is genuinely no, and then the recipe should say why. But asking converts a body of tribal practice into either a component or a stated reason, and both beat a habit.

**Source:** [Recursion Theory and Joy](../works/recursion-theory-and-joy.md) — the recurring pattern where each classical theorem is restated with a single outer program that transforms any input program into the required one, and the fixpoint case where that program is then adopted as a named operator.
