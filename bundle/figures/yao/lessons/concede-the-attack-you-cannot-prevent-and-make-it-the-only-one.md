---
type: lesson
title: "Concede the deviation you cannot prevent, then define correctness as that deviation being the only one available"
figure: yao
works: [protocols-for-secure-computations]
axes: [verifiability, primitive-count]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# Concede the deviation you cannot prevent, then define correctness as that deviation being the only one available

**Lesson:** No procedure run between mutually suspicious parties can stop a participant from supplying an input other than the one they actually hold. Their private value is private; nothing observable distinguishes an honest run on a lie from an honest run on the truth. Faced with an unpreventable deviation, the productive move is neither to pretend it away nor to abandon the goal, but to promote it to the definition: misbehavior counts as cheating exactly when the offender's actions are consistent with *no* input at all. Everything else — every clever mid-protocol divergence, every fabricated intermediate value, every attempt to make the other side compute the wrong function — is then either detected or is indistinguishable from playing honestly with a different starting value, which is by construction outside the guarantee.

The gain is that the adversary's whole space of strategies collapses onto a single normal form. Instead of reasoning about an open-ended set of attacks, you reason about one parameterized family, and the proof obligation becomes finite and checkable. That collapse is the actual engineering product; the impossibility that forced it was the enabling constraint, not a defeat. Notice too what the definition refuses to promise: it does not claim inputs are truthful, because truthfulness is not a property the mechanism can see. Guarantees stated over what the mechanism can observe survive; guarantees stated over the world behind the interface are wishes.

This is a general discipline for adversarial and fault-tolerant design alike. Before designing defenses, find the irreducible freedom the environment retains — a client can always send a well-formed but false field, a node can always crash between two writes, a caller can always retry — and write the specification so that that freedom is the entire residual attack surface. The system's job is to make every other misbehavior collapse into it or be caught. A specification that instead tries to outlaw the irreducible freedom is unimplementable, and one that never names it leaves the reader unable to tell which of their assumptions the mechanism is actually holding up.

**Source:** [Protocols for Secure Computations](../works/protocols-for-secure-computations.md) — the mutually-suspecting-participants discussion, where the observation that a protocol can never stop a party from behaving as though it held a different value is turned directly into the definition of successful cheating as behavior consistent with no value whatsoever.
