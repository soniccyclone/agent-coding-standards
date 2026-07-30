---
type: lesson
title: "Slowness costs you the user's held state, so make every operation small enough to complete inside their attention"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [hardware-affinity, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Slowness costs you the user's held state, so make every operation small enough to complete inside their attention

**Lesson:** Performance is usually justified in units of machine time, which makes it look like an efficiency concern that can be traded against other goods. The more useful frame treats the person and the system as a single circuit — information flowing from the person in, and results flowing back out — which persists only while their attention stays engaged. Latency does not merely cost seconds. Past some threshold the person's attention leaves, the circuit opens, and the real loss is the working state they were holding: on returning they must reconstruct where they were, which costs far more than the delay did and is invisible in any timing measurement.

The design response is not just "be fast," because you cannot always be. It is to shape the work so that no operation *requires* the person to hold partial state across it. Make each one closeable and atomic: it completes, it leaves nothing dangling, and the person's held context is never load-bearing while it runs. This has a pleasant consequence that reveals whether you have got it right — genuinely atomic operations need no mechanism for interrupting or resuming them, because they are short enough to finish inside the attention they already have. If you find yourself building cancel, resume, or save-my-progress machinery, that is evidence the operations are too coarse rather than evidence you need better machinery.

Where a delay is genuinely unavoidable, the remaining move is to keep the circuit closed rather than to keep the person waiting quietly: immediate response to input even before the work is done, visible progress on anything long, animation of transitions so a change of state reads as continuous rather than as a jump. All of that exists to hold attention, which is the actual resource being protected. So the transferable question when you catch yourself deciding whether an optimization is worth it: this is not milliseconds against effort, it is whether a person will still be holding their problem in mind when the answer arrives.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 7's user interface design rules, adapted from lectures by Bruce Horn and published there for the first time with his permission: the rule on maintaining the illusion of direct manipulation, which describes the user-computer circuit, warns that slow operations cause the person to wander off and then have to rebuild short-term memory, and derives closure (atomic operations requiring no partial state, and therefore no interruption facility) plus immediate feedback and progress indication.
