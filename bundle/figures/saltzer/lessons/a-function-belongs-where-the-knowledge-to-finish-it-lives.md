---
type: lesson
title: "A function belongs where the knowledge to finish it lives"
figure: saltzer
works: [end-to-end-arguments-in-system-design]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# A function belongs where the knowledge to finish it lives

**Lesson:** The usual way of assigning responsibility in a layered system is by
convenience: whoever is closest to the machinery that seems related gets the job.
This work replaces that instinct with a test that has an actual answer. Ask what
information a function needs in order to be *complete* — not merely to be
attempted. If the required information exists only at the outer edges of the
system, where the real intent of the operation is known, then no inner layer can
ever discharge the responsibility no matter how much machinery it accumulates. It
can reduce how often the outer check fires; it can never remove the need for the
check. The lower layer's version is therefore not a weaker implementation of the
same guarantee, it is a different thing wearing the same name.

This holds because guarantees compose by weakest link and because every layer
boundary is also an information boundary. A layer that has been handed a stream of
bytes has been handed exactly that, stripped of the meaning that would let it know
whether the bytes are right. It can defend the transit it controls and nothing
else, and the places it cannot defend — buffers, copies, crashes, the layers above
and below it — are precisely the places that still hold most of the failure
probability. So an inner guarantee eliminates one hazard from a list and leaves
the shape of the problem untouched.

A programmer who accepts this stops shopping for infrastructure that promises to
take a whole responsibility off their hands, because they now expect such promises
to be structurally impossible rather than merely unfulfilled. They locate each
responsibility once, at the level that can actually confirm the outcome, and they
let the layers below stay ignorant. This makes the lower layers smaller and
simpler, which is a side effect, not the motive: the motive is that the guarantee
now exists somewhere it can be believed. It also inverts the usual reading of a
thin, unhelpful-looking interface. Datagrams over virtual circuits, a spare
instruction set over a rich one, a replaceable library routine over a fixed
supervisor call — in each case the sparse option is chosen because the richer one
was going to be re-done above it anyway.

**Source:** [End-to-End Arguments in System Design](../works/end-to-end-arguments-in-system-design.md)
— the argument is stated as a general principle early on, worked out through the
careful-file-transfer scenario with its enumerated threat list, then shown to
generalize through delivery acknowledgement, encryption, duplicate suppression and
ordering, and finally into instruction-set and operating-system design.
