---
type: lesson
title: "Hierarchy is right for organizing control and wrong for organizing authority"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Hierarchy is right for organizing control and wrong for organizing authority

**Lesson:** Nesting is the natural shape for the flow of control: something has to be at the top, calls return to their callers, and a stack discipline gives a clean account of where a computation is. It does not follow that authority should be organized the same way. A ranked scheme of access — where each level can reach everything its inferiors can reach, plus more — imposes a total ordering on privilege that real requirements almost never have. Anyone who has tried to build a system of keys for a building, with masters and submasters, has met the discovery: the sets of rooms different people need do not nest, so a ranked scheme forces you either to grant too much or to deny what is needed.

The important move is to notice that these are two separate structures over the same components, and to let them have different shapes. A program can use strictly nested entry and exit for its flow of control while the sets of things reachable at each point form an arbitrary graph with no ordering at all. Once separated, the requirement that motivated the ranking — that there be some pinnacle of authority for scheduling and dispatch — is satisfied entirely within the control structure, leaving the access structure free to be exactly as irregular as the problem is. Two lines of work converged on this independently, one from the systems side and one from the language side under the name of abstract data types, which is a strong sign the constraint being removed was artificial rather than essential.

The practical test for whether you have conflated the two is to ask whether a component can be given more control responsibility without automatically gaining more reach, and whether it can be given more reach without moving up the call structure. If either answer is no, the two structures are welded together and one of them is being distorted. The distortion normally shows up as components placed at a level they do not belong at, because that was the only way to give them what they needed.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 1's argument that a hierarchical organisation is appropriate for the flow of control since there must be some pinnacle of authority but is unnecessarily restrictive for protection, the master-key analogy, the note that the non-hierarchical character of capabilities is their most distinctive feature, and the later observation that nested entry and return give hierarchical control while leaving the protection structure non-hierarchical.
