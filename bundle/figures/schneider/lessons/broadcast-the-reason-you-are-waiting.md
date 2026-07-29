---
type: lesson
title: "Broadcast the reason you are waiting, not just the fact of it, and global questions turn into local ones"
figure: schneider
works: [synchronization-in-distributed-programs]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Broadcast the reason you are waiting, not just the fact of it, and global questions turn into local ones

**Lesson:** Most blocking primitives publish a status and hide a reason. A process announces that it is suspended, or occupies a slot in a wait queue, but the *condition* it is waiting on stays private — encoded in a program counter, a local predicate, a closure over its own stack. That asymmetry is why so many global properties of a concurrent system are undecidable from inside it: no participant holds enough information to answer the question, and answering it requires a second, separate mechanism bolted on top.

Invert the choice. Make the message a process sends when it blocks carry the full description of what would unblock it — the whole set of counterparties and shapes of interaction it is currently prepared to accept — and make that description visible to everyone. Now every participant holds the same catalog of outstanding intents, and a family of questions that used to need dedicated machinery becomes ordinary local computation over that catalog. Two processes can independently pick the same interaction out of their overlapping intents without negotiating, because both are reading the same data and applying the same deterministic tiebreak. A cycle of mutually unsatisfiable intents whose participants all name each other and nobody outside is, on inspection, a deadlock — no detector, no probe messages, no global snapshot algorithm. The property was always there; publishing intent is what made it observable.

The economics matter. Announcing intent looks wasteful: a richer message, sent to everyone, describing possibilities that will mostly not be taken. But it is a single one-time cost that retires several downstream mechanisms, whereas hiding intent buys a cheaper message and then pays repeatedly — in an arbitration protocol to resolve conflicting choices, in a detector to find cycles, in the reasoning burden of proving those two components agree with each other and with the primitive they surround. Fewer moving parts that share one substrate beats more parts that each maintain a private view.

A programmer who takes this seriously designs blocking interfaces around declared acceptance sets rather than opaque waits, and treats the visibility of a waiting condition as part of the interface rather than an implementation detail. It also changes how they react to a request for a new diagnostic: before building a monitor, they ask whether the information the monitor would need could simply have been in the messages the system already sends. Very often the missing observability is not a tooling gap but a consequence of an earlier decision to keep a reason private.

**Source:** [Synchronization in Distributed Programs](../works/synchronization-in-distributed-programs.md) — lives in the construction of the conditional message-passing facility, where a process entering a communication publishes the entire set of communications it would accept; the deterministic independent guard selection and the throwaway remark that deadlock detection now needs nothing extra are both consequences of that one representational choice.
