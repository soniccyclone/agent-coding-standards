---
type: lesson
title: "A constraint that growing can never repair is worth more than one that merely rejects: it prunes, and it shrinks the alternatives too"
figure: hoare
works: [notes-on-data-structuring]
axes: [cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# A constraint that growing can never repair is worth more than one that merely rejects: it prunes, and it shrinks the alternatives too

**Lesson:** When a solution is assembled by adding elements one at a time, the constraints on it are not all equal in value. Sort them by one question: if a partial solution violates this, can any extension of it satisfy it again? For a constraint where the answer is no — a limit on how many elements, a limit on total weight, a forbidden pair — the first violation condemns not just the current candidate but every candidate containing it, and the whole region can be dropped without being visited. For a constraint that can be repaired by adding more, no such inference is available and you have to keep going and check at the end. The first kind is where all the leverage lives, and a search organized to test those constraints as early as possible does a fundamentally smaller amount of work than the same search that merely rejects finished candidates.

The stronger move is to convert a constraint into a reduction of the alternatives rather than a test on the candidate. Having committed to an element, immediately remove from the pool of things still available every element that is now excluded by it. The constraint is then discharged permanently: nothing that could violate it remains reachable, so no later step needs to test for it, and the pool shrinks with each commitment, which compounds. This is what makes the difference between a search that checks and a search that cannot go wrong — and it is also what makes the correctness argument short, since the property you want holds by construction over the whole exploration rather than being re-established at every node.

The design consequences are worth naming. Symmetry is the other big win available cheaply: fixing one element up front, on the grounds that it must appear in some part of the final answer and might as well appear in this one, removes an entire dimension of redundant re-exploration that would otherwise regenerate the same candidates on every outer round. And the whole scheme depends on the exploration restoring what it changed — anything removed from the pool on the way down goes back on the way up — because the pruning is only sound if the state each branch sees is exactly the state its own reasoning assumed.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the examination-timetable example's session-generation procedure, which observes that a trial failing one of the session conditions cannot be fixed by enlarging it and therefore generates supersets only of trials already found acceptable, removes from the untried pool every examination incompatible with one just added so that condition need never be tested again, fixes an initial examination to stop the same supersets being regenerated on every outer cycle, and saves and restores the pool and trial around each recursive call.
