---
type: lesson
title: "Precompute only what you can also precompute the failure of"
figure: wirth
works: [project-oberon]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Precompute only what you can also precompute the failure of

**Lesson:** Whenever all the inputs to an operation are known before the operation is due to run, there is an obvious saving available: perform it now and keep only the answer. The transformation is normally justified by showing that the result is the same, and that justification is incomplete. An operation has two possible outcomes, a value and a failure, and moving it earlier moves both. The failure now happens in a different place, at a different time, observed by different machinery, reported to a different person, and possibly not suppressible in the setting it has been moved to. If you cannot reproduce the failure behaviour faithfully at the earlier point, the transformation is not a saving; it is a change in what the program does when things go wrong, which is precisely where changes are least acceptable.

This yields a clean test to apply before hoisting any computation: for each way the operation can fail, ask what happens if it fails in the new location. Where the answer is that the failure can be detected and reported as if it had occurred where written, the move is sound. Where the failure would manifest as an uncontrollable event in the machinery doing the hoisting — a trap you cannot mask, an abort in a process that has no business aborting, a signal reaching the wrong handler — the move is unsound regardless of how the successful case compares. Notice that the answer varies by operation kind, not by transformation: the same hoisting is legitimate for one family of operations and illegitimate for another purely because of what their failures do.

Two further points make this practical rather than merely cautionary. First, the sound response to an inapplicable case is usually to decline it, not to build machinery for it, and the decision is worth stating along with its second justification — that the excluded case is rare and its author has a straightforward way to get the same effect by hand. Second, where a failure condition must be detected but the machine's own indication of it is unreachable or non-portable, test the precondition instead of the result: compare the operands against the limits before combining them rather than inspecting a flag afterwards. That formulation depends on nothing but the arithmetic itself, so it works wherever the program is moved — and it is the form that also lets the check be evaluated ahead of time.

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.7's account of code selection, which states that when the operands of an expression are integer constants the operation is performed by the compiler and no instructions are generated, that direct evaluation is also performed for Boolean negation and set union, and that constant expressions are not evaluated for real values because the rare and avoidable case hardly justifies the additional complexity and because overflow traps for floating-point operations cannot be suppressed; together with the accompanying note that overflow tests, though not shown in the listing, can be programmed in a computer-independent form by comparing an operand against the limit minus the other operand before performing the addition.
