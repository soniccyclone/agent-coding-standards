---
type: figure
title: Kenneth L. McMillan
description: b. ~1962, CMU/Cadence/MSR/UT Austin. Invented symbolic model checking, solving the state-explosion problem.
status: accepted
layer: implementation-mapping
subdomains: [formal-methods-and-verification]
tags: [figure, accepted]
---

# Kenneth L. McMillan

**Dates:** b. ~1962. American computer scientist, CMU/Cadence/Microsoft Research/UT Austin.

## Why a candidate
Invented symbolic model checking (BDD-based), solving the state-explosion problem that had capped explicit-state model checking to toy systems and enabling industrial hardware verification; later pioneered SAT/interpolation-based unbounded model checking.

## Top 10 most influential works
1. "Symbolic Model Checking: An Approach to the State Explosion Problem" (1992, CMU PhD thesis) — `public` (institutional repository)
2. "Symbolic Model Checking" (1993, book) — `paywalled`
3. "Symbolic Model Checking for Sequential Circuit Verification" (1994, with Clarke, Grumberg) — `paywalled`
4. "Interpolation and SAT-Based Model Checking" (2003, CAV) — `public` (self-archived at Berkeley)

## Lessons

McMillan's corpus teaches a consistent way of attacking a problem that looks like a wall. The state explosion is not defeated by a cleverer search but by refusing the framing that makes it inevitable: cost should track how intricate a system's description is, not how many configurations that description admits, so the leverage lies in the representation of sets and relations rather than in the algorithms running over them — change the substrate once and every fixed-point procedure above it inherits the win. From there the lessons are a catalogue of commitments declined. Do not assemble an object you only need to interrogate, and remember that your ceiling is the worst transient rather than the final answer. Do not order events nobody asked you to order, or analyse configurations the system cannot enter, or let a modelling convenience impose correlations the artefact does not have. Where exactness is unaffordable, be deliberately loose and pay for it with a convergence argument rather than optimism, and let the placement of a cut decide the vocabulary in which derived facts may be phrased. Running underneath is an unusually clear-eyed epistemology of tools: a solver's refusal is a reusable argument rather than a bit, a concrete witness outranks a proof because it inherits none of your modelling assumptions, sampling fails structurally rather than merely weakly against bugs needing long coordinated sequences, and human structural intuition belongs wherever search is expensive — supplied as a guess the machine validates, never as a claim it trusts. The engineering discipline matches: put guarantees in the notation so the restricted sublanguage is the default path, choose a one-directional comparison over an equivalence when you need to generalise across sizes and know which half of your requirements survives, and defend a scalability claim with the exponent of a parameterised family instrumented well enough to explain itself, never with a benchmark time.
