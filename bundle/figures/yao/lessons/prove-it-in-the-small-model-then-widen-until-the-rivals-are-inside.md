---
type: lesson
title: "Argue in the smallest model that makes the reasoning legible, then widen it until every rival design is inside"
figure: yao
works: [should-tables-be-sorted]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Argue in the smallest model that makes the reasoning legible, then widen it until every rival design is inside

**Lesson:** Two things are being optimized when you make a general claim about a class of designs, and they pull against each other. The argument wants the leanest possible model, because every extra capability in the model is another case to carry through the reasoning. The claim wants the fattest possible model, because a bound only rules out the designs the model can express, and a practitioner will always be able to point at a real technique that sits outside a lean one. Trying to satisfy both at once produces an argument nobody can follow about a model nobody trusts. Do them in sequence instead: state the stripped model where storage holds exactly the items and nothing else, prove the bound there where the induction is short enough to check by eye, and only then reopen the model and add capabilities one at a time.

The second pass is cheap in a way that is easy to miss. Widening a model usually means redoing the proof, but not if the widening only enlarges the finite space of behaviors the argument was already coloring. Allow the storage to hold bookkeeping symbols as well as items, allow items to be duplicated or omitted, allow more cells than items, allow the same collection to have several valid arrangements — each of these multiplies the number of distinguishable behaviors, and the counting argument absorbs a larger finite count without changing shape. Only the threshold at which the argument starts to bite gets worse. That is the signature of a well-chosen argument skeleton: the generalizations cost you a constant in the fine print rather than a new proof.

The discipline to import is the acceptance test for a model, which is not elegance but coverage of the named alternatives. Before believing your own negative result, list the techniques that would embarrass it — the hash table, the linked structure, the tree, the scheme that stores a pointer instead of a value — and check that each one is a legal inhabitant of the model as widened. If one is not, you have not proved what you think; you have proved something about a subclass, and the excluded technique is exactly where the next result comes from. That check is also how you locate the single assumption doing all the work, since after the widening only one restriction remains standing, and its removal is the interesting question.

**Source:** [Should Tables Be Sorted?](../works/should-tables-be-sorted.md) — the section that first sets out a basic model in which storage holds only the given items, proves the logarithmic bound there for clarity, then restates it as a generalized theorem admitting pointer symbols, duplicate and missing entries, and extra cells, noting that non-unique arrangements cannot help either and that the model therefore contains linked lists, search trees and the usual hashing techniques.
