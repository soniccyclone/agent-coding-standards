---
type: lesson
title: "Hierarchy is an artifact of thought, not a property of the world"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Hierarchy is an artifact of thought, not a property of the world

Trees are the decomposition everyone reaches for, and Reenskaug punctures the assumption with a brick. A house is a roof and four walls; the walls are made of bricks; the scheme is clean until you reach a corner, where one brick belongs to two walls at once. The containment story does not fail at the periphery of some exotic case, it fails at the corners, which is to say at every structural junction. Genuine hierarchies are rare in the world; what is common is a world with several overlapping organizations laid across the same material, and a mind that finds trees easy to hold.

This matters because encapsulation makes tree-shaped decomposition almost free, and the ease is seductive. A component can absorb arbitrary internal complexity and present a narrow face, so nesting components inside components feels like it scales indefinitely. What it cannot express is the corner brick — a part that genuinely belongs to two arrangements simultaneously, where forcing a choice of owner misrepresents the thing. The usual outcome is that one arrangement is written down as the structure and the others survive as folklore, cross-references, or duplicated state.

Reenskaug's illustration of the alternative is that primacy itself is relative to viewpoint: in a scheduling problem, resources look subordinate to the jobs that need them, and from the standpoint of the plant that owns the resources, jobs look subordinate to resources. Neither view is the container of the other. Enterprises are full of such overlaid structures — reporting lines, project teams, professional communities, temporary arrangements — and when they are genuinely independent nothing is needed, while when they interact the interaction is the thing worth modeling. So the useful move is to describe each arrangement separately and then describe the dependencies between them explicitly, instead of collapsing them into one tree and losing the ones that lost.

A programmer holding this treats a single containment tree as one view among several rather than the structure of the system, expects the important defects to sit where two arrangements meet, and reaches for a mechanism that lets one component participate in several arrangements before reaching for a deeper nesting.

**Source:** [Working with Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — the observation on hierarchical thinking among the general remarks about models, and the argument in the technology overview that role model synthesis exists because hierarchical decomposition cannot express the overlapping structures found in real organizations.
