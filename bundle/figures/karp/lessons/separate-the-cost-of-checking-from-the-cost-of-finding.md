---
type: lesson
title: "Ask how hard the answer is to check before asking how hard it is to find"
figure: karp
works: [reducibility-among-combinatorial-problems, combinatorics-complexity-and-randomness]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Ask how hard the answer is to check before asking how hard it is to find

**Lesson:** A problem's difficulty splits cleanly into two questions that people habitually run together. Given a candidate answer, how expensive is it to confirm the answer is right? And separately, how expensive is it to produce a candidate in the first place? The whole class of problems that dominates practical computing is exactly the class where the first question is easy and the second may not be: there exists a short piece of evidence, and a cheap procedure that inspects the evidence and pronounces. A coloring is hard to find and trivial to check. A tour is hard to find and trivial to check. Framing the class this way, as short-evidence-plus-cheap-checker, is what makes an otherwise vague notion of "requires search" into something you can prove theorems about.

The split matters to a programmer because almost all available engineering leverage lives in the gap between the two costs. If the checker is cheap, you are free to be reckless about how the candidate arrives: guess it, approximate it, get it from a heuristic that has no correctness proof, get it from an untrusted service, get it from a black-box optimizer, get it from a language model. The checker is what converts an unreliable producer into a reliable system, and the checker is the part you can actually afford to write carefully. Notice that this is the same shape as a proof and its proof-checker, as a certificate and its validator, as a compiler and a verifier for its output.

So the discipline is: write the checker first, always, even when you have no idea how you will produce the thing it checks. It is usually a fraction of the size of the producer, it is testable in isolation, it pins down the specification more honestly than prose does, and its existence tells you which side of the tractability line you are on. A programmer who skips it ends up with a search procedure whose output nobody can independently confirm, which means every future change to the search is unverifiable and every bug report is a research project.

**Source:** [Reducibility Among Combinatorial Problems](../works/reducibility-among-combinatorial-problems.md) — the section defining the nondeterministic class as short existentially-quantified evidence over a cheaply-decidable relation, and the equivalence it proves between that framing and the guessing-machine framing.
