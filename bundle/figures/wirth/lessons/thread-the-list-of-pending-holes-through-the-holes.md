---
type: lesson
title: "Thread the list of pending holes through the holes themselves"
figure: wirth
works: [project-oberon]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Thread the list of pending holes through the holes themselves

**Lesson:** A producer emitting a sequence in one pass will reach places where a value is required but not yet knowable, and must leave a gap to be filled once the value arrives. The reflex is to record the gap in a side structure — a list of positions awaiting each value — which means an auxiliary container, a capacity decision, and a failure mode when more gaps appear than were anticipated. But look at the gap itself: it is storage, already allocated, of exactly the width the eventual value needs, and it holds nothing until that value arrives. It can therefore hold the position of the previous gap awaiting the same value. Each gap links to its predecessor, the producer keeps only the head of the chain, and the auxiliary structure disappears entirely along with its capacity limit.

Filling is then a single walk: read the link out of a gap, write the value over it, follow the link to the next. The traversal is destructive and that is precisely correct, since each link is needed exactly once, at the moment its slot is overwritten. Three preconditions make this available and are worth checking rather than assuming: the gap must be at least as wide as a position reference, the gaps must be write-once so that consuming the link cannot lose information, and the producer must be able to hold one head per group of gaps that will receive the same value. That last one is what turns a construct with two possible outcomes into two chains carried side by side, one for each destination, which is a natural and cheap arrangement rather than a complication.

The reusable move is more general than the setting. Any time a design is about to allocate bookkeeping to track locations that are themselves currently unused, ask whether the unused locations can carry the bookkeeping. Space reserved for a future value is free scratch until that value exists, and using it costs nothing that the design was not already paying for. The same reasoning applies to slots awaiting a resolution, records awaiting a status, entries awaiting a link — the pattern is always the check that the storage is wide enough, written once, and dead until the moment it is filled.

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.7's treatment of Boolean expressions, which describes conjunctions and disjunctions yielding sets of conditional branches to be taken when the expression is false or true respectively, the locations of those branches being recorded in an F-list or T-list whose head is held in an attribute of the result item, and the links being embedded in the code in place of the branch addresses that will be inserted once the jump destinations are known; together with the worked example whose result item carries one element in each of the two lists simultaneously, and the note that in if, while and repeat statements the branch targets are known only after the whole statement has been processed.
