---
type: lesson
title: "Assume every participant is broken or hostile, and make whoever opens an interaction carry its risk"
figure: brinch-hansen
works: [rc-4000-software-multiprogramming-system, the-nucleus-of-a-multiprogramming-system]
axes: [parallelizability, verifiability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Assume every participant is broken or hostile, and make whoever opens an interaction carry its risk

**Lesson:** A synchronization primitive can be logically sufficient and still be the wrong thing to build a system on. Counting semaphores are enough to express any coordination you want, but they assume every participant obeys the protocol: one program that fails to release, or releases something it never took, corrupts the state that everyone else depends on, and nothing in the mechanism can tell the difference between a mistake and an attack. In a system where programs come and go, where some of them are being debugged, and where a few of them will simply be wrong, sufficiency is not the criterion. The criterion is what the mechanism does when a participant misbehaves.

Designing to that criterion changes the primitives. Give every exchange an identity, record who owns it, and check ownership on every operation, so no third party can inject itself into a conversation between two others. Make finite shared capacity a per-participant allowance rather than a global pool, so nobody can exhaust it and stall the system by talking to a partner who never answers. Push the cost of an interaction onto whoever initiates it: the party that opens an exchange puts up the resource it consumes and bears the consequence if the other side never responds, which means a single reckless program damages only its own budget. Most importantly, define what removal means while an interaction is in flight — outstanding requests to a departed party get synthesized failure replies, and its own outstanding requests are left where they are so that resources return as the world drains rather than leaking.

The underlying way of thinking is that partial failure is a normal state of the system rather than an exception to handle later, and that the mechanism must stay meaningful across it. A programmer who believes this stops asking whether a primitive can express the coordination needed and starts asking what an adversarial or half-dead caller can do with it, then designs so the honest answer is "hurt itself." Notice that the requirement is not defense in the security sense — it is the more basic demand that a system of independently failing parts stay in a state its remaining parts can still reason about.

**Source:** [RC 4000 Software Multiprogramming System](../works/rc-4000-software-multiprogramming-system.md) — the discussion of why buffered exchange was chosen over semaphores, which reasons explicitly about participants that break the rules, about ownership checks on buffers, and about what happens to pending traffic when a party is removed. Also [The Nucleus of a Multiprogramming System](../works/the-nucleus-of-a-multiprogramming-system.md) — the process-communication section, which states the safety and efficiency objections to semaphores and the per-participant limit on outstanding requests.
