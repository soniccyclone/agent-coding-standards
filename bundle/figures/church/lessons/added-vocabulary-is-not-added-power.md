---
type: lesson
title: "Added vocabulary is not added power: if its laws can be hypotheses and its names variables, the base language already had it"
figure: church
works: [a-note-on-the-entscheidungsproblem]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [foundations-of-computation, programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Added vocabulary is not added power: if its laws can be hypotheses and its names variables, the base language already had it

Church wants an unsolvability result about the bare predicate calculus, a system with no arithmetic in it at all. He does not attack it directly. He builds a fattened system by bolting on everything he needs — a constant for one, equality, successor, and symbols for the recursive functions that enumerate convertible expressions — plus the defining equations for all of it as new axioms. In the fattened system the hard result is already within reach. Then he takes the fat back off in two mechanical steps. The function symbols are traded for relation symbols describing their graphs, so no function vocabulary remains. And the added axioms are conjoined into a single formula whose added constants are replaced by fresh variables, so that a statement provable in the extended system corresponds exactly to an implication, from that formula to the translated statement, provable in the bare one.

The consequence is the interesting part. All that apparatus was never extra power; it was extra convenience. The base language could already say everything the extension said, by carrying the extension's laws around as an antecedent and its names as bound variables. Once that is established, hardness flows backward down the translation: if you could decide the poor system you could decide the rich one, so the poor system's undecidability follows from the rich one's. A faithful eliminative translation is simultaneously a proof that nothing was gained and a channel along which difficulty travels.

This is the sharpest available test for a claim that some feature must live in a system's core. If the feature's behavior can be stated as a set of assumptions and its identifiers turned into parameters, without changing which programs are expressible or which facts are provable, then the feature is notation and belongs outside the core. If it cannot — if some result holds with the feature and genuinely fails without it — that is real power, and you have learned what the core is actually for. Church's construction gives the shape of the argument in both directions.

A programmer who thinks this way responds to "we need to add a primitive for this" by first trying to write the primitive's laws as ordinary premises and its name as an ordinary argument. Most requests dissolve at that step, and the core stays small. They also use translations offensively: to prove some minimal language is hard enough to be dangerous, or expressive enough to be sufficient, they encode a system they already understand into it rather than reasoning about the minimal language from scratch.

**Source:** [A Note on the Entscheidungsproblem](../works/a-note-on-the-entscheidungsproblem.md) — the second half of the note, where the arithmetic-bearing system is stripped first of function symbols and then of its additional constants and axioms, yielding an implication in the bare functional calculus and transferring unsolvability to it.
