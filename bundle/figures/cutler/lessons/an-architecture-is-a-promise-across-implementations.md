---
type: lesson
title: "An interface is a promise about every future implementation, so whatever it leaves unsaid is where incompatibility will grow"
figure: cutler
works: [decwest-sdt-agenda-prism-vs-mips, oral-history-of-david-cutler]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# An interface is a promise about every future implementation, so whatever it leaves unsaid is where incompatibility will grow

**Lesson:** There are two ways to read a specification. One treats it as a description of the thing in front of you, in which case its silences are harmless because you can always look at the implementation to find out. The other treats it as a contract binding every implementation that will ever claim the name, in which case its silences are the most dangerous part of it, because each implementer will resolve them differently and every resolution will be locally reasonable. The observable symptom of the second reading being neglected is a set of supposedly compatible implementations that are all slightly incompatible with each other. Nobody violated the specification; the specification simply did not say, and so a family of products turned into a collection of near-relatives.

Which silences hurt is predictable. They cluster around behavior at the edges of the normal case: what happens when a program modifies the instructions it is about to execute, when a write becomes visible to another processor, when caches must agree, when an exception interrupts something mid-flight and the program has to be resumed. These are exactly the cases an implementer is most tempted to leave to the implementation, because pinning them down constrains the hardware, and exactly the cases the software above cannot avoid depending on. Software written against an unspecified edge is not portable software with a bug; it is software whose correctness argument was never about the architecture at all, only about one machine.

For a designer this produces a concrete discipline. Write the interface as the set of guarantees you are prepared to hold across implementations you have not designed yet, state explicitly what is unspecified so that nobody depends on it accidentally, and treat the appearance of divergence between implementations as evidence that a guarantee was missing rather than that someone misbehaved. And recognize that stability of the contract is itself the value being sold. A well-defined architecture with many compatible implementations protects everything built on it; an architecture that is merely a snapshot of the current silicon protects nothing, and every generation charges the software a migration cost that no one ever budgeted for.

**Source:** [DECwest/SDT Agenda: PRISM vs. MIPS](../works/decwest-sdt-agenda-prism-vs-mips.md) — the hardware-architecture critique and its conclusions, which treat the amount left unspecified or ambiguously specified, and the resulting mutual incompatibility of planned implementations, as a more serious defect than any individual missing feature. Also [Oral History of David Cutler](../works/oral-history-of-david-cutler.md) — his framing of a signed-off architectural specification as the thing hardware and software groups then build independently against.
