---
type: lesson
title: "The cheapest message is the one nobody sends: elapsed time can carry information if you have paid for synchrony"
figure: schneider
works: [implementing-fault-tolerant-services-using-the-state-machine-approach-a-tutorial]
axes: [expressiveness, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# The cheapest message is the one nobody sends: elapsed time can carry information if you have paid for synchrony

Communication in a distributed system does not have to consist of messages. If every participant holds a clock synchronized to within a known bound, and every participant knows what the passage of a given interval is supposed to signify, then the interval elapsing *is* a transmission — received simultaneously by everyone, requiring no bandwidth, no agreement protocol, and no handling of the sender dying halfway through. A participant who wants the default outcome expresses that by staying silent. Only a participant who wants something other than the default has to spend an actual message. When the default is the common case, nearly all traffic evaporates.

Two properties make this more than a bandwidth trick. First, it is immune to the failure mode that makes distributed agreement expensive in the first place: a sender that crashes mid-protocol, having told some recipients and not others, is the hard case for every dissemination scheme, and there is no such case when nothing was sent. Second, because each participant derives the same conclusion locally from its own clock, the conclusion arrives everywhere without any of them talking — the coordination happens through shared reference to time rather than through exchange. This is also why the technique repairs a failure that messages cannot repair: a participant that holds a resource and then dies never sends the release, but a scheduled deadline releases it anyway, because the deadline was never the dead participant's to send.

The exchange rate is exact and worth memorizing. What you get is messages eliminated and a whole class of partial-send failures made impossible. What you pay is, first, synchrony — clocks with a known bound on skew, and communication with a known bound on delay, which are physical assumptions about real hardware that the rest of the design must not violate — and second, expressiveness, because silence conveys only one predetermined thing. A timed signal carries no arguments. It can say "release" or "vote the default" but never "release with these parameters." The channel has a fixed vocabulary of exactly one word per timeout, which is why the technique applies narrowly and, where it applies, applies devastatingly well.

The transferable habit is to stop treating absence as the empty case. Any place a protocol currently sends a message to convey the ordinary, expected outcome is a place to ask whether the ordinary outcome could be inferred from a deadline instead, with messages reserved for the exceptions. And one refinement keeps the idea from being read too narrowly: what the silence means need not be a fixed constant chosen in advance. The default can be defined relative to whatever the exceptions turn out to be, so that a single participant bothering to speak determines what everyone else's silence said.

**Source:** [Implementing Fault-Tolerant Services Using the State Machine Approach: A Tutorial](../works/implementing-fault-tolerant-services-using-the-state-machine-approach-a-tutorial.md) — the section on using time to make requests, plus the scheduled-release construction earlier in the discussion of defending against clients that fail while holding a resource.
