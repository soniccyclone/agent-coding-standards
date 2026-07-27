---
type: lesson
title: "Eventually is the weakest promise worth making, and ordering claims come almost free from the same skeleton"
figure: manna
works: [a-temporal-proof-methodology-for-reactive-systems]
axes: [verifiability, expressiveness]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# Eventually is the weakest promise worth making, and ordering claims come almost free from the same skeleton

**Lesson:** Having proven that a waiting process always eventually reaches its critical section, Manna and Pnueli immediately point out what that guarantee fails to exclude. Nothing in it forbids a schedule where one participant is admitted once for every ten admissions of the other. The property is satisfied, the algorithm is starvation-free, and the behavior is still unacceptable. So they add a third class of claim, expressed as a bound on how many times you may be passed over while waiting, and prove that bound separately. The general point is that an eventuality claim says only that a bad state of affairs does not last forever; it says nothing whatsoever about the rate, and the difference between those two things is where real unfairness lives.

The reason no amount of cleverness extracts a bound from an eventuality proof is structural. The only engine available to such a proof is the scheduling assumption that an action which stays possible eventually runs, and that assumption is deliberately rate-free — a scheduler can honor it while being arbitrarily slow, so an argument resting on it cannot conclude anything counted. A bound has to come from a differently-shaped argument, one that counts. This is why the two claims are separate obligations rather than one claim in strong and weak flavors, and why proving the weak one gives you no partial credit toward the strong one.

The pleasing part is how little new machinery the counted claim needs. Their eventuality proofs are built from a set of phases ordered by distance from the goal, a requirement that no step ever moves backward through that ordering, and a requirement that some identified action must move strictly forward and is guaranteed to run. Drop that last requirement and keep the rest, and the same picture proves something else entirely: that the system passes through the phases in order, which is exactly what a claim about one thing preceding another says. One skeleton, two property classes, a single premise apart. The ordering claim is even easier to establish, since nothing has to be shown enabled and no action has to be nominated as the one that makes progress.

A programmer who has absorbed this treats every eventually-claim as an invitation to ask what an adversary can do while still honoring it, and writes the bounded version down as its own separate claim whenever the answer is unpleasant — bounded overtaking on a lock, a cap on retries before escalation, a ceiling on queue residency rather than mere drain-eventually. The second half of the lesson is where the leverage is: the phase decomposition already drawn for the liveness argument is very likely most of the ordering argument too, so the counted claim is usually much cheaper to add than it looks, provided you notice it needs adding.

**Source:** [A Temporal Proof Methodology for Reactive Systems](../works/a-temporal-proof-methodology-for-reactive-systems.md) — in the extended lecture-notes version, the section motivating precedence properties by observing that accessibility puts no measure on the wait, its specification of one-bounded overtaking for Peterson's algorithm, and its precedence rule, which is the response chain rule with the strict-decrease and enabledness premises removed.
