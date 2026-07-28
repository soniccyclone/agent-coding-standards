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
Designed Lisp from a handful of primitives (`quote`, `cond`, `car`, `cdr`, `cons`, `atom`, `eq`, `lambda`) from which `eval` itself is built — the anchor figure for the Lisp lineage, and the McCarthy side of this bundle's central McCarthy→Russell tension (see [tensions/resolutions](../../tensions/resolutions/index.md)).

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

## Lessons

Across twenty-nine lessons drawn from seven works, McCarthy teaches one governing habit: find the small closed set of things that generate the rest, then make everything else derived, stated, and inspectable. It starts as a search for a basis — a handful of operations from which the others follow by construction rather than decree, judged not by what it can express (any universal formalism can express anything) but by which operations it makes elementary and whether the changes you will want are small edits. It continues as a preference for one representation general enough to hold your own programs, so that the evaluator is an ordinary function and meaning can be given by the operations that take programs apart rather than by the notation people type. It becomes a discipline about specifications: the defining equation *is* the spec, undefinedness and evaluation order belong inside the semantics rather than in implementation lore, translation correctness is a commuting equation rather than a testing campaign, proofs should be conducted inside the system rather than about it, and you should deliberately specify less than you know so every refinement inherits the result. It becomes a discipline about honesty, too — publish a ladder of models and say which one answers which question, state the core completely and name what you left out, keep an explicit ledger of the features you cannot yet give semantics to, and remember that a symbol means exactly its rules and not its suggestive name. And it becomes a discipline about change: keep the general mechanism ignorant of the subject matter and put the judgment in what you feed it, extend by adding order-independent statements instead of editing procedures, build the channel by which a system can be *told* something before building the machinery by which it might learn, store only what structure cannot already derive, expose cost tiers as declarations instead of hiding one price, define liveness as reachability from a declared root set, and treat the fast compiled artifact as a cache whose only legitimate entry point for change is the definitions that generated it. Running underneath is a warning he learned the hard way and recorded himself: whatever runs first becomes the specification, so every provisional notation is a candidate permanent one.
