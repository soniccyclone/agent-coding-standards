---
type: lesson
title: "Build one expression language and spend it everywhere"
figure: date
works: [an-introduction-to-database-systems, databases-types-and-the-relational-model-the-third-manifesto]
axes: [primitive-count, expressiveness, verifiability]
subdomains: [databases-and-data-management, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Build one expression language and spend it everywhere

**Lesson:** It is natural to read an algebra over data as a query facility, and Date corrects that reading deliberately. The point of having operators that take the aggregate type in and give the same type back is that they compose, so results feed into further operators without limit, and what you actually own once you have them is a language of expressions. That language then turns out to be the right way to say almost everything a data system needs said. The same expressions delimit what a retrieval returns, what an update touches, what a constraint requires, what a derived table contains, what a unit of concurrency must hold stable, and what an authorization covers. Six problems that are usually solved by six unrelated mechanisms collapse into one notation with six uses.

That collapse is the real dividend of closure, and it is worth separating from the more familiar performance dividend. Because these are symbolic expressions rather than procedures, they obey algebraic laws, and a rewriter can transform one into an equivalent that costs less; Date's stated goal is that the price of a request should not depend on which of several equivalent phrasings the author happened to choose. He is also clear that composition is a conceptual claim and not an implementation mandate: an intermediate result need never exist in full, and a good implementation will stream values through a pipeline rather than materialize each stage.

The counting discipline he applies elsewhere shows up here too, in a form worth noticing. The operator set everyone learns is not minimal and was never meant to be; several members are definable from the others, and a smaller basis suffices, with an even more austere reformulation reducing the whole thing to a couple of primitives. Date's position is that the minimal basis and the working set are answers to different questions. Minimality is what you use to prove things and to establish a yardstick for measuring whether some other language is expressive enough. Convenience is what you ship, because a derived operator that appears in nearly every real expression earns direct support. Knowing which operators are primitive is what lets you add convenient ones without fear, since each is provably nothing new.

A programmer working this way looks, whenever a system grows a third or fourth little sublanguage for describing subsets of data, for the one expression language that could have served all of them, and treats the proliferation as a design failure rather than as separation of concerns. They also keep track of which of their own operations are primitive and which are conveniences defined in terms of them, because that record is what makes the surface safe to grow and the semantics possible to state.

**Source:** [An Introduction to Database Systems](../works/an-introduction-to-database-systems.md) — the relational algebra chapter's section on what the algebra is for, which lists the uses beyond retrieval, gives the rewriting example motivating optimization, and notes both that the familiar operator set is non-minimal and that a much smaller basis exists; the closure discussion in the earlier introductory chapter supplies the composition and pipelining argument. Also [Databases, Types, and the Relational Model: The Third Manifesto](../works/databases-types-and-the-relational-model-the-third-manifesto.md), whose appendix reworking the algebra onto a very small set of primitives shows the reduction carried out in detail.
