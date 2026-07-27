---
type: lesson
title: "Pick the binding rule that keeps your reasoning laws true, then check the cost model before believing it is expensive"
figure: steele
works: [scheme-an-interpreter-for-extended-lambda-calculus]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Pick the binding rule that keeps your reasoning laws true, then check the cost model before believing it is expensive

**Lesson:** A language must decide what a free variable inside a procedure refers to when that procedure is used somewhere else: the bindings in force where the procedure was written, or the bindings in force where it is applied. This work treats the choice as forced rather than tasteful. If you want the ability to reason about a program by replacing an application with its body, and to rename a parameter without changing meaning, then the procedure must carry the environment it was written in, because the alternative lets an unrelated caller capture a name and break both properties. Renaming freedom and substitutability are not decorations; they are the entire toolkit for reasoning equationally about code, and the binding rule is the price of admission.

The second half of the argument is the interesting part, because it attacks the reason the honest rule was widely avoided. Capturing environments was believed to be slow. The rebuttal is a cost analysis: with this rule the chain of bindings visible at any point is no longer than the nesting depth of the expression being evaluated, which is a fact about the program text and is fixed at compile time — it does not grow with recursion depth or any other runtime quantity. So a variable's position can be computed statically and reached without searching. The perceived expense came from conflating environment depth with dynamic call depth, which the rule itself rules out.

The transferable habit is twofold. First, when a design choice determines which algebraic laws hold over your code, treat the laws as the requirement and derive the choice from them, rather than choosing on convenience and discovering later that you can no longer reason about anything. Second, when performance folklore argues against a construct, reconstruct the cost model explicitly and find which quantity the folklore assumed the cost was proportional to. Often the construct is cheap and the folklore is a fossil of one bad implementation. The programmer who does this reflexively stops trading away verifiability for speed they never measured.

**Source:** [Scheme: An Interpreter for Extended Lambda Calculus](../works/scheme-an-interpreter-for-extended-lambda-calculus.md) — the environments-and-closures discussion, which introduces a closure as a pair of code and environment and then enumerates the consequences of closing in the definition environment, including the bound on environment depth.
