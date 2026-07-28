---
type: lesson
title: "Earn a new operator by making it eliminable, then prove theorems only about the kernel"
figure: milner
works: [algebraic-laws-for-nondeterminism-and-concurrency]
axes: [primitive-count, verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Earn a new operator by making it eliminable, then prove theorems only about the kernel

**Lesson:** Each time a language grows an operator, every theorem about the language faces a choice: be reproved from scratch over the larger syntax, or be shown to follow from the smaller case. This paper takes the second route deliberately and makes it a design constraint on the operators themselves. For concurrent composition, the central axiom is not an incidental property but a recipe: it rewrites a composition of two systems into a plain choice among the ways the composition can take its first step, with compositions surviving only inside the branches. Applied repeatedly, it drives the operator out of any finite term. The relabeling and restriction operators are given axioms with the same character. Every added operator is, by construction, an abbreviation.

With that in hand, the completeness argument for the rich language reduces to a small general lemma: if every term of the larger language can be normalized into the smaller one, and the equivalence on the larger language agrees with the smaller one when restricted to it, then the axiomatization of the smaller language plus the elimination axioms is already complete for the larger. The substantive combinatorial work happens once, over a signature with three operators, and the extensions cost almost nothing. That asymmetry — one hard proof, several trivial ones — is the payoff, and it was available only because the operators were designed to disappear.

There is a real trade being made, and the paper is candid about it. Facts that hold of the composition operator but are not derivable by equational reasoning from the axioms — associativity, commutativity, the neutrality of the null program — have to be proved separately by induction. Choosing axioms that give you elimination is not the same as choosing axioms that state the operator's most natural properties, and the paper takes the first, because reachability of a normal form is worth more to the theory than elegance of the individual laws.

The engineering analogue is treating any new construct as sugar with a stated expansion into a core you have already reasoned about, rather than as a peer of the core with its own semantics. Then invariants, analyses, and optimizations continue to apply without extension, and the cost of a new construct is bounded by the honesty of its expansion. Constructs that cannot be expanded away are the ones that genuinely enlarge the language — and knowing which of yours those are tells you where your theory actually has to grow.

**Source:** [Algebraic Laws for Nondeterminism and Concurrency](../works/algebraic-laws-for-nondeterminism-and-concurrency.md) — the expansion axiom for composition and the axioms for the relabeling family, noted as permitting stagewise elimination of those operators, together with the appendix's extension lemma that reduces completeness for the larger signatures to the smallest one, and the remark that associativity and commutativity of composition are not equationally derivable.
