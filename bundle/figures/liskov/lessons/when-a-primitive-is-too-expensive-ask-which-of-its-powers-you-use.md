---
type: lesson
title: "When a primitive is too expensive, find out which of its powers you actually use"
figure: liskov
works: [practical-byzantine-fault-tolerance]
axes: [hardware-affinity, primitive-count, verifiability]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming, algorithms-and-complexity]
tags: [lesson]
---
# When a primitive is too expensive, find out which of its powers you actually use

**Lesson:** A costly building block usually bundles several capabilities, and a protocol built on it typically leans on only one or two of them — but because the block came as a unit, nobody wrote down which. When the cost turns out to dominate everything, the reflex is to accept it as the price of correctness, or to swap in a cheaper block and hope. Both reflexes are wrong. The productive move is to enumerate the block's distinct powers, find where in the argument each is genuinely load-bearing, and discover that most of the traffic needs less than the whole bundle.

Concretely, evidence of authorship comes in two strengths: convincing the intended recipient, and convincing an uninvolved third party who will later be shown the evidence. The second is enormously more expensive than the first, and a protocol needs it only in the specific places where one participant must prove to another that some third participant said something. Everything else — the great bulk of the messages — needs only the cheap strength. Separating the two takes the expensive machinery off the common path and leaves it only on the rare one, which is where the order-of-magnitude difference lives.

The interesting part is that this separation is not a substitution of primitives; it is a change to the protocol. The places that appear to need transferable evidence often do not really need it, provided the argument is rebuilt to rest on collective agreement instead: rather than one participant carrying proof of another's statement, a sufficient set of participants each report what they saw, and the impossibility of that many of them being wrong at once does the work the transferable proof was doing. The cheap primitive plus a restructured argument reaches the same conclusion. That restructuring is real intellectual work, and it is the work that separates a scheme that demonstrates feasibility from one that can be deployed.

A programmer who believes this treats a performance ceiling as a prompt to re-derive the correctness argument rather than to shop for a faster library. The questions are: which property of this expensive thing does each use site depend on, how often is each site exercised, and can the rare-path property be replaced by an argument from collective evidence? Frequently the expensive mechanism survives only in the paths that run when something has already gone wrong, where nobody minds paying.

**Source:** [Practical Byzantine Fault Tolerance](../works/practical-byzantine-fault-tolerance.md) — the cryptography subsection, which identifies proving authenticity to a third party as the one power signatures have that cheaper authentication codes lack, and notes that the algorithm had to be modified to rely on protocol-specific invariants instead of that power.
