---
type: lesson
title: "Make the naming context a per-process parameter, not a property of the machine"
figure: thompson
works: [the-use-of-name-spaces-in-plan-9]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Make the naming context a per-process parameter, not a property of the machine

**Lesson:** Most systems treat the mapping from names to things as a fact about the installation: there is one directory tree, one set of libraries, one meaning for a given path, and every program on the box shares it. Once you accept that, every situation where two programs need different answers for the same name has to be solved by inventing a new mechanism — a search-path variable, a compatibility shim, a version selector, a container, special-case kernel code that overloads one magic name differently per caller. Each of those mechanisms is a local patch on the same missing feature. The alternative is to demote naming from a global fact to an ordinary inheritable attribute of a running process, on the same footing as its open files or its memory: a child gets its parent's view by default, may be given a copy it can edit privately, and may be given a view assembled specifically for it before it starts.

The reason this pays so well is that a startling number of unrelated-looking problems are actually the same problem wearing different clothes. Running the right binaries on mixed hardware, reading yesterday's snapshot of a directory, testing a program against an older library, giving each window its own console, letting a process reach a device that physically lives on another machine, and measuring exactly what one process asked the outside world for — all of these reduce to arranging that a particular process resolves a particular name differently from its neighbours. One mechanism handles the whole family, and the mechanism is small because it does nothing but decide what a name means. The corollary is uncomfortable but load-bearing: convention has to do the work that global structure used to do. If nothing is globally true, programs can only cooperate because everyone agrees, by discipline rather than enforcement, on what the conventional locations mean.

A programmer who has internalized this stops reaching for a configuration knob every time two callers need different behaviour, and asks instead whether the thing that ought to vary is the caller's view of the world rather than the code. It reframes portability, versioning, sandboxing and remote access as name-resolution questions. It also changes what counts as a good interface: an interface addressed by name, resolved late, in a context the caller controls, can be substituted without the code that uses it knowing or caring — whereas one addressed by a fixed identifier baked into the program cannot.

**Source:** [The Use of Name Spaces in Plan 9](../works/the-use-of-name-spaces-in-plan-9.md) — the argument runs through the paper's treatment of the mount and bind operations and the process-creation attribute that decides whether a child shares or copies its view, then through the examples of architecture-specific binary directories, the dated backup hierarchy, and per-window console files, each of which is the same mechanism applied to a different problem.
