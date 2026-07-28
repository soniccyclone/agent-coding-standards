---
type: lesson
title: "Make checking decidable even when finding is not, or the check itself will need checking forever"
figure: church
works: [introduction-to-mathematical-logic]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Make checking decidable even when finding is not, or the check itself will need checking forever

Church imposes four effectiveness requirements on any system he is willing to call a language: you must be able to decide whether a given symbol is one of the primitives, whether a given string is well formed, whether a given well-formed string is an axiom, and whether a proposed one-step inference obeys the rules. From those four it follows that checking whether a sequence of formulas is a proof is decidable. And he immediately points out the asymmetry that makes this interesting: it does not follow, and generally is not true, that you can decide whether a formula *has* a proof. Recognizing a solution is required to be mechanical; finding one is allowed to be arbitrarily hard.

The argument for the requirements is not a taste for tidiness, and this is the part worth stealing. Suppose deciding well-formedness were not effective. Then when someone asserts something, the hearer cannot tell whether an assertion has been made at all, so may reasonably demand a demonstration that the utterance is well formed. That demonstration has to accompany the utterance to do its job, which means it is really part of the utterance — and now the definition of well-formedness has to be revised to include it, at which point either the revised notion is decidable or the hearer demands a demonstration one level up. The same regress runs for proof: if proofhood cannot be checked, a proof no longer carries conviction, and every alleged proof needs an accompanying proof that it is one. Non-effective checking does not make verification expensive; it makes verification never terminate.

The design consequence is that a system's checkable surface is a deliberate construction, not a byproduct. Church accepts real inconvenience for it — including infinitely many primitive symbols and infinitely many axioms, which are fine precisely because they can be specified by a finite rule that answers membership questions mechanically. Infinite is acceptable; undecidable is not. What matters is that every question a recipient must answer to accept an artifact has a mechanical answer.

A programmer who works this way separates the hard part from the checkable part on purpose: let the search, the optimizer, the inference engine, or the human be as clever as it likes, and require its output to arrive in a form a small, dumb, terminating validator can accept or reject. Type annotations that make inference unnecessary at the boundary, a schema for the payload, a signature over the artifact, a machine-checkable certificate accompanying an expensive computation — all are instances. The failure to avoid is a validation story that itself needs judgment to apply, because then nothing has been validated; the obligation has just been moved one level up, where it will be moved again.

**Source:** [Introduction to Mathematical Logic](../works/introduction-to-mathematical-logic.md) — the section on the logistic method, which lays down the four effectiveness requirements on a primitive basis, notes that proof-checking is thereby decidable while theoremhood need not be, and defends the requirements by the regress that arises when well-formedness or proofhood cannot be effectively recognized.
