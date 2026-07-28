---
type: lesson
title: "When you generalize, the definitions break before the theorems do"
figure: post
works: [introduction-to-a-general-theory-of-elementary-propositions]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# When you generalize, the definitions break before the theorems do

Generalizing a system feels like a proof problem — take the results and see which ones survive with fewer assumptions. Post's paper shows the real obstacle appears earlier. When he drops the specific pair of connectives that the system he started from happens to use, and allows any collection of operators with any behavior, the theorems are not what fails first. The vocabulary fails. "Inconsistent" was defined as deriving something together with its opposite, and the general setting may have no operator that means opposite. The concept has been silently leaning on a feature that was never part of what it was supposed to mean.

His repair is the move worth stealing: re-express the property in terms that survive the removal. Instead of contradiction, he characterizes a broken system as one that derives the bare variable, i.e. one where everything whatsoever becomes assertable. In the original setting the two descriptions coincide, so nothing is lost; in the general setting only the second one is even sayable. He does the same for falsity, defining it by what adding an assertion does to the system rather than by a negation sign, and for sameness of systems, which becomes mutual embeddability rather than shared notation. Each redefinition is chosen so the old case remains a special case.

This is why generalization is genuinely hard work rather than deletion. You have to separate, for every concept you care about, the part that is the idea from the part that is an artifact of the machinery you happened to have. The test is mechanical: state the property without mentioning any specific primitive. If you cannot, you have found a definition that was never as fundamental as it looked, and it will quietly restrict every future extension.

For a programmer this is the discipline behind any real abstraction boundary. Before widening an interface to admit new backends, new value types, new failure modes, go through the concepts the existing code asserts — "equal", "valid", "empty", "failed", "later" — and ask which of them are phrased in terms of a facility the new cases will not have. The ones that are must be restated behaviorally, in terms of observable consequences, before any code moves. Skip that and the generalization ships with the old special case wired into its vocabulary, which is worse than not generalizing, because now the leak is load-bearing.

**Source:** [Introduction to a General Theory of Elementary Propositions](../works/introduction-to-a-general-theory-of-elementary-propositions.md) — the section on the postulational generalization, where consistency, falsity, closure, and equivalence are all redefined for systems lacking a negation primitive.
