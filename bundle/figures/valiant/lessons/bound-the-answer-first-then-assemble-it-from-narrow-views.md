---
type: lesson
title: "Bound the size of the answer first; that bound tells you how many narrow views you need to reconstruct it"
figure: valiant
works: [the-complexity-of-computing-the-permanent]
axes: [hardware-affinity, cognitive-load, primitive-count]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Bound the size of the answer first; that bound tells you how many narrow views you need to reconstruct it

**Lesson:** A capability that only works in the small is often mistaken for a capability that does not work. If your machinery handles restricted inputs — narrow values, a single residue, one shard, a coarse quotient — the temptation is to treat the general case as out of reach. The way through is to reverse the order of reasoning: bound the magnitude of the answer *before* deciding what machinery you need. An a priori bound converts the general problem into a known, finite number of restricted problems, because a value that provably fits in so many bits is determined by that many bits' worth of partial views, and a value determined by partial views can be assembled from whatever narrow mechanism you already have.

The structure of such an argument has three parts worth naming separately, since each is a place the reasoning can be checked. First, the bound: from the input's shape alone, how large can the result be? Second, the decomposition: a family of restricted computations whose results jointly determine any value below that bound, with the family's size controlled by the bound rather than by the input. Third, the lowering step: a way to squeeze each restricted instance into the impoverished form your mechanism actually accepts, without disturbing the quantity being computed. Only the third part is usually novel; the first is arithmetic and the second is standard. A great deal of apparent generality in a result is obtained exactly this way, by a bound plus a reconstruction wrapped around a construction that only ever handled the easy case.

The habit generalizes well past number theory. Fixed-width arithmetic reconstructing a wide value, a sketch answering a query no single counter could, a sharded store answering a global aggregate, a test suite establishing a property one case at a time — all are the same move, and all of them live or die on the same question, which is whether the bound on the answer was established independently of the mechanism. Where this goes wrong is when the bound is assumed rather than derived, because then the reconstruction is silently incomplete and produces a plausible wrong value rather than a failure. So derive the bound from the input, write it down, and make it the thing you check when the assembly misbehaves.

**Source:** [The Complexity of Computing the Permanent](../works/the-complexity-of-computing-the-permanent.md) — Proposition 3.4, which bounds the permanent of a bounded-entry integer matrix a priori, deduces that computing it modulo each of a polynomially long list of small primes suffices, and applies the earlier lemma that converts a matrix over a small range of entries into a zero-one matrix with the same permanent so the restricted machinery can absorb each residue instance.
