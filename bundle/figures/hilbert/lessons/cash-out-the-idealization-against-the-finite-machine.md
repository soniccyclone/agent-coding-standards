---
type: lesson
title: "Nothing you actually run is infinite; every guarantee has to be cashed out against the finite mechanism"
figure: hilbert
works: [uber-das-unendliche]
axes: [hardware-affinity, verifiability]
subdomains: [foundations-of-computation, operating-systems-and-systems-programming]
tags: [lesson]
---
# Nothing you actually run is infinite; every guarantee has to be cashed out against the finite mechanism

**Lesson:** Before arguing about the mathematics, Hilbert spends the first part of the lecture asking whether the infinite is realized anywhere in the physical world, and answers no in both directions. Matter is not endlessly divisible but built of discrete constituents; electricity, once the model of a continuous fluid, turned out to be granular; even energy came in quanta. Toward the large, the assumption of unbounded space had been inherited from Euclidean geometry, but a consistent geometry is not thereby a true description of anything — only observation settles that, and the physics of his day made a finite world entirely tenable. His summary is that unlimited divisibility is an operation carried out in thought only, and that the naive inference from "there is always more space outside a given region" to "space is infinite" confuses being unbounded with being infinite, two properties that do not exclude each other.

He then turns the finding into a methodological rule rather than a prohibition. The idealization keeps its place, because it is indispensable in thought; what it does not get is self-supporting authority. Operating with the infinite, he insists, can only be secured by means of the finite: whatever confidence the idealized reasoning deserves has to come from an argument conducted entirely within the concrete, surveyable domain, and its role is that of a regulative idea trustworthy exactly within the frame such an argument establishes.

The parallel for programmers is unusually direct, because the same gap sits between the languages we reason in and the machines we run on. Integers are unbounded in the semantics and wrap at a word boundary in the register; streams are infinite in the type and finite in the buffer; recursion is unlimited in the model and bounded by a stack; addresses are dense and continuous in the abstraction and paged, cached, and physically finite underneath. None of this argues for abandoning the idealizations — reasoning would be impossible without them. It argues for knowing precisely which of your guarantees are claims about the idealization and which have been cashed out against the real mechanism, because the second kind is what survives deployment. The bugs that occur here are almost always of one type: a law that holds without exception in the model, invoked in a situation where the finite substrate cannot honor it. Hilbert's discipline is the right one — take the idealization seriously, and separately know the finite argument that licenses it.

**Source:** [Über das Unendliche](../works/uber-das-unendliche.md) — the opening survey of whether physics realizes the infinitely small or the infinitely large, the distinction drawn between unboundedness and infinity, and the closing conclusion that operating with the infinite can be secured only through finite means.
