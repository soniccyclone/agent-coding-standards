---
type: lesson
title: "A specification tight enough to check is tight enough to build from"
figure: clarke
works: [design-and-synthesis-of-synchronization-skeletons-using-branching-time-temporal-logic]
axes: [expressiveness, verifiability, parallelizability]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# A specification tight enough to check is tight enough to build from

**Lesson:** The founding paper on model checking spends more of its length on a different activity: constructing the program from the specification rather than checking a program against it. The argument is a chain of consequences from one property of the logic. If a satisfiable formula is always satisfiable in a finite model whose size is bounded by the formula's length, then a decision procedure that produces a witness model when the formula is satisfiable is, in effect, a compiler. Feed it the conjunction of the coordination requirements, get back a finite state graph, and read the coordination structure of the program off that graph. The finite model property becomes a guarantee about implementability: anything you can say in this logic about coordination can be realized by finite-state processes running concurrently.

Two things follow that are easy to miss. First, the decision procedure's negative answer is as valuable as its positive one, but in a different currency. An unsatisfiable specification is not a program that cannot be built; it is a set of requirements that contradict each other, discovered before a line of code exists. Checking your requirements for consistency is a distinct activity from checking your code against them, and the same machinery does both. Second, the model that comes out is global — a single flowgraph over combined states — and the per-process programs have to be recovered from it by projection, keeping each process's own regions as nodes and turning the other processes' state components into the enabling conditions on its transitions. Where distinct global states collapse to the same projected label, an auxiliary variable is introduced to keep them apart, which is how the familiar turn-taking variable of mutual exclusion algorithms appears without anyone having invented it.

That last detail is the most instructive part. A mechanism practitioners reach for by instinct emerged as the forced consequence of separating a global specification into local processes. Coordination state is not a clever trick added to a distributed algorithm; it is the residue of the global picture that local views cannot reconstruct on their own.

A programmer who takes this seriously writes specifications in a form that could in principle generate the artifact, tests them for internal consistency before implementing, and treats the shared bookkeeping in a concurrent design as something derived from the global invariant rather than invented ad hoc. The authors were candid that the procedure's cost is potentially exponential and bet on skeletons being small enough for that not to matter, which is the right way to state such a bet.

**Source:** [Design and Synthesis of Synchronization Skeletons Using Branching Time Temporal Logic](../works/design-and-synthesis-of-synchronization-skeletons-using-branching-time-temporal-logic.md) — the introduction's argument from the bounded finite model property to realizability, the tableau-based decision procedure, and the synthesis section that specifies mutual exclusion as a conjunction of temporal formulas, builds a model, and factors per-process skeletons out of the resulting global flowgraph.
