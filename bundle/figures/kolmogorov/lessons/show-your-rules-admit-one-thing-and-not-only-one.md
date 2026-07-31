---
type: lesson
title: "Show your rules admit at least one thing, then make sure they do not pin down only one"
figure: kolmogorov
works: [grundbegriffe-der-wahrscheinlichkeitsrechnung]
axes: [verifiability, expressiveness]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Show your rules admit at least one thing, then make sure they do not pin down only one

**Lesson:** Two questions about any set of rules get run together and they have opposite desirable answers. Is the system satisfiable — does anything at all obey it? Kolmogorov answers that for his axioms immediately and cheaply, by exhibiting a single model: one possible outcome, two events, probabilities one and zero. Utterly uninteresting, which is the point. A degenerate instance is a complete answer to satisfiability, and it costs a minute. The second question is whether the rules determine their subject uniquely, and here he answers no and treats that as a feature rather than a gap: different problems require different probability fields, so a system with exactly one model would have been useless.

Keeping the two apart changes what a design review asks. A spec nobody can satisfy is broken, and the failure is embarrassing precisely because it is so easy to detect and so rarely checked — constraints accumulate from different reviewers until they contradict, and nobody notices for months because nobody has yet tried to build something obeying all of them at once. Constructing the most degenerate conceivable instance flushes that out early. Meanwhile a spec with many models is usually exactly right, because the models *are* the implementations, and which one you get is chosen by the problem at hand rather than by the spec. So the reviewer's question is not "is this fully determined?" but "which choices am I deliberately leaving open, and have I stated the properties that make the open choices interchangeable?" Freedom without stated invariants is ambiguity; freedom with stated invariants is polymorphism.

The stronger position, when you can reach it, is to characterize the entire model class rather than just one member. Kolmogorov follows his one-element example with a recipe that produces every finite model there is: pick the outcomes, assign nonnegative weights summing to one, and the events and their probabilities follow. Knowing the shape of the whole class tells you exactly how much freedom you granted, which is information a single witness cannot give you. It also tells you when to stop adding axioms: you add one when the class still contains members you are unwilling to accept, and you stop when the remaining variation is variation you *want* implementers to exploit.

**Source:** [Grundbegriffe der Wahrscheinlichkeitsrechnung](../works/grundbegriffe-der-wahrscheinlichkeitsrechnung.md) — Chapter I, §1, where consistency of the axioms is established by the single-element field with probabilities one and zero, the system is then declared incomplete on the grounds that different problems demand different probability fields, and the construction of finite fields from an outcome set with elementary probabilities summing to one exhibits the whole class of finite models.
