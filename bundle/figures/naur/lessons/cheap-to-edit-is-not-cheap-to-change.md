---
type: lesson
title: "Cheap to edit is not cheap to change; the medium's malleability says nothing about the cost"
figure: naur
works: [programming-as-theory-building]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Cheap to edit is not cheap to change; the medium's malleability says nothing about the cost

**Lesson:** The expectation that modifying an existing system should be much cheaper than building one rests on an unexamined inference from the medium. Source is text, text is trivially editable, therefore change is cheap — but that only follows if manipulating the text is where the cost lives. If the expensive part is instead working out how the new demand relates to what the system already does and whether the existing structure can carry it, then the ease of typing is irrelevant to the estimate. Every other complicated made thing tells the same story: altering a building is expensive enough that tearing it down and starting again is frequently the better economics, and nothing about software repeals that except an intuition about keystrokes.

Taking this seriously changes how you estimate. The honest first question about a change request is not how many files it touches but whether anyone can situate the new demand against the system's existing commitments — and that assessment is the bulk of the work, done before a line is edited. Estimates produced by scoping the diff are systematically optimistic in exactly the cases that hurt most: unfamiliar systems, absent original builders, requirements that graze the edge of what the design assumed. In those cases the diff can be genuinely small and the change still enormous.

The corollary runs the other way too, and it is the one people resist. If modification is not intrinsically cheap, then rewriting is not intrinsically extravagant, and the comparison between the two has to be made on the actual costs rather than on the reflex that reuse is thrift. Sometimes the numbers favor starting again. What you should stop doing is assuming an answer to that comparison because one option involves editing a file and the other involves an empty one.

**Source:** [Programming as Theory Building](../works/programming-as-theory-building.md) — the analysis of modification costs, which examines and rejects both supports for expecting cheap modification: the analogy with other complex constructions, where demolition and rebuilding is often preferable, and the assumption that text manipulation dominates the cost.
