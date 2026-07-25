---
type: lesson
title: "Measure Behavior Instead of Trusting Declarations"
figure: corbato
works: [an-experimental-time-sharing-system]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, algorithms-and-complexity]
tags: [lesson]
---
# Measure Behavior Instead of Trusting Declarations

**Lesson:** Corbató's multi-level scheduler decides how a job is treated using only two facts the system can see for itself: how much memory the job occupies, and how much processor time it has already consumed without finishing. There is no priority parameter, no urgency class, no way for a user to assert anything about his job at all. He calls this out as a property worth having, contrasting automatic classification against the declarations — or the hopes — of the people submitting work. The sharpest expression of the idea is that a long-running job has to demonstrate its length before it is charged for it: each time it survives its allotted burst it descends a level, so a job that dies unexpectedly early was never penalized for an expectation it did not fulfil.

The principle generalizes past scheduling. Declarations about future behavior are free to make and impossible to check, so any policy keyed on them decays exactly when it starts to matter — under contention everyone claims to be urgent, and a hint that cannot be verified becomes a hint that will be abused. Observed behavior is self-certifying: the system does not have to trust it, because it is the record of what actually happened. This also buys a second-order win on the interface. A policy with no declaration language has nothing for users to learn, nothing to get wrong, and nothing to game, and the vocabulary of the system stays smaller.

Someone who believes this reaches first for the evidence a system is already accumulating before adding a knob. Faced with a caller who "needs" to signal importance, the question becomes which measurement would carry the same information after the fact. The discipline has teeth precisely because it is inconvenient: it forces you to find an observable proxy for intent, and finding that proxy is usually where the real understanding of the workload comes from.

**Source:** [An Experimental Time-Sharing System](../works/an-experimental-time-sharing-system.md) — the multi-level scheduling algorithm, particularly the conclusion drawn under the heading about the highest serviced level, where the automatic nature of the classification is presented as one of the algorithm's guarantees rather than an implementation detail.
