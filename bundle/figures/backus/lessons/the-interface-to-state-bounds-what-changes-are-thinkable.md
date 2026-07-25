---
type: lesson
title: "The width of a system's interface to its state bounds the changes anyone can imagine making"
figure: backus
works: [can-programming-be-liberated-from-the-von-neumann-style]
axes: [primitive-count, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# The width of a system's interface to its state bounds the changes anyone can imagine making

**Lesson:** Consider how a conventional program talks to its state. Not through one channel with one rule, but through a bundle of specialized channels, one per construct, each with its own protocol — and the protocol for a given identifier depends on where it appears, so the same name means something different on the left of an assignment, in a declaration, and in a parameter position. The meaning of a program is then the accumulated effect of a large number of small conversations, each conducted under its own conventions. A striking consequence is not that this is complicated, but that it forecloses a whole category of operation: applying a general transformation to the entire state cannot even be contemplated, because nothing guarantees an arbitrary new state would still satisfy the fixed protocols. The interface's shape has already determined which changes are thinkable, and the thinkable ones are exactly the small ones the interface permits.

The way out is to separate a requirement from the habit that usually implements it. A system that must remember anything across runs genuinely needs state — that much is forced. What is not forced is that every detail of every computation must touch that state. Those are independent, and conflating them is what produces the wide protocol-laden interface. Loosen the coupling instead: let a computation proceed with no state change at all, and let a single transition occur once per major step, producing output together with a whole new state. The interface then collapses to a handful of rules — obtain a definition from the state, obtain the state itself, replace the state with the result of applying a function to it — and the state becomes an ordinary value that ordinary operations can transform wholesale.

The payoffs come from the collapse rather than from any individual rule. A transition that happens once per computation is a mathematical object simple enough to have properties worth stating, where a transition that happens on every step is not. Whole-state transformation becomes available, which is a strictly larger class of change than the old interface allowed. Multiple kinds of store with different naming and typing disciplines can coexist in one program, since each is now defined rather than built in. And a designer who takes the lesson generalizes it beyond languages: whenever a component's access to shared state is spread across many bespoke entry points, the cost is not only the complexity of each one but the invisibility of every operation those entry points cannot express.

**Source:** [Can Programming Be Liberated from the von Neumann Style?](../works/can-programming-be-liberated-from-the-von-neumann-style.md) — the comparison of an Algol-style program's many-channel communication with its state against the loosely coupled state-transition systems sketched later, including the argument that history sensitivity requires state without requiring pervasive state changes.
