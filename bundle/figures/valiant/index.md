---
type: figure
title: Leslie Valiant
description: b. 1949, Harvard. Defined #P for counting problems; formalized learning as a computational-complexity question (PAC learning).
status: accepted
layer: implementation-mapping
subdomains: [algorithms-and-complexity]
tags: [figure, accepted]
---

# Leslie Valiant

**Dates:** b. 1949. Hungarian-born British-American computer scientist, Harvard University.

## Why a candidate
Defined new complexity classes from first principles (#P for counting problems) and formalized learning itself as a computational-complexity question (PAC learning) — rigorous cost analysis applied to problem classes others hadn't formally modeled at all.

## Top 10 most influential works
1. "The Complexity of Computing the Permanent" (1979, defines #P-completeness) — `paywalled`
2. "A Theory of the Learnable" (1984, CACM, PAC learning) — `uncertain`
3. "A Bridging Model for Parallel Computation" (1990, CACM, BSP model) — `uncertain`
4. "Universal Circuits" (1976, STOC) — `paywalled`
5. "NP is as Easy as Detecting Unique Solutions" (1986, with Vazirani) — `paywalled`
6. "Evolvability" (2009, JACM) — `paywalled`
7. 2010 Turing Award lecture — `uncertain`

## Lessons
Valiant works by fixing what a model is allowed to see and how much it can move in one step, then reading the consequences off those limits. A bound on what a single step can span is what forces named intermediates into existence and sets their granularity; fixing the information channel and bounding its power from both sides comes before asking what is achievable at all. He is repeatedly concerned with charging cost to the right thing — to what actually appears rather than the size of the surrounding universe, and to the quantity an operation moves structurally rather than the one you happen to care about. Several lessons are about learning what kind of obstacle you have hit: classify which sort of barrier blocks you, because only some kinds can be engineered around; when a goal is proved unreachable, vary the goal's shape rather than reach for stronger tools; and notice that narrowing a specification to well-behaved inputs buys nothing until you show the hard inputs cannot be smuggled back in. His constructive techniques share a flavour of letting the mess cancel rather than preventing it — allow unwanted cases to annihilate and specify the piece that does it purely by its obligations, coarsen a question until a forbidden move becomes legal and let the precision you need cap the correction terms. The lesson that reaches furthest beyond theory is his rule for incremental progress: no step may be justified by a later payoff, so complexity has to arrive as a ladder of targets each worth reaching on its own.
