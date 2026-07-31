---
type: figure
title: Dana Scott
description: b. 1932, Oxford/CMU. Invented domain theory - rigorous mathematical foundation for denotational semantics; Turing Award 1976.
status: accepted
layer: design-thought
subdomains: [programming-languages-and-semantics]
tags: [figure, accepted]
---

# Dana Scott

**Dates:** b. 1932. American mathematician/logician, professor at Oxford then Carnegie Mellon.

## Why a candidate
Invented domain theory (complete partial orders), giving denotational semantics a rigorous mathematical foundation for recursively defined program meaning — the semantic partner to Church's syntactic calculus.

## Top 10 most influential works
1. "Toward a Mathematical Semantics for Computer Languages" (1971, with Strachey) — `public` (CMU/CiteSeerX)
2. "Outline of a Mathematical Theory of Computation" (1970) — `uncertain`
3. "Data Types as Lattices" (1976, SIAM J. Computing) — `paywalled`
4. "A Type-Theoretical Alternative to ISWIM, CUCH, OWHY" (written 1969, published 1993) — `uncertain`/`paywalled`
5. "Logic and Programming Languages" (1977 Turing lecture) — `uncertain`
6. "Lattice Theory, Data Types and Semantics" (1972) — `uncertain`

## Lessons
Scott's characteristic move is to stop arguing about notation and put the space of values on the table first. Meaning gets its own account, owed nothing to any implementation, because only such an account can judge an implementation at all; and each construct is given a meaning of its own rather than explained by translating it away. Where a definition is circular he takes its meaning to be the least thing satisfying it, and where objects are infinite he earns them as limits of finite ones. The recurring discipline is to be exact about what a construction actually delivers: existence without uniqueness is a construction rather than the abstraction you wanted, solving an equation by iteration does not name a unique answer since the starting point is part of the design, and a construction closed enough to solve your equation will admit objects you did not intend. He is unusually attentive to the status of one's own assumptions — before accepting a restriction, find out whether the mathematics forces it or you inherited it as caution; an impossibility result indicts a background assumption rather than the thing you wanted; an axiom your model refutes may be one you are better off without. His treatment of partiality is the emblematic case: make undefinedness an ordinary value ordered by how much it tells you rather than a hole outside the type, give conflict its own value, and never confuse conflicting with merely unrelated. Two habits generalize far past semantics — audit afterward which part of a borrowed theory you actually used, and treat being forced to store a representation instead of the thing as a report of a missing structure.
