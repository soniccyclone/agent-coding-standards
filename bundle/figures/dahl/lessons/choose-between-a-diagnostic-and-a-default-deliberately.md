---
type: lesson
title: "For every partial operation, decide consciously whether to trap or to default, and know that a default spends your ability to detect the unforeseen"
figure: dahl
works: [class-and-subclass-declarations]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# For every partial operation, decide consciously whether to trap or to default, and know that a default spends your ability to detect the unforeseen

**Lesson:** Calling a case "undefined" is a way of postponing a decision that will eventually be made by whoever implements the thing, which means it will be made badly and differently in each implementation. The honest alternative is to face each partial operation and choose between two positions. Forbid the case, which obliges the programmer to arrange his program so it cannot arise and obliges the implementation to carry a check that stops the program with a diagnostic when it does. Or supply a plausible standard behavior, which makes the construct easier to use because callers need not test for the awkward situation themselves.

The asymmetry between those two choices is the part worth internalizing. A default is not merely a convenience; it consumes a detection opportunity. It is right exactly when the plausible behavior is the behavior wanted in every situation the designer failed to imagine — and that is a strong claim about situations by definition not yet enumerated. A trap costs the programmer explicit handling and costs the implementation a runtime test, but it converts unforeseen circumstances into reports instead of into quiet wrong answers. The redundancy between an explicit test in the program and the implicit test in the compiled code is not waste; it is the diagnostic, and one can consider retiring it only for code believed to be finished.

The subtler point, and the one that turns this from a slogan into a design technique, is that the two choices interact across a chain of operations. A lenient rule at one step is defensible when a later step is guaranteed to trap the degraded value it produces. If a failed narrowing yields the empty reference rather than an error, and every attempt to read through an empty reference is a hard stop with a message, then the lenient rule has not lost the diagnostic, only deferred it to a point where it is cheaper and just as loud. So the unit of analysis is not the individual operation but the path a bad value can travel: pick your defaults where a downstream checkpoint will catch them, and trap wherever the bad value would otherwise escape into results.

**Source:** [Class and Subclass Declarations](../works/class-and-subclass-declarations.md) — the section on undefined cases, which sets out the two policies and their consequences for debugging, then resolves the paper's own two loose ends in opposite directions while noting that the strict one will ultimately catch most escapes from the lenient one.
