---
type: lesson
title: "When both halves want to be the caller, neither should be"
figure: wirth
works: [algorithms-and-data-structures]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# When both halves want to be the caller, neither should be

**Lesson:** Two components developed separately will each have grown a control structure that assumes it owns the loop. One is a machine for deciding where output should go and asking, at several points in its own logic, for the next unit of output to be produced. The other is a machine for producing units of output and asking, at several points in its own logic, where the current one should go. Each is correct. Each is written so that the other appears in it as a subroutine. Composing them by making one subordinate means unwinding the loser's control structure into a state machine, and the cost of that is not proportional to the size of the interface — it is proportional to how many distinct places in the loser's body the call appears.

That last quantity is the diagnostic, and it is worth measuring before you start rewriting. If the required call occurs at exactly one point in one of the two bodies, that body can be turned inside out cheaply: the single call site becomes the entry point, everything before it becomes setup, everything after becomes the continuation, and you have a procedure the other component can drive. This is the ordinary case and it is why subroutine composition usually feels free. The expensive case is when both bodies call at several points. Then neither inversion is local, both require reconstructing by hand the position information that the language's own control flow was tracking for you, and the resulting code is opaque in exactly the way the original two components were not.

The response is to stop looking for a winner. What the situation is actually telling you is that you have two processes, not a caller and a callee, and the relationship between them is symmetric: each runs until it needs something from the other, hands control across, and later resumes where it left off. Whatever mechanism your setting offers for that — resumable procedures, threads, generators, an explicit continuation — the point is the same, and it is a design point rather than an implementation detail. Say it in the structure. The alternative, choosing a master arbitrarily and paying to flatten the servant, buys nothing and destroys the readability of the half you flattened; and the flattening is not a one-time cost, because every future change to the servant's logic must now be expressed in the invented state machine rather than in its own terms.

The general shape: asymmetry in a composition should be discovered, not imposed. Before you decide which of two things calls the other, check whether either can bear the subordinate role cheaply. When neither can, that is information about the problem — it means the two really are peers — and the design should say so rather than hiding it under a hierarchy that the code then has to fight.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 2.4.5, the attempt to combine the Polyphase sort's initial-distribution phase with heap-based run generation: the observation that there would be no problem if the required procedure were called at a single place in one of the two programs, but that it is called at several places in both, and the consequent recourse to a coroutine as the natural expression of two coexisting processes in a producer-consumer relationship.
