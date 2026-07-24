---
type: lesson
title: "Work backwards from what must be true at the end, and let the proof obligations write the code"
figure: dijkstra
works: [guarded-commands-nondeterminacy-and-formal-derivation-of-programs, the-humble-programmer]
axes: [verifiability, expressiveness]
subdomains: [formal-methods-and-verification]
tags: [lesson]
---
# Work backwards from what must be true at the end, and let the proof obligations write the code

**Lesson:** Proving a finished program correct doubles the programmer's burden; deriving the program from the shape of its proof removes most of the burden instead. The move is to treat the postcondition as the primary object and ask, for each candidate statement, under exactly what starting condition it is guaranteed to establish the goal. That computed condition then becomes the guard under which the statement may run, and the remaining gap (the initial states not yet covered) tells you precisely what alternative branches are still owed. Construction becomes goal-directed: the specification pulls the code into existence rather than the code being checked against the specification afterward.

For loops the method honestly separates calculation from invention. Choosing the relation that stays true across iterations and the quantity that shrinks toward termination is genuine creative work; everything after that choice is systematic. Knowing where the invention lives is itself valuable: it tells a programmer what to think hard about (the invariant) and what to grind through mechanically (the guards and the bookkeeping), instead of treating the whole construction as undifferentiated cleverness.

This also settles how language semantics should be defined if you intend to build programs this way: a construct's meaning is most useful when stated as a rule transforming desired outcomes into required starting conditions, because that is the direction design actually proceeds. Semantics chosen for the convenience of an interpreter face the wrong way. And the discipline is a stance, not an algorithm: the claim is not that all programs should be manufactured by calculation, but that a programmer should always know what would have to be proven, and should prefer constructions whose proof obligations are visible while there is still time to pick different constructions.

**Source:** [Guarded Commands, Nondeterminacy and Formal Derivation of Programs](../works/guarded-commands-nondeterminacy-and-formal-derivation-of-programs.md) — the semantics-by-weakest-precondition machinery and the worked derivations of the maximum and greatest-common-divisor programs, where guards are computed rather than guessed. Also [The Humble Programmer](../works/the-humble-programmer.md) — the feasibility arguments include the case that correctness concerns, applied before and during construction, act as effective heuristic guidance rather than after-the-fact burden.
