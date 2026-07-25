---
type: lesson
title: "Enforce an invariant by removing the operation that could break it, not by forbidding its use"
figure: chaitin
works: [the-limits-of-mathematics, a-theory-of-program-size-formally-identical-to-information-theory]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# Enforce an invariant by removing the operation that could break it, not by forbidding its use

**Lesson:** Chaitin needed every program to consume its input without ever learning how much input there was, because a program that could measure the length of its own data would be smuggling in free information and the whole size accounting would break. He did not achieve this with a rule telling programs not to look. He built an interface in which looking is not expressible: the only access to the data is an operation that takes the next bit and aborts the computation if there is no next bit. Nothing returns a length, so no program can be written that depends on one. The same discipline shows up in the machine model, where the reading head can only advance and a run counts as a success only if it finishes exactly at the end of what it read.

The distinction matters because an invariant held by convention and an invariant held by construction are different kinds of fact. The first is a statement about the population of programs someone happened to write, and it decays the moment a program is written by an adversary, a random process, or a colleague in a hurry. The second is a statement about the space of programs that exist at all, and it holds for input nobody has seen. Chaitin's setting makes the difference stark, because the programs he reasons about are chosen by coin flips, and no convention survives that.

For a programmer this is the argument for shrinking capability rather than documenting restraint. Deleting a setter beats a comment asking callers not to use it. A handle that cannot name an object outside its scope beats a check that it does not. A read-only channel beats a review rule. The cost is real, since removing an operation removes some legitimate uses along with the illegitimate ones, and Chaitin pays it knowingly: his programs cannot do things that would be convenient, and in exchange every property he needs holds by inspection of the primitives rather than by faith in the population.

**Source:** [The Limits of Mathematics](../works/the-limits-of-mathematics.md) - the chapter on supplying binary data to expressions, which states outright that the reason for the bit-at-a-time primitive is that no algorithm should be able to find the end of the tape and use its length as data. Grounded in the machine definition of [A Theory of Program Size Formally Identical to Information Theory](../works/a-theory-of-program-size-formally-identical-to-information-theory.md), where the one-way read head and the halting condition make prefix-freeness a structural property of the apparatus.
