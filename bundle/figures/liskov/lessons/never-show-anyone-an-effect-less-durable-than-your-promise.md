---
type: lesson
title: "Never show anyone an effect that is less durable than the promise you made about it"
figure: liskov
works: [providing-high-availability-using-lazy-replication]
axes: [verifiability, hardware-affinity, parallelizability]
subdomains: [distributed-systems-and-concurrency, databases-and-data-management, operating-systems-and-systems-programming]
tags: [lesson]
---
# Never show anyone an effect that is less durable than the promise you made about it

**Lesson:** Visibility creates an obligation. The moment an observer sees an effect, that effect is part of the history the observer will reason from, and if it can still evaporate, the observer's subsequent behavior becomes unexplainable — it will have acted on a cause that no longer exists anywhere. This is a strictly worse failure than a delay, because it is undetectable and unrecoverable from inside the system. Hence a rule that constrains every asynchronous design: the threshold at which something becomes readable must be at least as strong as the threshold at which it becomes permanent.

The rule bites hardest where a system has decoupled acknowledgment from propagation for good reasons. If a single site can accept a change, answer immediately, and only later tell its peers, then between those two moments there is a window in which a reader could observe something that a crash would erase. The fix is not to abandon the decoupling but to define the readable point and the durable point to be the same point, and to accept that this makes the fast path slightly slower. The cost is honest and quantifiable; the alternative is a rare, silent corruption of causality.

There is a second, cheerier half. The durability threshold does not have to mean writing to a disk. Redundancy the system already possesses can serve: an effect recorded at some number of independent sites survives that many fewer failures, and the number is chosen from the reliability requirement alone — not from any voting arithmetic, and typically far below a majority. That reframing matters because the disk-based approach is both wasteful, duplicating redundancy that already exists, and worse for availability, since the single site holding the only durable copy becomes a bottleneck for anything that depends on it. When redundancy is already the architecture, adding a second, unrelated durability mechanism is usually a mistake.

A programmer who believes this identifies, for every effect, the exact moment it becomes visible and the exact moment it becomes unloseable, and treats any gap where the first precedes the second as a defect regardless of how narrow it is. They also audit the durability mechanism for redundancy with the replication scheme, and set the durability threshold from a stated failure-survival requirement rather than inheriting whatever number the consensus protocol happened to need.

**Source:** [Providing High Availability Using Lazy Replication](../works/providing-high-availability-using-lazy-replication.md) — the reliability and availability section, which defines stability in terms of the number of replicas holding an update, forbids queries from observing not-yet-stable updates because of the resulting loss of causality, and argues against stable storage as redundant with replication.
