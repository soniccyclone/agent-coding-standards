---
type: lesson
title: "A total repair always returns something; only good input comes back unchanged"
figure: scott
works: [data-types-as-lattices]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# A total repair always returns something; only good input comes back unchanged

**Lesson:** Scott gives a construction that takes a map defined on part of a space and produces one defined on the whole of it, and then, having proved the result well behaved, adds a single sentence that is easy to read past and should not be. The construction produces a well-behaved result no matter what it is fed, including things that were not well behaved to begin with; but when the input was not well behaved, the output is not an extension of it. It is a perfectly good object. It is simply not related to what you handed over.

Two different guarantees are in play and they are constantly conflated. Totality says the procedure always returns an answer of the right kind. Faithfulness says the answer agrees with the input. A construction can have the first everywhere and the second only on the inputs that already satisfied the condition it was supposed to establish — which is to say, exactly where it was not needed. Anything that repairs, coerces, sanitizes, normalizes, retries, or fills in defaults is a candidate: it is total by design, so it never signals, and the question of whether the result still means what the input meant is a separate property that no amount of exercising the happy path will surface. The characteristic failure is not a crash. It is a well-formed value flowing onward with no relationship to the thing it replaced.

The habit this asks for is to state the faithfulness condition explicitly as its own claim whenever you build something total, and to be clear about its domain — this operation agrees with its argument precisely on inputs already satisfying such-and-such, and on the others it returns a legal value about which nothing is promised. That single sentence is what lets a caller decide whether to check the precondition themselves or to accept a silent substitution. Without it a total operation reads as if it handles everything, and callers reasonably conclude that a lenient interface is a robust one. The two are opposites: leniency is what converts a detectable failure into an undetectable one.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — Appendix A's proof of the extension theorem for Section 1, which establishes that the constructed function is continuous whatever function it is given, and closes with the observation that if the given function is not continuous then the construction cannot be an extension of it.
