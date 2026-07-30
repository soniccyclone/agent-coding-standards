---
type: lesson
title: "Make abandonment a first-class correctness property, and specify it as a recovery procedure the injured party can run"
figure: yao
works: [how-to-generate-and-exchange-secrets]
axes: [verifiability, parallelizability]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# Make abandonment a first-class correctness property, and specify it as a recovery procedure the injured party can run

**Lesson:** Two properties dominate the specification of any multi-party procedure: it computes the right thing, and it discloses nothing beyond that. Both are properties of runs that finish. Neither says anything about the participant who reads the value it wanted and then stops answering, and that silence is where the real losses live — the counterparty holds a half-completed transaction, has already surrendered whatever it surrendered, and has no remaining move. Treating early departure as an operational nuisance rather than a specified property means the guarantee you wrote down and the guarantee you needed differ in exactly the case that costs money. It belongs alongside the other two as a separate obligation with its own statement, because no strengthening of correctness or of confidentiality implies it.

The instructive part is how to state it. The tempting phrasing is prohibitive — the deserter must not be able to end up ahead — which is a claim about the whole space of adversarial strategies and therefore hard to establish and easy to state vacuously. The stronger phrasing is constructive: for every strategy the deserter might follow, exhibit a procedure the abandoned party can run on the transcript it already holds which recovers the outcome, cheaply, with the failure probability driven below any threshold the parties choose in advance. Now the guarantee is a program, not a prohibition. It can be implemented, tested, and handed to the injured party as a concrete remedy; and its proof is an existence argument over strategies rather than a survey of attacks. The asymmetry the deserter hoped to create is answered by construction rather than by argument.

The reframe this forces is worth carrying everywhere partial failure is possible, not just where an adversary is assumed. The question stops being *can the other side cheat me* and becomes *what can I still compute from what I have when the other side stops*. A two-phase commit, a payment settlement, a partially applied migration, a distributed lock handoff — each has a state where one participant has gained and the other is stranded, and in each the useful specification names the stranded party's recovery routine and its cost. If you cannot write that routine, you have not designed a protocol; you have designed a happy path with an incident response plan attached.

**Source:** [How to Generate and Exchange Secrets](../works/how-to-generate-and-exchange-secrets.md) — the introduction's statement that adding fairness to the existing validity and privacy requirements is what motivated the paper at all, together with the fairness clauses in the secret-generation, exchange, and general-computation sections, each of which asserts the existence of a polynomial-time recovery algorithm run by the honest party rather than a bound on the cheater's capabilities.
