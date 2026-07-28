---
type: lesson
title: "A yes/no test earns its keep when the proof of 'yes' also builds the thing"
figure: post
works: [introduction-to-a-general-theory-of-elementary-propositions]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [formal-methods-and-verification, foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# A yes/no test earns its keep when the proof of 'yes' also builds the thing

There are two grades of decision procedure and they are easy to confuse. The lower grade tells you a property holds. The higher grade tells you the property holds *and*, as a side effect of how it convinced itself, hands you the artifact that exhibits it. Post's completeness argument is the second grade. The mechanical evaluation over all assignments settles membership, but the harder half of the argument — that everything the test accepts is genuinely derivable — is carried out by a staged recipe that pushes an arbitrary expression into a uniform shape and then assembles a derivation for that shape. The consequence he points out himself: pass the test and you can immediately write the formal proof down, not merely believe one exists.

The reason this matters is that a bare verdict is unusable at the boundary. When the answer is yes, a downstream consumer usually needs the object, not the assurance — the derivation to audit, the plan to execute, the schedule to run, the counterexample to fix. A decision procedure that only returns a bit forces whoever needed the object to search for it again, from scratch, with no help from the reasoning that just established it must be there. Worse, an existence-only argument can be non-constructive in ways that hide a genuine gap: it proves the search terminates without telling you where to look, and nobody downstream can tell the difference until they try to use it.

Practically, this converts into a design habit for anything that answers a question about a program: prefer the algorithm whose acceptance path is a construction. Type checkers that produce elaborated terms rather than a thumbs-up. Solvers that return the satisfying assignment, not just SAT. Optimizers that emit the rewrite trace. Linters that emit the fix. It usually costs more work up front and it usually forces you to normalize the input into a canonical shape first — Post pays exactly that price, flattening arbitrary expressions into a rigid disjunctive form before he can generate anything. The payoff is that verification stops being a gate you argue with and becomes a producer other stages can build on.

The corollary is a diagnostic. If you can prove your checker complete only by an argument that never touches an actual derivation, you have learned less than it appears, and you should suspect the completeness claim itself before you trust it.

**Source:** [Introduction to a General Theory of Elementary Propositions](../works/introduction-to-a-general-theory-of-elementary-propositions.md) — the sufficiency half of the fundamental theorem, worked in four stages culminating in the observation that the proof itself yields an immediate recipe for writing down a formal derivation of any expression the test accepts.
