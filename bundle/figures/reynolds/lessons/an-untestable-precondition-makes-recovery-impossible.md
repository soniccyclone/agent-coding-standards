---
type: lesson
title: "An operation that aborts on a condition the caller cannot test has no correct use"
figure: reynolds
works: [the-craft-of-programming]
axes: [expressiveness, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# An operation that aborts on a condition the caller cannot test has no correct use

**Lesson:** Consider an operation with a precondition it enforces fatally — call it when the condition does not hold and the whole computation is killed with a diagnostic — and no companion operation that reports whether the condition holds. Such an interface cannot be used correctly except by callers who happen to know the answer from somewhere else entirely. Any consumer processing an unknown quantity of input is now obliged to be told the count out of band, or to guess. The defect is not the abort; aborting on a violated precondition is defensible and often right. The defect is that the precondition is unobservable, so no caller can arrange to satisfy it.

Stated as a rule for interface design: every precondition you enforce must be one the caller can establish, which means either it follows from something the caller already did, or you expose a way to find out. A predicate that reports the state, an operation with a distinguishable outcome rather than a fatal one, a variant that returns a sentinel — the specific mechanism does not matter much, and each has different composition properties. What matters is that the caller has *some* route to the information. Where you find yourself unable to expose it, that is usually evidence that the underlying model is missing a concept, not that the caller should be more careful.

The general test is worth applying to your own interfaces as a matter of routine, because this class of defect is invisible from the implementation side. Take each way the operation can refuse or fail, and ask what a caller who wanted to avoid that outcome would have to do. If the honest answer is "there is nothing they could do", you have written something that only works when the world cooperates, and the failure will surface as an abort in a component that did nothing wrong. That is worse than a wrong answer, because a wrong answer at least leaves the caller in a position to notice and respond.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Appendix C.1's description of Algol W input, which states that a program attempting to read beyond the end of the input deck is terminated with an error message, and notes as regrettable that there is no way within a program to test whether the input has been exhausted; the same section flags the variant read operation that advances to a card boundary before its first item as inadvisable because of its potential to skip data items inadvertently.
