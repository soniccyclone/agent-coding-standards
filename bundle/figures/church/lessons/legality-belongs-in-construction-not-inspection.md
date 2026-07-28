---
type: lesson
title: "Make legality part of how an expression is built, not a check run over it afterward"
figure: church
works: [a-formulation-of-the-simple-theory-of-types]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Make legality part of how an expression is built, not a check run over it afterward

The cheap way to add discipline to a notation is to let anything be written and then run a validator over it. Church takes the opposite route. He starts from a system where every finite string of symbols counts as a formula, and then carves out the well-formed ones with a small inductive definition: a lone proper symbol is well-formed, abstraction over a well-formed body is well-formed, and application is well-formed only when the function's declared domain and the argument agree. The class of legal expressions is exactly the smallest class those rules generate, and each rule hands back a type along with the expression. There is no separate typing pass, because the rule that admits an expression into existence and the rule that assigns it a type are the same rule.

This inverts where the work goes. Under an after-the-fact checker, the interesting objects are the illegal ones, because they exist and must be diagnosed; under a generative discipline, they were never constructed and there is nothing to diagnose. That is why the resulting system can be reasoned about at all: every syntactic form the theory can talk about already carries a coherent interpretation, so a proof about the system never has to case-split on nonsense. Verifiability comes from the shape of the grammar rather than from an auxiliary tool that has to be kept in sync with it.

The discipline is not free, and Church says so before anything else. He opens by admitting outright that the conversion calculus cannot be carried into the type hierarchy intact if abstraction and application are to keep their meanings, and offers the partial merger anyway on the strength of what it buys. The cost shows up later as plumbing: a number living at one level of the hierarchy is a different object from the corresponding number one level up, so explicit transport machinery appears just to relate them, and an operation as ordinary as taking a predecessor within a single level turns out to need a whole extra primitive — a selection operator — that the untyped system never asked for. That is the honest ledger of a construction-time discipline: you buy away a class of meaningless programs and you pay in expressive contortions at the seams.

A programmer who takes this seriously spends design effort on making the bad state unrepresentable rather than on the error message that reports it, and accepts that the encoding will sometimes get uglier at the boundaries as a result. They also read the seams of an existing type discipline as diagnostic: wherever a system needs conversion or lifting machinery to move a value between levels that "obviously" hold the same thing, that is the stratification presenting its bill.

**Source:** [A Formulation of the Simple Theory of Types](../works/a-formulation-of-the-simple-theory-of-types.md) — the opening admission that a complete merger is impossible, the three formation rules for well-formed formulas in the section on well-formedness, and the later remarks on transporting numbers between types and on the predecessor function's need for descriptions.
