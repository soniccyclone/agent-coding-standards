---
type: lesson
title: "Failure paths belong to the interface, and they stop at your immediate caller"
figure: liskov
works: [clu-reference-manual]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Failure paths belong to the interface, and they stop at your immediate caller

**Lesson:** Most treatments of failure make two choices that look convenient and cost a great deal. The first is to leave the ways a routine can fail out of its declared interface, so a caller learns them from documentation, folklore, or a crash. The second is to let a failure travel arbitrarily far up the call chain, landing wherever somebody happened to install a catcher. Both choices break the property that makes modular reasoning possible — that you can understand a component from its stated interface alone — because the failure behavior is either unstated or is a conversation between two components that know nothing about each other.

The disciplined alternative declares the failure conditions alongside the results in the interface, each with its own name and its own payload types, so a caller can see the complete set of ways an invocation can turn out and the compiler can check that each is handled coherently. Then the failure goes exactly one level: to the code that made the call, which is the only code that has the context to decide what to do. A component that cannot cope with a failure it receives does not shrug and let it fly past; it converts the failure into something meaningful in its own vocabulary and reports that to its own caller. The names may even repeat at each level while the meaning and the accompanying data change, because each level describes the situation in the terms its clients understand.

Requiring that every possible failure be handled at every call would be too strict — a caller frequently knows from context that a given failure cannot occur, and forcing ceremony there is noise. The resolution is not to make the requirement optional but to make the default loud: an unhandled failure is not silently passed along, it is converted into an unmistakable general failure with an explanatory payload. So the cost of skipping a handler is a clear, attributable collapse rather than a quiet escape into somebody else's problem.

A programmer who believes this writes the failure modes into the signature and treats a fresh failure kind as an interface change. When a call can fail in a way they cannot handle, they translate rather than re-throw, and they never rely on a distant catcher to know what to do about something it did not initiate. Silent propagation is the thing to eliminate: either handle it, or restate it in your own terms, or fail loudly and be identified as the failure's origin.

**Source:** [CLU Reference Manual](../works/clu-reference-manual.md) — the exception-handling section, which puts signalled conditions in every routine heading, restricts a signal to the immediate caller, supplies an implicit handler that converts anything unhandled into an explicit general failure, and works an example where each level restates lower-level exceptions in its own terms.
