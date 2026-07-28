---
type: lesson
title: "Treat a function as the rule you can run, not as the pairs it happens to relate"
figure: church
works: [the-calculi-of-lambda-conversion, an-unsolvable-problem-of-elementary-number-theory]
axes: [primitive-count, expressiveness]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Treat a function as the rule you can run, not as the pairs it happens to relate

**Lesson:** There are two incompatible ways to say what a function is. One says it is a correspondence between two domains fixed in advance, so the domain exists before the function does. The other says the operation comes first and its domain is discovered afterward as the set of things the operation happens to accept. The second choice looks like a technicality and is actually the hinge on which an entire computational worldview turns, because only under it can an operation be handed itself as input. If domains must precede functions, self-application is incoherent by construction. If the rule precedes its domain, self-application is merely a question about whether the rule happens to work on that particular argument.

That single decision is what lets a formalism with two operations, building a rule and running a rule, reach universality without a stack of extra machinery. Every derived capability that follows, arithmetic, recursion, encoded data, self-reference, comes from the fact that the operation of application is total in its ambition and partial only in its outcome. Nothing is stratified out of reach in advance, so nothing needs a special escape hatch later. The price is that some applications produce nothing useful, and that price shows up honestly as computations without an answer rather than as a term the syntax quietly forbade.

A programmer who holds this view stops treating a first-class function as an advanced feature and starts treating it as the baseline. Higher-order code stops needing a justification. More importantly, the programmer stops trying to buy safety by making everything a member of a pre-declared universe, and starts asking a sharper question: given that the operation and its argument are the same kind of thing, which invariants do I actually need enforced, and what am I willing to pay for each one. That question is answerable; the reflex of forbidding whole shapes of program because they look circular is not.

**Source:** [The Calculi of Lambda-Conversion](../works/the-calculi-of-lambda-conversion.md) — the opening chapter's discussion of what a function is and why nothing prevents a function's own argument range from containing itself, together with the well-formedness rules that follow in the next chapter and their reuse in [An Unsolvable Problem of Elementary Number Theory](../works/an-unsolvable-problem-of-elementary-number-theory.md).
