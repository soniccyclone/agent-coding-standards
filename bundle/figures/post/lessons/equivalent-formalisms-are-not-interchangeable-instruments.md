---
type: lesson
title: "Equally powerful representations are not interchangeable; keep several and pick per problem"
figure: post
works: [recursive-unsolvability-of-a-problem-of-thue]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Equally powerful representations are not interchangeable; keep several and pick per problem

Post admits a frustration with his own field: the proliferation of mutually equivalent definitions of computability has made the subject harder to sell to outsiders, since a newcomer cannot tell why so many different-looking things are being maintained when they all delimit the same class. Then he turns the observation around. In this one proof he needs two of them and cannot substitute either for the other. His rewriting formalism is what naturally produces the hard problem he starts from. The tape-and-states formalism is what supplies the property the argument actually turns on, namely that the process is deterministic — one applicable step at each moment, in one way. Sameness of power is exactly the wrong measure: what distinguishes the formalisms is which facts they make manifest.

The reason this is not a curiosity about logic is that the property a proof needs is almost never a property of the function computed. It is a property of how the computation is written down. Determinism, locality, the fact that state lives in exactly one place, the fact that each step touches a bounded region — these are visible in one encoding and buried in another, even when the two encodings compute identically. Translating between them preserves the answer and destroys the leverage. So the right stance toward redundant representations is not to consolidate them but to keep them as a set of instruments, each carrying a different property on its surface, and to choose by asking which property the argument in front of you requires.

For a programmer this cuts against a strong tidying instinct. Having two models of the same domain — an event log and a materialized state, a declarative rule set and an imperative pipeline, a schema and the code that enforces it — feels like duplication to be eliminated. Sometimes it is. But when each form makes a different invariant checkable, collapsing them costs you the ability to reason. The log makes history and ordering evident and current state obscure; the materialized form does the reverse. A rule set makes coverage and conflict analyzable; the equivalent hand-written control flow makes efficiency evident and coverage guesswork. Keeping both, with a proven correspondence between them, is often what makes the system tractable at all.

The corollary is a question worth asking when reasoning stalls. Rather than pushing harder on the current representation, ask what property is missing and whether some equivalent encoding of the same thing puts that property in plain sight. Changing the representation to change what is obvious is a real move, not an evasion.

**Source:** [Recursive Unsolvability of a Problem of Thue](../works/recursive-unsolvability-of-a-problem-of-thue.md) — the concluding remark on the multiplicity of equivalent formulations of recursiveness, read against the body of the proof, which draws its starting problem from one formalism and its crucial determinism from another.
