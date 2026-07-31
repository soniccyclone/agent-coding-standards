---
type: figure
title: Maurice Wilkes
description: 1913-2010, Cambridge. Built EDSAC; invented memory cache; built CAP, the first working hardware capability-based system.
status: accepted
layer: implementation-mapping
subdomains: [operating-systems-and-systems-programming]
tags: [figure, accepted]
---

# Maurice Wilkes

**Dates:** 1913-2010. British computer scientist, University of Cambridge; led the Cambridge Computer Laboratory for decades.

## Why a candidate
Invented the memory cache ("slave memory") and, with Needham, built the CAP computer — the first working hardware capability-based system — putting him at the hardware-mechanism foundation this subdomain is specifically meant to credit.

## Top 10 most influential works
1. "Slave Memories and Dynamic Storage Allocation" (1965, origin of "cache") — `public` (mirrored on multiple university course pages)
2. "The Best Way to Design an Automatic Calculating Machine" (1951, first paper proposing microprogramming) — `uncertain`
3. "The Cambridge CAP Computer and Its Operating System" (1979, book with Needham) — `paywalled`
4. *Memoirs of a Computer Pioneer* (1985, book) — `paywalled`
5. *Time-sharing Computer Systems* (1968, book) — `paywalled`

## Lessons
Wilkes writes as an engineer who has watched the ground shift under several generations of design, and his lessons carry that long view. He defines complexity as interconnection that hides logical structure rather than as the amount of stuff, and treats a design principle as valuable precisely because it settles hundreds of small decisions nobody could argue individually. A structural property, he warns, decays through additions that individually violate nothing, so audit the property rather than the changes. On protection his position is unusually concrete: hierarchy is right for organizing control and wrong for organizing authority; to control an operation, guard the values it accepts instead of the actors permitted to perform it; prefer restrictions that make the forbidden thing unnameable over restrictions that merely catch the attempt; and treat a convenience pool of ambient authority as invisible overprivilege whose harmlessness is relative to a threat model you may later change. He repeatedly insists on making trades explicit rather than tasteful — put a number on how much extra you would pay for uniformity, design the principled version first so every economy afterwards has a visible price, and count the problems a design makes impossible to state rather than only the features it provides. Two observations reward anyone doing long-horizon work: refuse to build a craft around a constraint you expect the technology to remove, and expect a long, demoralizing gap between demonstrating a principle and being able to exploit the technology that makes it practical.
