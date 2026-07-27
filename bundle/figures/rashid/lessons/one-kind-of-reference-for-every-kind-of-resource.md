---
type: lesson
title: "A system that grows a new access mechanism per resource kind is losing the argument it started by winning"
figure: rashid
works: [mach-a-new-kernel-foundation-for-unix-development, accent-a-communication-oriented-network-operating-system-kernel]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# A system that grows a new access mechanism per resource kind is losing the argument it started by winning

**Lesson:** The early appeal of a small uniform interface is easy to state and easy to lose. A system that begins with one way to refer to a resource and a handful of operations on that reference gets composition for free: anything that speaks the interface can be plugged into anything else. What happens next, under pressure from real requirements, is that each new kind of resource arrives with its own access path — its own creation call, its own naming scheme, its own escape hatch for the operations that didn't fit. The interface count grows linearly with the resource kinds, and the property that made the original design valuable, that any two components could be joined without knowing each other's type, quietly stops holding. The system still works. It just no longer composes, and no one can say when that stopped being true.

The corrective insight is that uniformity has to be enforced at the level of naming, not merely offered as a convention. If the only thing a program can hold is a reference of one kind, and the only thing it can do with that reference is submit a request to it, then there is no place for a special-case mechanism to appear: a new service is a new receiver, not a new interface. Notice the second-order payoff. Because the reference carries no information about what implements it or where that implementation lives, the question of whether the responder is in the kernel, in another process, or on another machine becomes unanswerable from the caller's side, and therefore becomes someone else's problem to answer. Distribution and extensibility are not features added to such a design; they are consequences of the caller being unable to express a dependency on locality in the first place.

A programmer who takes this seriously treats every proposal for a new special-purpose access path as a design failure to be explained, not a feature to be scheduled. The practical discipline is to ask what would have to be true for the new capability to be expressible as an ordinary participant in the existing scheme, and to spend the effort there instead. The cost is real: a uniform request-based interface is more indirect than a bespoke call, and it demands that request contents be self-describing enough to cross boundaries the designer never enumerated. The payoff is that the number of things a maintainer must know to reason about resource access stays fixed as the system grows, and that whole categories of capability arrive without touching the core at all.

**Source:** [Mach: A New Kernel Foundation for UNIX Development](../works/mach-a-new-kernel-foundation-for-unix-development.md) — the design section's diagnosis of how a system that started with one uniform object interface accumulated a proliferation of parallel mechanisms for managing objects and resources, and the argument for a small primitive basis in which services are named by protected communication references.
