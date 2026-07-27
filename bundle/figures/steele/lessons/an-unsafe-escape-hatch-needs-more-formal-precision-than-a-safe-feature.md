---
type: lesson
title: "The features that move a proof obligation onto the programmer are the ones that need the most formal precision, not the least"
figure: steele
works: [common-lisp-the-language-2nd-edition]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming, formal-methods-and-verification]
tags: [lesson]
---
# The features that move a proof obligation onto the programmer are the ones that need the most formal precision, not the least

**Lesson:** Buried in the declarations chapter is an annotation that lets a programmer promise the system that certain objects will not outlive the construct that made them, so that storage for them can be taken from a stack rather than the heap. It is a pure performance escape hatch, it is unsafe, and violating it can corrupt the storage system itself. The striking thing is how the specification handles it: with far more formal machinery than it spends on ordinary features. It defines an auxiliary relation — one object being reachable only through another — in explicit terms, states the guarantee as a quantified assertion over the sequence of values the variable takes during one execution, and then works through five worked cases of code that violates it. Three of those cases look correct and are not, each for a subtler reason than the last; one of them turns on the fact that a returned value is briefly live even though the program discards it immediately; and the final example demonstrates that whether a particular use is legal can depend on whether the implementation treats small integers as identical objects, which means the only portable conclusion is the conservative one.

The reason this is the right allocation of rigour is that the mechanism has no runtime to fall back on. For a checked feature, an imprecise specification is annoying: someone writes wrong code, something signals, they fix it. For an unchecked promise, an imprecise specification is unusable, because the programmer's only tool is the text of the guarantee. Every case the specification does not resolve becomes a case where a programmer will guess, and guessing wrong produces a corrupted heap rather than an error message. So precision here is not academic tidiness; it is the entire safety mechanism, and the worked negative examples are not illustration, they are the specification.

The second half of the treatment is a judgement about audience, delivered without hedging: the author states outright that he does not encourage casual use, while noting that the people who asked for the feature have already accepted the debugging pain. That is a legitimate design position and one most systems avoid taking. A feature can be correctly specified, genuinely valuable, and still be something you tell most of your users not to touch — and saying so is more honest than either omitting it or presenting it as ordinary.

A programmer with this instinct spends their specification effort inversely to how much the runtime will catch. The interfaces that get the terse documentation should be the ones that check their own preconditions; the ones that trade a check for speed — unchecked casts, manual lifetime management, lock-free structures, anything marked unsafe — deserve a written-out contract, adversarial examples of near-miss misuse, and an explicit statement of who the feature is for.

**Source:** [Common Lisp the Language, 2nd Edition](../works/common-lisp-the-language-2nd-edition.md) — the treatment of the dynamic-extent declaration in the declarations chapter: its formal definition in terms of otherwise-inaccessible parts, the sequence of counterexamples culminating in the one that depends on implementation-defined object identity, and the closing warning about who should use it.
