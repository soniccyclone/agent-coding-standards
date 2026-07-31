---
type: lesson
title: "Existence can be enough: price finding the certificate against using it before demanding one"
figure: stearns
works: [an-algebraic-model-for-combinatorial-problems]
axes: [cognitive-load, verifiability]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Existence can be enough: price finding the certificate against using it before demanding one

**Lesson:** A fast method that exploits structure normally needs a certificate — an explicit description of the structure it is going to exploit — and the reflex is to make that certificate an input, which pushes the burden onto whoever is calling you and limits the method to cases where somebody already knew the answer. Before accepting that, compare two costs directly: the cost of searching for a certificate of quality *d*, and the cost of exploiting a certificate of quality *d* once you have it. If the search is no more expensive than the use, the certificate never has to be supplied. Search upward from the cheapest quality, stop at the first one that exists, and the total stays within a constant of what exploiting a handed-to-you certificate would have cost. At that point the mere *existence* of good structure in the input is enough to beat the unstructured method, and the caller supplies nothing.

The reason this is worth checking rather than assuming is that the two costs are often much closer than intuition suggests, and the search-upward trick converts an unknown parameter into a non-issue. Nothing has to be estimated, no heuristic decides when to give up, and the method degrades gracefully: an input with no good structure costs what the search cost, which is bounded by what the unstructured method would have cost anyway. The whole arrangement turns a precondition into an internal detail.

The habit generalises to every fast path gated on metadata. Before requiring a declaration — an index hint, a type annotation, a schema, a manually specified partitioning — price the discovery of that metadata against the fast path itself, and require the declaration only if discovery is genuinely the more expensive side. Systems that infer at runtime what earlier designs demanded up front are almost always exploiting exactly this asymmetry, and the ones that keep demanding declarations often do so because nobody ever did the comparison. Two things must be checked honestly for the argument to hold: the search has to be a search for the same object the fast path consumes, not a proxy for it, and the failure case has to be bounded, because a search that can run long on inputs with no structure has merely relocated the cost rather than removed it.

**Source:** [An Algebraic Model for Combinatorial Problems](../works/an-algebraic-model-for-combinatorial-problems.md) — the finding-good-structure-trees section, where a search procedure whose cost for quality parameter *d* is close to the cost of solving with a given structure of quality *d* is invoked repeatedly from the cheapest parameter upward, yielding the theorem that satisfiability can be solved faster than exhaustive search from the existence of good structure alone, followed by the explicit statement that no structure tree needs to be supplied as part of the input.
