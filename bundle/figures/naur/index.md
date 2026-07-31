---
type: figure
title: Peter Naur
description: 1928-2016, University of Copenhagen. "Programming as Theory Building" - a program's structure lives as shared theory in programmers' minds. Turing Award 2005.
status: accepted
layer: implementation-mapping
subdomains: [software-engineering-and-architecture]
tags: [figure, accepted]
---

# Peter Naur

**Dates:** 1928-2016. Danish computer scientist, University of Copenhagen; co-editor of the ALGOL 60 report (source of Backus-Naur Form).

## Why a candidate
"Programming as Theory Building" is a rigorous epistemic argument that a program's structure lives as shared theory in programmers' minds, not just in code — a direct, non-fad account of why systems decay when that theory isn't transferred.

## Top 10 most influential works
Genuinely influential body of work is thin outside these:
1. "Programming as Theory Building" (1985) — `public` (gwern.net, UW-Madison mirrors)
2. Revised Report on the Algorithmic Language ALGOL 60 (1963, editor) — `public` (widely mirrored standards document)
3. "The Place of Strictly Defined Notation in Human Insight" (1975) — `uncertain`
4. *Computing: A Human Activity* (1992, collected works) — `paywalled`
5. *Knowing and the Mystique of Logic and Rules* (1995, book) — `paywalled`

## Lessons
Naur's central claim is that what a team builds is a theory of some part of the world, and the program text is a by-product of holding it. That inverts the usual priorities. A system is alive only while someone still carries its theory, and that state cannot be reconstructed from documents afterwards — so the question "can this be handed over?" is about people, not artifacts, and built-in flexibility is a wager paid up front whereas real adaptability comes from whoever understands why the thing is shaped as it is. It follows that behavioral correctness does not settle whether a change is right: a modification has to be judged against the account the system embodies, and a patch that passes every test can still be wrong because it contradicts the theory. His language work applies the same conviction to notation. Build the vocabulary for describing a thing before describing it; fix the defining form for human understanding and treat every machine encoding as a transliteration of it; define each convenience by rewriting it into a core already defined, so the core stays small and the conveniences stay honest. Where a definition has a hole, mark the hole and name who must fill it, and where the notation carries something the machine ignores, say so explicitly. Throughout, method is teaching rather than governance — no prescribed ordering of steps produces understanding, which is exactly why understanding has to be cultivated in people instead of encoded in process.
