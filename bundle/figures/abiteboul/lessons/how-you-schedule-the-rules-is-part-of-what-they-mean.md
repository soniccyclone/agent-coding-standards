---
type: lesson
title: "How you schedule the steps is part of what the program means"
figure: abiteboul
works: [datalog-extensions-for-database-queries-and-updates]
axes: [parallelizability, verifiability]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency, databases-and-data-management]
tags: [lesson]
---
# How you schedule the steps is part of what the program means

**Lesson:** Scheduling is usually filed under implementation. You write the rules, and whether the runtime applies them one at a time or all at once is treated as an efficiency question that the language definition need not settle. This work shows that for a rule system with any negative condition, the choice is not an efficiency question at all. Take a pair of rules where each fires on the absence of the other's conclusion. Apply one instance at a time and you reach one of many possible stable states, each of them internally consistent, with the particular one you land in decided by the order of choices. Apply every applicable instance simultaneously and you reach a single stable state, reproducibly, and it is a state the one-at-a-time strategy can never produce. Same rules, different results, and the difference is not a bug in either strategy.

Two consequences follow, and they pull in opposite directions. Simultaneous application gives determinism, and determinism turns out to give control: because every applicable instance fires at once, you can rely on stage boundaries and use them to sequence phases of a computation. One-at-a-time application gives nondeterminism, which weakens your ability to control anything and forces you to add machinery for detecting and undoing choices that turned out wrong, but it can express outcomes the deterministic strategy cannot reach, such as breaking a symmetry by keeping an arbitrary one of two symmetric items. Neither strategy dominates. Rules meant to advance a whole population through generations want the simultaneous reading. Rules meant to resolve conflicts by picking a winner want the one-at-a-time reading.

For a programmer this reframes a large family of everyday decisions. Batch versus incremental, snapshot versus read-your-writes, whether a reducer sees a whole generation of events or one event at a time: each of these is a semantic commitment, and pairs of rules that read each other's absence are exactly where it becomes observable. The practical rule is to write the scheduling discipline into the specification rather than leaving it to the runtime, and, before deciding, to look for the negative dependencies in your logic, since those are the places where the two disciplines will disagree. Code that is silent about which discipline it assumes is code whose results depend on a decision nobody made on purpose.

**Source:** [Datalog Extensions for Database Queries and Updates](../works/datalog-extensions-for-database-queries-and-updates.md) — the informal walkthrough in the introduction, which traces the determinism split back to the single choice between firing one applicable rule instance and firing all of them, works a two-rule example whose stable states differ under the two readings, and then argues in the concluding survey that the simultaneous reading is the one that supplies control capability.
