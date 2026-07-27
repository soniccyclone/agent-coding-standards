---
type: lesson
title: "Carry your reasons inside the normative document, but mark them so nobody can implement them"
figure: steele
works: [the-java-language-specification]
axes: [cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Carry your reasons inside the normative document, but mark them so nobody can implement them

**Lesson:** A specification faces a dilemma that most technical writing never has to confront. Everything it says is an obligation, so anything it adds to help the reader — intuition, worked examples, the reasoning behind a choice, advice about which of two legal spellings to prefer — becomes something an implementor might be held to, or a user might depend on. The usual escape is to strip the document down to bare requirements and push all the explanation into a companion text, which then drifts out of sync and stops being read. This specification takes the other route: it establishes, before any of the language is described, a typographic register that is explicitly declared non-normative, and then uses it constantly. Rationale, historical notes about why a keyword was reserved and never used, advice about which literal suffix is easier to read, and admissions that a piece of terminology is a misnomer all live in that register.

The reason this works is that the two things being separated differ in kind, not merely in importance. A requirement has to be testable by a conformance suite; a reason cannot be. Once the boundary is marked mechanically rather than by tone, the document can be generous with reasons without inflating the set of things an implementation must do — and, symmetrically, an implementor knows exactly which sentences bind. The alternative failure is worse than it looks: when rationale is mixed into normative prose, implementors either treat helpful commentary as mandatory and over-constrain themselves, or learn to skim past prose that looks explanatory and miss real requirements hiding in it.

There is a second effect, less obvious. Because the non-normative register costs nothing to use, the document can afford to be honest about its own scars. It records features reserved for error messages rather than use, notational choices it considers regrettable, and cases where the language's rules produce a surprise that follows unavoidably from an earlier decision. A document with no non-binding channel has nowhere to put this material, so it silently drops it, and the next generation of maintainers has to rediscover why each rule exists by breaking it.

A programmer who takes this seriously stops treating "documentation" as one undifferentiated thing. Contracts, invariants, and error conditions go in a channel that is enforced and tested; the reasoning that produced them goes in a channel that is adjacent, deliberately marked, and never load-bearing. The practical test is whether a reader can tell, from formatting alone and without judgement, which sentences they are allowed to rely on — and whether removing every non-binding sentence would leave the artifact's meaning unchanged.

**Source:** [The Java Language Specification](../works/the-java-language-specification.md) — the notation section of the introductory chapter, which declares a distinct indented register for clarifying material and demonstrates it in the same breath, together with the pervasive later use of that register for rationale, advice, and self-criticism.
