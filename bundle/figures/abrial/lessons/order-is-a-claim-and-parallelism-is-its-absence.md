---
type: lesson
title: "Order is a claim you either make or decline, and declining it is the same act for a collection as for a sequence of statements"
figure: abrial
works: [data-semantics]
axes: [parallelizability, expressiveness, primitive-count]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
tags: [lesson]
---
# Order is a claim you either make or decline, and declining it is the same act for a collection as for a sequence of statements

**Lesson:** Any enumeration of a collection has an order, because something has to come out first. The question is whether that order carries meaning. Abrial makes this a declared property with four possibilities, crossing whether elements may repeat against whether their arrangement signifies: a set, a multiset, an ordered set, a sequence. A set is not unordered in the sense of lacking an internal arrangement; it has one, and the arrangement is declared meaningless, in the same way a floating-point normalization is a real choice whose particulars nobody is entitled to depend on. Which of the four you pick is a statement about your problem — summing ages needs repetition and does not need order, walking a calendar needs order and rejects it — and getting it wrong means either promising something you cannot honor or forfeiting freedom you never needed.

The payoff arrives when the same distinction is applied to control flow, and turns out to be identical. Statements separated in a way that says "these happen in this order" are the sequential case; statements separated in a way that says "the order is meaningless here" are the parallel case, and the loop construct splits along the same seam into a sequential form and a form whose iterations may proceed in any arrangement, physically including simultaneously. The two vocabularies then line up exactly: retrieval over an unordered collection is inherently a non-sequential program, and retrieval over a sequence is inherently a sequential one. Parallelism is not a feature bolted onto a language. It is what remains when you decline to assert an ordering, and it becomes available for free wherever you had no ordering claim to make in the first place.

For a programmer this reframes concurrency work from adding machinery to withdrawing claims. Every sequential composition and every ordered container in a program is an assertion about meaning, and most of them were written by reflex rather than judgment. Going back through them and asking which assertions the problem actually requires — rather than reaching for threads and coordination on top of an over-specified structure — is where the parallelism was hiding. Abrial is careful to note a subtlety that any such scheme must handle: an enumeration can be partially ordered, with the first element required to be first and the remainder unconstrained, so the choice is not always binary and a formalism worth having lets you say exactly how much order you mean.

**Source:** [Data Semantics](../works/data-semantics.md) — the further-investigations discussion of ordering and repetition, which classifies collections into four settypes and treats a set's internal enumeration order as a meaningless normalization, and the immediately following section drawing the analogy to sequential versus parallel composition of statements with sequential and parallel loop forms.
