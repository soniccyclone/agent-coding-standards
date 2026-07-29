---
type: lesson
title: "An abstraction's limit is what it implies, not what it can be made to encode"
figure: thompson
works: [the-use-of-name-spaces-in-plan-9]
axes: [expressiveness, cognitive-load, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# An abstraction's limit is what it implies, not what it can be made to encode

**Lesson:** When a unifying abstraction is working well, the temptation is to push everything through it, and the test people apply is whether the thing can be expressed at all. That test is worthless, because a sufficiently general abstraction can encode anything. The better test is what the abstraction silently promises about whatever is expressed in it. A representation carries the whole set of operations its other inhabitants support, and a client who finds a thing in that form will reasonably assume those operations apply. If they cannot, you have not extended the abstraction; you have installed a lie inside it, and the cost lands on every future reader who trusted the uniformity.

The sharpest version of this reasoning is about capabilities the representation implies but the underlying reality cannot honour. Something local and physically bound — memory shared between processes on one machine — can be dressed in a naming scheme whose other members are all reachable from anywhere. Doing so would advertise that it, too, can be reached from anywhere, which is false and cannot be made true. The right response is not to add a caveat in documentation but to keep that resource outside the abstraction and give it its own, less generous interface. Similar restraint applies where the candidate's structure genuinely does not fit the abstraction's shape, or where the operations that matter for it have no natural counterpart in the abstraction's small operation set: forcing the fit costs more clarity than the uniformity buys.

This is why a designer with taste can list, on request, the things their unifying idea deliberately does not cover, and why the absence of such a list is a warning sign. Stating the exclusions and the reasons is not an admission of incompleteness; it is what makes the uniformity trustworthy everywhere else, because a reader can then take membership in the abstraction as real information rather than as a stylistic convention. A programmer who believes this stops measuring an abstraction by its reach and starts measuring it by whether every guarantee it implies actually holds for every member — and accepts a second, honest mechanism for the outliers rather than one universal mechanism that quietly means different things in different places.

**Source:** [The Use of Name Spaces in Plan 9](../works/the-use-of-name-spaces-in-plan-9.md) — the paper's closing position section, where the authors enumerate what they refused to represent as files (process creation, network addressing, shared memory) and give the reason in each case, most tellingly that a file-like representation of memory would advertise remote access that could not be delivered.
