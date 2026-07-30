---
type: lesson
title: "When a normalization removes a parameter, find where the cost went before calling it a simplification"
figure: vardi
works: [on-the-complexity-of-bounded-variable-queries]
axes: [primitive-count, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# When a normalization removes a parameter, find where the cost went before calling it a simplification

**Lesson:** There is a standing temptation, when one construct in a formalism is making things expensive, to reach for a known theorem that eliminates it — collapse the alternating constructs into a single one, desugar the awkward feature into the primitive one, normalize the irregular form away. The elimination is real. What is easy to miss is that the cost did not vanish; it was relocated into some other parameter of the same problem. Vardi checks exactly this and finds the collapse buys nothing: removing nesting depth inflates the width of what remains, in direct proportion to the depth removed, and the evaluation cost is exponential in width just as it was in depth.

The discriminating question is which parameters are fixed and which are free. Nesting depth is a property of whatever query someone happens to write, so it varies without bound; the name cap is a design constant chosen once. Trading an exponent in a design constant for an exponent in a user-supplied quantity is a strict loss, even though the count of distinct constructs went down and the formalism got smaller. Fewer primitives is a genuine good — but only when the reduction does not smuggle the eliminated structure back in as size, and it very often does. A transformation that preserves meaning tells you nothing about whether it preserves tractability.

So build the reflex: after any normalizing rewrite, name every parameter the cost depends on, before and after, and mark each as fixed-by-design or supplied-by-the-caller. If the rewrite moved weight from the first column to the second, you have made the artifact prettier and the system worse. The same audit catches monomorphization that trades code size for dispatch cost, inlining that trades instruction cache for call overhead, and denormalization that trades join width for update fanout. In each case the honest verdict comes from knowing which of the two quantities the world is allowed to grow.

**Source:** [On the Complexity of Bounded-Variable Queries](../works/on-the-complexity-of-bounded-variable-queries.md) — the discussion following the naive nested-fixpoint evaluation, which considers using the known results that collapse alternating fixpoints into a single one, and rejects the approach because the collapse raises the arity of the resulting fixpoint in proportion to the alternation depth, leaving a cost exponential in a quantity that, unlike the variable bound, is not fixed.
