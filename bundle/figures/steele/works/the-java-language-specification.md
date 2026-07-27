---
type: work
title: "The Java Language Specification"
figure: steele
description: The authoritative definition of Java's syntax and semantics, co-authored by Steele with Gosling, Joy, and (from the 3rd edition) Bracha. Oracle (formerly Sun) publishes every edition free online rather than only in print, making it one of the few full commercial-language specifications with no paywalled canonical version. Included here as evidence Steele's minimal-core design instincts carried over from Lisp/Scheme standardization into a mainstream, heavily-used industrial language.
subdomains: [programming-languages-and-semantics]
year: 1996-2015
url: https://docs.oracle.com/javase/specs/jls/se8/html/index.html
access: public
host: institutional
tags: [work]
---

# The Java Language Specification

**Author(s):** James Gosling, Bill Joy, Guy Steele, Gilad Bracha (later editions add Alex Buckley)
**Venue/year:** First edition 1996 (Addison-Wesley); official free HTML/PDF editions published by Sun/Oracle for every Java SE release since.
**Source:** https://docs.oracle.com/javase/specs/jls/se8/html/index.html — live page, Oracle's own official hosting of the Java SE 8 edition.

## Lessons
- [Where you place a transformation in the pipeline is a semantic decision, and everything above it loses the power to protect itself](../lessons/where-you-place-a-transformation-in-the-pipeline-is-a-semantic-decision.md)
- [Prefer a rule a reader can apply without lookahead, even when it rejects programs another reading would have accepted](../lessons/prefer-a-rule-the-reader-can-apply-locally-over-one-that-accepts-more-programs.md)
- [Carry your reasons inside the normative document, but mark them so nobody can implement them](../lessons/put-your-reasons-in-the-document-and-mark-them-as-non-binding.md)
- [The only compatibility worth designing for is whether independently owned modules can adopt a feature one at a time](../lessons/the-only-compatibility-that-matters-is-whether-modules-can-migrate-independently.md)
- [When many situations each allow many transformations, name the transformations once and let each situation publish which ones it admits](../lessons/factor-a-permission-matrix-into-atomic-operations-times-sites.md)
- [Add permissiveness as a later phase that only runs when the strict phase found nothing](../lessons/add-permissiveness-as-a-later-phase-so-it-cannot-change-what-already-worked.md)
- [Separate the values a type denotes from the representations a machine may use for it, and let code declare whether it wants the latitude](../lessons/separate-the-values-a-type-denotes-from-the-representation-permitted-at-runtime.md)
- [Resolve a name in staged narrowings, and give every distinct way a name can miss its target its own word](../lessons/give-every-way-a-name-can-miss-its-target-a-separate-word.md)
- [Borrow global uniqueness from a registry that already exists, and then grant the borrowed hierarchy no authority whatsoever](../lessons/borrow-uniqueness-from-a-registry-that-exists-and-grant-the-hierarchy-no-authority.md)
