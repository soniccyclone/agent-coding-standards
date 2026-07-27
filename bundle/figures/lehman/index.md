---
type: figure
title: M.M. (Manny) Lehman
description: 1925-2010, IBM Research/Imperial College London. Laws of software evolution - empirical account of why large systems' complexity grows over time.
status: accepted
layer: implementation-mapping
subdomains: [software-engineering-and-architecture]
tags: [figure, accepted]
---

# M.M. (Manny) Lehman

**Dates:** 1925-2010. Worked at IBM Research, later Imperial College London.

## Why a candidate
The laws of software evolution are an empirically-derived account of why large systems' structural complexity increases over time absent deliberate counter-work — data-first reasoning about system-scale coupling, matching the vetting philosophy's preference closely.

## Top 10 most influential works
Small, tightly-focused body of work:
1. "Programs, Life Cycles, and Laws of Software Evolution" (1980, Proceedings of the IEEE) — `uncertain`
2. *Program Evolution: Processes of Software Change* (1985, book with Belady) — `paywalled`
3. "On Understanding Laws, Evolution, and Conservation in the Large-Program Life Cycle" (1980) — `uncertain`
4. "Metrics and Laws of Software Evolution — The Nineties View" (1997, with Perry, Ramil) — `uncertain`
5. "Software's Future: Managing Evolution" (1998, IEEE Software) — `uncertain`

## Lessons
Lehman's contribution to how to think about programming is to insist that a
long-lived system, the people changing it, and the world it operates in form
one coupled object with dynamics of its own, and then to study that object
empirically instead of theorizing about it. The starting move is to ask what
stands in judgment over a program before asking whether it is correct: where a
specification really is the last word, proof is available and the right leaf
modules can be made fully specified with the world's irreducible imprecision
parked at their boundaries; where the judge is a shifting reality, the program
is inside the situation it models, keeps invalidating its own requirements, and
formal correctness of the whole is beside the point. From there the corrosive
consequences follow: because editing software is nearly free, patching always
beats restructuring at every individual decision, so structural decay is the
default and only deliberate, unglamorous, feature-free expenditure holds it
back. Meanwhile the sizes of changes people can safely make are bounded not by
effort available but by how much re-understanding a batch forces on everyone
associated with the system, and a release exists precisely to manufacture the
one authoritative version that such understanding can attach to. What makes
this more than pessimism is the method: measure your own history with coarse
measures that mean the same thing to every observer, order it by causal
inheritance rather than the calendar, derive the process's own envelope from
it, and read proposed plans against that envelope rather than against
conviction. Hold the resulting regularities for what they are — statistical
claims about aggregate behavior, closer to biology than to physics, binding on
present practice yet possibly invalidated by being understood — and prefer
models that encode a mechanism you believe with the fewest parameters and the
quickest onset of predictive power. The deepest structural claim is that the
whole arrangement is a multi-loop feedback system, which is why decades of
genuine improvements to languages, methods, and tools moved outcomes so
little: the loops set the behavior, and the loops are where leverage lives.
