---
type: lesson
title: "A canonical form with any freedom left in it is not canonical, and the fix belongs in the definition"
figure: curry
works: [some-additions-to-the-theory-of-combinators]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# A canonical form with any freedom left in it is not canonical, and the fix belongs in the definition

**Lesson:** Defining a normal form and proving that everything can be brought to one is only half a job, and the missing half is the half that pays. What makes a canonical form worth having is that two objects are the same exactly when their forms coincide, which requires the form to be unique — and a definition that constrains the shape of a representation without pinning down every remaining choice inside that shape does not deliver uniqueness. Curry returns to his own earlier definition for precisely this reason. The overall layout was fixed, but one block of it still admitted several different representatives for the same behaviour, so the theorem he could state was existence rather than existence-and-uniqueness, and the comparison test he wanted was unavailable.

The repair is instructive because of where he puts it. He does not add a post-hoc procedure for picking among candidate forms, and he does not weaken the claim. He tightens the definition, with two ingredients: an ordering condition on the indices of the factors, so that the factors must appear in a forced sequence rather than any sequence, and an explicit tie-break for the one genuinely underdetermined choice — of the several rearrangements that would do the job, take the one that leaves alone whatever is already in place. With those in the definition, uniqueness becomes provable, and the payoff arrives immediately: for every behaviour there is exactly one representative, and every well-formed object is provably equal to exactly one normal one. The decision procedure for equality is now "normalize both and look."

The habit this teaches is to treat "we canonicalize" as a claim requiring proof, and to attack residual freedom rather than route around it. Whenever a system reduces values to a normal representation — a canonical serialization used as a cache key, an intermediate representation used for common-subexpression elimination, a deduplication fingerprint, a config after defaults are applied — the question is not whether normalization terminates but whether it can produce two different outputs for the same value. If it can, every equality test downstream is quietly wrong, and the bug is unfixable at the comparison site because the comparator is being handed genuinely different data. The correct move is to find each degree of freedom the specification failed to constrain and constrain it, choosing an arbitrary but total tie-break where no principled one exists. Arbitrary and forced beats principled and ambiguous.

**Source:** [Some Additions to the Theory of Combinators](../works/some-additions-to-the-theory-of-combinators.md) — the first of the paper's two amendments, which revises the earlier definition of normal form by adding an index-ordering condition on the rearrangement factors plus a rule selecting a specific one among the admissible rearrangements, and then proves the one-to-one correspondence and unique-representative results the original definition could not support.
