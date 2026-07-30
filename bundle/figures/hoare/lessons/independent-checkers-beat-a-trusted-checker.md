---
type: lesson
title: "You don't have to trust the checker if rival checkers can refute each other"
figure: hoare
works: [the-verifying-compiler-a-grand-challenge-for-computing-research]
axes: [verifiability]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# You don't have to trust the checker if rival checkers can refute each other

**Lesson:** Any tool that certifies other work invites an obvious regress: what certifies the certifier? Treated as a prerequisite, the question stalls the project forever, because establishing the checker to the same standard it enforces is at least as hard as the original problem and has the same regress waiting behind it. The escape is to notice that the regress assumes confidence must flow from a single trusted authority. It does not. If the thing being checked is an artifact that several independently built tools can each examine, then confidence comes from their agreement, and a disagreement is an alarm that points at a real defect in one of them. Nobody has to be trusted; the tools police each other. Self-certification of the checker becomes desirable rather than required, and can be pursued later on its own schedule instead of blocking everything.

For this to work the design has to make cross-examination possible, which is a constraint on interfaces rather than on any one implementation. The claims being checked must be stated in a form that is not proprietary to the tool that checks them, so that a second tool built on entirely different principles can consume the same claim about the same artifact and reach its own conclusion. The moment a checker's judgement is only expressible inside that checker, the whole arrangement collapses back into having to trust it. This is the same reason the interesting property of a proof is that it can be replayed by a skeptic, not that its author is reliable.

The habit generalizes past verification. Whenever a pipeline contains one component whose correctness everything downstream depends on, ask whether the cheaper move is to harden that component or to arrange for a second, differently constructed component to compute the same thing and compare. Independence is doing the work here: two implementations that share a design, a library or an author share their blind spots, and agreement between them proves much less than it appears to.

**Source:** [The Verifying Compiler: A Grand Challenge for Computing Research](../works/the-verifying-compiler-a-grand-challenge-for-computing-research.md) — the statement that the verifying compiler need not itself be verified, together with the Testable and Competitive criteria, which propose that proofs be submitted to rival proof tools for confirmation or refutation.
