---
type: lesson
title: "Test a formalism against the feature you would ban"
figure: strachey
works: [continuations-a-mathematical-semantics-for-handling-full-jumps]
axes: [expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Test a formalism against the feature you would ban

**Lesson:** The temptation when building a description method is to aim it at the constructs you approve of, and to treat the ugly ones as pathologies that a well-behaved language simply wouldn't have. That instinct produces frameworks that work beautifully on the examples chosen to demonstrate them and collapse on the first real system. The corrective is to take the single feature you find most distasteful, the one you would remove from the language if you had the authority, and make that the load-bearing test case for your framework. If the description survives it, the description is about meaning; if it only survives after you outlaw the feature, you had a description of your own taste.

Two separate moves make this discipline work. First, strip the test language down to almost nothing except the offending construct, so that no incidental richness can absorb the difficulty or let you fool yourself into thinking the hard part was handled. Second, keep the judgment about whether the feature *should* exist strictly apart from the requirement that it be *describable*. Approving of a construct and being able to say what it means are independent questions, and conflating them is how a formalism acquires an unadvertised normative agenda. A method powerful enough to give meaning to something you consider a mistake is a method whose adequacy you can actually trust.

This also inverts the usual relationship between theory and legacy. Existing languages, with all their accumulated irregularity, are not an embarrassment the theory must eventually be extended to cover — they are the pressure that keeps a mathematically-minded designer from smoothing away exactly the cases where the difficulty lives. The problems that resist your framework are the informative ones, and they get overlooked precisely because their significance is not obvious until the framework fails on them.

A programmer who takes this seriously builds type systems, effect systems, static analyses and specification languages against the constructs they wish weren't in the language, not against the subset they'd have designed. They notice when a proposal's soundness depends on a restriction that was introduced for the prover's convenience rather than the programmer's, and they treat "we exclude that case" as a claim about the method's limits rather than the language's.

**Source:** [Continuations: A Mathematical Semantics for Handling Full Jumps](../works/continuations-a-mathematical-semantics-for-handling-full-jumps.md) — the paper deliberately builds a language whose only real feature is the ability to transfer control at the worst possible moment, and its closing discussion insists that a construct the authors explicitly decline to endorse must still be within the descriptive reach of the semantics.
