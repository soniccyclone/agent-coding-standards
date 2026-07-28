---
type: lesson
title: "No ordering of decisions can be backed out of cleanly, so buy independence rather than a better order"
figure: parnas
works: [on-the-design-and-development-of-program-families]
axes: [cognitive-load, expressiveness, parallelizability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# No ordering of decisions can be backed out of cleanly, so buy independence rather than a better order

**Lesson:** Refining a design in stages, each stage committing to a little more, appears to solve the revision problem: to change your mind, return to the stage above the decision and descend differently. It does solve it in the lucky case, and the lucky case is what tutorial examples show. The general case fails, and it fails for a reason worth stating precisely. Returning to a stage is only useful if that stage happens to contain every decision you want to keep and none you want to discard. Since decisions were laid out in a line, the ones you keep and the ones you drop are interleaved along it, and there is no guarantee that any single point separates them. Foresight does not rescue you: even knowing exactly which decisions you would later revise, there may be no ordering at all that lets you back up without throwing away work you wanted, because the code implementing a decision you are keeping was written to fit against code you are now changing. Perfectly good design work gets recoded as collateral damage.

The escape is not a cleverer ordering. It is to stop making a total order the only structure available. Split the system into parts developed in ignorance of each other's insides — not the subprograms a main routine calls, but groupings of routines, each holding one decision — and revising that decision no longer requires reasoning about the sequence in which anything was decided. You gain the ability to reverse a representation choice without so much as looking at the code that implements an unrelated policy choice, because the two were never in a linear relationship to begin with. That is a categorically different property from having refined in a good order, and it is the reason the two techniques are complementary rather than competing: one controls complexity along a line, the other removes the line where a line was doing harm.

A related asymmetry falls out of the same observation. When every intermediate artifact is itself a program, the design pressure is toward settling sequencing early, because a program has to say what happens when. Decisions about order of events are then shared by the whole family and cannot distinguish its members. Describing parts by their externally visible behavior instead leaves sequencing unstated, at the price that sequencing becomes awkward to express at all — in practice you write a small ordering skeleton, and the telling detail is that it is written last, as one of many ways the parts could have been driven. Whichever technique dominates a project, ask which decisions its representation quietly forces to the front, and check that those are decisions you were happy to make early.

The practical habit: when someone proposes that better up-front sequencing would have avoided a painful rework, treat that as probably false. The fix for entanglement is independence between parts, and independence has to be designed in, not scheduled in.

**Source:** [On the Design and Development of Program Families](../works/on-the-design-and-development-of-program-families.md) — the passage following the free-space allocation example that identifies the fundamental problem with backtracking through refinement stages, the introduction of information-hiding modules as the way around it, and the "Which Method to Use" discussion of how each representation biases sequencing decisions.
