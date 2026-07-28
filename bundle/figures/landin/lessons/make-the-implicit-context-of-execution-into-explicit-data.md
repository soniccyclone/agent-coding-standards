---
type: lesson
title: "To understand a computation mechanically, turn everything implicit about it into named parts of an explicit state"
figure: landin
works: [mechanical-evaluation-of-expressions]
axes: [cognitive-load, hardware-affinity, verifiability, primitive-count]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# To understand a computation mechanically, turn everything implicit about it into named parts of an explicit state

**Lesson:** A rule that says what an expression's value *is* can be stated compactly and recursively, and Landin does state it that way first. But such a rule leans on the reader's own machinery: it says "evaluate this in an environment extended thus" and leaves the act of remembering and returning to human intuition. To make evaluation mechanical, he pins down every piece of context the recursive rule was borrowing and gives it a slot: what has been computed and is waiting to be used, what the free names currently mean, what remains to be looked at, and — the piece people forget — the whole suspended situation to come back to when the current one finishes. With those four parts in hand, evaluation becomes a single-step function from state to state that anyone or anything can apply blindly.

Two consequences fall straight out of the construction, and both are the reason to think this way. First, once state is explicit you can see which parts exist only because of a feature: the environment slot is needed only because expressions may contain free names, and the saved-situation slot only because functions can be applied at all. That gives an honest account of what each language feature costs to run, which no denotational restatement gives you. Second, the same explicitness reveals that a function's value cannot be its text alone. A function body means different things under different meanings of its free names, so the runnable object has to bundle text with the environment it was born in — the reason closures exist is a consequence of the accounting, not a design preference.

The third consequence is methodological. Because the mechanized process is separable from the value it computes, alternatives — evaluating an argument later or never, pre-transforming the expression, partially evaluating a body — can be understood as translations feeding one reference process rather than as rival semantics needing independent justification. Fix one canonical process, and every optimization becomes a claim about a source-to-source transformation preserving what that process computes.

A programmer who works this way debugs and designs differently. Confronted with behavior that makes no sense, the question is not "what does this code mean" but "what is in the state, and which part of the state did I never write down" — the implicit ambient context is where the bug is hiding. Designing a runtime, the same instinct says to enumerate the state components first and let their necessity be argued individually, because each one is real storage that real hardware must hold and real code must maintain.

**Source:** [The Mechanical Evaluation of Expressions](../works/mechanical-evaluation-of-expressions.md) — the move from the recursive definition of an expression's value to the four-component state and its single transition rule, the remark on which components would be unnecessary absent free variables or abstraction, and the closing discussion of other mechanizations as transformations feeding the reference one.
