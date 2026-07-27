---
type: lesson
title: "A specification only becomes a definition when the rules for deriving its answers ship with it"
figure: godel
works: [on-undecidable-propositions-of-formal-mathematical-systems]
axes: [verifiability, expressiveness, primitive-count]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# A specification only becomes a definition when the rules for deriving its answers ship with it

**Lesson:** Gödel arrives at the general notion of a computable function by repairing a proposal that was almost right. The proposal: write down a system of equations relating a new, unknown function to functions already accepted, and if those equations pin the unknown function down uniquely, call it computable. The repair is small in text and decisive in force. Uniqueness of a solution is a claim about the mathematical universe; it does not tell you how to get an answer for a given input, and it can hold while no procedure exists. So Gödel replaces it: for every tuple of arguments, exactly one value must be *derivable* from the equations by fixed rules of substitution and replacement. The object of the definition is no longer a function that happens to satisfy constraints, but a rewriting process that terminates with a unique numeral. He notes the same standard at the outset when characterizing formal systems generally — a system counts as formal only if there is a finite procedure to decide whether a string is well-formed, whether it is an axiom, and whether one string follows from others by a rule.

The distinction is the one between declarative intent and executable meaning, and it recurs constantly in practice under other names. A schema that says which documents are valid but offers no validation algorithm; a constraint set that names the solution but hands you no solver; a type system whose rules describe well-typed programs but for which no inference procedure is known; an API contract stated as an invariant with no way to check it. All of these are *specifications with a hole in them*, and the hole is exactly where Gödel put the requirement: the derivation. It is easy to convince yourself the hole is not there, because uniqueness feels like determinacy — if only one answer can be right, surely we can find it. That inference is invalid, and the gap between the two is where a large amount of engineering effort actually lives.

Two further things follow from Gödel's treatment. First, the derivability requirement carries a termination story with it: the arguments must be arrangeable so that computing any one value needs only values at earlier positions. Well-foundedness is not an extra nicety, it is what makes the recursion a definition rather than a wish. Second, the *schema* you permit determines the class you get — he observes that recursion on two arguments simultaneously escapes the class definable by recursion on one, so "defined by recursion" is not a single notion but a family, and which family you have chosen is a substantive design decision rather than a detail.

The practical upshot: when you write a specification, name the procedure that resolves it and the ordering that makes the procedure terminate, or state honestly that you have written a constraint rather than a definition. And when reviewing someone else's declarative design, the question that finds the trouble is not whether the semantics are well-defined but whether anything can compute them.

**Source:** [On Undecidable Propositions of Formal Mathematical Systems](../works/on-undecidable-propositions-of-formal-mathematical-systems.md) — the final section introducing general recursive functions, where the inherited "unique solution" criterion is replaced by derivability of a unique value under explicit rules, together with the opening section's insistence that a formal system's well-formedness, axiomhood, and inference relation each be settled by a finite procedure.
