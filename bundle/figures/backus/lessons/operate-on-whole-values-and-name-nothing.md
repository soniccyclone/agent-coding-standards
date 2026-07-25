---
type: lesson
title: "Say what the result is over whole values, and name nothing you do not have to"
figure: backus
works: [can-programming-be-liberated-from-the-von-neumann-style]
axes: [cognitive-load, parallelizability, expressiveness]
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
tags: [lesson]
---
# Say what the result is over whole values, and name nothing you do not have to

**Lesson:** Take two programs computing the same numeric result over two vectors: one a loop accumulating into a variable, the other an assembly of three operations over the vectors as single objects. They agree on the answer and differ on almost everything that matters afterward. The loop has to be mentally executed to be understood, because its structure is a schedule and the meaning lives in the sequence of states it passes through. The assembled version is understood by understanding its parts, once, in any order: knowing what each operation and each mode of combination does is knowing what the whole does. That difference is not stylistic polish. It is the difference between comprehension that costs a simulation and comprehension that costs a reading.

Two habits produce it. The first is operating on whole structures rather than on their elements, which removes the entire apparatus of indices, bounds, and repetition from the program's surface and lets the recurring bookkeeping be consolidated into named operators reused everywhere instead of being rewritten inline every time. The second is declining to name the arguments. A program that never mentions the identities of the things it works on is general by construction, applicable to any suitable input, and needs no parameter-passing machinery with its attendant questions about when and how substitution happens. Naming has a hidden cost: once names exist, a program can incorporate part of its own data by referring to specific ones, and generality then has to be recovered by a declaration mechanism whose semantics are harder than anything it enables.

Two further consequences follow that are usually treated as separate topics. Absence of hidden state means there is nothing for concurrent evaluations to fight over, so independent parts of a computation can be evaluated independently without any coordination being added — parallelism as a property of the program's shape rather than a feature bolted on. And absence of named state means there are only two rules of interpretation to hold in mind, applying an operation to a value and determining which operation a combination denotes, rather than a body of conventions about what each construct does to an invisible store. A programmer who believes this reaches first for a statement of what the result is in terms of whole values, and treats every index, accumulator, and named intermediate as a concession to be justified.

**Source:** [Can Programming Be Liberated from the von Neumann Style?](../works/can-programming-be-liberated-from-the-von-neumann-style.md) — the side-by-side comparison of an assignment-and-loop inner product against a composed functional one, with the paired lists of properties that follow from each, plus the later observations that absence of state changes during a computation permits independent evaluation.
