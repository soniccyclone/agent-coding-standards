---
type: lesson
title: "Let breakdown show up as the absence of any continuation rather than as a distinguished event"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [primitive-count, verifiability, expressiveness]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# Let breakdown show up as the absence of any continuation rather than as a distinguished event

**Lesson:** When something goes irrecoverably wrong, the tempting move is to invent a token for it — an error value, a broken state, a failure event appended to the log. There is a cheaper option that is usually also more honest: define the record of what happened to contain only ordinary occurrences, and let the catastrophe register as the fact that no possible record extends the one you have. Nothing is written down at the moment of breakage, because nothing observable happens; what is true afterwards is that the set of things that could happen next is empty. This costs no new primitive, adds no case to any consumer of the record, and cannot be forgotten in a branch, because it is not a branch — it is a property derived from the same machinery already used to say what the system can do at all.

The move only works if the model already answers "what could happen next," not merely "what did happen." That is the real content of the trade. A design that only accumulates a history has to name failure explicitly, because absence is not expressible over a single run; a design that also carries the set of possible continuations gets failure, termination, and deadlock as derived predicates over that set, for free. So the question to ask of any state-recording scheme is not which special values it needs but whether it can quantify over futures. If it can, most of the special values were never needed. The generalization is broader than failure: a surprising number of conditions people give their own flag — unreachable, finished, starved, never-to-be-granted — are the emptiness or singularity of a set you are already obliged to compute.

The discipline this imposes is worth having for its own sake. Two situations that a chosen vocabulary of observations cannot tell apart must not be distinguished by the model either, or you have quietly assumed an observer with powers nobody will have at runtime. So if orderly completion and hopeless deadlock both present as "nothing further can occur" and you genuinely need to tell them apart, the fix is not a flag bolted on outside the vocabulary; it is to admit a new observable occurrence that one of them performs and the other does not. That converts a vague wish to distinguish two outcomes into a concrete instrumentation requirement, which is a much better thing to be arguing about — and it keeps the model's claims exactly coextensive with what can actually be seen.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the traces section of the chapter on processes, where the record of behaviour is a finite sequence of the events that have occurred, the breakage of the over-fed vending machine is not itself recorded, and its having broken is indicated only by there being no event whatever whose addition yields another possible trace; together with the accompanying remarks that the concepts lying outside the chosen alphabet — the customer's hunger, the notion of a completed transaction, the eventual disposal of machine and customer — can neither be observed nor recorded.
