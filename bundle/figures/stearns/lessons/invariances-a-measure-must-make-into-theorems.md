---
type: lesson
title: "A cost measure earns trust by the invariances it turns into theorems"
figure: stearns
works: [its-time-to-reconsider-time]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# A cost measure earns trust by the invariances it turns into theorems

**Lesson:** Before defining any measure of cost, write down the transformations under which it must not change. A machine-level step count has no principled conversion into seconds, and even if one existed the conversion would move with each hardware generation, so any measure that distinguished a bound from twice that bound would be reporting an artifact of the encoding as a property of the problem. The right test of a definition is therefore whether the required insensitivity falls out as a consequence rather than being asserted alongside it. A definition from which the invariance must be proved, unforced, is one you can build on; a definition that needs the invariance bolted on as a convention will leak the discarded detail back in wherever the convention is forgotten.

Note carefully what such an invariance does and does not claim. Declaring a measure blind to constant factors is a statement about the layer the measure lives at, not a claim that constant factors are unimportant — they matter enormously in practice, and two programs with identical asymptotic cost are not interchangeable. The discipline is to keep the two concerns in separate vocabularies so that neither contaminates the other: the coarse measure gives you facts that survive re-implementation, and the fine measure gives you facts about the artifact in front of you. Confusion arises only when a result proved at one level is quoted as advice at the other.

The harder and more instructive case is an invariance you wanted and did not get. When richer machine variants gave measurably different classifications, there were two available responses: patch the model until the differences vanish, or find the coarsest level at which the property genuinely holds and relocate the concept there. Measuring the spread and discovering it was bounded by low-degree polynomial change licensed the second, and the field redefined the property to mean invariance under all models polynomially related to each other — after which only concepts robust at that granularity are allowed to carry weight. That is the general move: do not pretend a distinction is meaningful at a resolution where your abstraction cannot support it; establish the resolution empirically, then confine your claims to it.

**Source:** [It's Time to Reconsider Time](../works/its-time-to-reconsider-time.md) — the speed-up theorem and the commentary immediately after it, arguing that only the order of the bound is meaningful because transitions have no fixed relation to seconds and seconds vary with technology, that this falling out of the definition was itself evidence for the definition, and that constant factors nonetheless matter in practice; followed by the passage where the model's lack of machine independence is resolved by measuring the discrepancy and redefining the property as invariance under polynomially related models.
