---
type: lesson
title: "State the part of the contract the signature cannot carry, at the definition"
figure: naur
works: [revised-report-on-the-algorithmic-language-algol-60]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# State the part of the contract the signature cannot carry, at the definition

**Lesson:** A parameter list is a lower bound on what a routine depends on and an upper bound on what it declares. The gap between the two is where callers get hurt, so treat closing that gap as part of writing the routine, not as optional commentary. Three things reliably live in the gap. Names the body reaches for that are not parameters: state them, by name, as entering the routine from outside, because a reader tracing the parameters alone will conclude wrongly that the routine is self-contained. Constraints on the argument values that the type system cannot express — which argument is an input, which is a result, what governs the accuracy of the answer — because a list of same-typed arguments tells the caller nothing about which direction each one flows. And the intended shape of the computation, in enough detail that the caller can tell whether their problem is the one this routine solves.

The third item in the gap is the one people never write down: the protocol across calls. If a routine behaves differently on a first or isolated invocation than on a continuation of a sequence, and the difference is signalled by an argument the caller sets, then the meaning of that argument is a rule about the *history* of calls, and no signature can hold a rule about history. Say it explicitly: this flag must hold on a first or isolated entry; on subsequent entries in a chain it may be cleared, and clearing it is what buys the saving. The caller now understands that they own a sequencing obligation. Stateful routines are not the problem — hidden sequencing obligations are, and the fix is a sentence at the definition rather than an architecture.

The last piece of the contract is epistemic, and it is the most useful and least common. Say what standing the artifact has. If a piece of code embodies a technique you have reasoned about but never run, say that it may not be optimal in time or in rounding behaviour and that it has not actually been executed on a machine. This costs the author some pride and saves every reader from mistaking a worked illustration for a validated component. A specification's examples are especially prone to this confusion, because appearing in an authoritative document reads as endorsement; the discipline is to attach the artifact's provenance and test status to the artifact, so that the reader's confidence is calibrated by the author rather than by the venue.

**Source:** [Revised Report on the Algorithmic Language ALGOL 60](../works/revised-report-on-the-algorithmic-language-algol-60.md) — the examples of procedure declarations at the end of the report: the inner integration step whose commentary names the identifiers that enter it as non-local entities and marks that fact important; the enclosing routine whose commentary enumerates each parameter's role as input, order, tolerance or output, states that a further routine is required as a non-local identifier, and specifies that its Boolean argument must be true on an isolated or first entry while later calls in a sequence may pass false; and that example's footnote disclaiming optimality with respect to computing time and round-off and stating that the program had never been run on a computer.
