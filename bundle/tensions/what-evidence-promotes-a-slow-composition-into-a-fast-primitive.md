---
type: tension
title: "What evidence promotes a slow composition into a fast primitive"
figures: [ritchie, lampson]
lessons: [ritchie/promote-to-primitive-only-on-demonstrated-cost, lampson/the-price-of-a-primitive-decides-which-structures-you-can-think-in]
status: resolved-by-llm
tags: [tension]
---
# What evidence promotes a slow composition into a fast primitive

## The decision
A capability can already be assembled from what the system provides, but the assembly is slow. Something belongs in the foundation, or does not. What evidence entitles you to move it down, and how long do you wait for that evidence to arrive?

## Ritchie: wait for named damage, because a foundation entry is permanent
[Promote something to a primitive only when its absence has a demonstrated cost](../figures/ritchie/lessons/promote-to-primitive-only-on-demonstrated-cost.md) holds the line on the core interfaces and applies it to Ritchie's own system in public. Mutual exclusion built by creating and deleting an agreed-upon file is slower than a purpose-built mechanism would be and stays out on exactly that ground, because slower is not insufficient. The discipline is not stubbornness: he concedes the cases where somebody can be named and the damage described, and he separates those from generalized wishes. The reason for the asymmetry is that anything above the foundation can be replaced or ignored, while a primitive has to interact correctly with every other primitive forever and is carried by every future reader of the system. So the correct move is to build the composed version, ship it, keep a written record of who is being hurt, and wait.

## Lampson: the damage is paid in program shape and no one will ever file it
[The measured price of a primitive decides which program structures are available to you](../figures/lampson/lessons/the-price-of-a-primitive-decides-which-structures-you-can-think-in.md) argues that the cost of an expensive mechanism does not show up as a complaint. It shows up as the programs people wrote instead: the hand-rolled state machine, the pool with its own lifecycle bugs, the explicit table tracking who is waiting on what. Those programs work, so nobody reports a defect, and the awkwardness reads as poor taste rather than as the price of the primitive expressing itself in structure. His remedy is to treat the numbers as part of the published specification, measured against the constructs programmers are already choosing between rather than against zero, and to decide which operations get the fastest available implementation by how often they are used rather than by where they sit in a conceptual hierarchy.

## Resolution
**LLM DECISION — Nathan may overturn.**

These are two different decisions wearing one word. Ritchie's rule governs whether a new concept enters the interface; Lampson's governs how fast an existing concept runs and which layer implements it. Ritchie's brake is priced for permanent conceptual obligation, and Lampson's move does not incur any: making activity creation cheaper introduces no new name, no new interaction with the rest of the system, and nothing extra for a reader to hold in mind. Speeding up something already in the specification is free of everything Ritchie is protecting against. Note that Lampson's own split respects the distinction exactly, since scheduling and guarded entry go into the machine because everything touches them, while creation and joining stay in software because they are rarer and more intricate, and none of that changed what a Mesa programmer had to learn.

The mapping between the two layers is the useful part. Lampson's discipline is the instrument that makes Ritchie's evidence arrive. Ritchie is waiting for a measurement and Lampson has explained why the measurement never comes: the harm is invisible by construction, so a policy of waiting for complaints is a policy of waiting forever. But publishing the price of the composed version against the price of the hypothetical primitive converts the invisible harm into something a claimant can point at. Tell people that a file-based lock costs several trips through the filesystem where a real semaphore would cost a few instructions, and the coarse-grained programs stop looking like taste and start looking like a bill. That is a named claimant with named damage, which is precisely what Ritchie said he would accept.

So take Ritchie's threshold and Lampson's evidence standard. Do not add a new name to the foundation on theory. Do add it when someone is hurt, but stop defining hurt as a complaint filed, and start defining it as a survey of what people built instead. A designer who does both publishes the cost of every composed workaround they are asking users to accept, then reads the resulting program shapes as the evidence. Ritchie's semaphore-by-file was the right call under his own rule for as long as nobody could show the structural damage, and would have become the wrong call the moment somebody measured it and showed the programs it was forcing.

**Strongest counter-argument:** the split between concept and speed does not survive contact with implementation. A great many cost reductions cannot be delivered without new interface, because the fast path needs information the old interface does not carry, so the user has to be given a new call, a new flag, or a new object to hold, and Ritchie's permanent obligation is incurred after all. If the cheap version of the mechanism is a different mechanism, then Lampson is not adjusting a number, he is proposing a primitive, and Ritchie's brake applies to it in full force. Against that, the reply above concedes the point and falls back on Lampson's evidence standard alone, which is the weaker half of the resolution. Someone who thinks most performance work is interface work should take the counter-argument seriously and treat the layer split here as covering a smaller region than it appears to.

Related: [who owns the efficiency budget](who-owns-the-efficiency-budget.md), on whether a builder or a user is entitled to spend the cost multiple this decision creates.
