---
type: lesson
title: "Test whether a contract says enough by letting an adversary rewrite the state within it"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Test whether a contract says enough by letting an adversary rewrite the state within it

**Lesson:** There is a mechanical way to find out whether a description you have written at some interior point of a system is strong enough, and it does not require reading the surrounding code again. Freeze execution at that point. Let a hostile agent replace the entire state with any other state whatsoever, subject only to the one restriction that the description you wrote still holds of the replacement. Then resume. If nothing the adversary can substitute produces a wrong answer, your description carries all the information the rest of the computation actually depends on, and it is adequate. If some substitution does produce a wrong answer, then the real program was relying on something true at that point that you failed to write down, and you now have a concrete example of the missing clause.

What makes this test worth internalizing is that it converts an open-ended question — "is this comment, this precondition, this interface documentation sufficient?" — into a search for a counterexample, which is the kind of question people are good at. It also sharpens what adequacy means. A description is not adequate because it is true, and not adequate because it mentions the variables that happen to appear nearby. It is adequate exactly when it pins down every fact downstream code consumes, so that all states satisfying it are interchangeable as far as the rest of the computation can tell. That is the same criterion an abstraction boundary has to meet, and the adversary is just a way of asking whether the boundary leaks.

The test comes in two strengths, and the difference is instructive. Run it asking only whether the adversary can force a wrong result and you have checked adequacy for correctness. Run it asking additionally whether the adversary can force the computation never to finish — he is allowed to make it take longer, that is not a violation — and you have checked adequacy for termination as well. A description can easily pass the first and fail the second, because bounds and ranges that no correctness step needs are exactly what the progress argument runs on. Whenever you write down what holds at a boundary, decide which of the two questions you are answering, because a contract sufficient to keep answers right can still leave a caller hanging forever.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — the discussion following the flowchart verification conditions, in which adequacy of an assertion is defined by halting the computation at the corresponding arrow, allowing a demon to alter the state arbitrarily within the assertion, and then asking whether the demon can spoil the result or prevent termination.
