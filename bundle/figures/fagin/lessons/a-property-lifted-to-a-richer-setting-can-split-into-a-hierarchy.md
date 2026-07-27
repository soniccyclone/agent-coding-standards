---
type: lesson
title: "A property lifted into a richer setting can split, and the split is the information"
figure: fagin
works: [degrees-of-acyclicity-for-hypergraphs-and-relational-database-schemes]
axes: [primitive-count, verifiability, cognitive-load]
subdomains: [databases-and-data-management, foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# A property lifted into a richer setting can split, and the split is the information

**Lesson:** In ordinary graphs, being acyclic is one thing. Every reasonable way of defining it agrees with every other. Move to a structure where a connection can bind more than two elements at once and the single notion fractures into four, ordered from most to least demanding, none of them equivalent, all of them collapsing back to the familiar notion when you restrict to the two-element case. That is the situation Fagin maps. The temptation when generalizing is to pick whichever variant your proof needs and declare it the generalization. He does the opposite and treats the fracture as the subject matter, because each level turns out to characterize a genuinely different bundle of desirable behaviors.

The levels are not arbitrary points on a scale. What separates the weakest from the next one up is heredity: the weakest can hold of a whole system while failing for a part of it, and the next level is exactly the condition that the weakest holds for every part. That is a general recipe. When a property you rely on is not inherited by substructures, you do not have to accept the awkwardness or abandon the property. You can define the hereditary closure of it as a level of its own, at which point every guarantee attached to the weak property automatically relativizes: if the weak version buys you some behavior for the whole, the hereditary version buys the same behavior for every part you might later carve out. Fagin also notes that the weak level's failure of heredity is mathematically unnatural, and that the new levels do not have that defect, so the hierarchy fixes a wart rather than merely adding shelves.

Two habits follow. The first is to resist naming a generalization "the" generalization. If the concept you are lifting was unambiguous in the simpler setting only because several inequivalent conditions happened to coincide there, the useful output is the lattice of variants and a map from each variant to what it guarantees, not a winner. The second is about how to use such a hierarchy once you have it. Fagin borrows Codd's stance on normal forms explicitly: do not demand that a design sit at a given level, and instead give the designer a flag warning which guarantees are unavailable below it. A graded criterion with known consequences at each grade is more useful than a pass-fail mandate, because designs that fail the strongest level are often perfectly reasonable and the designer needs to know precisely what they have given up.

He adds a refinement that matters in practice. Rather than chasing a level for an entire system, aim for it in the portion any particular consumer sees, since a well-behaved view can sit inside a badly behaved whole. That converts an all-or-nothing structural property into something you can achieve incrementally where it pays.

**Source:** [Degrees of Acyclicity for Hypergraphs and Relational Database Schemes](../works/degrees-of-acyclicity-for-hypergraphs-and-relational-database-schemes.md) — the introduction and the section comparing the degrees, which establishes the strict linear ordering among them, identifies the hereditary level as the one whose guarantees relativize to every subscheme, and draws the analogy to normal forms as warning flags rather than requirements.
