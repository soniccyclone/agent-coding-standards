---
type: lesson
title: "Judge a checker against an independent account of what going wrong means"
figure: milner
works: [a-theory-of-type-polymorphism-in-programming]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Judge a checker against an independent account of what going wrong means

**Lesson:** Most static checkers are self-justifying: the rules define what "correct" means, so passing the checker is true by construction and says nothing beyond itself. The move worth learning here is to define failure once, in the runtime model, before writing any rule about programs. Give the evaluator an explicit distinguished outcome that represents a type violation actually happening, and separately define what it means for a runtime value to inhabit a type. Only then define the syntactic rules. Now the claim that the rules are worth obeying becomes a theorem with real content: every program the rules accept evaluates to something that inhabits a type, and the failure outcome inhabits none.

This holds because the theorem connects two things that were built for different reasons and could have disagreed. The value-level notion of a type is a semantic property — closed downward and closed under limits of approximations — and it makes no reference to program syntax. The rule system is a finite syntactic discipline that makes no reference to the semantic domain. Their agreement is contingent, so proving it is informative, and any mistake in the rules shows up as a case of the proof that will not close. Contrast a checker whose only specification is its own implementation: there is nothing for a proof to fail at, so errors in the discipline are invisible until users trip over them.

The practical payoff comes in what you may then delete. Once acceptance provably implies the violation outcome is unreachable, the runtime no longer needs to carry or consult type information — the checker has bought the right to erase. That is the shape to look for whenever you build an analysis: the guarantee is only worth an optimization if you can state it against a model of execution the analysis did not author.

A programmer who internalizes this stops writing validation layers whose contract is "whatever the validator happens to reject." They ask instead: what is the bad state, defined in terms of the running system? What property of a value rules that state out? And can I show my cheap syntactic gate implies that property? Absent those three, the gate is a ritual, and any downstream code that trusts it is trusting nothing.

**Source:** [A Theory of Type Polymorphism in Programming](../works/a-theory-of-type-polymorphism-in-programming.md) — the split between the section giving a denotational semantics with an explicit error value and a value-level possession relation for types, and the later section proving that syntactically well-typed expressions evaluate into a type.
