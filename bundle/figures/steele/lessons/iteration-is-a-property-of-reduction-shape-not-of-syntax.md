---
type: lesson
title: "Judge a control structure by how its state grows, not by whether the code appears to call itself"
figure: steele
works: [scheme-an-interpreter-for-extended-lambda-calculus]
axes: [cognitive-load, hardware-affinity, primitive-count]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Judge a control structure by how its state grows, not by whether the code appears to call itself

**Lesson:** Programmers usually classify code as recursive or iterative by looking at its surface: a procedure whose body mentions its own name is "recursive," a construct with a loop keyword is "iterative," and folklore then attaches a cost story to each label — recursion consumes stack, loops do not. This work replaces the surface test with a semantic one. Trace the computation as a sequence of rewrites and watch how large the intermediate expression gets. If the sequence settles into a cycle of expressions of bounded size that differ only in the numbers they carry, the computation is iterative no matter what the source text looks like. If the sequence grows a chain of pending work proportional to depth, it is recursive even when written in a style that superficially looks like a loop — continuation-passing being the sharpest example, since it looks flat but accumulates nested continuations holding exactly the information a return-address chain would have held.

Why does this hold? Because the space a computation needs is a property of what state must survive across a step, not of which keyword introduced the step. A call whose result is immediately the answer of the enclosing call has nothing pending to remember, so nothing needs saving; a call whose result must still be multiplied by something has that multiplication pending, and the pending part has to live somewhere. The syntactic label is a proxy for this that happens to be wrong in both directions.

A programmer who believes this stops using recursion-versus-iteration as a proxy for cost and instead asks, at each call site, what is still outstanding after the callee returns. That question is answerable by reading code, and it predicts memory behavior correctly across languages, whereas the syntactic label does not. It also changes what one demands of a language implementation: if the shape of the reduction is what determines space, an implementation that spends a frame on a call with nothing outstanding is losing information-free space, and that is a defect in the implementation rather than an inherent tax on the abstraction. This is what makes a language with only procedure application, and no loop construct at all, an honest way to express iteration — the small primitive basis loses nothing.

**Source:** [Scheme: An Interpreter for Extended Lambda Calculus](../works/scheme-an-interpreter-for-extended-lambda-calculus.md) — the substitution-semantics section, which traces three different factorial definitions step by step and compares how the intermediate expressions grow, then the control discussion that ties expression growth to when the interpreter must build a frame.
