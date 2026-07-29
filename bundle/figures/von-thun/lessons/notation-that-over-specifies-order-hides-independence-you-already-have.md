---
type: lesson
title: "Notation that over-specifies order hides independence you already have"
figure: von-thun
works: [an-informal-tutorial-on-joy]
axes: [parallelizability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# Notation that over-specifies order hides independence you already have

Writing a computation down usually forces you to commit to more than you mean.
Von Thun's small example is computing an average: you need a total and a count
from the same collection, and in a straight-line stack notation you must
duplicate the collection, take one quantity, shuffle the intermediate result out
of the way, take the other, then divide. The resulting program says the total is
computed before the count. Nothing in the problem says that. The sequence is an
artifact of having only one place to put things and one order in which to write
them, and once it is written down, the claim that these two computations are
independent has been erased from the text.

Two costs follow, and they are usually discussed separately even though they
have the same root. The first is legibility: the stack-shuffling operators carry
no meaning about the problem, so a reader has to reconstruct intent from
plumbing. The second is that no implementation can exploit what the notation has
thrown away — the two quantities could be computed simultaneously on separate
processors, but a program that states an order has, as far as any tool can tell,
required that order. Recovering the freedom afterward means analysis to prove
that the sequencing was accidental, which is work created entirely by the
notation. Von Thun's answer is a construct that states the real shape directly:
one input, several functions applied to it, results assembled. The order is
absent because it was never part of the problem.

The generalizable move is to notice that in most languages, sequence is the
default and independence must be specially declared, when the honest situation is
the reverse: independence is the common case and dependency is the exception
worth marking. Under that framing, every gratuitously sequenced pair of
statements is a small lie told to the compiler and the reader, and the plumbing
introduced to make the sequence work — the temporary variable, the shuffle, the
intermediate name — is the visible residue of the lie.

A programmer who takes this seriously reads any manipulation whose only purpose
is to get values into position as evidence that the notation is wrong for the
problem, not as evidence they need to be cleverer. They prefer forms that state
the dependency structure — apply these several things to this one input, collect
these results — over forms that state a schedule, and they treat accidental
sequencing as a defect to remove even where nothing is currently parallel,
because the cost is already being paid in comprehension.

**Source:** [An Informal Tutorial on Joy](../works/an-informal-tutorial-on-joy.md) — the passage in the quotations-and-combinators section that critiques its own arithmetic-mean program on two grounds, the unreadable stack manipulation and the imposed ordering of two computations that could run at once, and then replaces it with a construction combinator.
