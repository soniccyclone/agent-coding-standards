---
type: lesson
title: "When a requirement is stated in words nobody can check, replace it with a test that has an outcome"
figure: turing
works: [computing-machinery-and-intelligence]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# When a requirement is stated in words nobody can check, replace it with a test that has an outcome

Some questions cannot be settled because the terms in them have no agreed referent. The productive move is not to argue the definitions into shape, and not to poll people about how they use the words, but to substitute a different question — one whose terms are already unambiguous and whose answer is produced by running something rather than by reasoning about meanings. The substitution is a deliberate loss: the new question is not the old one, and anybody is free to complain that it misses the point. That complaint is cheaper to handle than an unbounded semantic dispute, because it can be answered on the merits of the substitute once the substitute is on the table.

The reason this works is that a good substitute question fences off the part of the disagreement that was never going to resolve. Choosing an interaction channel narrow enough to exclude everything irrelevant, and a pass criterion stated as a rate rather than an absolute, converts an argument about essences into a measurement with an error bar. The channel restriction is not a limitation to apologize for — it is what makes the measurement mean anything, because it settles in advance which evidence counts. Objections then arrive as concrete claims about the test rather than as claims about the concept, and concrete claims about a test can be examined one at a time.

A programmer who has internalized this stops accepting acceptance criteria written in unfalsifiable adjectives. Faced with a demand that a system be intuitive, robust, or intelligent, the response is to propose an observable protocol whose outcome everyone will agree to abide by beforehand, and to name explicitly what the protocol excludes. The same reflex applies to design disputes inside a team: when two people cannot agree what a word in the spec means, the exit is a runnable discriminator, not a longer definition. Refusing to answer the meta-question of whether the substitute is worthy — just adopting it and getting on with the work — is part of the technique, because that regress has no bottom.

**Source:** [Computing Machinery and Intelligence](../works/computing-machinery-and-intelligence.md) — the opening move of the paper, where the original question is set aside as too ill-defined to discuss and an interaction-restricted game is put in its place, together with the immediately following defense of why the swap is worth making at all.
