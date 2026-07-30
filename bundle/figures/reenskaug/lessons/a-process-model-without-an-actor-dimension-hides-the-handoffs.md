---
type: lesson
title: "A process model with no actor dimension smuggles in the author's own role as the default"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# A process model with no actor dimension smuggles in the author's own role as the default

**Lesson:** Standard software lifecycle models answer two questions — what happens, and when. Specification, design, implementation, test, installation, maintenance. The author's observation is that they almost all share an unstated third answer: *who*, silently fixed as the program developer, because developers wrote them. That omission is not a gap to be filled for completeness; it actively conceals work.

The demonstration is a single word. "Maintenance" appears in every such model as one late phase, and unpacking one instance of it — fixing a reported bug — yields a relay of six distinct people: the user who notices the irregularity, the operator who files it, the vendor's support contact, the development lead, the programmer who fixes it, and the same chain traversed backwards to deliver the patch. None of those handoffs is visible in the model. Each is a place where the report can be garbled, deprioritized, or lost, and where latency accumulates. So the phase name is not merely coarse; it is coarse in a way that makes the system's actual failure modes unmentionable, since you cannot discuss a queue that your vocabulary says does not exist.

Adding the actor dimension changes what the model is for. Two dimensions describe an artifact moving through stages, which is useful for scheduling and nothing else. Three dimensions describe a chain of producer-consumer relationships, where each participant's output is someone specific's raw material — and that framing generates questions the flat model cannot pose: what does this participant need in order to do their part, is their success measured by the satisfaction of whoever consumes their output, and where does work cross a boundary between people who do not share a vocabulary or an employer. Every one of those crossings is a real risk that a phase diagram renders invisible.

The transferable habit is to read any process description you are handed by asking whose viewpoint it was written from, and to treat a phase name that covers multiple people's work as a defect in the description rather than an abstraction. When one word in a model expands into a six-person relay, that word is where the process is actually failing, and no amount of refining the phases will show it.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 10 section 10.1, which notes that most lifecycle models describe the software's life from the program developer's point of view, unpacks the "apparently innocent word maintenance" into the six-person bug-report relay, and proposes extending the traditional what-and-when model with *who* as a third dimension, yielding the producer-consumer layers the author calls a value chain.
