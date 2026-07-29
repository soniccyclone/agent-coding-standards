---
type: lesson
title: "Make the machine's reality sayable instead of escapable"
figure: strachey
works: [the-main-features-of-cpl]
axes: [expressiveness, hardware-affinity, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Make the machine's reality sayable instead of escapable

**Lesson:** A specification of a computation and a program that performs it are not the same artefact, and the gap between them is not sloppiness — it is the finite machine. A clean description of an algorithm can say that the arithmetic is carried out to sufficient accuracy; a program has to decide, operation by operation, at what width each step is actually done. An abstraction built to be purely mathematical has nowhere to put that decision, so the decision does not disappear. It relocates, and the place it goes is outside the abstraction, into whatever escape mechanism the implementation offers.

That relocation is the real cost, and it is much worse than the ugliness it was meant to avoid. Once a programmer has to drop out of the high-level notation to say a necessary thing, everything the notation guaranteed is void for that region: not just the aesthetics but the portability, the checking, and the reasoning. The design response is to keep the language machine-independent in form while making it *oriented toward* real machines in content — the awkward facts get first-class ways to be expressed, so that saying them is an ordinary use of the language rather than a defection from it.

The general test is worth applying to every abstraction you build: enumerate the things a competent user will unavoidably need to say that your model has no vocabulary for, and check where you have forced them to go to say them. If the answer is "underneath," you have not simplified the job, you have partitioned it into a pleasant region and an unsupervised one, with the hardest parts in the unsupervised half. Coverage of the unpleasant cases, expressed at your own level, is what distinguishes an abstraction from a veneer.

**Source:** [The Main Features of CPL](../works/the-main-features-of-cpl.md) — the introduction's critique of Algol 60, where the observation that a precise algorithm is not yet a program motivates the stated aim of a language whose users never need to escape into machine code.
