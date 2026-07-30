---
type: lesson
title: "An audit that requires opening the box destroys the property it was protecting; buy tunable doubt instead"
figure: yao
works: [protocols-for-secure-computations]
axes: [verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# An audit that requires opening the box destroys the property it was protecting; buy tunable doubt instead

**Lesson:** There is always a trivial way to catch a cheater: make everyone reveal every private step afterwards and recompute. It works, it is certain, and it is worthless in exactly the settings that needed it, because the reason the parties ran a protocol instead of just exchanging their data was that they would not exchange their data. A detection mechanism whose evidence is the secret it protects has not been designed, it has been deferred. Recognizing that shape early saves a lot of wasted construction: whenever the fallback verification step would violate the system's headline invariant, the fallback is not an acceptable safety net and the real design problem is detection that stays blind.

The way out is to give up certainty for a knob. Accept that a cheater slips through with some probability, then make that probability an explicit parameter the participants choose, paid for in additional exchanged bits. This is a better deal than it first sounds. Certainty was never available at acceptable cost, whereas a failure probability driven low enough is operationally equivalent to certainty while leaving the protected property intact, and — the part usually missed — it is *composable with a budget*, because you can decide how much cheating-resistance a given transaction is worth rather than paying maximum price everywhere. A guarantee with a tunable error term is a guarantee; a guarantee that only holds if you dismantle the system is not.

The same reasoning recurs far from cryptography. Debugging by dumping production data into a developer's terminal, reproducing a fault by disabling the isolation that made the fault interesting, validating a redaction pipeline by inspecting the unredacted input: each is verification purchased by suspending the invariant under test. Ask, of any checking mechanism, what it requires to be true while it runs, and whether that is compatible with what the system exists to guarantee. If it is not, the honest options are a probabilistic check, a check on a derived witness that does not carry the secret, or no check — and knowing you have no check is worth more than believing you have one.

**Source:** [Protocols for Secure Computations](../works/protocols-for-secure-computations.md) — the note that cheating is always discoverable via a post-hoc stage in which both parties reveal their private computation, the immediate objection that this forces disclosure of the very variables at issue, and the replacement guarantee in which cheating succeeds only with a probability the protocol's parameters drive arbitrarily small at a cost in exchanged bits.
