---
type: lesson
title: "Keep the description unmaterialized until a step cannot be absorbed"
figure: wirth
works: [project-oberon]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, algorithms-and-complexity]
tags: [lesson]
---
# Keep the description unmaterialized until a step cannot be absorbed

**Lesson:** When a chain of refinements is applied to something — select a part, then index into it, then follow a reference, then read it — the naive producer performs each refinement as it is requested, so every step in the chain costs a step of work. The better arrangement is to carry a *description* of what has been selected so far and to try, at each refinement, to fold the new step into the description rather than perform it. Folding costs nothing; performing costs a step. So the algorithm is: never do the work while there remains a chance the next request can be absorbed, and materialize only when a request arrives that the current description cannot express.

What makes the discipline strict rather than merely preferable is that emission is a one-way door. Work already handed to the consumer cannot be withdrawn, so a step performed prematurely also destroys the opportunity to fold everything downstream of it into the same description. The cost of being eager is therefore not one wasted step but the collapse of the whole remaining chain into step-per-refinement. This is why the check has to come first in each case: establish that the situation cannot be handled by folding, and only then emit.

The design artifact that makes this reviewable is a table of transitions — for each current description and each kind of refinement, what the description becomes and whether anything was emitted. Writing it out has three payoffs beyond documentation. It shows at a glance which combinations are free and which are not, so the expensive paths can be counted rather than guessed at. It makes the analysis exhaustive by construction, since a blank cell is a case someone forgot. And it is exactly where a gap in the consumer's repertoire becomes visible: a transition that ought to be free but is not, because the destination happens to lack the one form that would express it, shows up as a lone exception in an otherwise regular table, and an exception you can point at is one you can decide about instead of one that silently degrades everything routed through it.

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.7's account of code selection, which states that the goal is to use all addressing modes the computer offers so as to avoid emitting unnecessary address-computation instructions, that this requires detecting the applicability of complex addressing modes and not emitting address computations before it is established that the situation cannot be handled by an available addressing mode, and that the Index, Field and DeRef procedures contain the necessary case analyses; together with the four tables of item mode transitions listing, for each starting mode and construct, the resulting mode and whether an instruction is emitted, and the note that one transition is inapplicable for external access because the processor lacks an indirect external addressing mode.
