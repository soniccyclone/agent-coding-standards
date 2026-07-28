---
type: lesson
title: "Judge a representation by whether the improvements you want are small edits, not by what it can express"
figure: mccarthy
works: [programs-with-common-sense]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Judge a representation by whether the improvements you want are small edits, not by what it can express

**Lesson:** Universality is the cheap property. Any of several notations — state machines, nets of primitive elements, straight-line machine code — can in principle describe every behavior you might want, and McCarthy grants this freely before dismissing it as beside the point. The property that actually decides whether a representation is worth building on is a metric property, not a coverage property: when you name a change you want in the system's behavior, does that change correspond to a small, local alteration of the description? A formalism can be able to express everything while every interesting revision to it requires rewriting the whole description, and such a formalism is useless for anything that has to improve over time.

Two failures follow from ignoring this, and McCarthy separates them cleanly. The first is density: in a space of arbitrary machine descriptions, the descriptions that do anything worthwhile are vanishingly rare, so undirected exploration finds nothing. The second, which he treats as the more serious one, is that abstract changes have no compact image. If the only encoding of a strategy is the low-level mechanism that carries it out, then the strategic insight — the thing a person would state in one sentence — has no counterpart in the encoding at all, and there is no edit corresponding to having had it. The blueprint analogy carries the argument: a system described at assembly-line detail responds to small perturbation with malformed output, never with a coherent variant, because the description has no joints at the level where meaningful variation lives.

The practical consequence is that you design the vocabulary of a system around the changes you anticipate wanting rather than around the operations the machine performs. If the improvements you expect are of the form "prefer this kind of situation" or "in circumstances like these, do that," then the representation must have terms for kinds of situations and circumstances, at roughly the granularity a person would use to describe them. McCarthy's whole reason for choosing a declarative, sentence-like medium is this and only this: it is the one medium he knows in which abstractions can be stated at all, therefore the one in which acquiring an abstraction is a small addition rather than a redesign.

A programmer who believes this stops treating "we can build anything on top of this" as an argument in a representation's favor, and starts asking for the diff. Before adopting a configuration format, an intermediate form, a policy language, or a schema, they write down three changes they expect to want in a year and check the size and locality of each one in the candidate. A representation where all three are one-line additions beats a more powerful one where all three are refactors, and the comparison is decidable in advance rather than after two years of accumulated pain.

**Source:** [Programs with Common Sense](../works/programs-with-common-sense.md) — the motivational stretch of the introduction, where McCarthy sets aside universal-behavior-simulation schemes as two-fold inadequate and lays out the genetic-versus-blueprint contrast, feeding into the second of his five listed requirements for a system that can evolve intelligence.
