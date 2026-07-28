---
type: lesson
title: "Make a constraint a consequence of the encoding rather than a rule to be checked"
figure: post
works: [a-variant-of-a-recursively-unsolvable-problem]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Make a constraint a consequence of the encoding rather than a rule to be checked

Halfway through this reduction Post is stuck with an ugly attachment. He has boiled a known-hard question down to a single string equation, but only solutions meeting an extra length restriction correspond to real answers, and the target problem has no way to express such a restriction. The equation alone is the wrong problem; the equation plus a side condition is not the problem he is aiming at. Two familiar bad options present themselves: carry the condition along as a caveat and hope the target can absorb it, or weaken the claim to the conditional version. He takes neither. He reworks the encoding — reversing the strings, threading in a fresh symbol, closing the system under rotation — until every solution of the plain equation satisfies the restriction automatically, and the proof of that fact is an accounting argument on how many copies of the new symbol can appear on each side. The condition does not need enforcing because nothing can be built that violates it.

He does the same thing again for a different obstacle. The equation still mentions a specific starting and ending string, which the general form does not allow. Rather than special-casing them, he interleaves a marker symbol through every pair in a staggered pattern and adds two purpose-built pairs, arranged so that a doubled marker can only sit at the very start and the very end. Any solution is forced to begin with the opener and finish with the closer, because the first letters would otherwise not agree and the doubled marker would otherwise be followed by the wrong thing. The required shape is not requested; it is the only shape the alphabet permits.

The generalizable move is to convert validity rules into structural impossibilities by spending symbols. When you find yourself writing a constraint that a checker must enforce — this field is only meaningful when that flag is set, these two lists must stay the same length, this handle is valid only between open and close — you have the option of redesigning the representation so the invalid configurations cannot be written down. Tagged unions instead of a flag plus a nullable field; a pair list instead of two parallel lists; a token whose type carries its scope. The check disappears, and with it the possibility that some code path forgot to run it. The price is extra structure in the representation and a translation at the edges, which is exactly what Post pays.

The judgment call is when the price is worth it. Post's reason is decisive: the side condition was not merely inconvenient, it was inexpressible in the language his result had to land in. That is the strongest signal — a constraint that cannot be stated where it must be honored has to become structural or be abandoned. Short of that, the deciding question is how many independent places would otherwise have to remember to check.

**Source:** [A Variant of a Recursively Unsolvable Problem](../works/a-variant-of-a-recursively-unsolvable-problem.md) — the three-stage reworking of the normal system that turns the length condition into a consequence provable by counting occurrences of the added symbol, followed by the marker-interleaving construction that forces the initial and terminal pairs.
