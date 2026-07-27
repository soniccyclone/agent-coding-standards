---
type: lesson
title: "Put mechanism in the privileged core and push every decision out of it, so the identity of the system lives in replaceable parts"
figure: rashid
works: [mach-a-new-kernel-foundation-for-unix-development, accent-a-communication-oriented-network-operating-system-kernel, from-rig-to-accent-to-mach]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Put mechanism in the privileged core and push every decision out of it, so the identity of the system lives in replaceable parts

**Lesson:** Every system has some region that cannot be replaced by ordinary users — the part running with privilege, the part everything else links against, the part whose bugs are fatal. The gravitational pull on that region is always inward: whenever a new capability needs privileged access or better performance, the cheapest path is to add it there. The result is a core that keeps growing and that encodes, irreversibly, one particular set of answers about how the system should behave. The claim worth taking seriously is that this growth is not the price of capability but a design choice, and that the core can be held to a much narrower job: supplying the mechanisms by which decisions can be carried out, while refusing to contain the decisions themselves.

The test for whether something belongs inside is whether it is a decision or a means. Delivering a request from one party to another is a means. Choosing which party answers a given kind of request is a decision. Enforcing which pages a computation may touch is a means; determining what data belongs on a page when it is first touched, and where it goes when evicted, is a decision — and once you see it as a decision, it becomes obvious that it can be answered by an unprivileged component that the core consults, rather than by code the core contains. The same reading dissolves the assumption that a system's user-visible personality has to be built in. If the core provides only naming, communication, address-space management, and dispatch to processors, then what the system *is* to a program becomes a function of which components are answering requests, not of what was compiled into the privileged part.

Two consequences follow that are hard to get any other way. First, one core serves configurations it was never specialized for, because specialization now happens by choosing components rather than by editing the thing that cannot be edited. Second, and this is the part that pays off over years rather than months, capabilities that would previously have required privileged code become experiments anyone can run and discard. The cost is real and should be stated plainly: pushing decisions outward converts what was an internal call into a boundary crossing, which is why designs of this shape live or die on how cheap that crossing is. This is exactly why the same body of work spent so much of its effort on making communication and memory transfer fast — the architectural argument is only viable if the mechanism it leans on is not expensive.

A programmer who believes this asks of every proposed addition to a privileged or foundational layer: is this a means or a policy, and if it is a policy, what mechanism would let something outside decide it instead? The reward is a core whose reasoning surface stops growing, and a system whose behavior can be changed without anyone touching the part that must not break.

**Source:** [Mach: A New Kernel Foundation for UNIX Development](../works/mach-a-new-kernel-foundation-for-unix-development.md) — the extensibility argument that a system's character comes from its servers rather than its kernel, together with the virtual-memory design in which page-fault and eviction handling are answered by ordinary non-privileged tasks, and the stated program of relocating compatibility functionality out of privileged state.
