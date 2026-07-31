---
type: lesson
title: "A representation that cannot express every value is where the compression comes from"
figure: reynolds
works: [the-craft-of-programming]
axes: [primitive-count, hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# A representation that cannot express every value is where the compression comes from

**Lesson:** When you go looking for a cheaper way to store something, the instinct is to find an encoding that can still express everything the general form could. That instinct is what keeps you at the general form's cost. The large savings live in encodings that are strictly *incapable* of representing most of the values in the abstract type — a scheme that stores each item as a reference to a previously stored item plus one increment cannot represent an arbitrary collection at all, only collections whose members happen to extend one another. Which is fine, because in this program they always do. The incompleteness is not a defect grudgingly accepted; it is the mechanism by which the space shrinks from quadratic to linear, and any repair that made the encoding total would give the savings back.

The price is that the encoding is no longer justified by the type. It is justified by the algorithm — specifically by an invariant about how the algorithm builds its values, which now has to be maintained forever or the storage silently stops meaning what it says. The invariant is usually about the pattern of writes rather than about the data: each entry is written exactly once, at the moment its subject first appears, and never revisited. Notice how easy that is to violate innocently. Someone adds a case that reconsiders an item already handled, updates its entry, and the encoding is now describing a structure that no longer exists — with no type error, no failed assertion at the write site, and corruption that surfaces somewhere else entirely.

So the discipline is to write the two things down together: the encoding, and the property of the program's behaviour that makes the encoding sufficient. Neither is meaningful alone. And treat the pairing as a design output rather than a coincidence — when you find yourself unable to compress something, the productive question is usually not "what other encodings exist" but "what could I promise about how these values get built, and what would that promise buy me?" Constraining the producer is frequently cheaper than out-clevering the storage.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 5.1.7, which extends the reachability program to record a path for each reachable node, rejects the straightforward two-dimensional array as grossly wasteful in space and time, and instead represents the path array by an array of back links exploiting that each stored path is a previously stored path plus one node; together with its observation that this representation is unusual in being incomplete — there exist path arrays no link array could represent — that such arrays never arise as values of this program's path array, and that this incompleteness is the underlying reason the representation can be so compact. Also the accompanying proof, which turns critically on the fact that the node being added is new, so that the assignments to its link and path entries overwrite nothing previously stored.
