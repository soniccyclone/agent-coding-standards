---
type: lesson
title: "A translator's case count is set by the destination's variety, not the source's"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, hardware-affinity, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A translator's case count is set by the destination's variety, not the source's

**Lesson:** A component that turns one form into another carries an internal description of each partial result — not what the result means, which comes from the source, but *where it currently sits*, which comes entirely from the destination. That second thing is what actually determines how complicated the translator is. Every distinct place the destination can hold a value becomes a case the translator must be able to name, must set up correctly, and must be able to combine with every other case when two partial results meet. So the case count grows with the destination's repertoire, and the combining logic grows roughly with its square. A source language of fixed size can be translated by a small program or a large one depending purely on how many distinct storage and addressing arrangements the target offers.

The consequence is the opposite of the intuition that a richer destination is easier to hit. A destination with more ways to say the same thing does reduce the number of steps in the output, but it does so by moving the choice into the translator, which must now decide among them and track which choice it made for every value in flight. Richness on the far side is not a gift; it is work relocated across the boundary, and it lands as permanent structural complexity in the translator rather than as a one-off cost. This is the accounting to do before congratulating a destination on its expressiveness — and before adding a new arrangement to a destination you control, since each one you add is a new case in every translator anyone will ever write for it.

Two practical consequences follow. First, when estimating the cost of retargeting, count the destination's distinct holding places, not the source constructs; the source is the part that stays the same. Second, keep the description of "where a partial result sits" as a separate, explicitly enumerated type rather than letting it hide inside the traversal code, so that the count is visible and the retarget is a matter of re-enumerating one list instead of hunting through a program for embedded assumptions.

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.3's account of the compiler's Item type, which represents the transitory constituents of expressions and statements, and its remark that all the non-basic modes effectively reflect the target computer's architecture, in particular its addressing modes, so that the more addressing modes a computer offers the more item modes are needed; together with the accompanying enumeration of the modes introduced for the NS-32000 target (indexed, indirect indexed, register direct, register indirect, register indexed, stack, condition code, absolute).
