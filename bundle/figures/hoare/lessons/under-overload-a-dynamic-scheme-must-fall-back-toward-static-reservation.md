---
type: lesson
title: "Under overload a dynamic allocator must fall back toward a static regime, so design the floors before the flexibility"
figure: hoare
works: [monitors-an-operating-system-structuring-concept]
axes: [parallelizability, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Under overload a dynamic allocator must fall back toward a static regime, so design the floors before the flexibility

**Lesson:** The case for dynamic allocation is that fixed shares waste capacity: participants with nothing to do hold resources that participants with work could use. That argument is entirely sound while the resource is plentiful, and it inverts exactly when the resource is not. Under saturation, dynamic sharing is precisely the mechanism by which one participant's demand becomes another participant's starvation, and every remedy that preserves liveness — reserving a minimum for each participant whether active or not, capping how much any one may accumulate, bounding the queue that feeds it — is a step back toward the static regime the flexibility was supposed to replace. This is not an admission of defeat about dynamic allocation; it is what dynamic allocation degrades into if it is to remain usable at the limit, and the choice you actually have is whether that degradation is designed or improvised.

The consequence for design order is the useful part. The floors and ceilings are the part that must be right under stress, so they should be established first, with the dynamic policy operating in the space above them, rather than added later as emergency patches once starvation has been observed in production. Deciding a minimum reservation per participant and a maximum accumulation per participant is cheap when the resource model is still on paper, and each of those decisions has a clear justification available: the minimum is what keeps a participant alive when everyone is competing, the maximum is what prevents an unreciprocated accumulation from consuming the pool.

The failure that makes the ceilings non-negotiable is the one outside the resource model altogether: a participant that stops consuming. A stalled or broken consumer keeps requesting nothing and returning nothing, and a purely demand-driven allocator sees no problem — the requester is behaving legitimately, so it gets served until the pool is empty. No policy defined in terms of relative demand detects this, because relative demand is exactly what a dead consumer stops expressing. Only an absolute bound stops it, which is the general point: dynamic policies reason about ratios, and the failures that hurt most are the ones where a quantity goes to zero or grows without limit, so every dynamic policy needs at least one absolute limit standing behind it.

**Source:** [Monitors: An Operating System Structuring Concept](../works/monitors-an-operating-system-structuring-concept.md) — the buffer-allocation discussion, which notes that a producer must be halted before acquiring too many buffers if its consumer stops altogether through mechanical failure, proposes fixing the size of the bounded buffer for that stream and reserving at least two buffers for every stream even when inactive, and remarks that it is an interesting comment on dynamic resource allocation that as soon as resources are heavily loaded the system must be designed to fall back toward a more static regime.
