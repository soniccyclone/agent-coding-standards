---
type: lesson
title: "Specify a stream component as a relation between its channel histories, plus a bound on how far behind it may fall"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [verifiability, expressiveness, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# Specify a stream component as a relation between its channel histories, plus a bound on how far behind it may fall

**Lesson:** A component that consumes and produces sequences invites description by its mechanism — the buffer it keeps, the counter it maintains, the shape of its loop. Describe it instead by a relation between the complete histories on its channels: what has gone out is a prefix of some function of what has come in. That one sentence carries the whole of correctness while mentioning no internal state, which means it survives every reimplementation, and it composes directly, because connecting two components makes one's output history the other's input history and the relations simply chain. Note that the relation must be stated as a prefix, not an equality: at every moment the output legitimately trails the input, so equality is false at every instant you could observe and true only in a limit nobody sees.

The other half of the specification is a bound on the lag — the output is a prefix of the transformed input with at most so many items still outstanding. That single parameter is the entire difference between an immediate transformer, a fixed-capacity pipeline stage and an unbounded queue, and it is exactly the property that decides whether the component can be built in bounded memory. Two consequences follow immediately. Lag bounds add along a chain, so the end-to-end lag of a composed pipeline is the sum of its stages' — a design number obtained by arithmetic rather than measurement. And a component whose relation is right but whose lag is unbounded is not a slower version of the correct one; it is a different product with a different resource profile, and treating the distinction as a performance detail is how a pipeline acquires a memory leak that is actually a specification error.

The general form is worth taking away for anything defined over histories: look for the two-part description consisting of a functional relation, which says what the output is while ignoring time, and a bound, which says how far behind it may run. Keeping them separate is what makes each one usable. The functional part yields to the ordinary algebra of sequences — including recurrences that define an output stream in terms of shifted copies of itself, which is a remarkably compact way to specify a generator without describing any mechanism at all — while the bound is arithmetic. Fuse them into a single condition and you get something that is correct and that nobody can reason with.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the specifications subsection of the input and output section of the communication chapter: the convention of naming the sequence of messages passed on each channel, the definition of a bounded prefix relation meaning one sequence is a prefix of another with no more than a stated number of items outstanding together with its transitivity law summing the bounds, the specifications given in that form for a copier, a doubler, an unpacker and a packer, and the specification of a Fibonacci generator written as an inequality between the output history and shifted copies of itself.
