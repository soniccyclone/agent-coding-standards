---
type: lesson
title: "To rule out bad outputs, find the property every rule preserves"
figure: post
works: [introduction-to-a-general-theory-of-elementary-propositions]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# To rule out bad outputs, find the property every rule preserves

A generative system — axioms plus rules that make new things from old — invites you to reason about it by walking its output. That road never ends, so questions like "can this system ever produce garbage?" look hopeless from the inside. Post's escape is to stop reasoning about individual products and instead find a property that every starting point has and that no rule can destroy. Once you have one, everything reachable has it, and anything lacking it is unreachable — proved without touching a single derivation. The whole infinite output space collapses into one check per axiom and one check per rule.

The leverage comes from the shift in what is being quantified. The system's own theorems are statements about particular products chosen because someone found them useful; the invariant is a statement about the entire population of products, and that is a different kind of claim, made from outside the system rather than inside it. Post is explicit that his results are about the logic he studies without being part of it. That outsider stance is what buys the strong negative results: you cannot show something is impossible by producing more examples of what is possible.

Note also how cheap the safety half is compared with its converse. Establishing that nothing bad gets out took Post a short paragraph of rule-by-rule inspection; establishing that everything good does get out took a four-stage construction. He points out that the easy half alone already settles consistency, and that a result which falls out immediately from the full characterization would be painful to reach directly. Preserved properties are asymmetrically generous that way: they are usually much easier to find than complete characterizations, and they already answer the question you were most afraid of.

A programmer who internalizes this stops trying to enumerate the states a system can reach and starts hunting for the thing that stays true across every transition — a type discipline no operation violates, a balance no transaction changes, a capability no call can amplify. The design consequence is bigger than the proof technique: if you cannot name a property your operations preserve, your operation set is probably the thing that needs redesigning, because nobody will ever be able to reason about it in aggregate.

**Source:** [Introduction to a General Theory of Elementary Propositions](../works/introduction-to-a-general-theory-of-elementary-propositions.md) — the argument establishing the necessity direction of the paper's fundamental theorem, and the consistency corollary that follows from that direction alone.
