---
type: lesson
title: "A design record is worth what its timing allows, not what its contents say"
figure: parnas
works: [software-aging]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# A design record is worth what its timing allows, not what its contents say

**Lesson:** Recording a design is usually treated as a reporting duty — the
description trails the artifact, and can in principle be produced whenever
somebody finds the time. Parnas's objection is economic rather than moral. A
precise account of a design earns most of its value by existing at the moment
decisions are still open: it is the only thing a reviewer can attack before code
exists, and the only thing that can be corrected while correction is still cheap.
Produce the identical document after the product ships and you have paid more for
it — reconstructing intent from code is harder than stating it while you hold it —
and bought less, because the review it could have enabled never happened. Same
words, different worth. The value was never in the artifact; it was in the
position it occupied in time.

There is a second reason the writing matters independently of the reading. Stating
a design precisely is not transcription, it is analysis. Committing to say exactly
what each part is responsible for, in a form that admits no vagueness, forces a
systematic pass over the whole system and surfaces things nobody was looking for:
duplicated functions, near-duplicates that differ in ways no one intended,
outright defects. Parnas reports getting a non-functional program working via a
documentation exercise where finding bugs was never the assignment. The rigour of
the notation is doing the work — an informal narrative can be written without
resolving the questions a precise one cannot dodge, which is exactly why the
informal version feels easier and finds nothing.

A programmer who takes this seriously stops arguing about whether documentation is
worth writing and starts arguing about when. The record is created as a medium for
making the design, not as a description of one already made, and it is treated as
having a deadline that precedes the code rather than following the release. It also
predicts a specific pathology: an organization that treats the record as a
deliverable rather than an instrument ends up with two of them — an official one
produced to satisfy an obligation, ignored because it is inaccurate, and an
informal one the maintainers actually trust. That outcome is not a discipline
failure to be scolded away; it is the natural result of writing the document at a
time when it could no longer do any work.

**Source:** [Software Aging](../works/software-aging.md) — the documentation
sections on prevention and on retroactive repair, including the claim that a record
created after shipping costs more and is worth less, and the anecdote of a
documentation exercise that revived a dead program as a side effect.
