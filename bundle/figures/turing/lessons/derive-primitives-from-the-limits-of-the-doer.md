---
type: lesson
title: "Derive your primitives from the limits of whoever does the work, not from the elegance of the notation"
figure: turing
works: [on-computable-numbers]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Derive your primitives from the limits of whoever does the work, not from the elegance of the notation

The usual way to build a formal system is to start from operations that compose beautifully and then argue that they are adequate. This work inverts that. It starts by asking what a person with paper and pencil can actually do in one indivisible act, and then keeps subtracting anything that turns out to be a convenience rather than a necessity. Two dimensions of paper get dropped because arithmetic layout never truly needs them. The alphabet is capped because unboundedly many distinct marks would eventually differ by less than a reader can distinguish. The number of internal states is capped for the same reason: states that shade into each other cannot be reliably told apart. Attention is confined to a bounded window, so anything wider must be reached by a sequence of small moves. Every restriction is justified not by mathematical taste but by a claim about the finiteness of a real observer, and each one is immediately defended against the objection that it loses power — larger alphabets are recovered by writing longer strings, richer mental states by writing more marks on the tape.

What makes this method more than philosophy is that the resulting primitive set is small enough to reason about exhaustively. Because the whole repertoire is read-one-square, write-one-square, step-one-square, change-state, the behaviour of any machine can be tabulated, the tables can be put in a canonical form, and the canonical forms can be counted. The austerity that looks like a self-imposed handicap is what later licenses every hard result in the paper. A model with a generous, comfortable instruction set could not have been enumerated, and without enumeration there is no diagonal argument and no undecidability theorem. Restriction bought analyzability.

The same paper gives the counterpart move: the definition is only worth anything if it captures everything it was meant to capture, so the work spends a whole section arguing extensional adequacy three separate ways — direct appeal to what a human calculator does, proof of agreement with an independently motivated formalism, and demonstration that broad familiar classes of numbers fall inside. Minimality alone is cheap; minimality plus an argued claim of full coverage is the expensive part.

A programmer who takes this seriously stops designing core abstractions from the notation down and starts designing them from the executing agent up. Before choosing the operations of a bytecode, a protocol, an instruction set, or a domain language, ask what the thing that will actually perform them can do in one uninterruptible step, what it can perceive at one instant, and how much state it can distinguish. Then ruthlessly remove anything expressible as a composition of the rest, and pay the debt of showing that nothing needed was lost. The payoff is not aesthetic tidiness — it is that a small, agent-grounded core is the only kind of core you can later prove things about.

**Source:** [On Computable Numbers, with an Application to the Entscheidungsproblem](../works/on-computable-numbers.md) — this thinking lives in the opening framing of the machine as an analogue of a human calculator and, far more explicitly, in the section defending the extent of the computable numbers, where each restriction on symbols, states, and attention is argued from the finiteness of a real observer.
