---
type: lesson
title: "Put the power to change a guard out of reach of what it guards"
figure: strachey
works: [time-sharing-in-large-fast-computers]
axes: [verifiability, primitive-count, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Put the power to change a guard out of reach of what it guards

**Lesson:** Any protection mechanism worth having runs into the same bind: the limits it enforces must be adjustable, or the system becomes rigid and useless, yet if they are adjustable by ordinary means then the very code being restrained can adjust them. Adding a check inside the mechanism does not close the gap, because a program that has gone wrong is not executing an argument you can reason with — it is executing an arbitrary sequence of operations, including whichever one lifts the restriction. The mechanism must be assumed to be attacked by nonsense, not by intent, and nonsense will eventually try everything.

The way out is not a cleverer test but a change in what confers authority. Make the ability to adjust the limits depend on *where the instruction is executing from* rather than on what it says or on any flag it can set. If the operations that reset the bounds only function when issued from a region no ordinary program can write into or jump into, then the question "may this code lift the restriction?" is answered by the code's location, which the code cannot forge. Notice the economy of it: one asymmetry in the substrate replaces an unbounded set of runtime checks, and the guarantee holds without anyone having to prove that the constrained programs are well behaved — which is exactly the thing you cannot prove about the programs you most need to constrain.

This is the reasoning pattern behind privileged execution modes, capability boundaries, immutable audit stores, and any design where a trusted core and untrusted tenants share a substrate. The generalisation for a programmer is that trust boundaries should rest on structural facts an adversary or a bug cannot alter, never on discipline, convention, or a check written in the same medium as the thing being checked. When you find yourself protecting a setting by asking callers not to touch it, you have not built a boundary — you have written down a wish. Ask instead what property of position, medium, or capability makes the wrong call simply impossible to express.

**Source:** [Time Sharing in Large Fast Computers](../works/time-sharing-in-large-fast-computers.md) — the discussion of store interlocks and their alteration, resolved by confining the limit-setting operations to instructions issuable only from the non-erasable region where the supervisory program lives.
