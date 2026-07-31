---
type: lesson
title: "Let claimants collide in one pool with an ownership tag rather than carving the resource up, because partitioning exports an allocation problem upward"
figure: wilkes
works: [slave-memories-and-dynamic-storage-allocation]
axes: [cognitive-load, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Let claimants collide in one pool with an ownership tag rather than carving the resource up, because partitioning exports an allocation problem upward

**Lesson:** There are two ways to let several competing users share one scarce fast resource. Divide it into reserved regions, one per user, or let them all use the whole of it and record with each occupied slot which user it belongs to. Partitioning looks tidier and delivers isolation, but it forces somebody to choose the boundaries, and that somebody sits above the mechanism. You have not solved the sharing problem; you have converted it into an allocation problem and handed it to a policy layer that will have to decide sizes, revise them as the population changes, and own the resulting failure modes. Tagged sharing keeps the decision inside the mechanism, where nobody allocates anything: entries simply displace one another, and the ownership tag preserves correctness through every collision. What you surrender is any per-user guarantee, in exchange for never having to state a policy.

Whether that trade is right turns on the shape of each user's benefit curve. If a user's gain from residency is smooth — some of its data surviving until its next turn is proportionately useful — pool the resource and let collisions happen, because the average case is what you get and the average case is good, especially when users run in short frequent bursts and only have to survive a brief absence. If instead a user's benefit has a knee, a minimum footprint below which it degenerates into constant reloading, then reservation earns its complexity, and the reservation should be sized to clear the knee rather than to look fair. The question worth asking early is which of these two curves you are dealing with, because it decides the architecture and it is answerable from measurement rather than argument.

The broader habit is to look at any two candidate designs and ask which of them leaves a decision to be made later, by a human or by a higher layer. That design is not simpler; it is incomplete, and the deferred decision will be made with less information than the mechanism itself had. The mechanism observes the real access pattern. The supervisor above it observes only its own model of that pattern, which is why explicit partitioning is consistently easier to draw and harder to operate. Push each decision to the level that can actually see what the decision depends on, and treat a clean diagram that requires an operator to tune it as evidence against itself.

**Source:** [Slave Memories and Dynamic Storage Allocation](../works/slave-memories-and-dynamic-storage-allocation.md) — the large-slave section's comparison of two schemes: subdividing the fast memory into sections each dedicated to one program block, which the text notes would hand the supervisor's designer a dynamic storage allocation problem of the kind Atlas faced, versus letting the whole fast memory serve several program blocks at once with tag bits naming the owning block, accepting that some words get overwritten but arguing the arrangement is advantageous on average when programs run in short bursts.
