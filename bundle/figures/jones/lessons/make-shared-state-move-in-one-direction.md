---
type: lesson
title: "Constrain shared state to move in one direction, and a stale read becomes merely conservative"
figure: jones
works: [tentative-steps-toward-a-development-method-for-interfering-programs]
axes: [parallelizability, verifiability]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# Constrain shared state to move in one direction, and a stale read becomes merely conservative

**Lesson:** The reason shared mutable state is frightening is that a value read a moment ago may now be anything at all, so nothing derived from it survives. Two disciplines together remove the fear without removing the sharing. First, require that the value only ever move one way along some ordering. Second, require that every value it is ever set to be already justified — a fact about the world rather than a step in someone's private calculation. Under those two rules a reader holding an out-of-date copy is not holding a wrong value, it is holding a weaker true statement than the current one, and a computation whose correctness only needs the weaker statement continues to be correct.

What this buys is that the frequency of communication drops out of the correctness argument. A participant may consult the shared value on every step, or once at the start, or never; the results differ in how much wasted work is done, not in whether the answer is right. Performance tuning is then completely decoupled from verification, and the same design admits a spectrum of implementations from maximally chatty to fully independent — including, at one extreme, the plain sequential program as a degenerate member of the family. When you find that a design's proof is sensitive to how often participants synchronize, that is a sign the shared value has not been given a direction and a justification obligation; when the proof is insensitive, you have earned the right to tune freely afterwards.

The obligation on writers is what makes it work and is the part usually skipped. Monotonicity alone is not enough: if a writer may lower a bound to a value it has not yet established is legitimate, then a reader that trusts the bound is trusting an intermediate step of somebody else's reasoning. Write-visible state must therefore only ever pass through states that are meaningful to an outside observer, which in practice means a participant does its speculative work privately and publishes only conclusions. That is the same rule that makes a data type invariant worth having, applied to the timeline instead of the type: never let the outside see a state you would not be willing to defend.

**Source:** [Tentative Steps Toward a Development Method for Interfering Programs](../works/tentative-steps-toward-a-development-method-for-interfering-programs.md) — the parallel development of the least-satisfying-index search, where the searchers rely only on the shared bound decreasing and guarantee that any change both lowers it and lands on a genuinely satisfying index; and the accompanying remarks that tasks are free to consult the bound less often than once per index and that the sequential program of the earlier section is a special case of the multi-task solution.
