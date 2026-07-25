---
type: figure
title: Peter Chen
description: b. 1947. The Entity-Relationship model gave schema design a semantic vocabulary independent of storage mechanism.
status: accepted
layer: both
subdomains: [databases-and-data-management]
tags: [figure, accepted]
---

# Peter Chen

**Dates:** b. 1947. Taiwanese-American computer scientist; PhD Harvard 1973; faculty at MIT Sloan, UCLA, Carnegie Mellon, LSU.

## Why a candidate
The Entity-Relationship model gave schema design a semantic vocabulary independent of any particular storage mechanism — a conceptual-modeling formalism adjacent to, though less purely algebraic than, the relational core. Boundary case — may be cuttable if corpus needs to stay tightly primitive-first.

## Top 10 most influential works
Influence concentrated almost entirely in one paper:
1. "The Entity-Relationship Model — Toward a Unified View of Data" (1976, ACM TODS) — `public` (scanned/mirrored copies circulate widely)
2. "English Sentence Structure and Entity-Relationship Diagrams" (1983) — `paywalled`

## Lessons

Chen's contribution to how programmers think is the insistence that a design
argument be located before it is won. His four-level ladder — what the
enterprise takes to exist, how that is organized into records, structure
innocent of access paths, structure built around them — turns most rivalry
between formalisms into a disagreement about which rung is under discussion,
and lets one small vocabulary at the top yield the others as projections
rather than defeat them. From that placement everything else follows. Meaning
must be stated to be checkable, so a representation holding only the shapes of
its columns will cheerfully combine two quantities that measure unrelated
things; a fact belonging to a pairing of things belongs nowhere else, and
forcing it onto one participant falsifies every later inference about what
determines what. Structure drawn from the domain's own categories survives
assumptions moving, while structure arrived at by repairing an inherited
grouping has silently baked today's multiplicities into its shape and must be
repaired again. A single mark must never assert both a claim about the world
and a route through the machine, or no claim can be read off it with
confidence — keep two artifacts and a uniform written derivation between them.
Some things have no identity of their own but borrow it from what they depend
on, and recording that dependence is what lets integrity and cascade rules be
derived instead of hand-written at every call site. Running through all of it
is a demand for traceability: every element of a model should answer to
something a person actually said, because a model containing its designer's
undocumented experience has stopped being derivable from its inputs and can no
longer be checked by anyone else. Chen's late observation that the grammar of
ordinary description already draws these same joints is the evidence that the
vocabulary was found rather than invented.
