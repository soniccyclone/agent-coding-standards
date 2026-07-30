---
type: lesson
title: "A model earns its keep by making impossibility sayable, not by making solutions prettier"
figure: yao
works: [protocols-for-secure-computations]
axes: [expressiveness, verifiability]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# A model earns its keep by making impossibility sayable, not by making solutions prettier

**Lesson:** A field accumulates clever constructions long before it can say what cannot be built, and the missing ingredient is always the same: a model precise enough that a question about the non-existence of a solution is even well-formed. Until then, "nobody has managed it" and "it is impossible" are indistinguishable, and effort keeps flowing into goals that no amount of ingenuity will reach. So the test of a proposed abstraction is not whether it makes the constructions you already have look tidier. It is whether, stated in that abstraction, a sharp question about limits — can parties who trust nothing agree on an outcome with this particular bias, can this exchange be made fair — has a determinate answer rather than a shrug.

Two properties make such a frame worth adopting. First, its degenerate corners must reproduce the problems already solved: set one participant's computation to a constant and you should be looking at the plain transmission problem the field started with; make the computation the hard part and you should be looking at the new territory. A frame whose special cases do not recover the known results is describing something else. Second, it must fix precisely what the participants may do, how long they may do it for, and what they are trying to learn, because impossibility proofs are exactly arguments about the boundary of the allowed, and a frame that leaves the boundary vague cannot support one. Where several mechanisms rest on genuinely different assumptions, that means several models, stated separately, rather than one blurred model that flatters all of them.

The practical form of this in ordinary engineering is that a specification you cannot use to rule things out is not a specification. If your consistency model, your permission model, or your failure model cannot answer "is behavior X achievable here at all," it is documentation of intent rather than a definition, and the first surprising incident will reveal it as such. Building the frame is unglamorous work that precedes the interesting results and makes them possible — including the results that tell you to stop.

**Source:** [Protocols for Secure Computations](../works/protocols-for-secure-computations.md) — the unified-view section, which motivates the framework by noting that questions about the intrinsic power and limits of one-way functions cannot even be posed without one, casts message-security and private computation as the two extremes of a single two-party evaluation setting, and pairs this with the closing section deriving concrete impossibility results inside the model so defined.
