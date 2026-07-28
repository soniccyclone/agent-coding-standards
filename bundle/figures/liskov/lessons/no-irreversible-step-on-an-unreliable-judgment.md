---
type: lesson
title: "Design so that no irreversible step rests on a judgment you cannot make reliably"
figure: liskov
works: [practical-byzantine-fault-tolerance]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Design so that no irreversible step rests on a judgment you cannot make reliably

**Lesson:** A recovery mechanism is part of the attack surface. The natural design for surviving a bad participant is to identify it and remove it — eject it from the group, then continue with the survivors. That design silently makes the whole system's correctness depend on the accuracy of the identification, and in an asynchronous setting accurate identification is not merely difficult, it is impossible: nothing distinguishes a participant that is broken from one whose messages are being held up. So the removal decision is guaranteed to be wrong sometimes, and each wrong removal ejects a healthy participant, eroding the margin the whole scheme was built on. An adversary who has quietly captured one member and can also slow the network does not need to misbehave visibly; it simply arranges for healthy members to be evicted until the margin is gone.

Cranking the suspicion threshold does not fix this, it only relocates the damage. Waiting longer before condemning someone reduces false accusations and correspondingly lengthens the interval during which a genuinely dead coordinator stalls everything. There is no setting of the dial that is safe in both directions, which is the signature of a mechanism resting on a judgment that cannot be made soundly.

The way out is architectural, not parametric: arrange the protocol so the unreliable judgment only ever triggers a reversible, non-destructive step. Suspecting the coordinator can rotate the coordinator role without anybody leaving; membership stays fixed, the margin stays intact, and a mistaken suspicion costs one round of churn instead of a permanent loss. The same discipline applies to housekeeping that seems unrelated: if reclaiming resources requires knowing who is alive, it inherits the same impossible judgment, so reclamation has to be justified by positive evidence from a sufficient set of participants rather than by inferring who is gone.

A programmer who believes this looks for every place a design converts a suspicion into a permanent change and rewrites it to convert the suspicion into a retryable change instead. The general question to ask of any fault-handling path is: what does this do if the diagnosis is wrong, and does a wrong diagnosis leave us weaker than before? A recovery mechanism that degrades the system when it misfires is not recovery, it is a second failure mode wearing a helpful label.

**Source:** [Practical Byzantine Fault Tolerance](../works/practical-byzantine-fault-tolerance.md) — the related-work critique of protocols that must exclude replicas from the group to make progress and to reclaim log space, and the design choice to use view changes only to rotate the primary rather than to alter membership.
