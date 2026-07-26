---
type: lesson
title: "An error whose consequences you cannot explain in the language's own terms has destroyed your ability to reason at all"
figure: dahl
works: [class-and-subclass-declarations, simula-67-common-base-language]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# An error whose consequences you cannot explain in the language's own terms has destroyed your ability to reason at all

**Lesson:** The motivating argument for the whole class mechanism is not reuse and not modeling. It is that a program which interprets storage under a wrong assumption about what lives there has consequences no one can derive: what happens next depends on the compiler's layout choices, the allocator's history, and the machine, none of which the programmer is reasoning in. At that moment the language has stopped being a language. The programmer holds a text whose meaning is not determined by the text, and every subsequent deduction about the program's behavior is unfounded. Debugging becomes search rather than inference, which is why this class of error dominates the cost of building anything large in an environment with explicit pointers and dynamic allocation.

The distinction being drawn is between an error that has a bad outcome and an error whose outcome is outside the vocabulary. A program that computes the wrong number is still an object you can reason about; you can trace it, form a hypothesis, and test the hypothesis with the language's own rules. A program that has read a floating-point field as a pointer has left the domain those rules cover. So the demand placed on the language is a closure property: the set of things a legal program can do must be describable in the terms the programmer thinks in, and the compiler must refuse or trap anything that would break out of that set. Automatic deallocation belongs to the same demand, because a pointer to reclaimed storage is exactly the same failure arriving by a different route, and a language cannot promise the closure property while leaving lifetime management to the programmer's diligence.

Notice what this reframing does to a design conversation. Once the goal is stated as closure rather than as convenience, the cost of a check is weighed against the loss of an entire reasoning method rather than against a few microseconds. It also explains why the checking must be tied to the *reference*, not to the operation: qualification travels with the variable, so the compiler knows statically what a dereference can legitimately mean and can localize the residual runtime discrimination to the few places where the static knowledge genuinely runs out.

A programmer who holds this view sorts failure modes by whether they stay inside the model, and spends the safety budget there rather than spreading it evenly. Undefined behavior, unchecked casts, raw reinterpretation of memory, and use-after-free go in one bucket, to be made impossible or trapped. Ordinary wrong answers go in another, to be handled by tests and types as convenient. The bucket that matters is the one where a failure invalidates every conclusion you would otherwise have drawn from the source text.

**Source:** [Class and Subclass Declarations](../works/class-and-subclass-declarations.md) — the opening argument, which frames protection against meaningless data references as the central idea, and specifically identifies implementation-dependent effects that cannot be determined by reasoning within the language as what makes such errors impractical to chase. Also [SIMULA 67 Common Base Language](../works/simula-67-common-base-language.md), whose introduction lists reference security as one of the three new requirements a language for complex programs has to meet, justified by the debugging burden it removes.
