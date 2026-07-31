---
type: lesson
title: "Write the unaffordable version first and keep it: the abstract program is the frame the efficient one is built on"
figure: hoare
works: [notes-on-data-structuring]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Write the unaffordable version first and keep it: the abstract program is the frame the efficient one is built on

**Lesson:** When you already know the direct expression of an algorithm will not run fast enough, the temptation is to skip it and write the intricate version straight away. Write the direct one anyway. Its value is not that it might turn out to be fast enough; it is that it settles what the algorithm *is*, in a text short enough to be checked by eye, before anything about storage layout is decided. The efficient version is then produced by changing only how the data is represented, with the abstract text acting as the pattern the new code is laid out against — same loops, same order of operations, same points at which each thing becomes true. What was one hard problem becomes two easy ones, and the second one is easy precisely because the first one is finished and written down.

The discipline that makes this more than a slogan is the identity claim you are obliged to maintain: from the abstract point of view the two texts express the same algorithm, and everything that differs between them is representation. Hold yourself to that and each fragment of the concrete version has a specific counterpart to be justified against, so you can check a fiddly piece of index arithmetic against a line of the original rather than against your memory of the intent. Let the claim slip — improve the algorithm and the representation in the same edit — and you lose the correspondence, at which point the abstract text is a stale comment and the concrete one is on its own.

The abstract version keeps earning after delivery, too. It is the artifact you go back to when the algorithm has to change, since the modification is stated there and re-derived downward, rather than reverse-engineered out of index arithmetic. This is also the answer to the objection that the abstract notation contains operations too expensive to run: the expense is the point. Those operations are what let you state the algorithm without deciding the layout, and eliminating them is the work of the second stage — not a reason to skip the first.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the sieve-of-Eratosthenes example in the powerset chapter, which writes the algorithm first over an idealized set type, declares it unexecutable at realistic sizes, rewrites it over word-sized sets, and then observes that the two express an identical algorithm differing only in data representation, with the first acting as the framework on which the more intricate second version is structured, simplifying the task of ensuring its parts work together.
