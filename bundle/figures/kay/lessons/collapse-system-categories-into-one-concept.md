---
type: lesson
title: "Collapse a system's categories when they differ only by rate, and delete the subsystems the distinction required"
figure: kay
works: [a-personal-computer-for-children-of-all-ages]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# Collapse a system's categories when they differ only by rate, and delete the subsystems the distinction required

**Lesson:** Systems accumulate categories that feel fundamental and are not. Data and procedure, stored file and live variable, user session and operating system, resident monitor and running program: each pair looks like two kinds of thing and gets two sets of machinery, two vocabularies, and a conversion layer between them. Often the members of a pair differ only in how fast they change or how long they persist — a thing that changes slowly is called data, the same thing changing quickly is called a function; a thing that persists while you are away is called a file, the same thing while you are present is called state. Once the distinction is recognized as a difference of rate rather than of kind, one concept can carry both, and the machinery that existed solely to bridge them can be deleted rather than improved.

The unifying concept has to be strong enough to bear the load, which in practice means each unit is a small complete computer: it holds state, accepts input, produces output, can be suspended and resumed, and can compute. Given that, the reduction is not a loss of expressiveness, because a general unit can simulate any specialized one, so specialized forms — records, collections, control structures — become things you define within the system rather than categories the system must provide. The measure of a good core, then, is not how many constructs it offers but how many it makes unnecessary. This is also what distinguishes a genuinely small language from a merely stingy one: the small language has few primitives because its primitives compose, not because it withheld features its users will now have to work around.

Two failure modes bracket this. One is the language that tries to supply everything anyone might want, which cannot converge and produces an unlearnable surface. The other is extensibility bolted onto a fixed core, where users may add notation but the core's own categories remain privileged and unreachable, so the extensions are second-class and the original distinctions survive underneath. What actually works is a core simple enough to be described honestly, in which every object is redefinable in terms of other objects, so extension is the same activity as ordinary use rather than a separate mechanism with its own rules.

**Source:** [A Personal Computer for Children of All Ages](../works/a-personal-computer-for-children-of-all-ages.md) — the language-design section rejecting both the all-things-to-all-people language and conventional extensibility, its stated principles of a uniform notion of object with message-passing evaluation and universal redefinability, the duality it draws between functions and tables where data and function differ by rate of change, the claim that each process has the attributes of a complete small computer and can therefore introduce arrays, records and recursive procedures as ordinary additions, and the replacement of separate file, operating-system and monitor notions by treating the user as another process whose state persists between sessions.
