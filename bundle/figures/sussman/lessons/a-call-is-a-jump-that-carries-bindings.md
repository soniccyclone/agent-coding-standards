---
type: lesson
title: "A procedure call is a jump that carries bindings; the stack exists only because you wanted a value back"
figure: sussman
works: [lambda-the-ultimate-imperative]
axes: [primitive-count, hardware-affinity, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# A procedure call is a jump that carries bindings; the stack exists only because you wanted a value back

**Lesson:** Strip a procedure call down and two independent things are happening: control is transferred somewhere else, and some names are bound to some values. Neither of those requires a stack. What requires a stack is the third thing, usually invisible, that happens when a call sits *inside* a larger expression: the caller must remember where to resume and must hold the results of already-evaluated subexpressions while the remaining ones are computed. Those hidden temporaries, not the transfer of control, are what the return-address discipline exists to manage. So a call in a position whose value nobody is waiting for costs exactly what a jump costs, and calling it recursion is a misnomer — nothing recurs, control simply moves, carrying arguments along. Once you see this, a labelled block with jumps and a set of mutually-referencing procedures called in value-free position are the same object written twice, and the "structured versus unstructured control flow" argument turns out to be about surface syntax rather than about machinery.

The consequence is a design rule with unusual reach: keep the two capabilities separate in your head and demand that your implementation not conflate them. A language that allocates stack for a transfer whose value is discarded is retaining information it provably does not need, which is the precise sense in which failing to handle tail calls is a defect rather than a policy. And because bindings can travel with a transfer, a jump can carry state — which is how mutation gets eliminated from a loop. Rather than assigning to a control variable, you transfer to the same code with different bindings. The loop's changing values, which looked like they demanded assignment, were only ever arguments.

The same decomposition explains what a continuation is with no new machinery. If you make the "where to resume" explicit as an ordinary argument, then no subexpression ever needs a temporary, every evaluation becomes trivial, and the order in which arguments are evaluated stops mattering because none of them can have an effect. What was the control stack has been moved into the environment, and the evaluator can be a loop. That is worth knowing even if you would never write in that style: the stack is not a fundamental feature of computation, it is the price of nesting expressions inside each other, and you can always pay it in a different currency.

**Source:** [Lambda: The Ultimate Imperative](../works/lambda-the-ultimate-imperative.md) — the continuations chapter's analysis of what steps a combination in a function body actually implies, where the transfer to the operator is identified as unconditional and the need for temporaries is traced to nested (non-tail) subexpressions; plus the earlier jump and assignment models, in which labels become argument-taking procedures called in value-free position, and the evaluation-order note proving that fully explicit continuation-passing permits a non-recursive evaluator.
