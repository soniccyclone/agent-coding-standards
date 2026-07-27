---
type: lesson
title: "The distinguished result is an assumption, not a fact — give it up and composition becomes symmetric"
figure: girard
works: [linear-logic, proofs-and-types]
axes: [expressiveness, parallelizability]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# The distinguished result is an assumption, not a fact — give it up and composition becomes symmetric

**Lesson:** Functional notation builds in a strong asymmetry that nobody usually notices: a term has many inputs and exactly one output. Reframed honestly, the inputs are not values waiting to arrive; they are the *places where questions are posed*, and the term is the single answer that depends on the answers to those questions. Composition is then always many-to-one. You can partly break the asymmetry inside the usual calculus — an input can be turned into an output by abstraction — but the transformation is lossy and one-directional, so the role swap gets tangled with other structural changes and cannot be repeated freely.

Make the negation of a type an honest involution and the asymmetry dissolves. An answer of one type simply *is* a question of the dual type, so a construct with several conclusions can be read as a function from any subset of them to the rest, chosen after the fact by the reader rather than fixed by the author. Application loses its direction: saying that one component is applied to another is a matter of exposition, not of structure. Connecting two constructs is the same operation regardless of which one you were mentally treating as the callee. What was a tree of nested calls becomes a graph of interconnected conclusions, and the two directions of travel through it correspond to asking and answering.

The uncomfortable consequence, stated plainly in the source, is that the resulting notation does not look like a functional language, and people trained on functional notation find that disorienting rather than liberating. The response is not to retreat but to be clear about who the notation is for. Familiar notation is enormously good for human imagination and will never be displaced for that job; but at a high enough level of abstraction it actively misleads, because it cannot express that a term of one type and a term of the dual type are the same object seen from two sides. The resolution is layered: let the symmetric representation be the machine's internal form — what a compiler produces and manipulates — while people continue to write in the asymmetric, comfortable one. That is a deliberate separation between the representation that is honest about structure and the representation that is kind to humans, with a translation between them, rather than a demand that one win.

A programmer who takes this seriously stops assuming that "what this returns" is a well-defined question about a component. Interfaces get described as a set of typed ports with polarities rather than a signature with one privileged result, and bidirectional or multi-consumer composition stops requiring special machinery.

**Source:** [Linear Logic](../works/linear-logic.md) — the questions-and-answers discussion in the computer-science exposition, where input/output is recast as question/answer and shown to be interchangeable under an involutive negation, together with the defense of a non-functional proof notation as the compiler's form rather than the programmer's. Also [Proofs and Types](../works/proofs-and-types.md) — the chapter on disjunctive rules, which diagnoses the same asymmetry from the other direction: what one wants to write has two conclusions, the single-conclusion restriction makes that unwritable, and the resulting need to commit early to where the branches rejoin is what generates the whole family of commuting rewrites.
