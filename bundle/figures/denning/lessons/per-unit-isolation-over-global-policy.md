---
type: lesson
title: "Allocate per unit of work so each one's performance depends only on itself"
figure: denning
works: [thrashing-its-causes-and-prevention, virtual-memory]
axes: [parallelizability, verifiability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Allocate per unit of work so each one's performance depends only on itself

**Lesson:** A policy applied across the whole shared pool — evict whichever item anywhere looks least useful — sounds both fairer and better informed than carving the pool into per-tenant partitions. Denning shows it is neither. Under a global rule, how much of the resource a tenant ends up holding is determined by its neighbors' appetites and by its own relative aggressiveness, and the bias is systematic rather than random: he works out that the tenants with the widest footprint are precisely the ones whose holdings get taken, under both of the popular global rules and for different reasons in each case. Wide-footprint tenants are the ones that can least afford the loss, so the global rule reliably punishes the programs that most need protection, and every tenant's performance becomes an emergent property of the whole population.

Under a per-tenant rule with an admission precondition, a tenant's miss rate becomes a function of its own parameter and nothing else — not of how many neighbors are resident, not of how large the pool is. That independence is the actual prize, and it is worth more than any information advantage the global rule could offer. It makes each tenant analyzable in isolation, turns the aggregate into a sum rather than an interaction, and removes the mechanism by which one tenant's growth starts a cascade in another. Denning's stated goal for the policy is not maximum utilization; it is making programs independent of each other, with utilization following from that.

There is a reason global rules resist incremental repair. With one undivided pool there is no local test for "overcommitted" and no way to guarantee any particular tenant enough room even when the pool is not full — the quantity a safe policy would have to check is not defined until you partition. That is a general property of shared-pool designs: the safety predicate you need does not exist in the shared formulation, so no amount of tuning inside it will produce one.

What changes in practice: reach for per-tenant reservations plus admission control before reaching for a cleverer shared eviction rule, and treat "my latency depends on who else happens to be running" as a design defect to be removed rather than a fact of multi-tenancy to be documented.

**Source:** [Thrashing: Its Causes and Prevention](../works/thrashing-its-causes-and-prevention.md) — the comparison of missing-page probability under the two global rules against the working-set rule, showing the large-program bias and the resulting independence claim. [Virtual Memory](../works/virtual-memory.md) — the passage contrasting local and global multiprogramming policies and explaining why global ones are suboptimal.
