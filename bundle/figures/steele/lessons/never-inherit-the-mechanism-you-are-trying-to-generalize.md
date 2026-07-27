---
type: lesson
title: "You cannot implement a mechanism more general than the host mechanism you borrowed to implement it"
figure: steele
works: [scheme-an-interpreter-for-extended-lambda-calculus]
axes: [expressiveness, hardware-affinity, cognitive-load]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# You cannot implement a mechanism more general than the host mechanism you borrowed to implement it

**Lesson:** The tempting way to build an interpreter is to lean on the host language for everything the host already provides: use host procedure calls for interpreted calls, host stack discipline for interpreted control, host interrupts for interpreted interrupts. This work argues that the borrowing silently transfers the host's restrictions into the language you are defining. If the host's control frames must be freed in last-in-first-out order, then the language you build on top of them can only offer control structures that respect that order, and the interesting things you wanted — resumable escapes, coroutines, processes that can be stopped and later continued — become impossible or grotesque. The remedy is deliberate refusal: represent the state of a computation as ordinary inspectable data you own, and step it forward yourself, in the manner of an instruction-fetch loop over explicit registers.

The same argument extends past control into scheduling. Preemption in the host cannot be used directly to preempt the interpreted program, because a host interrupt can land in the middle of a partially updated interpreter state, and the interpreter's own critical regions are then unprotected. The disciplined version is for the host's asynchronous event to do nothing but set one flag, and for the interpreter's own step loop to be the single place that observes the flag and decides to switch. Concurrency thereby becomes something the interpreter grants at points of its own choosing rather than something the substrate imposes at arbitrary points.

What a programmer does differently: before building an abstraction on top of an existing facility, ask whether the facility's restrictions are a subset of the restrictions the abstraction is allowed to have. If you intend to offer something strictly more general than what you are standing on, you must materialize the underlying state rather than delegate to it. This is the same reasoning that decides whether to model a state machine explicitly or to encode it in the call stack, whether to write your own event loop or to reuse threads, whether to represent a workflow as data or as a chain of nested function calls. Delegation is cheaper right up to the point where you need a behavior the delegate cannot express, and then it is a rewrite.

**Source:** [Scheme: An Interpreter for Extended Lambda Calculus](../works/scheme-an-interpreter-for-extended-lambda-calculus.md) — the implementation-issues discussion of frames and the "think machine language" framing of the interpreter's main loop, plus the treatment of how the alarm-clock signal is allowed to interact with the interpreter's registers.
