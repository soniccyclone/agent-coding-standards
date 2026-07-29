---
type: lesson
title: "Build behavior with the same tools you build data"
figure: von-thun
works: [an-informal-tutorial-on-joy]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Build behavior with the same tools you build data

If held-back code is an ordinary value of an ordinary type, then every operation
you already have for assembling values also assembles behavior, and you need no
separate mechanism for the job. Von Thun leans on this repeatedly: a fragment of
program is put together by consing a runtime value into a fixed skeleton, and the
result — a piece of behavior specialized to a value not known when the skeleton
was written — is produced with the same operator used to put a number in front of
a list. What other languages provide as a distinct feature, with its own syntax
and its own rules about what may be captured, here falls out of not having drawn
a boundary in the first place.

The reason this is more than a curiosity is that a specialized mechanism has to
be designed, learned, and reasoned about separately, while a general one is
already understood. When behavior is built from the vocabulary of data, the ways
of building it are exactly as numerous as the ways of building data: concatenate
two fragments, pull one out of a larger structure, transform a collection of them,
read one from input. Von Thun makes a point of noting that a piece of program can
arrive at the place where it will be run by any of these routes, and that how it
got there does not matter. That indifference is the payoff — the mechanism has no
opinion about provenance, so it composes with everything.

The corresponding trap is the one this figure is careful about elsewhere: unifying
code and data means equality of behavior stops implying interchangeability while
the code is inert, since two fragments computing the same thing can differ as
structures. The principle is therefore not that the distinction between program
and datum is meaningless, but that it should be a distinction of how you are
currently treating something rather than of what kind of thing it is. Collapsing
kinds while keeping modes buys uniformity of construction without pretending the
opacity isn't there.

A programmer who works this way stops reaching for a new construct every time
behavior needs to be assembled at runtime, and asks instead what representation
would let existing operations do it. They notice when a system has two parallel
vocabularies — one for composing values, one for composing actions — and treat
that duplication as a design smell. Concretely: a pipeline described by a data
structure that an interpreter walks, rather than by a bespoke builder API, gets
inspection, transformation, serialization, and testing for free, because those
were already solved for data.

**Source:** [An Informal Tutorial on Joy](../works/an-informal-tutorial-on-joy.md) — the quotations discussion, which insists a bracketed program can equally be treated as an inert structure or as something to run and can have arrived on the stack by construction, extraction, or input; the permutations program at the end is the sustained demonstration, assembling its inner functions from a fixed part plus a runtime value.
