---
type: lesson
title: "Confidence in a program can only come from its structure, never from sampling its behavior"
figure: dijkstra
works: [notes-on-structured-programming, the-structure-of-the-the-multiprogramming-system, on-the-cruelty-of-really-teaching-computer-science]
axes: [verifiability]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Confidence in a program can only come from its structure, never from sampling its behavior

**Lesson:** The input space of even a small component is so large that a lifetime of testing exercises practically none of it, yet we demand the component work on whichever inputs actually arrive, precisely because we abstracted away from specific values when we reasoned about the surrounding program. Treated as a black box, then, no mechanism can be convincingly validated. The only escape is to stop treating it as a black box: build the thing so that its internal structure carries the argument for its correctness, and let whatever testing remains be aimed by that structure rather than groping blindly. This inverts the usual relationship between construction and quality control. Which test cases are relevant is not decidable from the specification; it follows from how the mechanism is built, so making the relevant cases few and enumerable is a design obligation, not a QA problem.

Discrete systems make the black-box position even weaker than it looks. Analog intuition says nearby inputs behave alike, so probing the extremes brackets everything in between. In a digital artifact there is no metric under which small causes have small effects; a single flipped bit can produce arbitrary divergence, so interpolating between passing tests is logically groundless. Test results are evidence about exactly the runs performed and nothing more: they can reveal errors but can never certify their absence.

A programmer who accepts this designs differently from the start: state spaces kept small and legal states characterized explicitly, components arranged so each can be argued about in isolation, and the correctness argument grown alongside the code instead of reconstructed afterward. The payoff observed in practice is that once structure carries the proof, remaining defects are shallow transcription slips, cheap to find and fix; fear of the untestable interleaving or the unvisited input disappears because the argument never depended on visiting it.

**Source:** [Notes on Structured Programming](../works/notes-on-structured-programming.md) — the reliability-of-mechanisms section, with its combinatorial argument against exhaustive testing and the conclusion that demonstrable correctness constrains structure. Also [The Structure of the 'THE'-Multiprogramming System](../works/the-structure-of-the-the-multiprogramming-system.md) — the conclusions argue that relevant test cases can only be identified from internal structure, and the project's level-by-level verification shows the idea surviving contact with a real system. Also [On the Cruelty of Really Teaching Computer Science](../works/on-the-cruelty-of-really-teaching-computer-science.md) — the discussion of the computer as a large-scale digital device supplies the no-continuity argument for why sampling can never generalize.
