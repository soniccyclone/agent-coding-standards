---
type: lesson
title: "Never let a timing guess be load-bearing for correctness; spend it on progress instead"
figure: liskov
works: [practical-byzantine-fault-tolerance]
axes: [verifiability, parallelizability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification, operating-systems-and-systems-programming]
tags: [lesson]
---
# Never let a timing guess be load-bearing for correctness; spend it on progress instead

**Lesson:** Every distributed protocol eventually needs some assumption about time, because with none at all it cannot promise to finish. The decision that determines whether a protocol survives contact with a hostile network is not whether it makes a timing assumption but which of its two promises the assumption underwrites. Attach it to the promise that the system never produces a wrong answer, and you have handed an adversary a lever: anyone who can slow messages down can manufacture a violation of correctness without breaking into anything. Attach it only to the promise that the system eventually produces an answer, and the same adversary can at worst make the system slow — annoying, recoverable, and not a correctness failure.

The asymmetry matters because delaying traffic is vastly easier than subverting a participant. A protocol whose correctness argument contains a sentence beginning "assuming messages arrive within" has a correctness argument that a modest network attack refutes. And the temptation to make that assumption is real, because it simplifies everything: with known bounds you can conclude from silence that something has failed, and reasoning from silence is enormously convenient. Refusing that convenience is what forces a design where every conclusion is drawn from evidence actually received, never from evidence not received.

The counterpart is that a liveness-only timing assumption can be made remarkably weak and still do its job. It does not need a bound anybody knows; it is enough that delay does not grow without limit forever, coupled with a mechanism that stretches its own patience each time it is disappointed. That weakness is what makes the assumption plausible in a real network, where the honest description of the situation is that things get repaired eventually rather than that things arrive within any stated interval.

A programmer who believes this audits their correctness arguments for hidden appeals to elapsed time and moves each one into the progress argument, replacing it with something derived from messages in hand. They also stop treating a timeout as a fact — a timeout is a hint that something might be wrong, never evidence that it is, and any step taken purely on the strength of a hint must be one the system can survive taking wrongly.

**Source:** [Practical Byzantine Fault Tolerance](../works/practical-byzantine-fault-tolerance.md) — the service-properties section, which places safety in a fully asynchronous model, confines synchrony to liveness with a deliberately weak assumption about growth of message delay, and explains why relying on synchrony for safety exposes a service to denial-of-service as a correctness attack.
