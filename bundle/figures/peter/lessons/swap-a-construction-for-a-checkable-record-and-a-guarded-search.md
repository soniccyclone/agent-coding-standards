---
type: lesson
title: "Swap a construction for a checkable record plus a search you can guarantee"
figure: peter
works: [uber-die-mehrfache-rekursion]
axes: [verifiability, expressiveness, parallelizability]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Swap a construction for a checkable record plus a search you can guarantee

However deeply nested and multi-dimensional a recursive definition is, the act
of evaluating it at one point leaves behind a finite trace: a list of
argument-tuples paired with the values reached, where every entry is either a
base case or justified by entries already in the list. Péter's closing move —
crediting von Neumann for the argument, and noting it is more elegant than the
route she originally took — is to treat that trace as the primary object. Being
a valid trace is a purely local property: check each entry against the defining
equations and against earlier entries. Local checks over a finite object are
cheap to define, so the property "this number codes a valid computation of the
function at these arguments" lands in the weakest layer of the hierarchy, no
matter how strong the function was. The function itself then has a uniform
shape: search for a trace, read the answer off it.

The whole gradation of recursive strength therefore compresses into one
weak-layer relation plus one search. That is a striking relocation of difficulty.
Complexity that appeared to live in the definitional machinery turns out to live
only in *finding* the trace; recognizing one is easy. Péter is disciplined about
the search half: she permits the least-witness operator only where a procedure
for producing a witness is supplied alongside it, and pins down the value
otherwise. The search is a notational convenience backed by an existence proof,
never an appeal to luck, and the existence proof is done separately and
explicitly.

This is the certificate discipline, arrived at in the 1930s and now everywhere
worth using. Prefer designs where the hard part emits an artifact whose validity
a simple, independent routine can confirm: the optimizer emits a plan the
checker validates, the solver emits an assignment, the compiler emits a proof
witness, the distributed protocol emits a decision certificate. The checker is
small, auditable, and — since the checks are local — trivially parallel, while
the producer can be as clever and untrusted as it likes. And the second half of
Péter's discipline is the half most often skipped: an unbounded search is only
honest when you have separately proved a witness exists and said what happens
if one does not. A search without that proof is not a definition, it is a hope.

**Source:** [Über die mehrfache Rekursion](../works/uber-die-mehrfache-rekursion.md) — the final section deriving the explicit form, where computations are coded as finite sequences of tuples, the property of being such a computation is shown to be recursive at the base level, and the function is recovered by least-witness search.
