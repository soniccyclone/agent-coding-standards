---
type: lesson
title: "A construction with no bound on its cost is not usable knowledge, so put the budget inside the definition"
figure: cook
works: [feasibly-constructive-proofs-and-the-propositional-calculus, the-p-versus-np-problem]
axes: [verifiability, hardware-affinity]
subdomains: [foundations-of-computation, formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# A construction with no bound on its cost is not usable knowledge, so put the budget inside the definition

**Lesson:** There is a long tradition of prizing arguments that supply a procedure rather than merely asserting existence, on the grounds that a procedure is something you can actually run. The observation that punctures this is simple: an argument can hand you a genuine procedure whose output for a small input is larger than anything the physical universe could hold. In what sense do you then possess a method? The honest answer is that constructivity without a growth bound has bought you nothing operational. It has moved the vacuity from the claim into the cost, where it is harder to see.

The repair is to make the bound part of what the concept means, not an afterthought measured later. It is not enough to restrict quantification to a finite range and declare the result concrete, because a range described by a compact numeral can still be astronomically large; the discipline has to be stated in terms of the size of the description rather than the size of the thing described. Once the budget is inside the definition, statements gain a property that unbounded constructivity lacks: proving one gives you a uniform procedure together with the assurance that it will finish, and both halves are needed. A true statement whose verification cannot be carried out within budget is simply not the same kind of asset as one whose verification can.

Bridging such a formal budget to real feasibility requires an empirical claim, and it should be labeled as one rather than smuggled in. Identifying a polynomial bound with practicality is defensible only as a thesis about problems that actually arise, not as a theorem: an absurdly high fixed exponent is not feasible, a slowly-growing exponential is, and the thesis survives because naturally occurring problems seem not to sit in those corners. What makes this intellectually respectable is that the counterexamples are named rather than hidden, and each one is treated as a debt to be discharged by finding a genuinely practical algorithm for that case. A thesis defended that way is load-bearing; a definition that quietly assumes it is not.

The habit this instills is to attach a cost to every capability claim before believing it. "We can compute that" is an incomplete sentence, and the missing clause — within what budget, as a function of what input measure — is where all the engineering risk lives. When a design rests on the existence of some procedure, the first question is not whether it exists but what it costs on the sizes that will actually arrive.

**Source:** [Feasibly Constructive Proofs and the Propositional Calculus](../works/feasibly-constructive-proofs-and-the-propositional-calculus.md) — the introduction, which argues that a constructive proof says nothing about the length of the object it produces, notes that even a numerically bounded quantifier can require effort exponential in the length of its bound, and proposes polynomial verifiability as the property worth formalizing. Also [The P versus NP Problem](../works/the-p-versus-np-problem.md) — the digression stating the feasibility thesis explicitly as an empirical claim about naturally arising problems, with named potential counterexamples and the standard for retiring them.
