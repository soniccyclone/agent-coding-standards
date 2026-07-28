---
type: work
title: "A Language with Distributed Scope"
figure: cardelli
description: Presents Obliq, a lexically-scoped, interpreted language for distributed and mobile computation where object references — not just data — can migrate between address spaces while their scoping rules stay intact. It works out how to keep a coherent notion of lexical scope alive across network boundaries, a problem that vanilla distributed-object systems of the era mostly punted on. Obliq's distributed prototype-object model influenced later work on mobile code and ambient calculi.
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
year: 1995
url: http://lucacardelli.name/Papers/Obliq.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# A Language with Distributed Scope

**Venue/year:** Computing Systems 8(1), January 1995, pp. 27-59 (preliminary version: POPL'95, ACM Press, pp. 286-297). Related SRC Research Report 122 (1994), "Obliq: A Language with Distributed Scope," is also self-archived at the same site.
**Source:** http://lucacardelli.name/Papers/Obliq.pdf — self-archived on Cardelli's own site (verified 200, application/pdf).

## Lessons
- [Choose the one invariant that must survive the boundary, and let the rest of the design be forced by it](../lessons/carry-one-invariant-across-the-boundary-and-derive-the-rest.md)
- [When code moves, move its environment with it, because the worst failure is the one that succeeds with the wrong meaning](../lessons/ship-the-environment-not-the-text.md)
- [Before adding a mechanism, check whether a distinction the system already maintains can carry the new job](../lessons/get-the-second-mechanism-free-from-a-distinction-you-already-keep.md)
- [Fix what is not allowed to move, then build motion out of ordinary operations instead of a migration feature](../lessons/decide-what-must-not-move-then-program-the-motion.md)
- [Derive the organizing construct from what you already have, and its preconditions become visible instead of built in](../lessons/derive-the-organizing-construct-instead-of-building-it-in.md)
- [Separate the guarantee you require from the moment you establish it, and pick the moment per boundary](../lessons/when-you-check-is-not-what-you-guarantee.md)
