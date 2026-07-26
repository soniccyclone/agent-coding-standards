---
type: lesson
title: "Separate the concurrency in your description from the concurrency in your execution, and make the scheduler an inspectable data structure"
figure: dahl
works: [simula-an-algol-based-simulation-language, simula-67-common-base-language]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
tags: [lesson]
---
# Separate the concurrency in your description from the concurrency in your execution, and make the scheduler an inspectable data structure

**Lesson:** A system can be described as many entities acting at once while being executed as exactly one entity acting at a time. Simula takes that decoupling as a design axiom: components are conceptually parallel, but precisely one of them holds control, and transfers happen only at points the program names. The interleaving is therefore a property of the description, chosen by the author, rather than an artifact of a scheduler or a machine. Two consequences follow immediately. Every switch point is visible in the text, so the invariants an entity must restore before yielding are identifiable by reading rather than by imagining adversarial timings. And a run is reproducible, so a bug found once can be found again.

The second half of the idea is that the ordering policy itself should be ordinary data. Rather than compiling scheduling into the runtime as a fixed rule, the design keeps a list of pending activations, each carrying an explicit time value, kept in non-decreasing order, with named ways to place a new activation before or after a given one or ahead of others sharing its time. Simulated time is a number in that structure, unrelated to any clock, readable and comparable by the program. Because the ordering discipline is a data structure with published operations rather than hidden machinery, both the policy and its consequences are open to inspection, and the surrounding vocabulary of states an entity can be in (running, scheduled, idle-with-a-resumption-point, finished) is definable in terms of which parts of that structure refer to it.

This is where the verifiability payoff sits. Concurrency defeats reasoning mainly through two properties: unbounded interleaving and unobservable scheduling. Fixing switch points removes the first. Making the pending-work order into program-visible data removes the second. What remains is a system whose behavior over time is a function of an explicit structure you can print. True parallel hardware eventually reintroduces both problems, but the lesson is that the difficulty is not intrinsic to describing a world of simultaneous agents. It is the price of a particular execution strategy, and worth paying only where the throughput is actually needed.

A programmer who takes this seriously distinguishes "I need concurrency to model this" from "I need parallelism to run this fast enough," and refuses to pay the second's cost for the first's benefit. Concretely: prefer a cooperative structure with explicit yields for logic that is merely interleaved; if a scheduler exists, make its queue a first-class value that tests can construct, assert on, and step deterministically; and keep the model's notion of time as data so that a simulated hour costs no wall-clock time and an experiment can be replayed exactly.

**Source:** [SIMULA - an ALGOL-Based Simulation Language](../works/simula-an-algol-based-simulation-language.md) — the sections defining quasi-parallel operation, the ordered set of pending event notices with its time references and placement rules, and the enumeration of the states a process can occupy. Also [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md), whose sequencing chapter generalizes this into components of a quasi-parallel system, with control transfer only through the named detach and resume operations.
