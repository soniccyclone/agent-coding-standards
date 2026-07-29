---
type: lesson
title: "Build your convenience layer so it provably disappears, and the core stays small no matter how much you write in it"
figure: turing
works: [on-computable-numbers]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [programming-languages-and-semantics, foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# Build your convenience layer so it provably disappears, and the core stays small no matter how much you write in it

Working directly in a four-operation instruction set is unbearable past toy examples, and this work does not pretend otherwise. It introduces parameterized skeletal tables — patterns with placeholders for both states and symbols — and then names recurring routines with them: find the leftmost occurrence of a mark, erase every occurrence, append a symbol at the end, copy a marked run to the end, compare two marked runs and branch on whether they match. Higher-level names are defined by substitution into lower-level ones, several layers deep, and the universal machine is then written almost entirely in this vocabulary rather than in raw quadruples. By the end there is something that reads like a small library of subroutines built on a call convention of marking cells with tags.

The critical move is the accompanying declaration that all of this is abbreviation and nothing else. The layer is explicitly stated to be inessential: any expression in it expands, by mechanical substitution, into a table containing none of it. Nothing in the layer can be true of a program that is not already true of its expansion, so every theorem proved about the four-operation core automatically covers everything written in the convenience vocabulary. That is why the paper can spend pages writing in a comfortable derived notation and then, in a later section, reason about all machines as though they were bare tables — because they are. The abstraction is load-bearing for the human and weightless for the theory.

The paper is also careful about what makes such a layer safe. The substitutable arguments have to be an explicitly enumerated set, because if you allow a name to be applied to arbitrary expressions built from itself, the set of states it generates becomes infinite and the finiteness the whole model depends on quietly evaporates. Convenience that silently changes the size of the state space is not convenience, it is a different system wearing the same clothes.

For a programmer this is the discipline that distinguishes a macro layer, a DSL, or a set of combinators that genuinely costs nothing from one that becomes a second semantics to reason about. Ask whether your convenience construct has a mechanical expansion into the core, whether that expansion is total, and whether it can enlarge anything the core's guarantees are stated in terms of. If yes, yes, and no, you can write in it freely and still hold every property you proved of the core. If not, you have doubled the system you must understand while telling yourself you simplified it.

**Source:** [On Computable Numbers, with an Application to the Entscheidungsproblem](../works/on-computable-numbers.md) — the section on abbreviated tables and its extension into the library of copy, compare, erase, and find routines used to express the universal machine, together with its insistence that the layer is nothing but abbreviation and its restriction on what may legally be substituted.
