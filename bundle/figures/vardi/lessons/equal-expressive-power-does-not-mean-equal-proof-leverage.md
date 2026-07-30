---
type: lesson
title: "Equal expressive power does not mean equal leverage: techniques attach to structure, not to what is sayable"
figure: vardi
works: [on-the-complexity-of-bounded-variable-queries]
axes: [verifiability, expressiveness, primitive-count]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Equal expressive power does not mean equal leverage: techniques attach to structure, not to what is sayable

**Lesson:** Two formalisms can define exactly the same set of things and still be wildly unequal to work with. Vardi's evaluation technique for recursive queries turns on one structural fact — the recursion operator is monotone, so successive approximations only ever grow — and that fact is what licenses guessing an approximation and checking it grew correctly. A rival formalism known to have identical expressive power drops monotonicity in favour of a different iteration discipline, and the technique simply does not transfer; the best bound available for it stays far worse, not because it can say more, but because there is nothing for the argument to grip.

The general habit to build from this is to stop treating expressive equivalence as interchangeability. Expressive power tells you which problems you can pose. It tells you nothing about which proofs, which optimizations, or which static analyses will survive translation. Every technique quietly depends on an invariant — monotonicity, purity, immutability, termination, single assignment, a bounded number of live names — and translating a program into an equally powerful formalism that lacks that invariant destroys the technique while preserving the meaning. This is why "you can express the same thing in either" is a weak argument for a language choice and a strong argument for nothing at all.

The practical form is to ask, of any formalism you are about to adopt or any encoding you are about to perform: what structural property am I carrying, and which of my tools were resting on it? When you find that a tool was resting on something the target lacks, you have discovered the real cost of the migration, and it will not appear anywhere in a feature comparison. Conversely, when choosing between equally expressive designs, choose the one whose invariants your reasoning tools can see — that is the only dimension on which they actually differ.

**Source:** [On the Complexity of Bounded-Variable Queries](../works/on-the-complexity-of-bounded-variable-queries.md) — the remark following the fixpoint-logic upper bound, noting that the proof depends crucially on the monotonicity of the formulas, so the result does not carry over to the inflationary-fixpoint logic that is known to be equivalent in expressive power, whose best bound remains the much weaker one inherited from partial-fixpoint logic.
