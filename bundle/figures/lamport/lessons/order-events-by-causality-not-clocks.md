---
type: lesson
title: "Order events by what the system can observe, not by an imagined universal clock"
figure: lamport
works: [time-clocks-and-the-ordering-of-events-in-a-distributed-system]
axes: [parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency]
tags: [lesson]
---

# Order events by what the system can observe, not by an imagined universal clock

**Lesson:** Programmers carry an intuition of a single timeline on which every event has a position. In any system where communication delay matters, that intuition is not merely unimplementable, it is meaningless: a correctness condition stated in terms of "which happened first" refers to nothing the system can check. The only ordering a distributed system actually has is the one induced by its own communication, a partial order in which two events are ordered exactly when information could have flowed from one to the other. Everything else is a tie, and pretending the ties are secretly ordered is where the bugs come from.

The discipline this teaches is to specify correctness in terms of events observable within the system. If a requirement mentions time, either the system must contain real clocks whose error bounds enter the proof, or the requirement must be restated in terms of message causality. A programmer who internalizes this stops asking "what is the current global state?" and starts asking "what can this process know, given the messages it has received?" That reframing turns vague concurrency anxiety into concrete reasoning about information flow.

The companion insight is that a total order, when you need one, is a manufactured artifact rather than a discovered fact. Any consistent extension of the causal partial order will do, and different choices are equally valid; the arbitrariness is a feature to exploit, not a flaw to agonize over. But manufactured order can disagree with orderings users perceive through channels outside the system, so the boundary of "the system" must be drawn deliberately: either pull the external causality in, or pay for physical clocks tight enough to respect it.

**Source:** [Time, Clocks and the Ordering of Events in a Distributed System](../works/time-clocks-and-the-ordering-of-events-in-a-distributed-system.md) — the opening argument that specifications must refer to events observable within the system, the definition of the happened-before partial order, and the closing discussion of anomalous behavior when the constructed total order diverges from external causality.
