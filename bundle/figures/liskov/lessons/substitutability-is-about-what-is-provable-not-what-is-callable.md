---
type: lesson
title: "Substitutability is a claim about what clients can prove, not about what they can call"
figure: liskov
works: [a-behavioral-notion-of-subtyping]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification, programming-environments-and-object-systems]
tags: [lesson]
---
# Substitutability is a claim about what clients can prove, not about what they can call

**Lesson:** A replacement relation between types is usually stated in terms of shape: the stand-in must accept the same arguments and hand back a compatible result. That test is cheap, mechanical, and almost beside the point, because it only rules out the narrow class of failures where a caller reaches for machinery that isn't there. The caller's real dependence is not on the presence of names — it's on everything it was entitled to conclude from the declared type's description. Two collections can present the same handful of operations under the same names and still be catastrophic substitutes for each other, because one of them keeps a promise about ordering that the other silently abandons. Shape checking has no vocabulary for that promise, so it approves the swap.

The correct framing is to treat a type's description as a body of consequences a client may derive, and to require that the substitute's body of consequences contain it. Then substitutability stops being a question about interfaces and becomes a question about entailment: every conclusion licensed by the stated type must still be licensed when the actual object is a stand-in. This reframing costs nothing structurally — it does not demand a new language feature — but it relocates the obligation from the compiler to the designer, since the compiler cannot check a property that was never written down. Anything a client will lean on, but which the description leaves unsaid, is a latent break in the hierarchy waiting for someone to trip over it.

The discipline pays off in a way that feels backwards at first: taking entailment seriously starts rejecting hierarchies that the shape test happily accepted and that intuition had already blessed. A narrower numeric type turns out not to be a specialization of a wider one, because a client of the wider one had permission to expect certain operations to complete, and the narrower one revokes it. An append-only collection is not a generalization of one that also removes, because the append-only description licensed a conclusion — that what went in stays in — that removal destroys. Each rejection is not the criterion malfunctioning; it is the criterion catching something the shape test structurally could not see.

A programmer who believes this writes the entailments down before drawing the hierarchy, and treats "it compiles when I substitute" as evidence of nothing in particular. When a proposed specialization fails the entailment test, the response is not to weaken the test but to ask which unstated promise the parent was making, then either state it and give up the relation, or restate the parent so it never promised that much. The hierarchy becomes a consequence of the descriptions rather than a thing imposed on them.

**Source:** [A Behavioral Notion of Subtyping](../works/a-behavioral-notion-of-subtyping.md) — the paper's motivating argument that signature-level contra/covariance rules are too weak, and the justification sections that recast subtyping as containment between the theories a type's specification presents.
