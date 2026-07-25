---
type: lesson
title: "A classification earns its keep only when its cases differ in what an implementation must do"
figure: cardelli
works: [on-understanding-types-data-abstraction-and-polymorphism]
axes: [cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A classification earns its keep only when its cases differ in what an implementation must do

**Lesson:** Fields accumulate words that sound like they mean something and are used to mean four things at once. The cure is not a better dictionary but a test: propose a division, then check whether the cases force different behaviour from a compiler or a runtime. Applied to the idea of code that serves many types, the test cuts sharply. In one family, a single body of code runs unchanged for an unbounded range of types, which requires uniform representation and permits one compiled copy. In the other, the same name stands for several unrelated bodies chosen by context, or the argument is quietly converted before a single monomorphic body sees it, which means a finite set of implementations, possibly distinct code per case, and a result whose type no longer tracks the input's. Those are different engineering situations wearing one word, and once the test has been applied, claims like "these two languages are both polymorphic" can be assessed instead of merely asserted.

The same test also dissolves distinctions that turn out to be about nothing. Whether a particular mixed-mode arithmetic expression counts as a name serving several meanings or as a silent conversion of one operand cannot be settled from the source text, because it depends on an implementation choice; so the two readings are not describing different phenomena in the program, they are describing different possible compilers. Recognising this is not pedantry. It stops a design argument that has no content, and it flags that any language rule which relies on the distinction is really deferring to an implementation detail.

A programmer who applies this habitually gets two things. Vocabulary that survives contact with implementation, so a design discussion can converge rather than circling. And an early warning system for pseudo-abstraction: when a proposed category does not change what anything does, it is a label, and building structure on it will produce code whose organizing idea cannot be found anywhere in the behaviour.

**Source:** [On Understanding Types, Data Abstraction, and Polymorphism](../works/on-understanding-types-data-abstraction-and-polymorphism.md) — the taxonomy of kinds of polymorphism early in the survey, where each branch is justified by consequences for representation and code generation, and the worked mixed-arithmetic example whose classification is shown to be implementation-relative.
