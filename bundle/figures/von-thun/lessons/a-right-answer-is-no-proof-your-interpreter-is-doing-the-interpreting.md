---
type: lesson
title: "A right answer is no proof your interpreter is doing the interpreting"
figure: von-thun
works: [a-joy-interpreter-written-in-joy]
axes: [verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# A right answer is no proof your interpreter is doing the interpreting

When you re-implement an evaluator on top of the very system you are modelling, the naive handling of any construct that takes a program as an argument produces the right answer for the wrong reason. You dispatch on the higher-order operator, then hand its program argument straight to the host's version of that operator. Every test passes. Nothing has been defined. The host recursed, not you, and your evaluator is a pass-through wearing the costume of a definition. Von Thun flags exactly this case in his own draft and labels it wrong even while conceding it computes correctly — the sharpest possible statement that behavioural agreement is not the property being sought.

The property actually being sought is that control re-enters *your* evaluator at every nested position where a program appears. Getting there is a mechanical discipline: before invoking the host's higher-order operator, rewrite each of its program arguments so that it invokes your evaluator on itself. Arity is the only thing that varies; a family of small helpers, one per number of program arguments, absorbs the repetition. Once that rewrite is in place, the recursion is genuinely yours, and the interpreter's semantics are what determines nested behaviour rather than merely agreeing with it.

The generalisation reaches far past metacircular interpreters. It covers any shim, proxy, adapter, compatibility layer, or "reimplementation" that sits above the thing it claims to replace. A test suite comparing outputs cannot distinguish a layer that implements the semantics from a layer that forwards to something that already did. The distinguishing test is structural, not behavioural: trace whether your code is on the stack at every recursive descent, or verify by starving the layer of the host facility it might be leaning on. A programmer who internalises this stops treating a green suite as evidence of coverage in exactly the situation where the substrate can silently supply the answer, and instead asks which component the correctness is actually coming from.

**Source:** [A Joy Interpreter Written in Joy](../works/a-joy-interpreter-written-in-joy.md) — the sequence where von Thun writes the combinator dispatch cases the obvious way, marks them wrong despite their working, and replaces them with the arity-indexed rewrite that threads the interpreter into each quoted program argument.
