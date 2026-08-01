---
type: lesson
title: "What a correctness argument never mentions is what the mechanism is free of"
figure: ullman
works: [mining-of-massive-datasets]
axes: [primitive-count, verifiability, expressiveness]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# What a correctness argument never mentions is what the mechanism is free of

**Lesson:** Machinery invented inside an algorithm tends to stay there, named after the algorithm's purpose, reachable only by someone reading that algorithm. There is a mechanical way to notice when a piece of it is actually a general-purpose component, and it costs nothing: look at the argument that establishes the piece is correct, and list what that argument talks about. Anything absent from the argument is not a precondition. If the proof that a maintenance rule preserves some property never refers to why you wanted the property, never refers to what the enclosing computation does with it, and never refers to the surrounding algorithm's parameters, then the rule solves a problem strictly larger than the one it was written for, and can be lifted out and used elsewhere unchanged.

This is a stronger and cheaper test than the usual one, which is to stare at code and ask whether it feels reusable. Feeling is unreliable because familiarity with the context makes everything look context-dependent. Dependency is a syntactic property of the correctness argument, and reading off what a proof quantifies over is close to mechanical. It also gives you the exact boundary of the extracted component: the things the proof does mention are its interface, and the things it does not are the freedoms callers may exercise.

The payoff is larger than saving an implementation, because a lifted primitive composes with the other pieces of the same system. A mechanism that keeps a bounded uniform sample of an unbounded population, once recognised as independent of what the sample is used for, can be applied to any place in the same system where an unbounded set accumulates — including the output of a different sampling scheme whose per-key sets were growing without limit. Two techniques that each have a known failure of unboundedness turn out to fix each other, and that composition is invisible while both are described as steps of the algorithm that contains them.

The habit worth building runs in both directions. When you write a correctness argument, notice what you did not need; that is the honest scope of what you built and it belongs in the name and the documentation. When you read someone else's, notice the same thing, because it tells you what you may reuse without re-proving anything. The common alternative — generalising a component by imagining future callers — produces the wrong abstraction and an unearned interface, whereas generalising by reading off what the proof ignores produces an interface that is already justified.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the boxed aside in chapter 4 following the moment-estimation algorithm, which observes that the position-maintenance technique developed there actually solves the more general problem of keeping a uniform sample of stream elements, and applies it to cap the number of tuples retained per key by the chapter's earlier key-based sampling scheme.
