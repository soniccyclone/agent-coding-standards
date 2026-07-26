---
type: lesson
title: "Budget failures happening at once, not failures ever; then rejoining costs nothing"
figure: dolev
works: [reaching-approximate-agreement-in-the-presence-of-faults]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Budget failures happening at once, not failures ever; then rejoining costs nothing

**Lesson:** There are two very different readings of "tolerates up to t failures". The weak one bounds the total number of parts that misbehave over the whole life of the run, which means the system slowly consumes its budget and eventually exhausts it, no matter how briefly each part was actually sick. The strong one bounds only how many are misbehaving at any given moment, and imposes no limit at all on the lifetime count. Real deployments live under the second regime: machines get rebooted, links flap, processes get paged out past their deadline and come back. A design whose correctness argument uses the first reading is quietly betting that the aggregate of all transient trouble over months stays under a threshold sized for concurrent trouble.

Which reading you get is decided by whether participants carry accumulated state across rounds. If a participant's contribution in a round is a function of what it received in that round, then a participant returning from an outage has nothing to reconstruct. It publishes something arbitrary, collects, combines, and from that point forward its value is inside the honest range like everyone else's, because the combining rule was already built to neutralize a budgeted number of arbitrary contributions and does not care whether a given one came from a saboteur or a convalescent. Recovery is not a feature that had to be designed; it is what falls out of never having accumulated anything worth restoring. That is a strong argument for state that is recomputed rather than maintained, well beyond agreement protocols.

The residue is instructive too, because it is not literally free. A returning participant does need to learn which round the group is on and how much longer the run has to go, and it cannot simply believe the first answers it hears, since some of them may be lies or stale. The fix is the same arithmetic used everywhere else: collect enough answers that the budget cannot dominate them, and take the order statistic that a budgeted adversary cannot push. Under weaker timing guarantees this takes a little more care, because a naive rejoin can attach itself to a round whose messages have already gone by. The general point is that the only recovery machinery needed is whatever is required to relocate yourself in time, not to rebuild your beliefs.

A programmer who takes this seriously asks of every fault-tolerant component: does my budget refresh? If a component's invariants depend on the cumulative history of who has ever misbehaved, its stated tolerance is optimistic in production. If they depend only on how many are misbehaving right now, and each cycle refreshes state from fresh input, then intermittent failure is ordinary operation rather than a slow leak toward the cliff.

**Source:** [Reaching Approximate Agreement in the Presence of Faults](../works/reaching-approximate-agreement-in-the-presence-of-faults.md) — the resilience discussion that upgrades the claim from a bound on total faulty participants to a bound on participants faulty at any one time, together with its sketch of how a recovered participant re-enters, including the order-statistic trick for picking a safe re-entry round and obtaining a fresh termination estimate.
