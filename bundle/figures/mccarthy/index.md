---
type: figure
title: John McCarthy
description: 1927-2011, Stanford. Borrowed Church's lambda notation for Lisp, though early Lisp's dynamic scoping diverged from the calculus's semantics until Scheme's fix decades later.
status: accepted
layer: design-thought
subdomains: [programming-languages-and-semantics]
tags: [figure, accepted]
---

# John McCarthy

**Dates:** 1927-2011. American computer scientist, Stanford professor, co-founder of the MIT and Stanford AI labs, coined "artificial intelligence."

## Why a candidate
Designed Lisp from a handful of primitives (`quote`, `cond`, `car`, `cdr`, `cons`, `atom`, `eq`, `lambda`) from which `eval` itself is built. Central to project-state.md §2's McCarthy→Russell tension/resolution (frozen) — this is the anchor figure for the Lisp lineage.

Correction (2026-07-24): McCarthy's own account ("History of Lisp," 1978, cited below) describes adopting lambda as convenient notation for functions, not a project to implement Church's formal reduction system. Early Lisp used dynamic scoping, which breaks the substitution semantics Church's calculus requires under nested abstraction (the FUNARG problem) — a real divergence, not just a simplification. Lisp didn't get lexical scoping, and genuine fidelity to lambda calculus, until Scheme (see [sussman](../sussman/index.md), [steele](../steele/index.md)), decades later. So: notation borrowed and clearly influenced by Church, not a direct translation of the calculus — contrast with [chuck-moore](../chuck-moore/index.md) (independent convergent invention, zero exposure) and [von-thun](../von-thun/index.md) (deliberate combinatory-logic derivation) as the other two points on this spectrum.

## Top 10 most influential works
1. "Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I" (1960, CACM) — `public` (self-archived on Stanford page)
2. "LISP 1.5 Programmer's Manual" (1962, with others) — `public` (Stanford/archive.org)
3. "A Basis for a Mathematical Theory of Computation" (1963) — `public` (Stanford AI memo)
4. "Towards a Mathematical Science of Computation" (1962, IFIP) — `public` (Stanford self-archived)
5. "History of Lisp" (1978/1981, ACM HOPL I) — `public` (self-archived)
6. "Programs with Common Sense" (1959) — `public` (self-archived)
7. "A Micro-Manual for Lisp — Not the Whole Truth" (1978/79) — `public` (self-archived)

All confirmed public — McCarthy self-archived nearly everything.
