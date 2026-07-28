---
type: lesson
title: "Promote something to a primitive only when its absence has a demonstrated cost, not a theoretical one"
figure: ritchie
works: [unix-time-sharing-system-a-retrospective]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Promote something to a primitive only when its absence has a demonstrated cost, not a theoretical one

**Lesson:** Ritchie states a promotion rule for the system's core interfaces and then applies it to himself in public. The rule: a mechanism that can already be built out of what exists does not get added underneath, and only serious, demonstrable inefficiency justifies complicating the basic interfaces. The applications are unglamorous. Mutual exclusion is available by agreeing that creating and removing a known file stands for acquiring and releasing, which is admittedly slower than a purpose-built primitive would be — and stays out anyway, because slower is not the same as insufficient. Reserving a device for one user over several commands needs no kernel change at all, since devices are named by files and files already have owners, so an assignment command can be written entirely outside the system.

Two things make this a real discipline rather than a slogan. First, "demonstrated" means someone points at a case, and Ritchie is willing to be shown: the same paper concedes that the network implementers genuinely need asynchronous I/O, that projects are being driven to split one logical task across several processes for lack of shared writable memory, and that pipes cannot reach a long-running server process because they require a common ancestor. Those are named claimants with named damage, and he treats them differently from the general desire for a message facility. Second, the rule is about the *foundation* specifically. Nothing stops a mechanism from existing as a library or a command; the question is only whether it earns a place in the interface that every future client must carry.

The reason to hold this line is asymmetry of consequences. A convenience implemented above can be replaced or ignored; a primitive is a permanent obligation, has to interact correctly with every other primitive, and is remembered by everyone who reads the system afterward. Cheap-looking additions to a foundation compound into a surface nobody can hold in mind.

A programmer who believes this answers "we need X in the core" by first building X out of what already exists, shipping it, and waiting for a measurement. When the measurement arrives they add the primitive without embarrassment; when it never arrives, the composed version was the right answer all along. They also keep a written record of who is being hurt by each omission, so the eventual decision rests on accumulated evidence rather than on whoever argued last.

**Source:** [UNIX Time-Sharing System: A Retrospective](../works/unix-time-sharing-system-a-retrospective.md) — the process-environment section stating the rule and the semaphore-by-file example, read alongside the "What UNIX Does Not Do" section where specific, sourced complaints about asynchronous I/O, shared memory, and daemon communication are conceded.
