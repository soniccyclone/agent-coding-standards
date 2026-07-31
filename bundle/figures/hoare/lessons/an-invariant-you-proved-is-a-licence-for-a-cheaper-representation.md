---
type: lesson
title: "Size the problem before choosing representations, and treat each proved invariant as a licence for a cheaper one"
figure: hoare
works: [notes-on-data-structuring]
axes: [hardware-affinity, verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Size the problem before choosing representations, and treat each proved invariant as a licence for a cheaper one

**Lesson:** Representation decisions are unanswerable in the abstract and nearly mechanical once two things are on the table: the expected magnitudes, and the operation mix. Write down the sizes first — how many of each kind of thing, how many typically and how many at worst — as explicit assumptions rather than as background knowledge. Then take each variable in turn, name which operations dominate its use, and pick the layout that makes those cheap. The answers stop being matters of preference. A collection that is repeatedly added to and removed from at one end wants a stack-shaped layout; one that is repeatedly intersected and differenced with others wants a bit-per-member layout; one whose occupancy hovers near half wants no sparse machinery at all. When a quantity is asked for often and is expensive to recompute, store it alongside and maintain it on every update.

Sizing also converts space arguments from anxiety into arithmetic. A conflict table costing the square of the number of items sounds alarming until the number is fixed and the product turns out to be a few thousand words, at which point the speed it buys settles the matter and the search for something cleverer is called off. That is the disposition worth copying: compute the number, compare it to what the machine has, and stop optimizing when the answer is clearly affordable. Half of representation folklore consists of avoiding costs that were never going to matter at the scale in play.

The subtler move is to notice when a property you already established permits a representation you would otherwise not be entitled to. If the pieces of a result are guaranteed disjoint, then instead of storing the pieces and their contents you can store, for each element, which piece it fell into — a far smaller and simpler structure, and one that is only correct because of the disjointness. Invariants are usually filed under correctness, but they are equally an inventory of what you are allowed to leave out; when a proved property lets a whole level of structure vanish, that is the invariant paying for itself twice. Look for it deliberately: after establishing each invariant, ask what it now makes redundant.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the data-representation section of the examination-timetable example, which fixes the expected magnitudes of examinations, students, hall capacity and session count before any representation is chosen, then selects each variable's representation from its dominant operations (stack-like insertion and removal for a session, bit-pattern sets for the repeatedly intersected and subtracted sets, redundant maintenance of the session count), accepts the large incompatibility table as justified by the speed it buys on the machines in question, and replaces the timetable-as-set-of-sets with a simple map from examination to session number, a representation made possible only by the already-established mutual exclusivity of the sessions.
