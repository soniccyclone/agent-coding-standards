---
type: lesson
title: "A designated role is hidden state that has to be rebuilt after a crash; symmetric designs have nothing to re-elect"
figure: schneider
works: [synchronization-in-distributed-programs]
axes: [parallelizability, verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# A designated role is hidden state that has to be rebuilt after a crash; symmetric designs have nothing to re-elect

**Lesson:** Appointing one participant to decide something is the most natural simplification in distributed design, and designers usually defend it by noting that the appointment is temporary or migratable — the role moves around, so no one is permanently privileged, so the asymmetry seems harmless. That defense answers a fairness objection while missing the structural one. A role is state. It is state that does not live in any single participant's memory but in the agreement of all of them about who currently holds it, and every such piece of state has to be reconstituted after a failure. The steady-state benefit is visible in the design; the reconstitution cost is invisible until something crashes.

And that cost is not small, because it compounds. Re-establishing the role needs a selection procedure, which is itself a distributed agreement problem — the very thing the role was introduced to avoid, now reappearing in the failure path where it is hardest to get right. Worse, the new holder starts empty: the decisions it must make depend on the state of everyone else, so it has to gather that state from every remaining participant before it can act. Two nontrivial subproblems, both dormant during normal operation, both on the critical path exactly when the system is already degraded. The bottleneck people usually cite about central arbitration is the lesser complaint.

The alternative is to give every participant the same job and no participant a special one: all of them observe the same ordered history and compute the same decision from it independently. This costs more in the common case — everyone does the work, everyone stores the history — and pays for it by having nothing to re-elect. A participant that fails and returns is not resuming an office, it is catching up on a log, which is a mechanically simpler operation with a mechanically simpler correctness argument. The asymmetric design is cheaper to run and harder to prove; the symmetric one is the reverse.

What changes in practice is where a programmer looks for hidden complexity during review. Any coordinator, leader, primary, owner, or token holder gets read as an unstated commitment to build a selection protocol and a state-transfer protocol, and the design is judged including those. When they are absent from the plan, the design is not simpler than the symmetric alternative — it is incomplete, with the missing pieces deferred to the moment they will be most expensive to write.

**Source:** [Synchronization in Distributed Programs](../works/synchronization-in-distributed-programs.md) — the related-work comparison against token- and sequencer-based schemes, which argues that a designated arbitrator is not only a bottleneck but leaves behind two hard problems on failure, in contrast to having every process independently simulate the same decision machine.
