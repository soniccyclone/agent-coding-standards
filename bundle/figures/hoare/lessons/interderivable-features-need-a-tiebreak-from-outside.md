---
type: lesson
title: "When two candidate primitives can each define the other, the tiebreak has to come from outside the algebra"
figure: hoare
works: [communicating-sequential-processes-paper]
axes: [primitive-count, hardware-affinity, expressiveness]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
tags: [lesson]
---
# When two candidate primitives can each define the other, the tiebreak has to come from outside the algebra

**Lesson:** A recurring shape of design argument is: mechanism A should be primitive because B is easy to build from it. The trap is that the relation is often symmetric. Unbuffered handoff can synthesize a queue by interposing a process that holds values; a queue can synthesize handoff by pairing a send with a wait for acknowledgement. Naming the peer directly and naming a local port wired to a peer are, once each port connects to exactly one partner, the same semantics under two spellings. In every such pair, expressive-power reasoning terminates in a tie, and a designer who keeps arguing derivability is just restating the tie in more words. The honest move is to say out loud that the derivation argument is symmetric and then reach for a criterion that lives outside it.

The criterion worth reaching for is what each candidate costs on the machines you actually intend to run on, especially the least forgiving one. Synchronized handoff needs nothing but a rendezvous between two participants, so it is realizable both on a single shared store and on a set of processors with disjoint memories connected only by wires; automatic buffering silently assumes somewhere to put unbounded pending output, which the shared-store implementation has and the disjoint-processor network does not. That asymmetry, invisible to the algebra, decides the question. Note the direction of the reasoning: the primitive is chosen to be the one whose implementation obligation is discharged on the *hardest* target, and the convenience is then recovered where wanted by explicit construction, paid for by whoever wants it. Choosing the other way round makes the convenience unremovable and quietly narrows the set of machines the language can honestly claim.

A second, weaker criterion applies when even the cost argument ties: what the notation is *for* right now. Two semantically identical spellings can differ in how much redundancy a checker can exploit and how much apparatus a reader must hold, and those pull opposite ways depending on whether you are exhibiting a semantic idea or building large programs. That is a legitimate reason to pick one and record that you picked it for exposition rather than for production — which is a very different claim than pretending it won on the merits. Keeping the two grades of argument separate is what lets a later designer overturn the notation without disturbing the semantics.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-paper.md) — the discussion sections weighing automatic buffering against synchronized communication, where the deciding reason is realizability on multiple disjoint processors and Hoare concedes the derivability argument runs equally well in both directions, together with the parallel treatment of port names as an attractive but semantically equivalent alternative chosen against on grounds of directness for the paper's purpose.
