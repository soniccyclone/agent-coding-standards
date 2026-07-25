---
type: lesson
title: "Assumptions are purchases; make them deliberately and stay willing to retract"
figure: chaitin
works: [the-limits-of-mathematics, an-invitation-to-algorithmic-information-theory, incompleteness-theorems-for-random-reals, meta-math-the-quest-for-omega]
axes: [verifiability, primitive-count]
subdomains: [formal-methods-and-verification, foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# Assumptions are purchases; make them deliberately and stay willing to retract

**Lesson:** If reasoning cannot produce content that its premises do not already carry, then the only route to conclusions with more content is to assume more. Chaitin draws the practical inference and presses it hard: a field that treats its assumptions as self-evident truths has given up the one mechanism it has for extending reach. He argues that assumptions should instead be adopted the way a physicist adopts a law, because it organises a large amount of experience, with the standing willingness to withdraw it when something contradicts it. That willingness is the part practitioners resist, because withdrawing an assumption invalidates work built on it.

The framing turns a philosophical stance into an accounting discipline. Each assumption has a price in risk and a yield in derivable conclusions, and both are estimable. Something long-standing and heavily exercised is cheap and probably yields a lot; something convenient and untested is expensive whatever it yields. The mistake is not assuming, it is assuming without noticing, so that the price is paid and the yield is never claimed, and nobody knows which conclusions rest on what.

Programmers do this constantly under other names. Every invariant asserted rather than checked, every precondition documented rather than enforced, every trusted boundary, every claim that a value cannot be absent, is an axiom bought with risk. Making the purchase explicit means writing down what is assumed, what it buys, and what observation would refute it, then treating a refutation as a retraction rather than a defect to be argued away. This is also where the corpus's other figures push back hardest, and the tension is real: Chaitin's position is that beyond a certain size the alternative to assuming is not proving, it is not knowing.

**Source:** [The Limits of Mathematics](../works/the-limits-of-mathematics.md) - the two lecture excerpts on experimental mathematics, which argue that to prove more one must assume more and compare adopting new axioms to a physicist adopting a new equation. Argued at greater length in the discussion section of [An Invitation to Algorithmic Information Theory](../works/an-invitation-to-algorithmic-information-theory.md), stated as the conclusion of [Incompleteness Theorems for Random Reals](../works/incompleteness-theorems-for-random-reals.md), and restated in the concluding chapter of [Meta Math! The Quest for Omega](../works/meta-math-the-quest-for-omega.md).
