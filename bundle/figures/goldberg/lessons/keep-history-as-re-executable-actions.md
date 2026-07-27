---
type: lesson
title: "Record what you did as re-executable actions, and keep separate records for the two different questions you will ask of history"
figure: goldberg
works: [smalltalk-80-the-interactive-programming-environment]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Record what you did as re-executable actions, and keep separate records for the two different questions you will ask of history

**Lesson:** A live, always-modifiable system has an obvious hazard: state accumulates by mutation, and the record of how it got that way lives only in the programmer's memory. This environment answers with a discipline worth generalizing far beyond it. Every alteration and every expression evaluated is written out, as it happens, to an external log — in the form of expressions that can simply be executed again. That single choice of representation does most of the work. Because the log is not a description of what happened but a means of making it happen again, recovery after a crash is not reconstruction: you restart from the last saved state, find the marker written at that save point, and re-execute the entries that follow, choosing which ones you want. Sharing work with a colleague uses the same artifact for the same reason. There is no separate export format, because the log already is one.

The sharper insight is structural: this book maintains *two* records with deliberately different properties, because two different questions are being asked. One is an in-memory set describing what has been changed — collapsed to one entry per changed thing, unordered, answering "what is different now." The other is the external log — ordered, complete, including evaluations and not just definitions, answering "what happened, in what sequence." The book notes the differences explicitly: the set does not retain order or repeated versions, the file does, which is what makes stepping back to an earlier version of something possible from the file and not from the set. Most systems build one history structure and then discover it answers only half the questions. Deciding up front which questions history must answer, and accepting two representations if the questions differ, is the transferable move.

The rest follows from having the record. Merging separate people's work becomes a matter of reading several logs and asking mechanically whether any of them define the same thing differently — conflict detection as a query over recorded actions, not a diff over text. And the presence of a real record is what makes an aggressively mutable system responsible rather than reckless: you can freely change anything precisely because everything you changed is enumerable, reviewable, removable, and replayable. Notably, the book also treats the boundary of the mechanism honestly — coordinating releases across a group is described as a practice with a named human owner and tooling built on top, not something the environment solves by itself.

A programmer who takes this on logs actions in a form that can be re-run rather than merely read, and asks of any audit trail whether it can rebuild state or only describe it. And when someone proposes a single history structure, the question becomes which questions it cannot answer.

**Source:** [Smalltalk-80: The Interactive Programming Environment](../works/smalltalk-80-the-interactive-programming-environment.md) — the system backup and recovery chapter: the enumeration of what enters the change set, the description of the external log as executable expressions with save-point markers, the recovery procedure of re-executing entries after the last save, the change-management browser's ordering and conflict-checking commands, and the contrast drawn between the ordered external log and the unordered internal set.
