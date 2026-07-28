---
type: lesson
title: "Trade nesting depth for index arithmetic"
figure: peter
works: [uber-den-zusammenhang-der-verschiedenen-begriffe-der-rekursiven-funktion]
axes: [expressiveness, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Trade nesting depth for index arithmetic

Nesting — a call whose argument is itself the result of a call at the same level — is the structural feature that makes a definition look irreducibly self-referential. Péter dissolves it by refusing to perform the substitution in one bound. Instead she stretches the computation out: every intermediate expression that the nested version would have produced implicitly becomes an explicitly numbered element of a single flat sequence, and the original values are located inside that sequence by a growth function computed alongside it. The nesting does not vanish; it is relocated into the bookkeeping that says which flat position corresponds to which original step.

The cost accounting here is the interesting part. Flattening is not free — the flat sequence grows far faster than the original index, and the price of the transformation is a small family of auxiliary functions that answer "which original step am I inside" and "how far back do I reach." But those auxiliary functions are drearily ordinary, defined by the weakest scheme available, while the structure they replace looked like it demanded something stronger. Structural complexity got converted into arithmetic on positions, and arithmetic on positions was already cheap.

A programmer who internalizes this stops treating recursion-shaped problems as requiring recursion-shaped machinery. Any nested computation can be turned into a loop over an explicit worklist with an addressing scheme, and the difficulty migrates entirely into getting the addressing right. That is why the transformation is worth knowing even when you would not choose it: it tells you where the real difficulty of an implementation lives. When someone claims a construct cannot be compiled away, cannot be expressed without a stack, or cannot be flattened, the question to ask is whether they have tried paying in index arithmetic — and whether they can define the addressing function, because that, not the nesting, is the actual obstacle.

**Source:** [Über den Zusammenhang der verschiedenen Begriffe der rekursiven Funktion](../works/uber-den-zusammenhang-der-verschiedenen-begriffe-der-rekursiven-funktion.md) — the treatment of nested recursion, which first reduces the general nested form to a narrow special case and then flattens that case by interleaving all intermediate substitution steps into one sequence with an explicit position-tracking function.
