---
type: lesson
title: "Let the machine's own dispatch be your data structure"
figure: thompson
works: [regular-expression-search-algorithm]
axes: [hardware-affinity, expressiveness, primitive-count]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Let the machine's own dispatch be your data structure

The obvious way to build a matcher that advances a set of live positions is to represent the positions as data — numbers, records, pointers into a graph — and write a loop that walks the collection and interprets each entry. Thompson does not do this. The entries in his frontier are control transfers into generated code, and advancing the frontier is executing them. There is no interpreter loop deciding what each entry means, because entering an entry *is* what the entry means; the exploration of every possible continuation from a position happens as a consequence of jumping there rather than as work performed on the position's behalf.

The general principle is worth separating from its 1968 setting. Any structure you invent has a traversal cost that you then pay on every step, and that cost is pure overhead relative to the mechanism the underlying machine already provides for exactly this purpose: deciding where to go next. If the shape of your problem can be expressed in the host's dispatch mechanism instead of in a structure the host has to be told how to read, the interpretive layer disappears entirely rather than being optimized. This same reasoning is why generating code beats walking a tree, and why a table-driven dispatch beats a chain of comparisons — the level of the machine's own control flow is a level, and abstractions that decline to use it are paying rent to avoid it.

Thompson also settles the accounting objection before it is raised. Introducing a translation step looks like added cost only if you assume the alternative has none, and it does not: any implementation must convert the pattern into some form the machine can act on, so the question is never whether to pay for translation but whether to pay once, in advance, or repeatedly, hidden inside the matching loop. Framed that way, staging is free and the interpretive design is the one carrying an unpriced expense. That accounting move generalizes to every build-time-versus-run-time argument.

A programmer who believes this looks at a hot interpretive loop and asks what the machine could be made to do directly, rather than how the loop could be tightened. They also become careful about comparing a staged pipeline against a direct implementation by counting only the stages they can see.

**Source:** [Regular Expression Search Algorithm](../works/regular-expression-search-algorithm.md) — the implementation section's observation that the maintained lists hold transfer instructions rather than characters, so entering the list performs the search, together with its argument that a compiling phase costs nothing because any search must translate the pattern regardless.
