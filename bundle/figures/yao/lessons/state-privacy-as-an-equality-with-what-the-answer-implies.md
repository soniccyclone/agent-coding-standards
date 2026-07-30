---
type: lesson
title: "State a privacy requirement as an equality with what the answer already implies, quantified over what an adversary can compute"
figure: yao
works: [protocols-for-secure-computations]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# State a privacy requirement as an equality with what the answer already implies, quantified over what an adversary can compute

**Lesson:** The naive way to say "this party learns nothing extra" is to enumerate what was not sent. That framing fails twice over. It ignores the leak the result itself carries — being told which of two quantities is larger already narrows the other party's possibilities, and no protocol can undo that — and it stops at the transcript, when the real question is what a participant can *derive* from the transcript afterwards at leisure. The durable formulation runs the other way: fix the reference knowledge a participant is entitled to, namely the answer plus everything logically forced by it, and demand that their actual belief about the hidden input be indistinguishable from that reference. Now the unavoidable leak is inside the specification instead of being an embarrassment outside it, and the property has an exact shape you can argue against rather than a list of blocked channels that grows every time someone thinks of a new one.

The second half matters as much as the first. The requirement has to range over the adversary's *computation*, not merely their received messages, because the cheapest attack on a protocol that transmits nothing incriminating is to sit down afterward and grind: guess a value, apply the public transformation, see whether it matches something you were handed, and learn a fact you were never told. Bounding the extra work the adversary may do — and admitting that with some small probability the grinding succeeds — converts an absolute claim nobody can prove into a two-parameter claim you can: the derived belief is within a small factor of the reference, except with small failure probability. The parameters are the honest price of the property being computational rather than informational.

Generalize past cryptography and this is how to write any "must not escape" requirement — isolation between tenants, redaction in a log, capability confinement. Name the observer, name exactly what the observer is licensed to know, then require equivalence with an idealized version of that observer, and be explicit about how much effort the real one is allowed to spend trying to close the gap. Requirements shaped as equivalence to an ideal admit proofs and survive attacks nobody enumerated; requirements shaped as a blacklist of leaks are refuted by the first channel the author did not think of.

**Source:** [Protocols for Secure Computations](../works/protocols-for-secure-computations.md) — the informal security argument for the millionaires' protocol, its own follow-up observation that a participant could search offline for a preimage and thereby learn a fact outside the sanctioned answer, and the resulting formal privacy constraint stated as an approximate match to the distribution consistent with the computed value under a bounded amount of further private calculation.
