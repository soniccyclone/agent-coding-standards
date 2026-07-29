---
type: lesson
title: "Evaluation-order pathologies are a symptom of substitution, not of laziness"
figure: von-thun
works: [recursion-theory-and-joy]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Evaluation-order pathologies are a symptom of substitution, not of laziness

The classical fixpoint combinator of the lambda calculus is famously unusable under call-by-value: no matter what function it is given, the attempt to reduce it runs away, and a different variant has to be constructed for eager settings. This is normally taught as a fact about strictness — a hazard you accept as the price of eager evaluation. Von Thun shows it is a fact about substitution. In a language with no formal parameters there is nothing to substitute for, so there is no reduction step that can be performed too early. He traces the initial steps of his fixpoint combinator to the point where a doubled quotation is sitting on the stack with the further expansion textually present inside it, and observes that the expansion simply does not happen: a quotation is inert data, and nothing in it runs until a combinator explicitly calls it. The runaway reduction that dooms the eager lambda version has no corresponding step available.

The general principle is that the eager/lazy dichotomy is not fundamental. It arises specifically because expressions get plugged into positions and the language must then decide when the plugged-in thing gets reduced. Remove the plugging and the decision disappears — deferred computation becomes an ordinary value that is inspectable, storable, and transformable, and it runs exactly when something invokes it. There is no strategy to pick and therefore no strategy to get wrong.

The practical version of this is a preference for representing deferred work as data rather than as a property of the evaluator. A pending computation you can hold, examine, pass around, and choose to run is easier to reason about than a promise whose timing depends on where you wrote it and what the surrounding language decided about strictness. It is also why the same idea recurs everywhere it is available: an explicit continuation, a queued command object, a plan the executor later walks. Each replaces a timing question with an ownership question. Von Thun's point sharpens the motivation — you are not trading laziness for eagerness, you are removing the mechanism that made the trade necessary.

**Source:** [Recursion Theory and Joy](../works/recursion-theory-and-joy.md) — the section on evaluation order, which contrasts the failure of the lambda-calculus fixpoint combinator under applicative order with the reduction trace of its Joy counterpart, and pins the difference on quotations never being reduced automatically.
