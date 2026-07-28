---
type: lesson
title: "Agreement between a program and its explanation has to be structural, because discipline does not hold it"
figure: knuth
works: [literate-programming]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Agreement between a program and its explanation has to be structural, because discipline does not hold it

**Lesson:** The slogan everyone remembers from this paper is the reversal of audience: treat the reader rather than the machine as the party being addressed. The part that actually does the work is one file feeding two independent processors, one producing a typeset document and the other producing something a compiler will accept. That arrangement is not a convenience. It is the difference between two representations that agree because someone remembered to update both and two representations that agree because they cannot disagree. Every programmer already applies a standing discount to comments, and the discount is rational: an out-of-date comment produces no error, no failing test, no incident. It is the only class of defect in a codebase with no feedback channel at all, which is precisely why it is universal.

Generating both artifacts from one authority removes the failure mode instead of exhorting people to avoid it. Knuth is candid about the price, and the price is instructive. The machine-facing output is explicitly abandoned as something a person would read — identifiers mangled, case flattened, formatting arbitrary, structure scrambled. He gives up the readability of the compiled-against form entirely, in exchange for having exactly one place where meaning lives. There is also a bootstrap cost he does not hide: getting the system running at all requires shipping a pre-generated artifact, since the generator is written in the language it generates. A regime of derived artifacts always has this chicken-and-egg step, and it has to be planned for rather than discovered.

What generalizes is a decision rule for redundancy. Whenever the same fact has to appear in two forms — a schema and the code that reads it, a protocol and both ends of it, an interface and its documentation, a configuration and its validator — you are choosing between designating one form authoritative and generating the rest, or accepting a permanent obligation to keep them in step with no signal when you fail. The second option is not cheaper, it is deferred, and the deferral is unbounded because nothing forces settlement. The reason this feels like extra machinery is that the cost of generation is visible up front and the cost of drift is invisible until someone acts on a stale statement.

A programmer who believes this stops asking whether documentation is worth writing and starts asking where the authoritative copy of each fact lives. When the answer is "in two places, kept aligned by care," that is a finding, not a status quo. It also changes how you evaluate tooling: a tool that lets you write a thing once and project it into several shapes is buying you a class of correctness, not saving you keystrokes.

**Source:** [Literate Programming](../works/literate-programming.md) — the description of the dual-processing pipeline early in the paper, together with the later sections showing the deliberately unreadable generated program and typesetting input, and the bootstrapping procedure needed to install the system.
