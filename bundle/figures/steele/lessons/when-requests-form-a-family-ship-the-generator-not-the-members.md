---
type: lesson
title: "When every feature request is individually justified and collectively impossible, the requests are a family and you should ship its generator"
figure: steele
works: [growing-a-language]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# When every feature request is individually justified and collectively impossible, the requests are a family and you should ship its generator

**Lesson:** This work stages a decision procedure rather than stating it, and the staging is the argument. Steele walks through a sequence of requests for built-in numeric types: complex numbers, rationals, intervals, a wildly obscure kind of number from combinatorial game theory, vectors, matrices. For each he supplies the arithmetic and an honest estimate of the constituency, which ranges from a substantial minority down to about three people worldwide. For each he asks whether it should be a language type. And he concedes that considered one at a time he would say yes to every one of them, while considered together he must say no to all of them, because the aggregate would burden every programmer with vocabulary belonging to somebody else's niche.

The escape is visible only once the requests are laid side by side, and it is visible because they are laid side by side. Every item on the list has the same shape: a small tuple of numbers, plus rules for adding and multiplying, wanted by people who expect to write those operations with the notation ordinary numbers get. That common shape is the real object of design. Grant the shape — a way to define lightweight aggregate types with user-supplied operators and parametric containers — and every member of the family becomes something a few interested people build once and publish, available to those who want it and invisible to everyone else. Steele states the payoff as an exchange rate: growing the language along a few carefully chosen dimensions removes the need to grow it along a hundred others, because the users take over the rest of the work.

The reasoning generalizes past languages to any system with a request queue. A backlog of individually reasonable, jointly unaffordable requests is diagnostic information, not a prioritization problem. Sort the requests by shape rather than by importance or by who asked, and look for the isomorphism class with the most members. If you find one, the correct build is not the top-ranked request but the mechanism that makes all of them unnecessary — and the test of whether you got the mechanism right is whether the resulting user-built version is as good to use as the built-in one would have been. If it is worse, you have not solved the problem, you have declined it while appearing to solve it.

The discipline also tells you which requests to grant directly. What survives is the vocabulary genuinely common to everyone, plus, as Steele suggests, one or two members of the family shipped as worked examples so that people can see how the mechanism is meant to be used. A programmer who works this way keeps the shared core small on purpose, and treats every accepted special case as evidence that a generator was missed.

**Source:** [Growing a Language](../works/growing-a-language.md) — the run of candidate numeric types and their arithmetic, the admission that each answer is yes and the collective answer must be no, and the conclusion that a few growth-enabling additions remove the need for a hundred specific ones.
