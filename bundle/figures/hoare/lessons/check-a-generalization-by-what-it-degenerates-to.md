---
type: lesson
title: "Check a general framework by what it degenerates to, and charge its extra notation only to the general case"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Check a general framework by what it degenerates to, and charge its extra notation only to the general case

**Lesson:** A framework built to handle a hard case has to be validated against the easy case it subsumes, and the validation is specific: restrict it to the situation the older, specialized method covers, and confirm that what you get is mathematically the same thing the older method gives — not similar in spirit, not compatible, the same. Two payoffs follow immediately. Everything already established with the specialized method transfers rather than needing redoing, and anyone who knows the old method has a place to stand while learning the new one. A generalization that cannot be shown to collapse onto its predecessor is not a generalization; it is a second, competing account, and someone will eventually discover that the two disagree about a case both claim to cover.

The honest part of the exercise is admitting what the collapse costs. In the degenerate case the general framework will be more cumbersome than the specialized one — carrying variables that are always trivial, discharging conditions that are always satisfied, writing clauses about a dimension that has collapsed to a point. That extra weight is real and should be acknowledged rather than argued away, because the argument for the framework does not depend on it being free. The argument is that the same weight is exactly what makes the general case tractable, and that the general case is one you actually have. Stated that way the burden becomes acceptable, and stated the other way — insisting the general framework is no harder — it invites the entirely fair reply that the simpler tool is right there.

The practical consequence is a rule about when to adopt a general apparatus at all. If your problems live in the degenerate case, use the specialized method; the general one costs you notation and buys nothing today. Adopt the general apparatus when problems that need it are present or imminent, and when you do, keep the degeneracy result visible, because it is what lets a team use the light-weight reasoning for the light-weight parts of the same system without maintaining two disconnected theories. A framework you can enter and leave at the right places is worth much more than one that demands to be used everywhere.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the specifications subsection of the assignment section in the sequential processes chapter, which after developing a calculus of total correctness for sequential programs observes that a proof in that form establishes a precondition/postcondition pair in the sense of Cliff Jones, that where the postcondition does not mention initial values the assertion is equivalent to Dijkstra's weakest precondition, and that for non-communicating programs the proof methods are mathematically equivalent to already familiar ones though notationally more clumsy because of the explicit clauses about the empty and terminating traces — with the closing remark that the extra burden is necessary and therefore more acceptable once the methods are extended to communicating processes.
