---
type: lesson
title: "Who starts an exchange need not be who paces it"
figure: wirth
works: [project-oberon]
axes: [expressiveness, hardware-affinity, verifiability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Who starts an exchange need not be who paces it

**Lesson:** In most interactions between two components we quietly assume that the one who initiated is the one in charge for the duration: it asks, the other answers, and control flows outward and back. That assumption is a convenience, not a necessity, and it costs something. The initiator is generally the party that knows *what* is wanted and the responder is generally the party that knows *when* each step can happen — how long an operation takes, when a buffer is free, whether the request was acceptable at all. Keeping control with the initiator therefore forces the party with the knowledge to communicate its timing to the party without it, which means either the initiator guesses and polls, or the responder acquires a way to signal readiness, and either way the arrangement has to be reinvented per operation.

Handing control to the responder immediately after contact is established resolves this cleanly. The initiator's role shrinks to naming the counterpart and then supplying what is asked for, when it is asked for; the responder drives, requesting each element of the command, then the data, then reporting status, at intervals it chooses. Nothing has to be estimated by the party that cannot estimate it, and back-pressure is not a feature that needs adding because it is the shape of the interaction. The pleasant consequence is that the initiator's code becomes a loop that answers requests rather than a sequence with waits embedded in it, which is both shorter and much less sensitive to changes in the responder's speed.

The price of the inversion is that "who may speak now" is no longer implicit, so it has to be made explicit and cheap to determine. This is why such arrangements come with an unambiguous notion of the current stage of the exchange, observable by both parties, and why any element of a transaction that has no use — a status the initiator does not care about, a final message it will ignore — must nevertheless be consumed rather than skipped. Under initiator control, ignoring an unwanted reply is harmless. Under responder control, the parties' agreement about where they are in the exchange is the only thing keeping the interaction coherent, so leaving anything unread desynchronises them, and the next transaction fails for reasons that have nothing to do with itself. Choose which party drives; then honour the stage discipline that choice implies.

**Source:** [Project Oberon](../works/project-oberon.md) — section 9.4's account of the disk interface, in which the initiator begins by selecting a target on the shared bus and, from that point onwards, the target acts as master and the initiator as server; the six prescribed phases in which the target requests the command bytes, then the data, then sends status and finally a message; and the remark that this last message has no significance for the application but must be received anyway according to the rules of the standard.
