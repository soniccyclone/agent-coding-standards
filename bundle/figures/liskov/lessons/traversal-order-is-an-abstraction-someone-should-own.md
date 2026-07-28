---
type: lesson
title: "Traversal order is an abstraction, and the collection should own it"
figure: liskov
works: [abstraction-mechanisms-in-clu]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Traversal order is an abstraction, and the collection should own it

**Lesson:** Almost every loop does two unrelated jobs at once: it decides which
element comes next, and it does something with that element. Fusing them means
the walking logic is written fresh at every use site, so knowledge of the
structure being walked leaks into every consumer, and a change to the structure
touches all of them. Once you notice that the *sequencing method* is itself a
nameable abstraction — an answer to "in what order do these elements arrive?" —
it can be defined once, next to the data it walks, and consumed by code that
never learns what the data looks like.

The interesting part is what this does to the loop construct. Languages
typically ship a small fixed set of iteration forms, most commonly counting
over integers, and everything else becomes hand-rolled index arithmetic. If
sequencing is user-definable instead, one loop construct suffices for all
collections forever, and the language gets smaller rather than larger while
covering more ground. Multiple orderings over the same collection become
multiple named abstractions rather than a parameter someone has to interpret,
so choosing to walk in reverse or in sorted order is a choice of vocabulary
word, not a rewrite of the loop.

Producing elements one at a time rather than materializing a sequence is what
makes this practical rather than merely tidy. The intermediate collection never
has to exist, so a walk over a large structure costs no proportional storage,
and a consumer that stops early — a search that finds its answer on the third
element — never pays for the rest. That is a real efficiency, not a
consolation. A programmer who thinks this way stops writing structure-aware
loops in client code entirely: when they find themselves indexing into
something whose layout they should not know, the fix is to ask the owner of the
data for a sequencing abstraction rather than to remember the layout more
carefully.

**Source:** [Abstraction Mechanisms in CLU](../works/abstraction-mechanisms-in-clu.md) — the treatment of control abstraction, where the selection of the next object is split away from the action taken on it and given its own definable construct, and the argument for generating elements incrementally rather than building a sequence object.
