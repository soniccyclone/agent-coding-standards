---
type: lesson
title: "Compare two implementations by implication between their contracts, and read the difference as the calls that distinguish them"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, expressiveness]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Compare two implementations by implication between their contracts, and read the difference as the calls that distinguish them

**Lesson:** Two components claiming to do the same job are usually compared by inspecting their bodies, which tells you very little, or by benchmarking, which tells you about speed and nothing about substitutability. The informative comparison is between the statements of what they guarantee. If one component's contract implies the other's, then every call the second serves correctly the first also serves correctly, and you may swap it in without auditing a single call site. If neither implies the other, they are not interchangeable however similar their code looks, and the question is which uses each one covers.

The residue is where the value is. When one contract strictly implies the other, the part of the stronger one that the weaker cannot derive is an exact description of the calls that work with the better implementation and fail with the worse — not a vague "handles more cases" but a statement you can check a call site against. In the classic instance, a parameter-passing discipline that copies arguments in and out survives being handed the same variable twice, while one that substitutes textually does not; the stronger contract's extra content is precisely the family of aliasing calls, and reading it tells you which existing calls would break if you switched back.

Getting contracts into a form where this comparison is possible imposes one requirement worth naming: a postcondition must be phrased in terms of quantities the caller can still refer to when the call returns. A guarantee stated about something the callee copied and discarded is unusable, because the caller has no way to evaluate it afterwards; the useful form relates the result to values as they stood at entry, which needs names for those values that the code itself cannot disturb. That reformulation looks like pedantry until you try to compare two contracts, at which point it is the thing that makes the comparison mean anything — and it is also the thing that makes the contract survive being handed arguments that overlap.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 3.3.9's third example, a factorial procedure using call by value and result, which yields procedure assumptions stronger than the previous two examples because the procedure still behaves correctly when its parameters interfere, notes that expressing this extra strength requires ghost identifiers and parameters, explains that a caller has no access to the by-value parameter's final value and therefore no interest in a guarantee about it but does care that the result is the factorial of the value held before execution, has the reader verify that the stronger assumptions imply the earlier ones so the procedure behaves correctly whenever they do, and then exhibits the instance that the stronger assumptions additionally yield — the aliased call that characterizes exactly the kind of call which would not behave correctly under call by name.
