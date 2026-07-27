---
type: lesson
title: "Bound the size of the answer and you have bounded every algorithm at once"
figure: hartmanis
works: [computational-complexity-of-random-access-stored-program-machines]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Bound the size of the answer and you have bounded every algorithm at once

**Lesson:** Self-reference is the famous way to prove that something cannot be done quickly, and it is also the crudest. A diagonal construction builds an object that defeats an enumeration of candidates, which establishes that a resource ceiling is real but leaves the ceiling's exact height blurred by whatever slack the simulation of candidates cost you. There is a humbler technique that yields far sharper statements: look at the instruction set, find the maximum rate at which any single step can enlarge the thing being produced, and divide. If the required answer is astronomically large relative to the input, and no operation can more than double the working value, then the step count has a floor that follows from arithmetic rather than from any argument about strategy. No cleverness escapes it, because the bound is about production capacity, not about method.

This reframes lower-bound reasoning as budget accounting on the primitives. The question stops being "is there a smarter algorithm" — an open-ended search with no natural end — and becomes "what is the most this instruction set can accomplish per step, and how much has to be accomplished," which is finite and checkable. Bounds obtained this way are tight enough to rule out even fractional improvements, which diagonal arguments generally cannot do. They also compose: change the instruction set to include an operation with a higher growth rate and the same accounting immediately tells you how much faster the richer machine can be.

The stance a programmer takes from this is to look at the output before looking at the code. How much information must this computation emit, and what is the most any single primitive operation can emit or construct? That ratio is a floor under every implementation, in every language, forever. It is the reason certain jobs cannot be made fast by better engineering, and knowing it early is the difference between renegotiating the requirement and burning a quarter on optimization. The inverse discipline is just as valuable: if the required output is small, a large measured cost is somebody's inefficiency rather than the problem's nature, and it is worth hunting.

There is a methodological point underneath as well. Reaching for the most powerful available proof technique is a habit worth resisting; the strongest tool in the box tends to give the weakest quantitative answer, because generality is bought by throwing away the structure of the specific case. Counting what the machine can physically produce uses that structure instead of discarding it.

**Source:** [Computational Complexity of Random Access Stored Program Machines](../works/computational-complexity-of-random-access-stored-program-machines.md) — the section built on arguments about the magnitude of the computed function, presented there as an alternative to diagonalization, including the observation that repeated accumulator-doubling is the fastest available growth and therefore fixes a minimum operation count.
