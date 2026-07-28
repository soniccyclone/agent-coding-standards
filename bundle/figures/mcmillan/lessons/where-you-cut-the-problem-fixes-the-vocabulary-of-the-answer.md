---
type: lesson
title: "Where you cut the problem fixes the vocabulary the answer can use"
figure: mcmillan
works: [interpolation-and-sat-based-model-checking]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Where you cut the problem fixes the vocabulary the answer can use

The technical hinge of interpolation-based checking is a property that sounds like a limitation and turns out to be the whole point: the derived fact may only mention the symbols that both halves of the split problem share. Everything private to one side is unmentionable. So the engineer's real design decision is not the algorithm but the placement of the cut — put it between the first transition step and all the rest, and the shared symbols are precisely the machine's state after one step, so the fact you get back is a statement about reachable states. Slide the cut somewhere else and the derived fact would be about something else entirely.

This inverts the usual relationship between a decomposition and its results. Normally you decompose a problem to make each piece tractable and treat the interface as bookkeeping. Here the interface *is* the specification of the output: the shared vocabulary is a filter that forces the answer to be phrased in the terms you care about and forbids it from leaking the internal machinery of either side. You get abstraction not by asking for it, and not by writing an abstraction function, but by choosing what the two halves are allowed to say to each other.

Why it holds is a matter of information flow. If a fact were permitted to reference a symbol living on only one side, it could not serve as a summary — it would be a fragment of one side's internals, useless to the other. Restricting to the common alphabet is exactly the condition that makes a fact a legitimate interface between the parts. The strength of the resulting abstraction is then bounded by how narrow the shared alphabet is, which is why the choice of where to slice is a substantive engineering judgement rather than a formality.

The transferable habit: when you split a system, ask what the seam permits either side to say, and recognise that this determines the shape of every summary, invariant, log line, or contract that can ever cross it. If the answers coming out of a decomposition are the wrong kind of thing, do not patch the algorithm — move the seam. And when you want a module boundary to yield useful, implementation-independent facts, deliberately keep its shared vocabulary small, because the narrowness is what does the abstracting.

**Source:** [Interpolation and SAT-Based Model Checking](../works/interpolation-and-sat-based-model-checking.md) — the definition of an interpolant and the accompanying discussion of how the unrolled bounded problem is partitioned so that the shared variables are exactly the state after a single transition.
