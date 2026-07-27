---
type: lesson
title: "A jump is a call whose value nobody wants, and a loop variable is a parameter, so control flow and data flow are one mechanism"
figure: steele
works: [lambda-the-ultimate-imperative]
axes: [primitive-count, expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# A jump is a call whose value nobody wants, and a loop variable is a parameter, so control flow and data flow are one mechanism

**Lesson:** Two constructs that every language keeps separate turn out to be the same construct seen from different sides. A jump to a label is what remains of a procedure call once you delete the expectation of a returned value: control transfers unconditionally and nothing is left pending. Conversely, a procedure call in a position where the caller does want the value is a jump plus an obligation to come back, and that obligation is the only reason any storage is needed. This reframing dissolves the ordinary hierarchy in which jumps are cheap machine-level things and calls are expensive language-level things — they differ by exactly one bit of information about whether a value is wanted.

The second half is what makes the identification useful rather than cute. A label is not merely a jump target; make it a procedure and it can take arguments, and then the variables that a loop assigns to on each pass become parameters supplied at each transfer. A block full of labels, gotos, and assignments to shared variables rewrites into a family of mutually referring procedures that call one another with updated values and never assign to anything. The mutation was never essential; it was a consequence of labels not being able to take arguments. What was a set of variables silently changing under a reader's feet becomes a set of values explicitly handed from one step to the next.

The consequence for a working programmer is a reliable rewrite in both directions. Any state machine expressed with a mutable state variable and a dispatch loop can be expressed as procedures that transfer to one another with their state as arguments, and the rewritten version has no shared mutable variable to reason about — each step's inputs are visible in its signature, which is exactly what makes a step's invariant statable. It also settles the language-design question honestly: a language that handles value-free transfers without accumulating bookkeeping does not need a jump construct, because it already has one, and a language that lacks such transfers is retaining information the program cannot possibly need.

**Source:** [Lambda: The Ultimate Imperative](../works/lambda-the-ultimate-imperative.md) — the imperative-programming section's transformation of a labeled block with assignments into mutually recursive parameterized procedures, and the continuations section's argument that a tail position is better understood as a transfer than as a recursion.
