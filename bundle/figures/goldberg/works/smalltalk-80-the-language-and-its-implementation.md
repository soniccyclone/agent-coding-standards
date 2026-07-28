---
type: work
title: "Smalltalk-80: The Language and Its Implementation"
figure: goldberg
description: The canonical reference for Smalltalk-80, known informally as the "Blue Book." Part one specifies the language itself — objects, classes, messages, blocks — from a user's point of view; part two gives a complete, buildable specification of the virtual machine, including bytecode formats, the object memory, and the interpreter loop, precise enough that multiple independent Smalltalk-80 implementations were built directly from it. It set a rare standard for what it means to fully document both a language's semantics and its implementation in one book.
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
year: 1983
url: https://rmod-files.lille.inria.fr/FreeBooks/BlueBook/Bluebook.pdf
extraction: complete
access: public
host: institutional
tags: [work]
---

# Smalltalk-80: The Language and Its Implementation

**Author(s):** Adele Goldberg and David Robson
**Venue/year:** Addison-Wesley, 1983 (the "Blue Book").
**Source:** https://rmod-files.lille.inria.fr/FreeBooks/BlueBook/Bluebook.pdf — full scan hosted under INRIA's RMoD research team "FreeBooks" collection (rmod-files.lille.inria.fr), a long-maintained Smalltalk preservation archive; institutional host, verified live PDF.

## Lessons
- [Designing an object is designing a vocabulary, so the real work is choosing what may be asked of it](../lessons/every-object-you-design-is-a-vocabulary-you-are-inventing.md)
- [Refuse privileged tiers: make one mechanism cover everything, and accept the implementation bill on the expectation that technique will pay it down](../lessons/buy-uniformity-and-pay-the-implementation-bill.md)
- [Keep the promise and the mechanism in separate documents, and turn every deliberate hole into something the system can state at runtime](../lessons/make-the-unfinished-parts-executable-declarations.md)
- [Define a family's whole meaning against a handful of operations, then let specializations override only for speed — never for meaning](../lessons/tiny-semantic-core-overrides-only-for-speed.md)
- [When a concept keeps showing up only in explanations, promote it to a thing the program can hold](../lessons/give-an-object-to-the-thing-you-keep-explaining-in-comments.md)
- [A specification is finished when a stranger can rebuild the machine from it — which means fixing behavior and leaving code shape free](../lessons/a-spec-is-done-when-a-stranger-can-rebuild-the-machine.md)
- [Reach the machine through the abstraction, not around it: build the escape hatch so the model never notices](../lessons/escape-hatches-to-the-machine-that-stay-inside-the-model.md)
- [Carve a domain by what its things do and what they need coordinated, and say out loud over what interval your idealizations hold](../lessons/model-by-what-things-do-and-name-the-interval-your-idealization-holds.md)
- [Debug a computation that is still alive: make the halted state an object you can question, edit, and resume](../lessons/debug-a-live-computation-not-a-corpse.md) — this work supplies the failure-as-ordinary-request mechanism; the lesson is led by the Orange Book
