---
type: lesson
title: "Keep the slow general method underneath the fast special one"
figure: sutherland
works: [sketchpad-a-man-machine-graphical-communication-system-afips-1963]
axes: [expressiveness, verifiability]
subdomains: [programming-environments-and-object-systems, algorithms-and-complexity]
tags: [lesson]
---
# Keep the slow general method underneath the fast special one

**Lesson:** A solver that only handles the cases you can analyze structurally is not a solver; it is a lucky special case with a crash waiting behind it. The move worth copying here is layering: implement first the method that always terminates with *something* for *any* problem the user can pose, however slowly, and only then add the analyzer that recognizes the well-behaved subset and dispatches it exactly. The fast path becomes an optimization rather than a load-bearing assumption, which means its failure to apply is an ordinary event with a defined consequence, not a defect report.

This ordering holds because the two paths answer different questions. The general iterative method buys coverage: it will accept relations whose error is nonlinear, time-varying, or dependent on things outside the model entirely, because all it ever asks of a relation is a number to shrink. The structural method buys exactness and speed, but only where the dependency graph happens to admit an evaluation order — and whether it does is a property of the user's problem, not of your code, so you can never make it true by trying harder. Notably, the hardest-to-order problems and the ones the general method handles worst are not the same set, so the two methods cover each other's weak regions instead of duplicating each other's strengths.

A programmer who believes this stops writing solvers, planners, and query optimizers that throw when the input falls outside the analyzable class. Instead they define, up front, what the fallback is and what its cost is, and they treat "the fast path did not apply" as a normal outcome worth measuring rather than an error worth reporting. It also changes what you build first: the boring universal engine ships before the clever analyzer, so the clever part can be wrong without taking the system down. And it makes performance honest — the analyzer's hit rate on real workloads is a number you can watch, rather than a claim buried in an assumption.

**Source:** [Sketchpad: A Man-Machine Graphical Communication System (AFIPS 1963)](../works/sketchpad-a-man-machine-graphical-communication-system-afips-1963.md) — the constraint-satisfaction section, which introduces the general iterative relaxation procedure as the reliable-but-slow base and then the ordering pass as the exact method that supersedes it wherever an order exists, including the frank admission of a worked example for which no order can be found.
