---
type: lesson
title: "Make progress a guarantee the shared object owes each caller, not a favor its callers do each other"
figure: herlihy
works: [wait-free-synchronization]
axes: [parallelizability, verifiability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---

# Make progress a guarantee the shared object owes each caller, not a favor its callers do each other

**Lesson:** The default way to share mutable state is to let one participant at a time inside, which quietly makes everyone's liveness contingent on everyone else's continued good behavior. In an asynchronous system that contingency is not a rare failure mode, it is the normal case: a participant inside the critical region can be descheduled, take a page fault, lose its quantum, or run on a slower core, and to everyone waiting outside, unhurried is indistinguishable from dead. The fix is not better scheduling hygiene but a change in what the shared object promises. State the guarantee per caller and independent of all others: any operation completes within a finite number of that caller's own steps, whatever the others are doing or failing to do.

Two things fall out of taking that formulation seriously. First, it dissolves the failure-detection problem instead of solving it. If no participant's progress depends on another's, then arbitrary slowness and outright halting collapse into the same harmless case, and no timeout, heartbeat, or liveness assumption is needed anywhere in the correctness argument — which is why the resulting proofs need no fairness hypotheses at all. Second, it forces honesty about specifications. An operation defined to block until some condition becomes true — dequeue that waits for a non-empty queue — cannot possibly satisfy the guarantee, since its completion depends by construction on somebody else acting. So the discipline pushes you to define every operation as total, returning an explicit refusal rather than waiting. That is a real design constraint felt at the interface, not an implementation detail, and it is the price of the guarantee.

It is also worth separating this guarantee from its weaker sibling. Promising that the system as a whole always advances is much cheaper than promising that each participant does, and it still rules out the deadlock that locking invites; but it permits an unlucky participant to be starved indefinitely by more aggressive neighbors. Which one you need is a product question about whether individual latency bounds matter — real-time deadlines, heterogeneous cores, adversarial or unpredictable co-tenants — and the interesting fact is that the impossibility results bite equally on both, so the choice between them buys nothing in terms of which primitives you need.

**Source:** [Wait-Free Synchronization](../works/wait-free-synchronization.md) — the introduction's critique of critical sections under delay and failure, the formal implementation conditions that rule out both busy-waiting and conditional waiting without invoking fairness, the restriction to total sequential specifications, and the remark distinguishing the system-wide progress condition from the per-process one.
