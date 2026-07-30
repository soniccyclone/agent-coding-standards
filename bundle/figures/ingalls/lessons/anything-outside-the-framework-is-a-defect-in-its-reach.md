---
type: lesson
title: "Treat everything that does not fit your framework as a defect in the framework's reach, not as a separate layer to live with"
figure: ingalls
works: [design-principles-behind-smalltalk]
axes: [cognitive-load, expressiveness, primitive-count]
subdomains: [operating-systems-and-systems-programming, programming-environments-and-object-systems]
tags: [lesson]
---
# Treat everything that does not fit your framework as a defect in the framework's reach, not as a separate layer to live with

**Lesson:** The name for the residue that accumulates outside a language — the storage arrangements, the file access, the display handling, the input devices, the debugger, the way one program starts another — is the operating system, and the useful provocation is to say that this residue should not exist. Not that its functions should not exist, but that they should not be a separate world with its own conventions. Every time work forces a person to leave the framework they have been thinking in, they abandon the context they have built up and re-enter a smaller, more primitive vocabulary to accomplish something that was conceptually part of the same task. That discontinuity is a real cost, paid repeatedly, and it is usually accepted as inevitable rather than examined.

It is not inevitable, and the recipe for eliminating it is uniform across cases: represent the facility as an ordinary participant in the framework and give it a normal repertoire of requests. Files and directories become ordinary things you can ask ordinary questions of. The screen becomes an instance of the same kind used for any image, and drawing on it uses the operations you already know. Input devices become things you interrogate for state or history. The bottom of it — reading a physical page from a disk — remains a genuine primitive, but it is reached through the same request mechanism as everything else, so no user of it has to leave the framework to get there. The primitive is preserved; the separate world is not.

The strongest form of this is applied to the system's own workings. Make the running state of a computation an ordinary object with ordinary structure, and a debugger stops being privileged machinery: it is a program written in the same terms as any other, which happens to inspect and adjust a suspended computation. That is also what lets every component present itself for inspection and manipulation at the user's level, since a thing that has a repertoire of requests already has, in effect, a small language of its own that a user interface can render and drive. The design rule to carry away is that a separate mechanism, tool, or environment appearing beside your framework is evidence about the framework, and the first response should be to ask what it would take to bring that thing inside.

**Source:** [Design Principles Behind Smalltalk](../works/design-principles-behind-smalltalk.md) — the Operating System principle declaring such a system to be a collection of things that do not fit into a language, its enumeration of storage, files, display, input, subsystems and the debugger folded back into ordinary objects and messages, the reification of processor state as a process object owning stack frames, and the Reactive Principle requiring every user-accessible component to present itself for observation and manipulation.
