---
type: lesson
title: "Decide whether your state is closed under its own consequences, because that decides what deletion means"
figure: vardi
works: [on-the-semantics-of-updates-in-databases]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [databases-and-data-management, foundations-of-computation]
tags: [lesson]
---
# Decide whether your state is closed under its own consequences, because that decides what deletion means

**Lesson:** Writing is easy to specify and unwriting is not, and the reason is that stored state is almost never a bare collection of independent items. Rules, constraints, and derivations mean that recorded items imply further items, so removing a record leaves an unanswered question about everything that record was supporting. Vardi's example makes the shape of the difficulty concrete: retract a three-way relationship and the three weaker two-way facts it entailed are now in limbo — still plausibly true, no longer justified, and with no operation in the vocabulary that says which. Any system with derived data, cascading rules, or invariants has this problem whether or not its API admits it.

The decision that clarifies everything downstream is whether your representation holds only the asserted items or also everything derivable from them. Keep the two separate and you get a meaningful distinction between an item that is present and an item that merely follows, which in turn gives you two genuinely different retractions: stop asserting something, versus arrange that it can no longer be concluded at all. Collapse them — treat consequences as first-class members of the state — and every consequence acquires the same standing as the thing it came from, so a small correction can force you to abandon a large amount of unrelated-looking structure, because a derived connection between two facts is now as unassailable as either fact.

Two consequences worth carrying. First, retracting a claim is not the same operation as asserting its negation: one says you no longer have grounds, the other says you have grounds for the opposite, and a system that offers only one of them will have users encoding the other badly. Second, a system that permits retraction is inherently non-monotone — adding information can destroy conclusions that previously held — so any cache, index, or memo built on the assumption that derived facts only accumulate is wrong in principle, not just in edge cases. The design question is therefore not "how do I implement delete" but "which layer of my state is asserted, which is derived, and what am I promising about each."

**Source:** [On the Semantics of Updates in Databases](../works/on-the-semantics-of-updates-in-databases.md) — the introduction's two motivating examples (the constraint that forces an automatic insertion and then leaves the subsequent retraction undefined, and the ternary supply relation whose deletion leaves three implied weaker facts unaccounted for), together with the section-two treatment of closed versus non-closed theories, its worked propositional example showing that closure forces a far larger collapse on insertion, and the remark that the resulting logic is non-monotonic.
