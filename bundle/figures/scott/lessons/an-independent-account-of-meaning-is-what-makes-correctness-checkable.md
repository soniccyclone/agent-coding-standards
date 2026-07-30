---
type: lesson
title: "Only an account of meaning that owes nothing to the implementation can judge the implementation"
figure: scott
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Only an account of meaning that owes nothing to the implementation can judge the implementation

**Lesson:** If the only statement of what a system means is the thing that runs, then "the implementation is correct" is not a claim — there is nothing for it to be correct against. Whatever the code does is by construction what the system means, and every disagreement is settled in favour of the artifact. This is the condition most systems are actually in: the translation into machine terms is complete and faithful in the sense that it produces the intended bit patterns, and completely uninformative in the sense that the concepts of the original design are no longer recoverable from it. An account of meaning that is fixed independently of any implementation is what breaks the circle. It gives you a second, non-negotiable statement of intent that the running thing can then be measured against.

Notice how much this changes about which questions can even be asked. Before there was a definition, a claim like "this algorithm computes the same thing the notation denotes" had no content, because there was no denotation to compare against — proving it correct was not hard, it was meaningless. After the definition, the same claim is a theorem with a proof, and the proof usually needs an induction, which tells you it was carrying real content all along. The pattern generalizes past correctness: an independent semantics is also what lets you ask whether an intended meaning is realizable at all, since you can now name the object a construct is supposed to denote and ask separately whether anything mechanical could produce it. Questions about feasibility become well-posed only once meaning has been pinned down somewhere other than in the thing whose feasibility is in question.

Two working consequences. When you find yourself resolving a dispute about intended behavior by reading the source or running an experiment, you have discovered that your system has no specification, only an implementation — and the discovery is worth acting on before the behavior in question becomes load-bearing for someone else. And when you do write the independent account, keep it independent: the moment it starts describing registers, buffers, or the sequence of steps some particular implementation takes, it has stopped being a standard and become a second implementation, which can disagree with the first without either being wrong.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the opening statement that the purpose of a mathematical semantics is a correspondence between programs and mathematical entities entirely independent of implementation, given that compilers reduce programs to bit patterns in which the original concepts are obscured; the remark that the correctness of digitwise addition could not even be stated before the evaluation function was defined and requires an inductive argument once it can be; and the conclusion that the mathematics supplies the standard against which an implementation is judged and makes it possible to ask whether a defined function is calculable at all.
