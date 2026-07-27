---
type: lesson
title: "When an abstraction is expensive, the defect is in the implementation; do not teach programmers to hand-compile around it"
figure: steele
works: [lambda-the-ultimate-declarative]
axes: [hardware-affinity, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# When an abstraction is expensive, the defect is in the implementation; do not teach programmers to hand-compile around it

**Lesson:** A construct acquires a reputation for being slow, the reputation hardens into advice to avoid it, and the advice gets taught as a programming technique. This work attacks that cycle at its root using the most reputationally damaged construct available at the time — the procedure call — and shows the cost was an artifact of how calls were being translated, not of what a call means. A call whose result is the caller's own result needs no bookkeeping at all; the caller's own destination can simply be inherited. Once translation happens that way, a chain of calls compiles into a loop, and code written with the general construct comes out the same as code written with a special-purpose one. The same argument then runs on a construct that looks far more expensive — data represented as a procedure that answers requests about itself — and shows that ordinary optimizations already in the literature, inlining plus constant folding plus dead-code elimination, reduce a field access through such a representation to the single machine instruction the hand-written version would have used.

The polemical edge of the argument is aimed at a specific failure the work found in the contemporary literature: a paper that documented large speedups from hand-transforming procedure calls into jumps with explicit stack manipulation, and then recommended teaching the transformation to programmers rather than putting it in the compiler. That inverts the point of having a high-level language. Every such recommendation converts a one-time implementation cost into a permanent tax on everyone who writes the code, and it does so in the least reviewable place, spread through application logic where nobody can later tell which contortions are algorithmic and which are compensation for tooling.

The habit this leaves a programmer with is to route performance complaints to the layer that can absorb them once. When the abstraction that expresses the intent clearly turns out to cost more than the awkward version, treat that gap as a defect in the compiler, runtime, library, or query planner, and check whether it can be closed there before deforming the source. The same reasoning argues for making the shared substrate small and general rather than machine-shaped: a translation layer built from the primitive control and naming operations can serve many surface languages and many targets, turning a multiplicative pile of special-purpose translators into an additive one, whereas the historically failed attempts at such shared layers failed by sitting too close to a particular machine and thus too far from what the source languages actually meant.

**Source:** [Lambda: The Ultimate Declarative](../works/lambda-the-ultimate-declarative.md) — the compilation walkthrough of an iterative procedure into a loop, the optimization of procedurally represented data down to a single instruction, and the note collecting contemporary evidence and criticism about procedure-call cost.
