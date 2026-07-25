---
type: lesson
title: "A verifier that can only say yes is half a verifier"
figure: clarke
works: [model-checking-algorithmic-verification-and-debugging, automatic-verification-of-finite-state-concurrent-systems-using-temporal-logic-specifications, counterexample-guided-abstraction-refinement]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# A verifier that can only say yes is half a verifier

**Lesson:** Most programs, most of the time, are wrong. A method whose only output is a certificate of correctness therefore spends nearly all of its working life producing the answer "no" with no further information, which is close to useless. The corrective is to design the negative answer as a first-class deliverable: when the property fails, hand back an execution trace that exhibits the failure. Clarke's own retrospective assessment is that the importance of this feature cannot be overstated, and that some users adopt the technique purely for it, never caring about the proofs. The original checker did not produce traces; someone added them within two years and no serious tool has shipped without them since.

Two consequences follow, and both cut against the instinct of a proof-oriented mind. First, a diagnostic trace is what makes the method usable by engineers rather than logicians, because it lands in the vocabulary they already work in — a sequence of states — instead of the vocabulary of the logic. That accessibility, not the completeness of the theory, is what drove adoption. Second, and more radically, once counterexamples are the valuable output you can deliberately give up completeness and still ship something excellent. Bounded checking unwinds the system only to a fixed depth and asks a solver whether a failing trace of that length exists. If none does, you have learned very little, since a longer one may exist and computing a sound bound is itself hard. This is enough to find subtle bugs in circuits with thousands of latches in seconds, and the technique became the most widely used variant in industry despite proving nothing when it stays silent.

The same asymmetry powers the refinement loop: an abstraction is worth building not because it can confirm correctness but because when it fails it produces a candidate trace, and that trace is either a real bug or information about the abstraction. Failure carries payload; success carries only a bit.

A programmer who takes this to heart designs every checking mechanism around the quality of its failure output. Assertions that name the violated invariant and dump the state that violated it, type errors that point at the conflicting site rather than the last token parsed, tests whose failure message is a diagnosis. And they stop dismissing incomplete methods: a technique that catches many real defects and proves nothing can be worth more in practice than one that would prove everything if only it terminated.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/model-checking-algorithmic-verification-and-debugging.md) — Clarke's section on model checkers and debugging, which states the primacy of counterexamples and credits their late addition to the original tool, plus the bounded-checking section that trades completeness for bug-finding power. The 1986 paper notes the counterexample facility as a recent, debugging-oriented addition; the CEGAR paper makes the failing trace the engine of the whole method.
