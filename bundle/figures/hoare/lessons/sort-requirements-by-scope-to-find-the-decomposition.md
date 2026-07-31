---
type: lesson
title: "Sort the requirements by what each one mentions, and the decomposition falls out"
figure: hoare
works: [notes-on-data-structuring]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Sort the requirements by what each one mentions, and the decomposition falls out

**Lesson:** Once the conditions a correct answer must satisfy are written down, sort them by scope: which ones talk about the whole result, and which ones talk only about one part of it and never mention the whole. That sorting is a decomposition proposal, and usually a better one than any arrived at by thinking about components directly. The conditions confined to a part become the entire specification of a routine that produces one part; the conditions about the whole become the specification of the loop that assembles parts into a result. Each half can then be worked on without the other in view, which is the property you were looking for when you started drawing boxes.

The reason this is more than a tidy heuristic is that it partitions the proof obligation along with the code. A part-producing routine that establishes its own conditions can be checked in isolation, against a list short enough to read, and its correctness does not change when the assembly strategy changes. The assembly loop then has only the whole-result conditions left to worry about, and those are few enough to handle by the standard move: pick one of them to be maintained throughout and one to be driven toward, so the loop's invariant and its termination condition both come from the requirement list rather than from invention. Anything that has to be carried between iterations to keep the invariant true — the residue of work still outstanding, typically — announces itself at this point as a variable with a stated relationship to the result so far, which is exactly the kind of variable whose purpose stays clear a year later.

The diagnostic use is as valuable as the constructive one. A requirement that mentions both the whole and a single part is a warning: it will not sit cleanly in either half, and it is the thing that will couple your modules no matter how the boxes are drawn. Either it is genuinely global, in which case the decomposition has to be organized around it rather than despite it, or it is over-stated and can be weakened into a per-part condition. Finding this out while the requirements are still text is much cheaper than finding it out as a mysterious dependency between two finished components.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the examination-timetable example, where the six formalized conditions are observed to fall into those relating to the timetable as a whole and those relating only to an individual session without mentioning the timetable, which suggests an inner part selecting a suitable session and an outer loop assembling the timetable from such sessions; the outer loop then takes exclusiveness as its invariant and exhaustiveness as its termination condition, and introduces a variable holding the not-yet-scheduled examinations defined by its own invariant relation to the timetable built so far.
