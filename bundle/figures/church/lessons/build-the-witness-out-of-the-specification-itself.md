---
type: lesson
title: "When you must exhibit something satisfying a description, try building it out of the description's own bookkeeping"
figure: church
works: [introduction-to-mathematical-logic]
axes: [verifiability, primitive-count]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# When you must exhibit something satisfying a description, try building it out of the description's own bookkeeping

Church has to show that any consistent collection of statements is true of something. The obvious reading of that task is a search: go find a structure in the mathematical world that happens to fit. He does not search. He manufactures the structure out of the statements themselves — the individuals of the domain are the very constant symbols the language supplies, and the truth value of each atomic statement is defined to be nothing more than whether that statement sits in the extended collection. Interpretation collapses into membership lookup. Once that is set up, the proof that everything in the collection comes out true is a routine induction, because each closure property he had arranged for the collection was chosen to line up one-for-one with a clause in the definition of truth.

The transferable move is to stop treating the described object and the description as living in different worlds. When a specification is consistent and you owe someone an instance of it, the cheapest instance is often the specification's own record-keeping promoted to first-class status: the log of what was asked becomes the thing that answers. But this only works if you first close the description under every question the semantics will put to it. That is why nearly all the labor sits upstream — extending the collection until it decides every statement one way or the other, and supplying a concrete witness name for every existential claim it makes. Constructing the model is a paragraph; earning the right to construct it is the entire proof. If you skip the closure work you get an object with holes exactly where the interrogation goes, and the failure shows up as an unanswerable query rather than a wrong answer.

Two consequences worth carrying. First, this is why a consistency question and a realizability question are the same question, and why the answer to "does anything behave like this?" can be gotten without knowing anything about the domain the requirements were written for. Second, the object you get satisfies precisely what you wrote down and not one thing more. That is a feature when the point is to show some further property is not forced — the syntactic model is the natural counterexample generator. It is a trap when you were quietly hoping the instance would also have properties you never stated, because a construction built from your own words cannot supply what your words omitted.

**Source:** [Introduction to Mathematical Logic](../works/introduction-to-mathematical-logic.md) — §45, where the domain of individuals is taken to be the individual constants themselves and the values of propositional and functional variables are read off membership in the maximal consistent class, with the preceding closure properties deliberately mirroring the clauses of the definition of value.
