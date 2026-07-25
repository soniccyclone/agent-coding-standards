---
type: lesson
title: "Minimality is owed by the layer you reason in, speed by the layer you run on, and neither should be asked of the other"
figure: cardelli
works: [the-functional-abstract-machine, on-understanding-types-data-abstraction-and-polymorphism, an-imperative-object-calculus]
axes: [primitive-count, hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, programming-languages-and-semantics]
tags: [lesson]
---
# Minimality is owed by the layer you reason in, speed by the layer you run on, and neither should be asked of the other

**Lesson:** The same author who spent years shrinking object-oriented programming down to four syntactic forms designed an execution machine with a deliberately large and open-ended instruction set, no interest in minimality, and a data-type inventory chosen for whatever the compiler finds convenient. That is not inconsistency. Small bases are for the layer where you argue about meaning, because an argument has to be repeated once per primitive and every extra primitive multiplies the cases in every proof. Rich bases are for the layer where you argue about cost, because there the goal is that each frequent source construct has a direct target that a peephole pass can recognize, and a lean instruction set only pushes the same work into longer sequences you can no longer optimize as units.

The corollary that makes the split work is that obligations flow downhill, and must be stated. The execution layer here performs no run-time type discrimination at all and is therefore not safe on its own; it is safe because the layer above proved what it needs, and the design says so out loud. Where a genuine run-time decision is required, it is not smuggled back in as a universal tag check but expressed in the source language as a tagged sum, which keeps the check visible in the program instead of hidden in the machine. The general shape is that each layer names the invariant it assumes from above and the invariant it guarantees below, and the assumption is precisely what buys the speed.

The trap this avoids is holding one aesthetic across an entire system. Insisting on a tiny instruction set in a compiler backend produces slow code and unreadable emitted sequences; insisting on a rich, convenient vocabulary in a semantics produces a specification nobody can prove anything about, and a design where two features interact in a way no one predicted. A programmer who has internalized this asks, of every layer, which property that layer exists to optimize, and refuses to import the neighbouring layer's standard of merit.

**Source:** [The Functional Abstract Machine](../works/the-functional-abstract-machine.md) — the introduction's explicit trade of minimality for compilation convenience and portability, along with the decision to omit run-time type checking and rely on source-level checking, plus tagged variants where dynamic discrimination is genuinely needed. Also [On Understanding Types, Data Abstraction, and Polymorphism](../works/on-understanding-types-data-abstraction-and-polymorphism.md) — the opposite pole, where a deliberately impractical kernel language is built precisely so that features can be compared and reasoned about. Also [An Imperative Object Calculus](../works/an-imperative-object-calculus.md) — the framing of a compact kernel as what gives conceptual unity and enables formal analysis, with convenience constructs pushed out to derived notation.
