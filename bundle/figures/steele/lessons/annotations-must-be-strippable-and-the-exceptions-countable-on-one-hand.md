---
type: lesson
title: "Advice you attach to a program must never change what a correct program means, and the exceptions must be countable on one hand"
figure: steele
works: [common-lisp-the-language-2nd-edition]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Advice you attach to a program must never change what a correct program means, and the exceptions must be countable on one hand

**Lesson:** This specification carries a substantial second language layered on top of the first: a vocabulary for telling the system things it could not work out for itself — which values a variable will hold, which calls to open-code, which of speed, size, safety and compilation time matter here. The rule governing all of it is stated in the first sentence of the chapter and then defended throughout: this vocabulary is optional, and correct advice does not alter the meaning of a correct program. Advice may cause better code, or extra checking, or a warning; it may not cause different behaviour. The specification then names the single construct that violates the rule — the one that changes whether a binding is textual or temporal — flags it explicitly as the exception, and moves on. One exception, called out by name, in a chapter describing a dozen kinds of annotation.

The property that rule buys is that the annotation layer becomes removable. You can delete every annotation from a working program and still have a working program; you can add annotations to a working program without re-testing its behaviour, only its performance. That is what makes it safe for an implementation to ignore whole classes of advice it does not understand, which in turn is what makes advice portable at all — a compiler on a machine where a given hint is meaningless simply drops it. The specification pushes the same logic one level further and provides a way to declare that a name *is* a valid annotation even though this compiler has never heard of it, precisely so that one implementation's advice can travel through another's front end without generating noise. Inertness is the precondition for all of that; the moment a hint can change results, none of it works.

The rule also disciplines the designer, because it forces every proposed annotation to be classified before it ships. Does honouring this change any observable behaviour of a correct program? If yes, it is not advice — it is a feature, and it belongs in the language proper with full semantics, or it does not belong at all. Most of the pressure in real systems runs the other way: a hint that "usually" preserves behaviour is easy to add and hard to remove, and once a few of them exist nobody can tell which subset of the annotations a program actually depends on.

A programmer holding this line keeps configuration, build flags, type hints, and pragmas strictly separated into those that tune and those that decide, refuses to let a tuning knob acquire semantic weight, and treats "this only changes behaviour in the edge case" as disqualifying. The test is concrete and worth applying literally: if stripping every annotation from the source changes what the program computes, the annotation layer has failed and you no longer have two languages, you have one badly documented one.

**Source:** [Common Lisp the Language, 2nd Edition](../works/common-lisp-the-language-2nd-edition.md) — the opening of the declarations chapter, which states that declarations are optional and semantically inert, names the sole exception, and later provides the mechanism for declaring non-standard declaration names so foreign advice can pass through a compiler untouched.
