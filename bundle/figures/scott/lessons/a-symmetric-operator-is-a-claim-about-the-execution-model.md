---
type: lesson
title: "A symmetric operator is a claim about the execution model, not just a truth table"
figure: scott
works: [a-type-theoretical-alternative-to-iswim-cuch-owhy]
axes: [parallelizability, expressiveness, hardware-affinity, primitive-count]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency, foundations-of-computation]
tags: [lesson]
---
# A symmetric operator is a claim about the execution model, not just a truth table

**Lesson:** Once a language admits an undefined value, its operators split into ones that can be evaluated by examining arguments in a fixed order and ones that cannot, and the split is visible in a property that looks purely algebraic: symmetry in the arguments. An operator that returns a definite answer whenever *either* argument is definite, without caring which, cannot be implemented by inspecting the first argument and then the second, because the first inspection may not terminate while the answer was available from the second all along. Honoring the operator's stated behavior therefore requires advancing both computations together and taking whichever resolves. The truth table did not mention concurrency; it entailed it.

This is why an operator has to be evaluated against the execution model it commits you to, not only against whether it seems reasonable. The candidate here is well-behaved by every local test — it is monotone in the information ordering, it is definable by three tidy equations, and together with negation it generates every monotone truth function of any arity, which is a real expressiveness argument for including it. It also changes the answer to what counts as computation in the whole language: an ordinary recursive definition that happens to use it forces two subcomputations to run in step, which is a different flavor of algorithm from the one-step-at-a-time reckoning everything else in the system rests on. Scott raised exactly that objection, could not settle it, and left it as an open question rather than pretending the operator was free.

The transferable habit is to look at every primitive you are considering adding and ask what evaluation order it permits, because that is where the cost hides. Asymmetric operators fix an order and stay compatible with sequential implementation. Symmetric ones give more expressive power and buy it with a commitment that propagates to every program written in the language, not merely the ones that use the feature — the runtime now has to be able to interleave, whether any particular program needs it or not. Either answer can be right. Choosing without knowing which one you picked is what to avoid.

**Source:** [A Type-Theoretical Alternative to ISWIM, CUCH, OWHY](../works/a-type-theoretical-alternative-to-iswim-cuch-owhy.md) — Section 4's discussion of the symmetric monotone disjunction on the three-element truth domain: its axiomatization, the observation that it and negation define all monotone truth functions, and the worked recursive definition whose evaluation requires computing two functions in parallel and stopping at whichever answers, which Scott flags as a different flavor of algorithm he is not sure should count as computable.
