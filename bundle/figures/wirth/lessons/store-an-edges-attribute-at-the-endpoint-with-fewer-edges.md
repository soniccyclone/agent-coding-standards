---
type: lesson
title: "An attribute of a connection can live at either end; pick the end with fewer connections"
figure: wirth
works: [algorithms-and-data-structures]
axes: [primitive-count, hardware-affinity]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# An attribute of a connection can live at either end; pick the end with fewer connections

**Lesson:** When a property belongs to a connection rather than to the things it connects, there is no field to put it in — connections in most representations are not objects, they are references held by one thing and pointing at another. So the property has to be parked at one of the two endpoints, and both choices work. Held at the origin, an element needs one copy of the property for each connection leaving it. Held at the destination, an element needs one copy for each connection arriving at it. In a structure where each element is reached by exactly one connection but issues several, those two counts differ, and the difference is a direct multiple in the storage cost of the whole structure.

The choice is therefore mechanical once you ask the right question: what are the two multiplicities, and which is smaller? The answer is not a matter of taste, and it is not affected by which direction feels more natural to talk about, because the two representations carry identical information — every statement about a connection's property can be translated between them, and there is an exact correspondence between the two forms of the structure. Nothing is lost by choosing the cheaper one. What changes is which code has the property conveniently to hand: with the attribute at the destination, an element knows how it was reached but not how it reaches others, and any operation that needs the outgoing view must consult the elements at the other end. Check that no operation is made awkward before taking the saving.

The wider lesson is to be suspicious of the instinct that an attribute belongs where you first thought of it. Properties of relationships are the most common case of this, and they are also where the two representations most often get treated as different designs with different names, when they are one design with the bookkeeping relocated. Recognizing two structures as the same structure under a relocation of an attribute is worth doing explicitly: it collapses two bodies of literature into one, and it means results proved about either apply to both.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 4.7.2's closing comparison of the symmetric binary B-tree with its later rediscovery, where the difference is stated to be that every node of the former carries two flags indicating whether its two emanating pointers are horizontal while every node of the latter carries a single flag indicating whether its incoming pointer is horizontal, with the colouring convention that names the structure, the same resulting guarantee that no two horizontal links follow each other on a path and hence that every search path is at most twice the tree's height, and the noted existence of a canonical mapping between the two representations.
