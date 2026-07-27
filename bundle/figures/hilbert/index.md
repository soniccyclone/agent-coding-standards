---
type: figure
title: David Hilbert
description: 1862-1943, Göttingen. Architect of the formalist program; posed the Entscheidungsproblem that forced Church and Turing to define computability rigorously.
status: accepted
layer: design-thought
subdomains: [foundations-of-computation]
tags: [figure, accepted]
---

# David Hilbert

**Dates:** 1862-1943. German mathematician at Göttingen.

## Why a candidate
Posed the Entscheidungsproblem (1928, with Ackermann) and his formalist program is itself an explicit reduction of mathematics to a minimal primitive rule-set. Included as the antecedent/motivator rather than a computability theorist himself — most of his oeuvre (geometry, invariant theory, physics) is outside this subdomain's scope. Flag for Phase 2: does "posed the question" count as strongly as "answered it"?

## Top 10 most influential works
1. "Mathematische Probleme" (1900 Paris lecture, 23 problems) — `public` (widely reprinted/translated, out of copyright)
2. "Grundlagen der Geometrie" (1899) — `public` (out of copyright, archive.org/Project Gutenberg)
3. "Über das Unendliche" (1926, Mathematische Annalen) — `uncertain`
4. "Grundzüge der theoretischen Logik" (with Ackermann, 1928) — `uncertain`
5. "Grundlagen der Mathematik" (with Bernays, Vol. I 1934, Vol. II 1939) — `paywalled` (Springer)

Fewer than 10 — only 5 works tied directly to this subdomain's relevance.

## Phase 3 access flag
Item 4, "Grundzüge der theoretischen Logik" (with Ackermann, 1928) — the work
that formally poses the Entscheidungsproblem cited in this figure's "why a
candidate" case above — has no publicly accessible copy anywhere checked:
Springer paywalls the modern reprint; every scanned edition on the Internet
Archive (1928 German original searched but not found scanned there at all;
1967 German reprint at `archive.org/details/grundzugedertheo0027hilb`; 1950
English translation "Principles of Mathematical Logic" at
`archive.org/details/principlesofmath0000hilb` and
`archive.org/details/principlesofmath0000dwac`) is marked
`access-restricted-item: true` — controlled digital lending only, not a public
source under this project's rules; HathiTrust's catalog record is
Cloudflare-gated and its held volumes (1-97, 1869-1930) could not be confirmed
full-view; no self-archived PDF turned up on any math-history or logic course
page; Wayback Machine has no snapshot of a dead public PDF link either (a CDX
search for `*hilbert*grundz*logik*` returned zero captures). Item 5,
"Grundlagen der Mathematik" (with Bernays), remains paywalled as originally
flagged — same archive.org access-restricted pattern, Springer paywall
confirmed current — except for a genuinely partial self-archived resource
(title pages, prefaces, and sections 1-2 only, not the full text) at
`wirth.bplaced.net/p/hilbertbernays`, which doesn't rise to "the work is
public" and was left out of `works/` on that basis. Both stay excluded from
`works/`; flagging per standing procedure rather than blocking on it.

## Lessons rollup
Hilbert teaches that the way to get control of a subject is to fix, exactly and
in the open, what it rests on — and that once you have done so, questions that
looked philosophical become technical. His primitives are introduced as
unspecified things whose only content is the relations declared about them,
which is what makes a specification a real object: an inconsistent one
describes nothing, and consistency is both the definition of existence and the
sole price of admission for any convenient fiction you adjoin to keep the laws
simple. From that base come the working habits: account for which assumptions
each result actually consumes rather than resting on the whole pile; test
whether an assumption is load-bearing by constructing the functioning world in
which it fails; hunt for the local checkable law equivalent to a global
structural property, and for the algebra, built from the domain's own objects,
whose identities are a readout of your assumptions; characterize what a fixed
toolset can reach by the closure it generates instead of by trying harder. His
demands on problems are the same discipline turned outward — ask for the
procedure that decides a whole family, not the answer to one instance; treat
"this cannot be done under these premises" as a theorem to go prove; and when
stuck, change altitude rather than effort, defaulting downward to the simpler
unsolved question. Two of his moves are directly the ancestry of programming
practice: making the derivation itself a finite inspectable object so that
global claims about a system become checks over data, and insisting that
reasoning conducted in an idealization is only as good as the finite argument
that licenses it, because the bounded claim and the unbounded one are different
kinds of claim and nothing you actually run is infinite. Rigor, in his telling,
is not the tax for all this; it is what makes the work smaller.
