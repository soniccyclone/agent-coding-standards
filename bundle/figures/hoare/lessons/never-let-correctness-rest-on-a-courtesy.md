---
type: lesson
title: "Never let correctness rest on a courtesy the implementation was never obliged to provide"
figure: hoare
works: [communicating-sequential-processes-paper]
axes: [verifiability, parallelizability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
tags: [lesson]
---
# Never let correctness rest on a courtesy the implementation was never obliged to provide

**Lesson:** Every specification that leaves a choice open creates two distinct populations of behavior: what an implementation is required to do, and what a good implementation will do anyway because it wants to be fast or responsive. These must be kept rigorously apart, because a program's correctness argument may draw only on the first. The temptation runs the other way. Real implementations behave decently — they will not starve a request that has been waiting forever, they will pick the branch that is ready — and code written against observed behavior appears to work, so the dependence goes unrecorded. It surfaces later as an inexplicable failure on a different implementation, a different scheduler, or a machine with a different number of processors, and the failure is unfixable by local reasoning because nothing in the program text was ever wrong.

The right posture is to state the weak guarantee in the definition, urge the strong behavior on implementors as a quality obligation, and put the burden on the programmer to prove the program correct without it. This looks harsh but it is the only arrangement where all three parties can do their jobs. If the definition promised the strong behavior, implementors would be obliged to deliver it in cases where the cost is unbounded, and the language would have committed to outcomes it cannot guarantee. If the programmer may assume it, then every implementation is retroactively constrained by whatever existing programs happen to lean on, which is a set nobody can enumerate. The same discipline already applies in sequential code without anyone remarking on it: an implementation will naturally favor whichever branch it can execute more cheaply, and no one considers that a licence to depend on the choice.

There is a corollary about programs that dodge the question by never ending. If a system is intended to run forever, termination arguments are vacuous and the temptation to lean on implementation goodwill is unchecked, since the day of reckoning never comes. That should be read as a reason for suspicion about the design rather than as an exemption. A long-running system that cannot be brought to an orderly stop on request has no defined final state at all, which means the only way to stop it is to break it — and a system with no clean stopping point is one whose invariants were never actually stated.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-paper.md) — the fairness discussion, which gives an example program whose termination depends on the implementation not persistently favoring one alternative, argues that the language definition must not require fairness while an efficient implementation should nonetheless avoid unreasonable starvation, draws the analogy with branch selection in sequential alternative commands, and questions whether programs intended to run forever should be written at all.
