---
type: lesson
title: "A system can only acquire on its own what it could first have been told, so build the telling channel before the acquisition machinery"
figure: mccarthy
works: [programs-with-common-sense]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A system can only acquire on its own what it could first have been told, so build the telling channel before the acquisition machinery

**Lesson:** McCarthy states an ordering constraint that reads almost as a tautology and is in fact a design discipline: a program cannot come to hold a piece of knowledge by its own effort unless there already exists a form in which that knowledge could have been handed to it directly. Autonomous acquisition is not a separate faculty bolted on beside the ordinary input path; it is that same path driven from the inside. So whatever the system cannot be told, it also cannot learn, and no amount of cleverness in the acquisition mechanism repairs a representation that has no slot for the thing to be acquired.

This inverts the usual order of ambition. The tempting plan is to build the machinery that discovers, and to treat the question of how discoveries get represented as a detail to settle later. McCarthy takes the opposite route deliberately: of the five capabilities he lists as necessary, he commits his effort to the second one — that interesting changes be simply expressible — and sets the rest aside, including learning from experience, which is the actual goal. The interim target is a system that can be told to change a specific aspect of its behavior by someone who knows no more about its internals than they would need to instruct a person. Only once that channel exists does he expect it to be possible to tell the system how to learn, which is itself just another thing told through the same channel.

The reason this holds is that instruction from outside and acquisition from inside must terminate at the same place. Both end in a statement deposited somewhere the system consults. If the system's behavior is not encoded in statements at all, then the only way to change it is to edit the mechanism, and neither an outside instructor nor an inside learner can do that without full knowledge of the mechanism's current state — which defeats the point in both directions at once. The telling channel is thus a strictly easier problem that is a strict prerequisite, which makes it the right thing to solve first.

A programmer who takes this seriously uses "could I explain this change to the system in the terms the system already has?" as a design test long before any adaptive behavior is contemplated. It gives a concrete, near-term milestone for systems whose real goal is far off, and it kills a common category of waste: adaptive layers, tuning loops, and feedback mechanisms built over a substrate in which the adaptation has nowhere to be written down, which end up able to adjust only the handful of numeric knobs someone remembered to expose.

**Source:** [Programs with Common Sense](../works/programs-with-common-sense.md) — the passage where McCarthy narrows his effort to the second of his five listed features and states the being-told prerequisite, together with the tabulated comparison of instruction by imperatives against instruction by declaratives that follows it.
