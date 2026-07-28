---
type: lesson
title: "The Limits On A Running Program Were Set At Levels Above The Program"
figure: nygaard
works: [program-development-as-a-social-activity]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# The Limits On A Running Program Were Set At Levels Above The Program

**Lesson:** Nygaard stacks the subject matter of the field into alternating layers: a live process of information being handled by people and machines; the constraints that pin that process down, of which the program text is only one part alongside hardware limits and the unwritten conventions people follow; the development activity that produces those constraints; the organizational and resource limits that shape the development activity; and the learning and research that slowly change those limits. What matters is the direction of dependence. If the running process behaves badly, the cause frequently sits two or three layers up, in how the constraints were produced rather than in what they say.

The layers are not separate objects — the same afternoon of work can be viewed as programming or as an organization changing what it knows how to do, and both views are accurate. Nygaard's point is that a discipline which declares only the bottom two layers to be its business has amputated the explanations for most of its own failures, and can then only describe them as regrettable externalities. He makes the same move against staged methods: the neat sequence of investigate, then design, then build, then decide does not survive contact with real projects, because investigating, constructing, and changing are happening simultaneously at every stage. A method that prescribes the tidy order will be departed from, and studying the departure is more informative than restating the prescription.

For a working programmer this reframes debugging and improvement. A recurring defect class that survives every local fix is a signal to look at what produced the code, not to fix it harder — the escalation is up a layer, to how the work was split, what the team knew, or what the schedule permitted. It also predicts that a process document describing an orderly sequence of phases is a description of an aspiration, so plans should be built around the fact that understanding, building, and changing will interleave. And it argues for measuring the actual shape of development against the claimed shape, since the gap between them is where the real constraints are visible.

**Source:** [Program Development as a Social Activity](../works/program-development-as-a-social-activity.md) — the enumerated process-and-structure levels and the argument that the field cannot be confined to the lowest two, followed by the critique of stage-ordered development methods.
