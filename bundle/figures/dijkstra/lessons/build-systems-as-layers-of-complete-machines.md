---
type: lesson
title: "Structure a system as a stack of complete machines, each one abstracting a physical resource out of existence"
figure: dijkstra
works: [the-structure-of-the-the-multiprogramming-system, notes-on-structured-programming]
axes: [cognitive-load, verifiability, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Structure a system as a stack of complete machines, each one abstracting a physical resource out of existence

**Lesson:** The powerful form of layering is not grouping related code but constructing, at each level, a complete machine on which everything above runs. Each layer's job is to make one awkward physical reality disappear for good: once the lowest layer multiplexes the processor, the count of real processors is not merely hidden but unmentionable above it; once the next layer maps information units onto storage units, physical addresses cease to exist as a concept; and so on up through devices and consoles. The test of a layer is whether the levels above could be written by someone who has never heard of the resource it manages. A layer that leaks its resource upward, even through naming, has not done its job.

The reason to build this way is combinatorial. Uncoordinated interrupt sources and shared resources multiply into a state space no one can enumerate; each abstraction layer quotients that space, so the states relevant to any one level become few enough to reason about and even to test exhaustively before the next level is added. Verification can then proceed bottom-up in the same order as construction, and each level's argument stays valid regardless of what is built above it. The same holding-power appears in a subtler benefit: a stopped layer boundary is a clean state, with everything below passive and everything above mid-instruction, which gives a principled answer to when interpretations of system state are valid at all.

Two corollaries follow for anyone designing this way. First, the ordering of layers is forced by dependency logic, not convenience: whatever a layer's own implementation must use has to already exist below it. Second, the discipline scales the opposite way from intuition: the bigger the system, the more essential the layering, because the state-space explosion it tames grows with size. Deep conceptual hierarchies are not an indulgence of tidy minds; they are the only known instrument for spanning the enormous ratio between a machine's grain of action and a system's span of behavior.

**Source:** [The Structure of the 'THE'-Multiprogramming System](../works/the-structure-of-the-the-multiprogramming-system.md) — the level-by-level survey where processors, then pages, then the console, then peripherals each lose their identity, and the design-experience section explaining how this kept exhaustive testing feasible. Also [Notes on Structured Programming](../works/notes-on-structured-programming.md) — the program-model section, which recasts the same idea for single programs: each level a program for a virtual machine, implemented by the level below.
