---
type: lesson
title: "Preserve the programmer's indifference to order"
figure: strachey
works: [fundamental-concepts-in-programming-languages]
axes: [parallelizability, expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# Preserve the programmer's indifference to order

An expression built by applying operators to operands constrains evaluation only partially: an operator cannot be applied before its operands are ready, but nothing says in which order independent operands are done. That partial ordering is not an incidental fact about expressions; it is information the programmer possesses about which steps genuinely depend on which. Strachey's observation is that most languages throw it away. Fixing a left-to-right rule buys an exactly defined program, but it forces the author to commit to an ordering he had no opinion about, and the commitment is not recoverable afterwards by any analysis.

The cost lands in two places. The programmer is made to take a large number of logically unnecessary decisions, some of which affect efficiency in ways he cannot predict; and the implementation loses the ability to distinguish sequencing the author cared about from sequencing the notation imposed. Note that this is a statement about what a language can express, not about parallel hardware, which is why it was worth saying in 1967 — the missing capability is a way to say "these are independent," and once it is missing every reader and every compiler must assume dependence. Strachey also shows the limit case honestly: reducing everything to one-argument application does not remove the freedom, since the choice between evaluating operator and operand first still leaves the same latitude, and a conditional is genuinely different because one of its branches may be undefined and so must not be evaluated eagerly. Real dependency structure has to be modelled, not assumed uniform.

What follows for a designer is that determinism and over-specification are separable goals, and conflating them is the error. You want a defined meaning for every program; you do not want a notation whose only way of writing two independent computations is to write one before the other. Strachey's semantic treatment demonstrates the payoff: once commands are modelled as functions over states, the notion of sequencing largely evaporates and is replaced by the partial order that function application already implies. A programmer who has absorbed this reads an imposed total order as lost information, and prefers constructs that let independence be stated rather than inferred.

**Source:** [Fundamental Concepts in Programming Languages](../works/fundamental-concepts-in-programming-languages.md) — the evaluation rule for applicative expressions and the remark on partial ordering that follows it, together with the closing observation of the semantics section that sequencing is subsumed by functional application.
