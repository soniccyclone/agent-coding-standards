---
type: lesson
title: "Characterize a class both by what its members do for you and by what they are made of"
figure: scott
works: [continuous-lattices]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Characterize a class both by what its members do for you and by what they are made of

**Lesson:** There are two incompatible-looking ways to pin down the class of objects a theory should be about. The external way defines membership by a capability exercised against arbitrary other objects: this thing is in the class if, whenever some map into it is defined on a part of a larger object, the map extends to the whole. Nothing internal is mentioned; the definition is entirely about what the object can do for anything you might put next to it. The internal way defines membership by inspectable structure: these operations exist, these equations hold, every element is the limit of the elements definitely below it. Nothing external is mentioned; you can check the definition by looking only at the candidate.

Each is useless for what the other does well. The external definition explains why you want the class at all — the capability is the reason the objects are worth having — but it gives you no way to construct a member, no way to verify a candidate without quantifying over all objects in the universe, and no handle for proofs. The internal definition gives constructions, closure results, and a checkable criterion, but on its own it looks like an arbitrary axiom list; nothing in it says why anyone should care. So the theorem worth chasing is that the two definitions pick out the same objects. Once proved, you get to move between them freely: use the capability when you need to know what is guaranteed, use the structure when you need to build something or prove something, and the choice becomes a matter of convenience rather than of commitment.

The engineering translation is direct and is worth making a habit. Any abstraction you define by contract — what callers may rely on, stated without reference to internals — should eventually be matched by a structural characterization that says what an implementation has to look like, and the match should be a theorem rather than an assumption. Absent that, you have a contract nobody can be sure they satisfy, or an implementation pattern nobody can explain the value of. Having both, and knowing they coincide, is what turns an interface into something you can reason about from either side.

**Source:** [Continuous Lattices](../works/continuous-lattices.md) — the paper's overall arc: Section 1 defines injective spaces purely by the extension property for continuous functions from subspaces, Section 2 defines continuous lattices by internal order-theoretic conditions on limits from below, and Theorem 2.12 identifies the two classes exactly. The passage after the proof of 2.11 makes the point explicitly, noting that the lattice approach supplies a completely internal characterization, and that the extension capability can then be exhibited by an explicit formula.
