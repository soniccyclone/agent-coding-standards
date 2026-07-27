---
type: lesson
title: "To find out whether an assumption is load-bearing, build the world where it fails"
figure: hilbert
works: [grundlagen-der-geometrie]
axes: [verifiability, primitive-count]
subdomains: [formal-methods-and-verification, foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# To find out whether an assumption is load-bearing, build the world where it fails

**Lesson:** Arguing about whether a rule is necessary is unproductive; constructing a functioning system that obeys every rule except that one settles it. This is the entire method of the second chapter of Hilbert's geometry. To show his axioms cannot contradict each other, he does not reason about them directly — he builds a small arithmetic world out of a countable set of numbers, interprets points and lines as tuples and ratios in it, and shows every axiom comes out true there, so any contradiction derivable from the axioms would have to show up as a contradiction in that arithmetic. Then, one axiom at a time, he does the reverse: a bounded-disc interpretation where uniqueness of parallels fails, a redefined notion of segment length where a congruence rule fails, a system built over rational functions of a parameter where repeated addition never overtakes a distinguished element and so the Archimedean rule fails. Each of these is a working geometry. Each proves its missing axiom was independent.

What makes the technique available is a decision made at the very start: the primitives are introduced as three collections of unspecified things, and the axioms are declared to be the complete account of how they relate. Nothing anywhere in the development may appeal to what a point or a line really is. That refusal is not asceticism — it is precisely what lets the same axiom text be reinterpreted over discs, over functions of a parameter, over broken lines that detour along circular arcs. If the primitives had been tied to their intended meaning, no alternative interpretation would have been admissible, and the independence questions could not even have been posed.

The programming translation is direct and underused. Whenever a system carries a rule someone insists is essential — an ordering guarantee, a uniqueness constraint, a rule that some operation is total — the way to learn its real role is to construct the variant where it does not hold and see exactly which results collapse. Sometimes nothing does, and you have found a rule to delete. Sometimes a specific consequence dies, and you have learned what the rule was actually buying. The prerequisite is the same as Hilbert's: your components must be specified by the properties they promise rather than by their current implementation, because only then is a second implementation with one property deliberately broken a legitimate object to reason about rather than a mere bug.

**Source:** [Grundlagen der Geometrie](../works/grundlagen-der-geometrie.md) — the opening section's treatment of points, lines, and planes as unspecified systems of things, and the whole of the second chapter, where consistency is shown by interpretation into an arithmetic domain and each independence claim is settled by constructing a geometry that violates exactly one axiom.
