---
type: lesson
title: "The success criterion you optimize deforms the artifact you get"
figure: boehm
works: [software-engineering-1976, a-view-of-20th-and-21st-century-software-engineering]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# The success criterion you optimize deforms the artifact you get

**Lesson:** Boehm's cost breakdowns land on a proportion that still gets ignored: the large majority of what a long-lived system costs is spent after it first works. Construction is the short, loud, visible phase; modification is the long, quiet, expensive one, and the gap between the two is not a factor of two but a factor that can reach three digits per unit of change on badly structured systems. If that is where the money goes, then the structure of the system should be optimized for the activities that dominate that period, and Boehm decomposes them precisely: understanding what is already there, changing it without unintended consequences, and re-establishing confidence afterward. Each of those maps onto a structural property rather than a documentation practice. Understanding wants locality and honest naming; changing wants boundaries that confine the blast radius; re-establishing confidence wants the ability to retest selectively rather than entirely.

The sharper observation is about incentives. Optimizing for delivery date or for machine efficiency does not merely fail to help maintainability, it actively produces the opposite, because both push toward tight coupling, omitted structure, and representations chosen for the machine rather than the reader. Choosing a success criterion is therefore choosing a shape for the artifact, whether or not anyone intends it. Boehm makes the same point about measurement in general: emphasizing percent-coded reliably gets people coding early and skipping the activities that would have prevented rework. The measure does not merely observe the work, it deforms it.

None of this argues for ignoring speed. Later, Boehm is explicit that delivery time carries real economic value, since a system in service earlier starts returning earlier. The point is that the criterion has to span the whole life of the thing rather than the phase currently under management scrutiny, and that structural investments which look like pure overhead against a delivery date look entirely different against total ownership cost.

A programmer who believes this evaluates a design choice by asking who will have to understand this in two years and what they will need to change, treats the ability to change one thing without re-reasoning about ten as a first-class design goal, and is suspicious of any metric that rewards visible construction over the invisible work that prevents rework.

**Source:** [Software Engineering](../works/software-engineering-1976.md) — the maintenance section with its life-cycle cost breakdowns across several organizations, its decomposition of maintenance into understanding, modifying, and revalidating, and the management section's catalogue of inappropriate success criteria. [A View of 20th and 21st Century Software Engineering](../works/a-view-of-20th-and-21st-century-software-engineering.md) — the 1980s discussion of maintenance dominating organizational effort and of modularity work aimed at it, together with the later principle that delivery time carries genuine value when quality holds.
