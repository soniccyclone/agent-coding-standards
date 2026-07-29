---
type: lesson
title: "Put the description of the behaviour into the same medium as the data, and one artifact replaces an infinite family"
figure: turing
works: [on-computable-numbers]
axes: [expressiveness, primitive-count, hardware-affinity]
subdomains: [foundations-of-computation, operating-systems-and-systems-programming, programming-languages-and-semantics]
tags: [lesson]
---
# Put the description of the behaviour into the same medium as the data, and one artifact replaces an infinite family

The pivot of this work is a change of representation that costs almost nothing and buys almost everything. A machine's behaviour table is first flattened into a string over a tiny alphabet, then that string is read as a numeral. Once behaviour is a string, and strings are exactly what the machine manipulates, there is no longer any type distinction between the thing being run and the thing being worked on. That single collapse makes it possible to build one machine that, handed the description of any other, reproduces its output — and the argument for its existence is almost casual: a machine that carries its own rules written inside itself can be made to consult them each step, and rules you can consult are rules you can swap.

The lesson is about where to put behavioural specification. Encoding behaviour as ordinary data in the same medium the system already processes converts an unbounded family of special-purpose artifacts into one general artifact plus a supply of descriptions. Every subsequent capability follows from that and not from any added machinery: descriptions can be enumerated, generated, transformed, compared, fed to each other, and used as the subject of proofs. The paper does all of these — it builds a machine that takes a description and emits a series of modified descriptions, it feeds descriptions of machines to machines that analyze them, and it makes the numeral encoding of a machine the object over which theorems about all machines are quantified. None of that is available while behaviour lives in a different substance than data.

There is a subtlety in how the encoding is done that matters as much as the fact of it. The translation from configuration to string is applied only after the configuration has been assembled, because doing the substitution too early would turn an implicit infinite background of blank cells into an infinite explicit string. A serialization that is correct on the finite foreground and wrong about the default background is not a serialization at all. Likewise the layout interleaves two classes of cell — one for the durable result, one for scratch marks that may be freely overwritten — so that working notes never contaminate the answer and the answer never has to be recomputed to make room for notes.

A programmer who internalizes this reaches for data-driven designs by reflex: interpreters over hand-rolled dispatch, configuration and rules as inspectable values rather than compiled-in control flow, wire formats that carry meaning rather than assume it, and a clean separation between the durable output channel and the scratch space. And when doing it, they check the two things this paper checks — that the encoding does not have to materialize an infinite default, and that scratch and result do not share the same cells.

**Source:** [On Computable Numbers, with an Application to the Entscheidungsproblem](../works/on-computable-numbers.md) — the encoding of behaviour tables into standard descriptions and description numbers, and the construction of the universal machine that consumes them, including the remark about why the substitution must be performed after configurations are assembled and the convention that divides the tape into result cells and erasable cells.
