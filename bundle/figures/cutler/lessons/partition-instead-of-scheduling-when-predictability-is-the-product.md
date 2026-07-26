---
type: lesson
title: "When predictability is the requirement, remove the sharing instead of scheduling it better"
figure: cutler
works: [oral-history-of-david-cutler]
axes: [parallelizability, hardware-affinity, verifiability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# When predictability is the requirement, remove the sharing instead of scheduling it better

**Lesson:** The default instinct of operating-system design is to maximize utilization by
multiplexing every resource: processors are time-sliced, physical memory is reclaimed from
whoever is least likely to need it next, and a scheduler arbitrates. That instinct is
correct when the goal is throughput across unknown workloads, and it is actively wrong
when the goal is that one workload behave identically on every run. Multiplexing converts
a private resource into a shared one, and sharing means another component's behavior is
now an input to yours. No scheduler is clever enough to hide that, because the variance is
not a scheduling artifact; it is the semantics of sharing.

The alternative is to partition rather than arbitrate: give the workload that needs
determinism a fixed set of cores and a fixed region of memory that nothing reclaims, and
let it keep them whether or not it is currently using them fully. This trades measurable
efficiency for a property that has no incremental version. Either the workload's timing is
independent of what else is running or it is not, and the halfway design gets the costs of
both. Where a system faces both kinds of demand at once, the answer is to make the
partition itself the thing that gets reconfigured, moving whole resources between isolated
domains at coarse grain rather than interleaving at fine grain.

The reasoning generalizes past game consoles and hard real-time. It is the same argument
that favors dedicated connection pools over one shared pool, per-tenant capacity over
best-effort fairness, and static allocation over garbage collection in latency-critical
paths. In each case the shared-resource design has better average numbers and a tail
determined by other people's behavior, and the question is whether the tail is part of the
specification. Partitioning also buys verifiability: reasoning about a component that owns
its resources requires no model of the rest of the system, so the analysis is local.

A programmer who believes this asks early whether the requirement is throughput or
reproducibility, and refuses to answer "both" without saying which one is permitted to
degrade. When the answer is reproducibility, the design work is drawing the isolation
boundary and giving each side hardware of its own, not tuning a scheduler.

**Source:** [Oral History of David Cutler](../works/oral-history-of-david-cutler.md) — the
account of the game console operating system, where cores and memory are assigned to
isolated virtual machines and reassigned in blocks as the foreground changes, explicitly
rejecting the demand-paged timesharing model so that a title's audio and video behave the
same on every run.
