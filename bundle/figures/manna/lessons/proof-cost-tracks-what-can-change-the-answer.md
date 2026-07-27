---
type: lesson
title: "Proof cost tracks how many things can change the answer, not how big the program is"
figure: manna
works: [a-temporal-proof-methodology-for-reactive-systems]
axes: [cognitive-load, verifiability, parallelizability]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# Proof cost tracks how many things can change the answer, not how big the program is

**Lesson:** On paper, proving a property holds throughout every execution of a concurrent program is quadratic misery: one check per candidate assertion per possible step, and a program with two processes of ten statements each has plenty of steps. In practice Manna and Pnueli discharge nearly all of it with two observations they state as working heuristics before touching a single verification condition. Any step that writes none of the state the assertion reads preserves the assertion for free. And among the steps that do write it, only those that could turn it from true to false need examining at all, since a step that can only turn it true carries no obligation. What was a check against every step becomes a check against a handful, identified by inspection.

This is worth stating as a principle about cost rather than as a proof trick, because it tells you what makes a property cheap or expensive to maintain, and that is a design fact. The price of a claim is proportional to the number of places that write the state the claim mentions. A claim about state written from one place is nearly free forever. The same claim about state written from twenty places costs twenty separate arguments, and costs them again on every change, and there is no clever proof technique that recovers the difference — the cost is inherent in the write set. Their small examples make this visible: the assertions relating a process's flag to its own position in its own code are dispatched in a line each, while the assertion coupling both processes' positions to a shared turn variable is the one that takes real work and eventually needs helper claims.

The same paper applies the identical principle in a different register, which is what convinces me it is the general idea rather than a local convenience. In their liveness arguments, the case analysis is refined in fine detail around whichever process is currently responsible for making progress, and the other process's positions are lumped into coarse groups. When responsibility switches — when the party you are waiting on changes — the refinement switches with it: the newly-responsible process gets pulled apart into cases and the previously-responsible one gets collapsed. Detail is allocated to whatever can change the outcome, and everything else is deliberately blurred. The authors call this out as a conscious effort to keep the number of cases down.

A programmer who internalizes this counts writers before adding an invariant, and treats a large write set as a signal to relocate state rather than as a reasoning problem to be brute-forced. It is the same instinct that makes encapsulation valuable, arrived at from the cost side rather than the aesthetic side: put the state where few things can touch it, because the number of things that can touch it is the number of arguments you will owe forever. And when reasoning about waiting, name the party you are waiting on and spend attention only on them, because everything else in the system is, for that argument, noise you are allowed to ignore.

**Source:** [A Temporal Proof Methodology for Reactive Systems](../works/a-temporal-proof-methodology-for-reactive-systems.md) — the two heuristics stated in the invariance sections for discarding transitions from consideration (irrelevance of the write set, and restriction to potentially-falsifying steps), and the closing remarks on the accessibility diagram explaining why case analysis is refined around the helpful process while the other process's locations are grouped.
