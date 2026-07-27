---
type: lesson
title: "A proof method should formalize the argument the programmer already had"
figure: pnueli
works: [the-temporal-logic-of-programs]
axes: [cognitive-load, verifiability]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---

# A proof method should formalize the argument the programmer already had

**Lesson:** There are two ways to judge a verification method. The first asks only whether it is sound and complete — whether every true property is provable in it. The second asks whether the proofs it demands resemble the reasoning by which someone became convinced the program was right in the first place. These come apart badly. A system can be provably complete and still be one in which the natural argument for a concurrent program is impossible to write down, which is a real defect even though no theorem records it. If a method forces you to re-derive your conviction in a foreign shape, the derivation is where mistakes and abandonment happen.

There is a good reason to take the human's argument as the target rather than as a rough draft to be replaced. Somebody wrote the program and believed it correct, and that person could not have enumerated exponentially many interleavings — they had a handful of reasons for structuring it the way they did. Those few reasons are the actual content of the correctness argument. So the job of a proof formalism is to let those reasons be stated rigorously and, in the stating, made conscious; a method whose cost blows up combinatorially has by construction stopped tracking the argument that convinced anyone of anything. Complexity in a proof method is evidence about the method, not only about the program.

This also explains a preference between two ways of establishing that something eventually happens. You can argue negatively, showing that a decreasing measure makes endless or wrong computations impossible, or positively, following a chain of events each of which forces the next until the goal is reached. The second is what people actually do, and it leaves the reader knowing something about how the program works, not merely that no counterexample survives. A programmer who takes this seriously writes down the chain of forced steps behind their design while designing, treats a specification language's inability to express that chain as a fault in the language, and is suspicious of any verification effort whose difficulty far exceeds the difficulty of the belief being verified.

**Source:** [The Temporal Logic of Programs](../works/the-temporal-logic-of-programs.md) — the introduction's second stated trend, toward proof methods approximating a programmer's intuitive reasoning; the comparison of well-founded-set arguments against chains of inevitable events in the survey of proof principles; and the argument in the concurrency section that a human author cannot have considered exponentially many cases, so the method designer's job is to make the author's few guiding reasons rigorous.
