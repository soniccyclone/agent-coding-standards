---
type: lesson
title: "Multiplexing independent streams couples them, buffering only postpones the coupling, and per-stream backpressure is the only cure"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [parallelizability, hardware-affinity, verifiability]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# Multiplexing independent streams couples them, buffering only postpones the coupling, and per-stream backpressure is the only cure

**Lesson:** Two independent flows, one shared conveyance. The obvious arrangement tags each item with the flow it belongs to, sends it across, and untags at the far end. It works, and it quietly couples the two flows: if the consumer of one is not ready, the item at the head cannot be handed over, and everything queued behind it waits — including items belonging to the other flow, which has nothing to do with the stall. What was independent in the problem statement has become dependent in the implementation, for the plain reason that the flows now share a queue and a queue serves one thing at a time. Nothing about this is a bug in the code; it is a property of the arrangement chosen.

The instinctive repair is to insert buffering, and it postpones the symptom by exactly the buffer's capacity. Once the buffer is full — which it will be if the slow side is durably slow rather than momentarily slow — the coupling returns unchanged, and the only thing purchased was a delay before the diagnosis. That is the general character of buffering: it converts a persistent problem into a delayed one and promises nothing beyond its own size. The standard misreading, that a bigger buffer was needed, misses that what was needed is a way for the healthy flow to keep moving while the stalled one waits, which no shared queue can offer at any capacity.

The real remedy runs in the opposite direction to the data. The receiving end needs a way to tell the sending end to stop producing for the flow that is not being consumed, which means a channel back and a notion of permission granted per flow. Two consequences are worth carrying away. A system that multiplexes must have a reverse path; a strictly one-directional design cannot be made to work, and reaching for buffers instead is treating the absence of that path as though it were a capacity shortfall. And the permission must be per flow rather than aggregate — halting the whole conveyance because one consumer is slow reproduces exactly the coupling you were trying to remove, now with more machinery to maintain and a more convincing appearance of having solved something.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the line-sharing example in the buffers and protocols subsection of the pipes section, where two independent copying tasks must share a single wire, the transmitter tags each message and the receiver untags and routes it, and the accompanying commentary observes that if the recipient of one stream is not ready the whole system waits and the other stream may be seriously delayed, that inserting buffers on the channels will only postpone the problem for a short while, and that the correct solution is another channel in the reverse direction on which the receiver signals the transmitter to stop sending on the stream for which there is little demand — the technique named flow control.
