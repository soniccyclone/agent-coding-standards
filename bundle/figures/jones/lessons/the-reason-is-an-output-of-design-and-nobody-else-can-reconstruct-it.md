---
type: lesson
title: "The reason a design is believed correct is an output of designing it, and nobody downstream can reconstruct it"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# The reason a design is believed correct is an output of designing it, and nobody downstream can reconstruct it

**Lesson:** A development step produces three things, not two. There is the statement of what was required, there is the proposed solution, and there is the reason the designer believed the second meets the first. Ordinary practice captures the first two and throws the third away — it lived in one person's head during the hour the decision was made and is gone by the afternoon. The loss is invisible at the time, which is why it keeps happening, and it is expensive later, because every subsequent reader of the design is reduced to guessing which properties were deliberate and which are accidents.

The reason this cannot be fixed by adding reviewers is that the argument is not recoverable from the artifact. A reviewer handed a specification and a solution has to invent, on the spot and under time pressure, the chain of reasoning the designer spent days constructing; whatever the reviewer produces is a fresh and shallower argument, not a check of the original one. So the responsibility is not divisible: the person who makes a design decision is the only person positioned to record why it holds, and any process that assigns designing to one role and justifying to another has already lost the thing it was trying to capture.

This reframes what a design review is for. If the argument arrives with the design, the review stops being a hunt for defects — an activity with no criterion for when it is finished — and becomes an examination of a specific claim, which either convinces the room or does not. It also supplies the missing completion criterion for a design stage. Without a recorded argument there is no positive test for "this step is done"; work moves on when someone runs out of doubts. With one, the step is done when the argument covers the specification, and the gaps in the argument are exactly the work remaining.

The practical form the argument takes should be as light as the situation permits — a couple of definitions plus the claim that they fit a known pattern is often enough. What matters is not the ceremony but that a written reason exists at all, attached to the step that produced it, while the person who had it is still the person writing.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 1's background section on the state of design verification in practice, where the specification (WHAT) and the proposed solution (HOW) survive but the reason (WHY) is described as lost forever, together with the observation that walk-throughs and inspections became accepted in place of any recorded reasoning; the closing statement of the "Specific Approach" section that recording the correctness argument is the developer's responsibility and that separating the tasks is not workable, and the accompanying claim that development is thereby given positive criteria for the successful completion of a design stage.
