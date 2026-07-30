---
type: lesson
title: "To show a description is realizable, build the artifact out of the descriptions themselves"
figure: vardi
works: [reasoning-about-knowledge]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# To show a description is realizable, build the artifact out of the descriptions themselves

**Lesson:** Two very different questions get confused constantly. One is syntactic: can this set of requirements be derived-from-nothing to a contradiction? The other is semantic: does anything actually exist that meets them? The gap between them is where most bad reasoning about specifications lives — a team argues that no rule is being violated and concludes a configuration must be achievable, or argues that they cannot picture a valid instance and concludes the requirements are inconsistent. Neither inference is free. Closing the gap requires an actual construction, and the trick worth stealing is that the construction can be made mechanical: take as the states of your model the maximal consistent descriptions themselves, one state per way of answering every question the language can ask without contradicting yourself. Each state is nothing but a total, coherent set of commitments; the transition or accessibility structure is then read off from those commitments rather than invented.

The reason this works is that it makes the model as coarse as the language and no coarser. A state has no content beyond what can be asserted about it, so there is nothing left to accidentally get wrong, and the proof that the construction satisfies exactly the intended description reduces to structural induction over the language. It also explains why one direction of such a proof is easy and the other is not: showing every derivable requirement is genuinely satisfied is a routine check, while showing every satisfiable requirement is derivable needs the construction, which is why the two halves of a soundness-and-completeness claim feel so lopsided in effort.

Two habits follow for ordinary engineering. First, when a rule is added to a system, ask what property it forces on the generated artifact — the canonical construction turns each added rule directly into a structural constraint, and if a rule cannot be traced to any such constraint it is decoration. Second, treat "I cannot derive a contradiction" as a weaker claim than "here is an instance," and reach for the mechanical instance-from-descriptions construction before hand-crafting an example, because a hand-crafted example proves only that one point exists while the construction proves that every non-contradictory description has one.

**Source:** [Reasoning About Knowledge](../works/reasoning-about-knowledge.md) — the completeness argument in the chapter on completeness and complexity, where a model is built whose states are the maximal consistent sets of formulas and the accessibility relation is defined from those sets, plus the subsequent demonstration that each additional axiom forces the corresponding structural property on that construction.
