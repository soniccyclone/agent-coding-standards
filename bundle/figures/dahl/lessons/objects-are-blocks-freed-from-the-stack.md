---
type: lesson
title: "To get a new kind of thing, take a construct you trust and delete one of its incidental restrictions"
figure: dahl
works: [simula-67-common-base-language, class-and-subclass-declarations, simula-an-algol-based-simulation-language]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# To get a new kind of thing, take a construct you trust and delete one of its incidental restrictions

**Lesson:** The unit of decomposition in a block-structured language is already almost everything one could want: a named region that describes some data together with the actions over it, whose local names mean the same thing no matter what surrounds it. That locality property is the whole reason decomposition works at all, because it lets a reader interpret a component correctly without holding the rest of the program in mind. What the block did *not* have was independent existence. Entering it created an instance, leaving it destroyed the instance, and instances therefore stood in strict nesting order in time. Look closely at that constraint and it is not part of the idea of a block; it is a property of one convenient storage discipline that happened to be underneath.

Delete it, and the payoff is enormous and almost free. Let a block instance be generated on demand, be named by a value, outlive the expression that created it, and coexist with siblings, and you have simultaneously invented the object, the reference, the linked data structure, and the coroutine. None of these needed a separate primitive. The formal machinery ends up describing one thing, the block instance, with a small amount of extra state about whether it is currently attached to a caller, standing detached with its own suspended position, or finished. The familiar stack-shaped program is then not a different language but the degenerate case in which every instance happens to be attached.

The habit worth stealing is the diagnostic move that precedes the design. Before adding a mechanism, ask which of the restrictions on the mechanism you already have are essential to its meaning and which are artifacts of how it is currently implemented. The essential ones you keep, because they are what make reasoning possible. The artifacts you can price and remove, and removing one usually buys more expressive power than any new feature would, at a much lower cost in primitives to learn. Programmers who work this way grow a language or a system by unlocking what is already there, and their designs stay small while their reach grows.

**Source:** [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md) — the introductory discussion of decomposition and the block concept, which walks from block-as-pattern to block-instance to class-of-objects, and the later chapter that puts all block categories under a single execution-state model. Also [Class and Subclass Declarations](../works/class-and-subclass-declarations.md) — the semantics section, where a class body is stipulated to behave as a block and objects are defined as its instances. Also [SIMULA - an ALGOL-Based Simulation Language](../works/simula-an-algol-based-simulation-language.md) — the process concept, presented as a program-like carrier of both data and actions whose relationships are symmetric rather than nested.
