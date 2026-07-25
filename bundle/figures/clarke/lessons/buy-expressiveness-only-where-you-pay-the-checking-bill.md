---
type: lesson
title: "Buy expressiveness only where you are willing to pay the checking bill"
figure: clarke
works: [automatic-verification-of-finite-state-concurrent-systems-using-temporal-logic-specifications, design-and-synthesis-of-synchronization-skeletons-using-branching-time-temporal-logic, model-checking-algorithmic-verification-and-debugging]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Buy expressiveness only where you are willing to pay the checking bill

**Lesson:** A specification language is not free to grow. The logic used for model checking restricts what may follow a path quantifier to a single temporal operator, and that restriction looks arbitrary until you price the alternatives. Allow an arbitrary linear-time formula after the quantifier and checking becomes PSPACE-complete. Allow only unnested operators, or only the eventuality operator, and it is still both NP-hard and co-NP-hard. Even the earlier attempt to permit an assertion that some path satisfies a conjunction of eventualities collapses into Hamiltonian path. Each syntactic liberty you grant is paid for on every single query, forever, by everyone who uses the language.

The subtler lesson is what to do when you genuinely need a capability the cheap language cannot express. Fairness is the case in point: restricting attention to executions where every process runs infinitely often is not expressible in the branching-time logic at all, and switching to a linear-time logic to get it would have surrendered the complexity result. The response was to leave the syntax alone and change the interpretation, redefining the path quantifiers to range only over fair paths. The extended logic looks identical on the page, the checking algorithm changes only in its treatment of strongly connected components, and the complexity bound survives. Expressive power was added at the semantic layer, where it cost a factor rather than an exponent.

That is the general move worth keeping: when a formalism is too weak, distinguish between enriching what can be written and enriching what the writing means. The first grows the primitive count and the search space; the second can sometimes deliver the same practical capability by narrowing the domain of quantification. The authors' own framing is telling — they judged the intractability of the richer logics to be a justification for staying inside the restricted one, rather than a defect to be engineered around.

None of this makes expressiveness unimportant. The Turing lecture argues the opposite, that being able to state the properties you actually care about is the precondition for the whole method mattering, and that convenience of expression, informal as it is, drove years of industrial logic design. The point is that expressiveness, succinctness, and cost trade against each other, and a language designer who does not know the exchange rate is guessing.

**Source:** [Automatic Verification of Finite-State Concurrent Systems Using Temporal Logic Specifications](../works/automatic-verification-of-finite-state-concurrent-systems-using-temporal-logic-specifications.md) — the fairness section, which moves fairness into the semantics rather than the syntax, and the extended-logics section, which prices each relaxation of the path-quantifier restriction. The 1981 paper's NP-hardness reduction makes the same point earlier; the Turing lecture's discussion of expressiveness, succinctness, convenience, and efficiency states the trade-off in general terms.
