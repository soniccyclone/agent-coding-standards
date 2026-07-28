---
type: lesson
title: "Price a design method against the breadth of variation you will actually use"
figure: parnas
works: [on-the-design-and-development-of-program-families]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Price a design method against the breadth of variation you will actually use

**Lesson:** Advocates of a design discipline rarely name its cost, which is how disciplines turn into dogma. The honest form of the argument states both sides: refining a design in stages adds nothing to the effort of producing the first working variant and usually reduces it, because it keeps complexity manageable, so it is worth doing unconditionally. Writing external descriptions of independently developed parts is a different proposition — the effort of producing those descriptions can exceed the effort of just writing one complete working program. What that effort buys is a wider space of variants and the ability to complete separate parts with no communication between the groups doing them. Wider space and parallel completion are worth a great deal when you will actually exercise them and worth nothing when you will not. So the method is conditional on an estimate: how many genuinely different members of this family do you expect to build?

Notice what kind of claim this is. It is not that one technique is more rigorous or more modern, but that the two differ in where they sit on a cost curve, and that a competent designer is expected to locate the project on that curve before choosing. Getting the estimate wrong in either direction has a real price. Underestimate and you pay in a family too narrow to accommodate the variants that show up, each requiring rework of things that should have been swappable. Overestimate and you have paid more than the cost of the whole program for flexibility along axes nobody ever moves.

The same reasoning extends to when variability gets resolved. Variation can be discharged during design, at the moment a specific member is materialized for a target, or left live so a single program adapts at run time. Pushing everything to run time makes the materialization step unnecessary and makes the result comparatively inefficient; resolving variation earlier trades adaptability for capacity. This is a design decision in its own right, not a consequence of the design method, and the family framing makes it legible: a description of a family is what a materialization step consumes, so a good family description simplifies that step rather than replacing it. The pleasing special case is that a family often contains larger members where something varies and smaller ones where it is fixed, and the machinery written for the general member is exactly what produces the restricted one.

A programmer who thinks this way answers "should we build this with proper interfaces between independently developed parts" with a question about expected variants rather than an appeal to principle, and is willing to say out loud that a technique costs more than it returns on this particular project.

**Source:** [On the Design and Development of Program Families](../works/on-the-design-and-development-of-program-families.md) — the "Which Method to Use" section weighing the extra effort of writing module specifications against the breadth of family obtained, and the following section relating families to system generators and to variability resolved at generation versus run time.
