---
type: figure
title: Gregory Chaitin
description: b. 1947, IBM Research/Auckland/Rio/Buenos Aires. Founded algorithmic information theory - randomness and provability limits defined via program-size complexity.
status: accepted
layer: design-thought
subdomains: [foundations-of-computation]
tags: [figure, accepted]
---

# Gregory Chaitin

**Dates:** b. 1947. Argentine-American computer scientist/mathematician; IBM Research for decades, later Auckland/Rio de Janeiro/Buenos Aires.

## Why a candidate
Independently developed algorithmic information theory, defining randomness and provability limits (Chaitin's incompleteness theorem, the halting probability Ω) purely in terms of program-size complexity on a minimal universal machine — the most direct living continuation of the "how few primitives" question. Boundary case flagged: still active, arguably belongs partly to Algorithms & Complexity.

## Top 10 most influential works
1. "The Limits of Mathematics" (1994/1997) — `public` (self-archived on arXiv)
2. "An Invitation to Algorithmic Information Theory" (1996) — `public` (Auckland CDMTCS page)
3. "Algorithmic Information Theory: Some Recollections" (2007) — `public` (arXiv math/0701164)
4. "A Theory of Program Size Formally Identical to Information Theory" (1975, JACM) — `paywalled`, but `public` self-archived copy via Auckland CDMTCS
5. "On the Length of Programs for Computing Finite Binary Sequences" (1969, JACM) — `paywalled`
6. "Incompleteness Theorems for Random Reals" (1987) — `paywalled`/`uncertain`
7. *Algorithmic Information Theory* (1987, book) — `paywalled` (scanned copy on Internet Archive)
8. *Information, Randomness & Incompleteness* (1987) — `paywalled`
9. *Exploring Randomness* (2001) — `paywalled`
10. *Meta Math! The Quest for Omega* (2005, popular book) — `paywalled`

## Lessons
Chaitin's thinking starts from one equation between two things nobody had equated: understanding something and being able to state it more briefly than itself. Everything else follows from taking that seriously and measuring. Explanation becomes a size ratio, so an abstraction that is no smaller than the cases it covers explains nothing; incompressibility turns out to be the normal condition, so compact form is a rare find rather than an entitlement; and deduction turns out to conserve information, so no set of assumptions yields conclusions carrying more content than the assumptions do, which sets a hard ceiling on what any specification can pin down about a system larger than itself. He is equally instructive on how the measuring apparatus gets built. Awkward correction terms in a formalism's own laws indict its definitions rather than its theorems. Making each part declare where it ends is what makes assembly cost a constant instead of growing with the number of parts. Invariants should be enforced by deleting the operation that could break them, error taxonomies collapsed to one failure mode when the host must run untrusted code, and restrictions judged by what they cost asymptotically rather than by how restrictive they feel. Against the temptation to worship minimality he supplies his own counterweights: the shortest form of anything reads like noise, no procedure certifies that a program is the smallest of its kind, and the notation you can both reason about and actually run occupies a narrow band worth choosing deliberately. His practical conclusions are unusually concrete for a foundational figure. Run the construction, because the constant you left unexamined is where you are fooling yourself. Rewrite the artifact when your model of the problem gets simpler, since patches encode a theory you have abandoned. And treat assumptions as priced purchases rather than self-evident truths, because past a certain size the alternative to assuming is not proving, it is not knowing.
