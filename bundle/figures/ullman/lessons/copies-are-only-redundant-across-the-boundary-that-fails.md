---
type: lesson
title: "Copies are only redundant across the boundary that actually fails"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, verifiability, parallelizability]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# Copies are only redundant across the boundary that actually fails

**Lesson:** Redundancy gets discussed as a count — three copies, five replicas, quorum of seven — and the count is the least interesting part of the arrangement. What determines whether the copies help is where they sit relative to the boundaries along which the system actually loses things, and those boundaries have to be enumerated before the count means anything. In a machine room the enumeration is short and specific: an individual node can die, and a whole enclosure of nodes can vanish at once. Three copies placed inside one enclosure survive the first mode and none of the second, so the honest reading of "replicated three times" is "replicated once, with respect to the failure that takes out forty machines together."

The step people skip is asking *why* the larger unit fails as a unit, because the answer usually reveals that nothing physical was destroyed at all. An enclosure of machines is normally lost not because its disks died together but because the one network element connecting it to everything else stopped working — the data is intact and unreachable, which is the same thing from the outside. That reframing is what makes the placement rule derivable rather than folklore. The shared component is the failure domain, so you find the shared components in the path to each copy and require that no two copies share one. Once stated that way the rule travels: two processes on one host share a kernel and a power supply, two services in one availability zone share a network, two backups on the same schedule share the operator error that runs the schedule, and two independently written checks that both parse the same input share the parser.

The habit worth keeping is to write down what the unit of loss is before choosing a replication factor, and to treat the factor as a consequence of that list rather than an input to it. Doing it in the other order produces systems whose reliability arithmetic is exactly right about a failure mode they do not have. It also produces a useful second question: which failures are you deliberately *not* covering, given that no placement covers everything and there is always a boundary large enough to swallow the whole arrangement. A design that names its uncovered case is doing engineering; one that reports only a replica count is reporting a number nobody can check.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 2's account of large-scale file-system organisation, which requires the nodes holding copies of one chunk to be on different racks and explains that a rack "fails" when the interconnect among its nodes fails, so the rack, not the disk, is the unit that must be replicated across.
