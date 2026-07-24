---
type: lesson
title: "Reduce every distributed coordination problem to agreeing on one sequence of commands"
figure: lamport
works: [time-clocks-and-the-ordering-of-events-in-a-distributed-system, paxos-made-simple, the-part-time-parliament]
axes: [primitive-count, verifiability]
subdomains: [distributed-systems-and-concurrency]
tags: [lesson]
---

# Reduce every distributed coordination problem to agreeing on one sequence of commands

**Lesson:** Distributed coordination problems look endlessly varied — mutual exclusion, replicated storage, reconfiguration, leader handoff — but they share a single kernel: if every node applies the same deterministic state machine to the same sequence of commands, every node computes the same state. That reduction collapses the whole zoo into one primitive, agreement on the contents of a numbered log. Solve consensus once and any synchronization discipline you can phrase as a state machine comes for free.

This is a lesson about where to spend design effort. Instead of inventing a bespoke protocol per coordination problem and proving each one separately, prove one hard thing (the agreement protocol) and then get each application's correctness by construction: determinism plus identical input order equals identical replicas. The correctness argument for the application layer becomes trivial exactly because all the distributed difficulty was funneled into a single, reusable, already-proved component. Even system reconfiguration folds in, by making the set of participants itself part of the machine state that commands can change.

A programmer who thinks this way treats "what is the state machine, and what are its commands?" as the first design question for any replicated or coordinated system, and treats any coordination logic living outside the agreed log as a red flag — a second, informal consensus protocol hiding in the design, unproved. The fewer distinct agreement mechanisms a system contains, the closer it sits to something a human or a proof system can actually verify.

**Source:** [Time, Clocks and the Ordering of Events in a Distributed System](../works/time-clocks-and-the-ordering-of-events-in-a-distributed-system.md) — the generalization from the mutual-exclusion example to arbitrary synchronization via a replicated State Machine driven by the totally ordered commands. [Paxos Made Simple](../works/paxos-made-simple.md) — the final section, which builds a fault-tolerant distributed system as a sequence of consensus instances choosing log entries, including reconfiguration through the state itself. [The Part-Time Parliament](../works/the-part-time-parliament.md) — the parliamentary ledger as the same construction: a numbered sequence of decrees whose agreement is the entire problem.
