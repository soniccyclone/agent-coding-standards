---
type: figure
title: Richard E. Stearns
description: b. 1936, GE Research/SUNY Albany. Co-author of the founding paper of computational complexity theory.
status: accepted
layer: implementation-mapping
subdomains: [algorithms-and-complexity]
tags: [figure, accepted]
---

# Richard E. Stearns

**Dates:** b. 1936. American mathematician/computer scientist; General Electric Research (1961-78), then SUNY Albany.

## Why a candidate
Co-author (with Hartmanis) of the founding paper of computational complexity theory; later did foundational work with Harry Hunt on reducibility and equivalence problems. Same thin-corpus caveat as Hartmanis — consider vetting as a pair.

## Top 10 most influential works
1. "On the Computational Complexity of Algorithms" (1965, with Hartmanis) — `public` (AMS open backfile)
2. "A Regularity Test for Pushdown Machines" (1965/67, with Hartmanis) — `uncertain`
3. Work with Harry B. Hunt III on equivalence/containment problems (1970s-80s) — `paywalled`
4. "Hierarchies of Memory-Limited Computations" (1965, with Hartmanis, Lewis) — `uncertain`
5. 1993 Turing Award lecture — `uncertain`

## Lessons
Stearns is concerned with what a cost measure buys you and what it quietly hides. A measure earns trust through the invariances it turns into theorems, not through intuitive appeal, and every convenience admitted into a definition should be paid for with a theorem bounding what the convenience cost. The sharpest form of this is that what you refuse to charge for decides how finely you can see: a resource left unpriced is a distinction the theory can no longer draw, which is why the invariance you demanded can be the very thing that makes your question undecidable. He is equally insistent that the model be examined before the result — ask how well it fits before asking how hard the theorem was, and check which direction your formalism can even assert in before setting a goal it cannot state. Several lessons are about extracting structure from proofs rather than imposing it: let the argument tell you what the interface is, since the right abstraction is exactly the laws the proof consumed; toggle one structural freedom at a time to learn which one owns the limit; and to show something impossible, count what can be remembered against what must be distinguished. Where methods have incomparable costs he declines to choose, racing them instead because the pointwise minimum is nearly free — and where knowledge runs out he states the ignorance as precisely as the knowledge, mapping which unknown carries the others.
