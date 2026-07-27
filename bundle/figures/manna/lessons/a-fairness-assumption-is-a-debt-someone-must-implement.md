---
type: lesson
title: "A fairness assumption is a debt someone has to implement, not a fact about the world"
figure: manna
works: [temporal-verification-of-reactive-systems-progress]
axes: [verifiability, parallelizability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming, formal-methods-and-verification]
tags: [lesson]
---
# A fairness assumption is a debt someone has to implement, not a fact about the world

**Lesson:** Manna and Pnueli open their treatment of progress under general fairness by asking, of each fairness notion, what physical or engineered thing it stands in for. Weak fairness stands in for something real and nearly free: separate processors run at the same time, so a process that stays ready will proceed. It appears as an explicit assumption only because the model flattened genuine parallelism into one-step-at-a-time interleaving, and the assumption pays back what that flattening removed. Strong fairness stands in for something else entirely — an implemented arbitration mechanism, a request queue, a hardware arbiter, some protocol with actual code in it. The assumption is not a description of how the world behaves. It is a specification handed to whoever builds the primitive.

They then say the thing that reframes an entire literature: the study of mutual-exclusion algorithms that use no semaphores can be read as the study of how to implement strong fairness out of weak fairness alone. Every one of those algorithms constructs a semaphore. That is what the exercise was, whether or not it was presented that way. And they note the deliberate lossiness of the abstraction — the queue underneath may well serve requests in arrival order, but what is exported upward is only the far weaker promise that a request made infinitely often is eventually granted, so that nothing built on top can accidentally depend on the queue discipline.

Two habits follow. The first is to ask, of every liveness assumption in a design, who pays for it. An assumption that mirrors physical concurrency costs nothing; an assumption that some contended resource is granted fairly is a mechanism that either exists in your stack or does not, and if it does not, the guarantee resting on it is fiction. This is the same reason a fetch-and-add instruction and a semaphore support different provable claims: the difference is what mechanism sits behind them, and you inherit whichever one is actually there. The second habit is the export discipline. When you do implement the mechanism, publish the weakest promise sufficient for your callers, not the strongest one your implementation happens to satisfy — otherwise every caller silently couples to an implementation detail you will want to change, and the coupling is invisible because it lives in their liveness arguments rather than in their code.

The framing also buys a useful piece of modeling flexibility, which the same chapter exploits: because a fairness assumption is just a named promise about what eventually happens, anything with that shape can be modeled the same way, regardless of what it physically is. A protocol layer, an arbiter, a scheduler, and a component that is merely unreliable-but-not-adversarial all become the same kind of assumption, and one reasoning apparatus covers them.

**Source:** [Temporal Verification of Reactive Systems: Progress](../works/temporal-verification-of-reactive-systems-progress.md) — the opening of the Response Under Fairness chapter, which explains justice as the compensation for modeling concurrency by interleaving and compassion as an abstraction of an implemented queueing or arbitration protocol that deliberately exports a weaker guarantee than first-come-first-served, and observes that the semaphore-free mutual-exclusion algorithms studied earlier amount to implementations of compassion from justice.
