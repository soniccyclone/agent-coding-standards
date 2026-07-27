---
type: lesson
title: "Admit undefinedness as a first-class outcome and your operations become unconditional"
figure: kleene
works: [recursive-predicates-and-quantifiers]
axes: [primitive-count, expressiveness, cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Admit undefinedness as a first-class outcome and your operations become unconditional

**Lesson:** Insisting that every function be defined everywhere seems like the conservative, disciplined choice, and it has a hidden cost that shows up as soon as you try to build an algebra of construction operations. Composition, recursion, and projection are all unconditionally safe; the search operator is not, because searching for the first argument satisfying a test only yields a value if such an argument exists. To keep the class closed under search you must attach a side condition to every use of it — and that side condition is an undecidable claim about all inputs at once. So the "clean" total world forces every construction step to carry an obligation nobody can discharge mechanically. Drop the totality requirement, let a function simply have no value where the search does not finish, and the side condition evaporates. The operations become total on the class, closure is unconditional, and the obligations move from the construction to wherever you actually need to know that something terminates.

The second payoff is that partiality is what makes a universal interpreter possible. There is a single partial function of one extra argument that reproduces every function in the class when you supply the right index — one program that runs all programs. That construction cannot be pulled off inside the total world, because the indices denoting everywhere-defined functions cannot even be listed. Universality and partiality come as a package: something that runs arbitrary programs must be permitted to hang, or it is not running arbitrary programs.

The price of admitting undefinedness is real, and it is conceptual rather than technical: equality splits in two. There is the relation that says "both sides have a value and the values agree," which is itself undefined when either side is, and the stronger relation that says "either both are defined and equal or both are undefined." Reasoning has to say which one it means, every time. Along with that comes the need to decide, when you *do* want a total answer, which way to complete a partial predicate — treating undefined as false, or as true — and those two completions have genuinely different properties: the false-completion is what "confirmable by search" means, the true-completion is its dual.

Anyone who has designed with option types, nullable values, partiality monads, futures that may never resolve, or a totality checker knows this trade-off from the other side. The lesson tells you what you are buying: an unconditional algebra of composition and the ability to write interpreters, in exchange for the obligation to distinguish two notions of sameness and to make completion choices explicit. It also names the failure mode of pretending otherwise, where undefinedness is smuggled in as a sentinel or an exception and the two equalities silently get conflated.

**Source:** [Recursive Predicates and Quantifiers](../works/recursive-predicates-and-quantifiers.md) — Part II, which extends the function class to functions that need not be defined everywhere, states the two equality relations and the positive and negative completions of a partial predicate, proves closure of the partial class under all the construction schemes with no side condition on the search operator, and exhibits a single partial function of one extra argument that enumerates the whole class.
