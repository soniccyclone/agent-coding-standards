---
type: figure
title: Alan Kay
description: b. 1940, Xerox PARC/Apple/HP/VPRI. Coined "object-oriented programming," led the Smalltalk team, articulated objects/messages as a design philosophy.
status: accepted
layer: both
subdomains: [programming-environments-and-object-systems]
tags: [figure, accepted]
---

# Alan Kay

**Dates:** b. 1940. Computer scientist at Xerox PARC's Learning Research Group in the 1970s, later Atari, Apple Fellow, HP Fellow, founder of Viewpoints Research Institute.

## Why a candidate
Coined "object-oriented programming," led the team that built Smalltalk as a live, message-passing environment, and has written extensively and explicitly about objects/messages as a *design philosophy* distinct from computing as something explored, not compiled-and-run.

## Top 10 most influential works
1. "A Personal Computer for Children of All Ages" (1972) — `public` (mprove.de, ACM proceedings mirrors)
2. "Personal Dynamic Media" (1977, with Goldberg) — `public` (augmentingcognition.com)
3. "The Early History of Smalltalk" (1993, ACM HOPL II) — `public` (worrydream.com)
4. "STEPS Toward the Reinvention of Programming" (2007, with collaborators) — `public` (self-archived at vpri.org)
5. "The Reactive Engine" (1969 PhD thesis) — `uncertain`
6. "Microelectronics and the Personal Computer" (1977, Scientific American) — `paywalled`
7. "User Interface: A Personal View" (1990, book chapter) — `paywalled`

Strongest, most citable items are #1-3 and #4; rest thin into talks/interviews.

## Lessons
Kay's design instinct is to find the one mechanism a whole system is secretly made of, pick the element that stays meaningful at every level, and then refuse to let any part be weaker than the whole. That refusal is the load-bearing commitment: never divide a system into kinds of thing less capable than the system itself, make every capability equally reachable by hand and by program, and keep every object equally open to inspection. Where two categories differ only by rate rather than kind, collapse them and delete the subsystems the distinction required. He treats representation as consequential rather than cosmetic — a representation people internalize becomes invisible and reshapes their thinking, so it should be judged by the thinking it installs, and where a domain already has a picture everyone explains it with, that picture should be the program. Several lessons concern building for people whose needs you cannot enumerate: ship a medium plus exemplars instead of a feature list, make every convenient default visible and replaceable at every scope because a default is an absent designer's guess about you, and build on the ad hoc procedures people actually hold rather than the consistent axioms they do not. His method for attacking hard problems recurs — name the part you do not know how to do, build inward from both ends, and treat the intermediate models as instruments to be discarded. Two warnings sit alongside: a replacement must not be worse than the incumbent in any way its users care about and must not stop at imitating it, and a theory is a filter for judging candidates rather than a source of them, suppressing the obvious answer once you push it past its range.
