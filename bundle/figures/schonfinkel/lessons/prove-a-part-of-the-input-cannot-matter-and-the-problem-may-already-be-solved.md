---
type: lesson
title: "Prove a part of the input cannot matter, and the problem may already be solved"
figure: schonfinkel
works: [entscheidungsproblem-der-mathematischen-logik]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [formal-methods-and-verification, foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Prove a part of the input cannot matter, and the problem may already be solved

The hard case of the paper — an existential quantifier standing before a universal one, with genuine two-argument relations inside — is dispatched by an erasure. The criterion for the disjunction being valid is that some atomic component occurs in it both negated and unnegated. The authors then examine the components that mix the two variables, the ones that record a relation holding between distinct individuals, and show that such a component can appear in only one of the disjuncts, and within that disjunct always at a single polarity, because the normal form they chose has that property. A symbol that cannot appear at both polarities can never satisfy the criterion. Therefore it can never affect the outcome, and every occurrence of it may be struck out.

What survives the erasure is a formula in which the relations only ever compare an individual with itself — which is to say, no relations at all, just predicates. The main case has become an instance of the case solved earlier in the paper, and with it inherits the earlier finite bound and the freedom from any fixed domain size. Nothing was approximated. The reduction is exact and it was obtained not by finding a clever encoding of relations into predicates, but by proving that the relational part of the input is inert with respect to the question being asked.

That is a different and more powerful move than simplification. Simplification makes an input smaller while preserving meaning; this makes an input smaller by proving that part of its meaning is unobservable through the specific decision you are performing. The proof is local and syntactic — count where a symbol occurs and at what polarity — and its payoff is global, because the residue lands in a class with a known algorithm. Program slicing, cone-of-influence reduction before a model check, dead-parameter elimination, and dropping columns a query provably never reads all have this structure, and all of them are worth attempting before you attack the full problem, because they sometimes do not merely shrink it but retire it.

The working heuristic follows from what made the erasure detectable: it worked because the representation had been canonicalized first, so polarity was fixed and countable. Irrelevance arguments are usually invisible in an arbitrary representation and obvious in a normalized one. So normalize, then ask of each ingredient what would have to be true for it to change the answer, and check whether the representation makes that impossible. When it does, delete without ceremony, and look hard at what remains — the residue is often something you already know how to decide.

**Source:** [Zum Entscheidungsproblem der mathematischen Logik](../works/entscheidungsproblem-der-mathematischen-logik.md) — section 4, where the mixed-argument components are shown to occur in only one disjunct at a single polarity, are therefore struck from the distinguished conjunctive normal form, and the remaining formula is recognized as a pure predicate formula already handled in section 2.
