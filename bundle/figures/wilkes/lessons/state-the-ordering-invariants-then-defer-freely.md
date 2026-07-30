---
type: lesson
title: "State crash safety as ordering invariants, then defer every write the invariants do not pin down"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [verifiability, parallelizability]
subdomains: [operating-systems-and-systems-programming, databases-and-data-management]
tags: [lesson]
---
# State crash safety as ordering invariants, then defer every write the invariants do not pin down

**Lesson:** Several records that must agree cannot be made durable simultaneously, so there is always a window in which the persistent state is inconsistent, and a failure inside that window is not an exotic case but the normal one. The productive response is not to shrink the window heroically; it is to choose which inconsistency the window contains. Write down a small set of rules of the form "nothing may be recorded in A unless it is already recorded in B" — chosen so that the only surviving inconsistency is the harmless direction, where some resource is committed but unreferenced rather than referenced but uncommitted. Then a failure leaves state that a recovery pass can force into consistency at a bounded, describable cost.

The payoff is that the invariants tell you exactly which writes must be serialized and, more valuably, which need not be. Any deferral that cannot violate a rule is free: the result can be returned to the caller as soon as memory is updated, with the durable write handed to something that will get to it eventually. Without stated invariants nobody can distinguish the orderings that matter from the orderings that happen, so either everything is serialized — and the system is slow for no reason — or nothing is, and recovery is guesswork. The invariants are what convert a vague desire for safety into a specific, small set of constraints, leaving the rest of the schedule available for optimization.

There is a second return that is easy to overlook. A system with explicit invariants can tell the difference between an inconsistency its rules predict, which recovery handles automatically, and a state its rules say is impossible, which means a defect or a hardware failure. Being able to say precisely when a human is needed — and to be confident that the rest of the time nobody is — is a direct product of having written the rules down. Without them every anomaly looks equally alarming, and the response to all of them is the same expensive shrug.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 4's disc management section, which states the two ordering rules governing the allocation map, the name directory and the file directories, notes that inconsistency is inevitable and that care was taken to make it fall on the safe side, describes the optimizations that defer durable writes wherever the rules permit while returning control to the user immediately, and observes that the resulting precision makes it possible to say exactly when an expert should be called.
