---
type: lesson
title: "Make the write a separate verb, and put the danger in the name"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, programming-environments-and-object-systems]
tags: [lesson]
---
# Make the write a separate verb, and put the danger in the name

**Lesson:** A tool that edits a structure directly, with no validation between the operator and the medium, needs its own safety discipline because none is inherited from anywhere. Two devices do most of the work and both are cheap. First, split every modification into two operations that cannot be confused: one that brings a unit into a working copy and one that sends the working copy back, with all editing happening on the copy in between and every intermediate state displayed. Nothing reaches the medium except by the operator naming the sending operation, so a mistyped edit costs a re-read rather than a destroyed unit, and the operator always sees what will be written before it is written. The working copies are also worth keeping distinct per kind of unit, because a tool that holds one buffer will eventually write the contents of one kind of unit to the location of another.

Second, encode destructiveness in the name of the operation itself rather than in documentation, a confirmation prompt, or the operator's memory. A shared marker on every command that touches the medium means the property is legible in the command list, in a transcript of a session, and in the moment of typing — and it makes an accidental destructive command require a deliberate extra keystroke that no safe command requires. This is worth more than a confirmation dialogue, which trains the reflex that dismisses it, and it costs one character of syntax. The general form is that a hazard should be visible in the shortest representation of the action, because that is the representation people actually read.

Both devices share a premise worth extracting: in a tool whose operator is expected to be careful, the design's job is not to prevent mistakes but to make the dangerous act distinguishable from the safe one at every point where it could be confused — while typing, while reading back what was done, and while deciding whether the state on screen is the state to commit. Safety that depends on the operator remembering which operations are dangerous has put the invariant in the wrong place.

**Source:** [Project Oberon](../works/project-oberon.md) — section 14.3's description of DiskCheck, whose commands that write to the disk are all marked with an exclamation mark, and whose sectors are always read into one of several distinct buffers — sector, directory, header, track — with changes made on the buffered data, displayed after each read or change, and transferred to the disk only by a writing command.
