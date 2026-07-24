---
type: lesson
title: "Treat your own working memory as the binding resource and design down to it"
figure: dijkstra
works: [the-humble-programmer, notes-on-structured-programming]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Treat your own working memory as the binding resource and design down to it

**Lesson:** The scarce resource in programming is not machine time or memory but the programmer's head, and the honest response to that scarcity is to restrict oneself, on purpose, to constructions one can fully reason about. This restriction costs less than it appears: the class of intellectually manageable programs is still rich enough to solve realistic problems, and confining the search to it shrinks the design space so drastically that both finding a solution and trusting it get easier at once. Cleverness inverts this. A trick that squeezes advantage out of an unusual construction spends comprehension, the one budget that cannot be extended, which is why puzzle-mindedness is a liability rather than the mark of a strong programmer.

Scale is the reason modesty is not optional. Differences of a few orders of magnitude are differences in kind: intuitions built on hundred-line programs simply do not transfer to systems ten thousand times larger, and the induction "what I can do once I can do arbitrarily often" is false for human reasoning. Effort need not grow quadratically with program length, but the only mechanism that keeps it near linear is abstraction, deliberately applied: each new semantic level must be precise enough to reason on without reopening the levels below. Abstraction is not vagueness; it is the creation of a new level at which one can again be exact.

A programmer who believes this behaves conservatively in a specific, productive way: familiar structures by default, heightened alertness the moment a construction is unusual for them, and suspicion of any solution whose justification takes longer than seems proportionate, reading that length as a warning about the construction rather than a failure of the prover. Humility here is not an attitude of self-deprecation but an engineering datum: the skull is small, its size is fixed, and designs that ignore a fixed constraint fail.

**Source:** [The Humble Programmer](../works/the-humble-programmer.md) — the arguments for restricting attention to intellectually manageable programs and the closing case that respecting the mind's limits is the precondition for the whole discipline. Also [Notes on Structured Programming](../works/notes-on-structured-programming.md) — the opening sections on our inability to do much and on mental aids: the incomparability of things differing by large factors, the quantitative nature of clarity, and abstraction as the chief tool for economizing enumeration.
