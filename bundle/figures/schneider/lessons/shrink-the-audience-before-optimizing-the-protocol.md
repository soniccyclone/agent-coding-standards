---
type: lesson
title: "The cost of coordination is set by the size of its audience, so shrink the audience before tuning the protocol"
figure: schneider
works: [synchronization-in-distributed-programs]
axes: [parallelizability, hardware-affinity, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# The cost of coordination is set by the size of its audience, so shrink the audience before tuning the protocol

**Lesson:** When a coordination step is expensive, the instinct is to attack the step: fewer round trips, cheaper messages, a tighter encoding. But the dominant term is usually not in the algorithm at all — it is in how many participants must be heard from before the step can be declared settled. If every participant in the system must be consulted, the cost is proportional to the whole system, and no amount of cleverness inside the protocol changes that proportionality. The productive question is not "how do I make this operation faster" but "who genuinely has to be in this conversation."

Usually far fewer than everyone. Coordination is almost always *about* something — a particular resource, a particular queue, a particular pair of endpoints — and only the participants that ever touch that thing have anything to contribute to decisions about it. Parameterize the protocol by the object it coordinates, give each object its own independent history, and the audience for any single decision collapses to the participants that actually use that object. The mechanism does not change; the scope does. Systems structured as a hierarchy of small subsystems get this almost for free, because the natural hierarchy already partitions who cares about what, and the partition can be pushed all the way down into the transport — a channel per object, with each participant listening only to the channels it has a stake in, so uninvolved parties do not even pay for the packets.

Take the bill honestly, though, because the scoping has a real cost and it lands in recovery. Once no single participant holds the full history, no single participant can restore a peer that lost its history. Reconstruction becomes a multi-party operation, and the recovery protocol grows a join across partitions that a globally-replicated history would not have needed. That is a genuine trade, not a free win: steady-state traffic falls roughly with the audience size while the failure path gets structurally harder. Choose it knowing which of the two you would rather debug.

The habit this instills is to look for the participant set before looking at the message count. A programmer who has internalized it treats "all nodes must acknowledge" as a design smell rather than a given, asks what the coordination is actually about, and expects the answer to license a much narrower quorum. They also stay suspicious of their own optimization when the audience is still global — a constant-factor improvement on a term that scales with the system is a distraction from the term that does.

**Source:** [Synchronization in Distributed Programs](../works/synchronization-in-distributed-programs.md) — the implementation-considerations discussion of communication volume, where the per-phase-transition message count is reduced by giving each instance of a mechanism its own history and acknowledger set, with the complication for reconstructing a failed participant's history named in the same breath.
