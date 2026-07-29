---
type: lesson
title: "Noticing a fault is cheaper than surviving one, so buy redundancy per layer instead of uniformly"
figure: schneider
works: [byzantine-generals-in-action-implementing-fail-stop-processors]
axes: [hardware-affinity, verifiability]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# Noticing a fault is cheaper than surviving one, so buy redundancy per layer instead of uniformly

Detection and masking are different services with different prices. To notice that something has gone wrong, it is enough to have two independent parties who should agree and find that they don't — disagreement is the signal, and a small amount of duplication produces it. To continue operating correctly through a fault, you need enough copies that the correct answer can be identified among the wrong ones, which takes materially more. Applying one redundancy factor across an entire system therefore overpays everywhere except the one layer that actually needed masking.

The resulting shape is a small, heavily replicated core that masks failures, wrapped around a larger, lightly replicated body that only detects them. The application logic — the expensive part, the part there is a lot of — is duplicated just enough that a fault shows up as a mismatch. The narrow core that records durable state and adjudicates those mismatches is replicated to the strength required to survive faults outright, because it is the thing nothing else can back up. This is a general argument about where to spend, not a fact about processors: locate the components whose failure must be invisible, and pay masking rates only there.

A consequence that looks wrong at first: once a layer is replicated for masking, its instances can be packed onto shared physical resources without invalidating the independence the design depends on. Independence is a claim about the *failure budget*, not about hardware allocation. If the system tolerates some fixed number of failures overall, and every logical service in the core has more copies than that number, then even a hostile concentration of all tolerated failures onto the shared machines leaves each service with a surviving majority. The intuition that co-location always destroys fault independence is a heuristic standing in for an arithmetic check that is worth actually doing — because doing it is how the core's cost stops scaling with the number of things it serves.

The final piece is about granularity of blame. When detection operates on an aggregate, the aggregate is what gets declared dead, and that condemns healthy members along with the faulty one. If the unit of declaration is also the unit of permanent write-off, the healthy resources drain away monotonically at a rate set by the failure rate. The fix is to separate the two: declare the aggregate failed immediately, since that is what safety needs, then individually re-adjudicate its members, testing them and returning the sound ones to the pool. Fast condemnation and slow, individual rehabilitation are compatible, and a system without the second half quietly bleeds capacity every time the first half fires.

**Source:** [Byzantine Generals in Action: Implementing Fail-Stop Processors](../works/byzantine-generals-in-action-implementing-fail-stop-processors.md) — the closing discussion contrasting the replication factor of the storage kernel with that of the application processes, the section on assigning processes to processors and why sharing does not break the guarantee, and the recycling scheme for reclaiming healthy processors from a halted unit.
