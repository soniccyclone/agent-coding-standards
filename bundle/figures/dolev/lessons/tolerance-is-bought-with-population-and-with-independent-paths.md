---
type: lesson
title: "Fault tolerance is purchased with two separate redundancies, and no protocol can substitute for either"
figure: dolev
works: [the-byzantine-generals-strike-again]
axes: [hardware-affinity, verifiability]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# Fault tolerance is purchased with two separate redundancies, and no protocol can substitute for either

**Lesson:** How much arbitrary misbehaviour a system can absorb is not a property of its protocol. It is a property of two structural resources, and both are physical. The first is population: enough participants that honest ones outnumber the failure budget by a large enough margin to outvote it. The second is connectivity: enough vertex-disjoint routes between every pair of participants that the budget cannot cover them all. The second one is the one people forget, because the standard formulation of agreement quietly assumes everyone can reach everyone directly. Drop that assumption and the fault threshold becomes a graph invariant. Connectivity is exactly the number of independent routes available, so a sender can push copies of the same value along more routes than there are possible saboteurs, guaranteeing that a majority of the copies arrive untouched.

The sharp part is what the threshold does not depend on. It does not depend on which flavour of agreement is wanted, on whether the network is treated as synchronous, on whether routes are fixed in advance, or on how ingenious the algorithm is. Weakening those assumptions can make an algorithm simpler or cheaper; none of them lowers the threshold as long as broken parts are allowed to act arbitrarily. That is the mark of a genuine resource floor rather than an artifact of a particular construction: you can move work around above it, but you can only cross it by buying more of the underlying resource, which means more machines or more independent links.

For anyone building a real system, this reframes the tolerance conversation. A claim like "the cluster survives two arbitrary failures" is not answerable from the consensus implementation alone. It has to be answered against the deployment graph: how many independent paths exist once you account for the shared switch, the shared rack, the shared availability zone, the shared cable trench. Two participants whose only routes to each other pass through one intermediary are one failure away from being partitioned regardless of the quorum arithmetic. The design questions that actually determine tolerance are therefore procurement and topology questions, and the protocol's job is only to make full use of the redundancy the topology already contains.

**Source:** [The Byzantine Generals Strike Again](../works/the-byzantine-generals-strike-again.md) — the two-part characterization stated up front, the reduction of route availability to graph connectivity that supplies enough clean copies to every receiver, and the closing observation that relaxing assumptions may simplify algorithms but leaves the fault threshold untouched.
