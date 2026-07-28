---
type: lesson
title: "Waiting for the answer is what creates the dependency"
figure: saltzer
works: [the-multics-kernel-design-project]
axes: [verifiability, parallelizability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Waiting for the answer is what creates the dependency

**Lesson:** It is tempting to think that invoking something is what makes you depend on
it, so a lower component that needs a higher one to act is stuck in a cycle. Look closer
and the coupling comes from a narrower thing: the caller has left state behind — a
suspended frame, a held resource, unfinished business — and its own correctness now
requires the callee to come back and behave. Remove the expectation of return and the
relationship changes character entirely. Transfer control upward along with everything the
recipient needs, keep nothing pending, and the lower component's correctness no longer
rests on what happens next. It has handed the problem off rather than delegated it.

This is a sharper tool than it first appears, because it separates two things that get
conflated in every discussion of layering: direction of control flow and direction of
dependency. Control is allowed to go anywhere. Dependency is what must stay acyclic. A
handoff sends control up while leaving the dependency arrow pointing down, which is
precisely the trick needed for conditions that are noticed at the bottom of a system but
can only be resolved at the top. The general design of asynchronous notification,
message queues between levels, event-based signalling, and continuation-style transfer all
buy the same property, and it is worth knowing that this is the property they buy, rather
than reaching for them out of fashion.

There is a cost that has to be paid honestly. A handoff gives up the convenient fiction
that the operation will resume where it left off with everything intact. The recipient has
to be given enough context to make sense of the situation, and after it acts, the original
activity typically has to be restarted rather than resumed — which means the operation must
be safe to attempt again. That requirement is the real price, and it is the same
requirement that makes systems recoverable, so it is usually worth paying anyway.

A programmer who holds this distinction stops treating "lower code must not invoke higher
code" as the rule, and instead asks, at each upward transfer, whether anything is left
pending across it. Where nothing is, the structure is intact. Where something is, they
have found a real cycle wearing the disguise of a helpful callback.

**Source:** [The Multics Kernel Design Project](../works/the-multics-kernel-design-project.md)
— the treatment of upward signalling, in which one class of dependency loop is broken by
a mechanism that transfers control and arguments to a higher-level manager without leaving
activation records or unfinished work behind, followed by restart of the original activity;
also the real-memory queue used to carry events from the lower to the upper level of the
two-stage process implementation.
