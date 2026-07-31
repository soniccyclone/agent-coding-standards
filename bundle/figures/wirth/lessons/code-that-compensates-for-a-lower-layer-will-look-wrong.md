---
type: lesson
title: "Code that compensates for a defect below will look wrong, and should be labelled rather than beautified"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, verifiability, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Code that compensates for a defect below will look wrong, and should be labelled rather than beautified

**Lesson:** Some code cannot be made to read well, and the reason is not that its author lacked taste. When a layer you depend on and cannot change gives an answer that is sometimes wrong — a status flag that fires early, a value that must be sampled twice and compared, an interval that has to be spent in a counting loop because no timer is fine enough — the compensating code has no clean form available to it. Its shape is dictated by the shape of the defect, and the defect is arbitrary. Recognising this changes what you do about it. The instinct to keep refactoring until the passage looks principled is wasted effort at best, and at worst it produces something that reads beautifully while quietly no longer covering the case it existed for.

The productive response is to make the compensation legible as compensation. Confine it to the smallest possible region, ideally a single procedure whose interface is the clean one everybody wanted, and state at that boundary what is being worked around and why the ugly form is necessary. That note is not decoration; it is the only thing that lets a later reader distinguish "this is convoluted because someone was careless" from "this is convoluted because the world is". Without it, the passage will be simplified by a well-meaning maintainer and the original symptom will return, in a form that is now much harder to trace because the code no longer admits to having a reason.

Two further things follow. First, a workaround is a claim about an external artefact and therefore has an expiry date: it is worth recording what would have to change for it to be deleted, because a compensation for a bug in something you do not control is exactly the code that should be re-examined when that thing is replaced. Second, the presence of such passages is real information about the interface below you. Counting them, and noticing where they cluster, tells you which of your dependencies is actually costing you — and a component that requires a great deal of compensating is a component whose specification you should stop trusting, and whose replacement you should start pricing. The ugliness is a measurement. Do not erase the instrument.

**Source:** [Project Oberon](../works/project-oberon.md) — the fifth comment following the network driver in section 9.3, which reports that the controller's end-of-frame status bit is not reliable and sometimes signals the end prematurely, that the situation is saved by testing a number of times while no further data arrives, and that the resulting program section does not appear very neatly conceived but that software fixing a hardware deficiency never does; together with the same list's first comment, that the sequence in which the device's registers must be initialised is essential to correct functioning and was undocumented, and the fourth, that a required interval is too short for the available timer's resolution and so must be programmed as a tight delay loop whose constant depends on the machine's clock rate, described as unfortunate.
