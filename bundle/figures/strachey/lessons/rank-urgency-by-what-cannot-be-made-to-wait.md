---
type: lesson
title: "Rank urgency by what cannot be made to wait"
figure: strachey
works: [time-sharing-in-large-fast-computers]
axes: [parallelizability, hardware-affinity, verifiability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Rank urgency by what cannot be made to wait

When several activities compete for one processor, the tempting basis for ordering them is importance: the valuable computation first, the incidental chores after. Strachey orders them by a different and far more useful property — whether the activity is attached to something that will keep moving whether or not you attend to it. A mechanism in motion has already committed; if its data is not taken within a fixed interval it is simply lost, and no amount of later attention recovers it. A computation has no such commitment. It can be suspended for an unbounded time and resume with nothing missing. The ranking follows directly: whatever has momentum outranks whatever does not, and the largest, most valuable calculation sits at the bottom because it is the one thing that can always be resumed.

This turns priority from a judgement call into a derivable fact about the system's coupling to the physical world, which is what makes the design analysable at all. Once each class of work has both a deadline imposed from outside and a known cost to service, you can compute how many such devices the machine can carry simultaneously and what fraction of its time remains. Strachey's worked arithmetic makes a subtler point visible: the same total amount of work is feasible or infeasible depending purely on how the steps are assigned to classes. Splitting one handler into an urgent part that must run within the interval and a deferrable part that may itself be interrupted transforms a design that supports two devices into one that supports many. Nothing got faster; the deadline structure got honest.

A programmer who has absorbed this stops asking "which of these matters more" and starts asking "which of these has a clock running that I did not start." Interrupt priorities, queue disciplines, and the placement of work between a fast path and a background sweep all fall out of that question. It also produces a healthy suspicion of any scheduling scheme whose ordering cannot be justified by an external constraint, since such an ordering can neither be verified nor used to bound anything.

**Source:** [Time Sharing in Large Fast Computers](../works/time-sharing-in-large-fast-computers.md) — Developed where the paper introduces priority classes for interrupt handling, states the classification principle in terms of processes possessing inertia, and then works through timings for tape transfer at character and word granularity.
