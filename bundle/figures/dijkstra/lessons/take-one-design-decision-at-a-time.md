---
type: lesson
title: "Compose programs one decision at a time, and treat every program as a member of a family"
figure: dijkstra
works: [notes-on-structured-programming]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Compose programs one decision at a time, and treat every program as a member of a family

**Lesson:** Since a programmer cannot decide everything at once, the craft is in sequencing the decisions: at each refinement step commit to as little as possible, prefer the decision that takes the least investigation to justify, and keep everything already written valid whichever way the open questions later resolve. Data representations deserve the same deferral as algorithms; large parts of a correct program can be written against an object whose representation is still undecided, and the moment of committing to a representation should be chosen, not stumbled into. Ordering matters materially: settling a representation too early forces every subsequent piece to be phrased in low-level terms that a better ordering would have let stay abstract, and the resulting program is measurably more entangled. Elegance here is quantitative, not aesthetic.

The deeper reframe is that a program should never be conceived as an isolated artifact. Each intermediate refinement stage is a common ancestor of every program reachable by resolving its open decisions differently, so the half-finished design is already a family, and the finished product is one member picked from it. This turns modification from text surgery into re-derivation: to change a program, return to the ancestor above the decision being revised and descend again, reusing the correctness argument and the code of everything outside that decision's range of validity. A decision to be changed and a decision not yet taken are the same object seen at different times.

A programmer who works this way also anticipates differently. Instead of bolting generality on, they ask which aspects of the problem statement are likely to move, and arrange the decision sequence so those aspects are decided late and in one place. The structure of the program then documents its own change-capacity: what can be swapped smoothly is exactly what sits below a late decision point.

**Source:** [Notes on Structured Programming](../works/notes-on-structured-programming.md) — the prime-table walkthrough (composition in minute steps, deciding as little as possible each time), the program-families section, and the pearls-and-necklace discussion including the experiment showing how reordering the same decisions yields a messier program.
