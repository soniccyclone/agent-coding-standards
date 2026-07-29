---
type: lesson
title: "Redundancy is unfinished until you can name who does the final combining, and shared fate can make a component free"
figure: schneider
works: [implementing-fault-tolerant-services-using-the-state-machine-approach-a-tutorial]
axes: [verifiability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Redundancy is unfinished until you can name who does the final combining, and shared fate can make a component free

Every redundancy scheme eventually needs something to reduce many answers to one. That reducer is a component, so it can break, so replicating everything upstream of it and stopping there accomplishes nothing — the whole ensemble's correctness now hangs on one part. Replicate the reducer and the problem moves rather than vanishing: now something must reduce the reducers. The recursion does not terminate inside the system. It terminates only when you can point at something outside the boundary that performs the last combination and is not yours to make reliable: a person glancing at one of several displays and looking at another if it seems wrong, a physical control surface that moves in the direction the majority of its actuators push. Naming that thing is part of the design, and a resilience argument that cannot name it has an unexamined single point of failure at its tip.

This has a hard consequence worth stating plainly, because it is the point at which the theory admits a limit. Some final combiners cannot be built. A component that cannot be reliably silenced when it goes bad — an actuator whose shutoff may itself fail — puts a hard ceiling on lifetime tolerance no protocol removes, because the standard trick of ejecting a broken part and continuing depends on ejection actually working. Where the world will not let you disable something, redundancy stops accumulating, and the honest move is to say so rather than to keep counting replicas.

The counterweight is the more surprising half, and it inverts a reflex most engineers hold. Correlated failure is usually the enemy of redundancy, since independent failure is what replication is purchasing. But when a reducer shares fate with the *only consumer of its output*, its unreliability becomes free. Put the vote-taker inside the requester, on the same machine, and it is broken exactly when the requester is broken — in which case nobody was going to act correctly on the result anyway. The failure has no victim. That same shared fate also collapses the work: a requester co-resident with one member of the ensemble can simply trust that member, because if the machine is bad the requester is bad too and its behavior is already outside the guarantee.

So the question to ask about any component in a fault-tolerance argument is not "can this fail?" — everything can — but "when this fails, who is left to be harmed?" If the answer is a party that is already failed by the same event, the component needs no protection and costs nothing to trust. If the answer is anyone else, it needs to be replicated, and the recursion continues until it exits the system. Two questions, applied at every stage, and the boundary of what redundancy can actually buy becomes visible instead of assumed.

**Source:** [Implementing Fault-Tolerant Services Using the State Machine Approach: A Tutorial](../works/implementing-fault-tolerant-services-using-the-state-machine-approach-a-tutorial.md) — the section on tolerating faulty output devices, which pushes the voter regress out past the computing system to a reader it does not control, together with the co-residency optimization for client-side combining and the later observation about output devices that cannot be disabled.
