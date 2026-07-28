---
type: lesson
title: "Buy tractability with deliberate imprecision, then pay for it with a convergence argument"
figure: mcmillan
works: [interpolation-and-sat-based-model-checking]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# Buy tractability with deliberate imprecision, then pay for it with a convergence argument

The step that made SAT-only unbounded checking work is a step that looks like giving up: the reachable-state computation is replaced by something known to be too big. The set it produces contains states the system cannot actually enter. That is a real loss — it can make the checker claim a bad state is reachable when it is not. The classical alternative computes the exact set and is correspondingly exact, and it is the exact version that runs out of memory on industrial designs.

What licenses the trade is not optimism but a proof about the limit. The over-approximation is not arbitrary: it is constructed so that it cannot reach the bad state within the horizon the search was run to, and that single guarantee is enough to show that as the horizon grows, the procedure must eventually settle into either a genuine counterexample or a genuine invariant. Imprecision is thus made safe by an argument about what happens as a parameter increases, rather than by making any individual step precise. The approximation error is real at every step and vanishes in aggregate.

The design also refuses to pretend. When the loose set produces an ambiguous situation, the procedure does not guess — it stops and reports that this horizon was insufficient, and the caller enlarges it. Admitting a third outcome besides yes and no is what keeps the method sound while remaining sloppy, and it converts an accuracy problem into a scheduling problem: how aggressively to grow the horizon, where too small wastes runs and too large makes each run intractable. The same paper is candid that a performance tweak which pushes further in this direction sacrifices the termination guarantee outright, and that this showed up as observed divergence on a couple of real circuit models — a reminder that the convergence argument is the thing paying for the imprecision, so weakening it has to be a priced decision, not a free speedup.

A programmer who internalises this stops treating approximation as a compromise of last resort and starts treating it as a design axis with an explicit invoice. The questions become: which direction does my error point, is that direction the safe one for my use, what parameter drives the error to zero, and what does the system do when it cannot tell? A procedure allowed to answer "not yet" honestly beats one forced to answer and therefore forced to be exact.

**Source:** [Interpolation and SAT-Based Model Checking](../works/interpolation-and-sat-based-model-checking.md) — the over-approximate image operator and the accompanying termination result, together with the section on optimisations that notes which speedups forfeit the guarantee.
