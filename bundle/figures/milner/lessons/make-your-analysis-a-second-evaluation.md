---
type: lesson
title: "Make your analysis a second evaluation, not a second formalism"
figure: milner
works: [the-definition-of-standard-ml]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Make your analysis a second evaluation, not a second formalism

**Lesson:** A static analysis is usually built as its own thing: a separate pass with its own vocabulary, its own data structures, and its own idea of how programs are shaped. The approach taken across this definition is the opposite. There is one form of assertion — against a background, a phrase yields a result — and it is used unchanged for both phases. Determining a program's types and interfaces is described as an abstract evaluation of it: the same judgment, the same left-to-right structural decomposition, the same treatment of local scopes and recursion, differing only in what the results are. In one reading the results are types and interfaces; in the other, values and mutable state. Over half the document is the abstract reading, and it introduces no new machinery to be that.

This is worth more than notational thrift. Because both phases are presented in the same shape, they can be compared rule by rule, which is how you actually gain confidence that the static phase predicts the dynamic one — the two rules for a construct sit in corresponding positions and either agree or visibly do not. It also means the analysis inherits the language's structure instead of imposing a different one, so a construct cannot exist in the language without someone having had to write its abstract counterpart. Gaps become conspicuous rather than latent.

The factoring is genuine, not cosmetic, and the document is careful about where the readings diverge. The dynamic phase runs on a reduced syntax with all type annotations deleted, because they have already done their work. The static phase never needs to mention a value. Neither is a projection of some larger combined semantics that must be maintained; each stands alone, and a full runtime value — a concrete thing with a type attached — never has to be presented at all. That independence is what makes it reasonable to run one phase once and the other many times, which is precisely what compilation and execution are.

The practical form of this is to build a checker, a simulator, a cost model, or a permissions analysis as an interpreter over abstract values rather than as a bespoke traversal. Same recursion, same environment handling, same treatment of binding — different domain. It costs less to write, it stays in step with the real interpreter as the language grows, and when it disagrees with the concrete semantics you can point at the pair of rules where the disagreement lives.

**Source:** [The Definition of Standard ML (Revised)](../works/the-definition-of-standard-ml.md) — the preface's characterization of type and interface inference as abstract evaluation using exactly the method used for values, the introduction's phase-by-level organizing grid, and the reduced syntax adopted at the start of the dynamic sections.
