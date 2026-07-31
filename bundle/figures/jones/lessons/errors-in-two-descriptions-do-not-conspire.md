---
type: lesson
title: "Two descriptions from different viewpoints catch errors because their mistakes do not conspire"
figure: jones
works: [software-development-a-rigorous-approach]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Two descriptions from different viewpoints catch errors because their mistakes do not conspire

**Lesson:** The standard objection to writing an argument alongside a piece of code is that you are now producing two artifacts, both of which can be wrong, and a beginner will get the second one wrong more often than the first. The objection is factually correct and it misses what is actually happening. The question is never whether the argument contains errors. It is whether an error in the argument can cancel an error in the code so that the pair looks consistent. It almost never can, because the two are written in different terms, from different directions, about different aspects — one says how the result is produced, the other says what relationship the result bears to the input. For a mistake in one to hide a mistake in the other, the two would have to be wrong in precisely matching ways, and mistakes are not that cooperative.

So the failure mode is benign and informative. You attempt to connect the two, some step will not go through, and you have learned that something is wrong. You do not yet know which of the two is at fault, and that ambiguity is fine — you have localized the disagreement to one small place, and finding out which side is wrong from there is easy. This is worth stating explicitly because people abandon the practice at exactly the moment it starts paying: their first few arguments fail, they conclude they are bad at arguments, when in fact the mechanism is working.

The same effect explains something everyone has experienced and few connect to it. Asking a colleague to look at a stubborn bug frequently produces the answer before they have said anything useful, because explaining the code forces you to describe it in different terms than the ones you wrote it in, and the mismatch surfaces. Writing down what the code is supposed to achieve is that shift of viewpoint made permanent and repeatable, available at any hour without a colleague. The general design principle: when you want to catch errors, do not check the artifact against itself more carefully — check it against a description of it built on a different basis, and let the independence do the work.

**Source:** [Software Development: A Rigorous Approach](../works/software-development-a-rigorous-approach.md) — chapter 5's summary, addressing the concern programmers raise on first encountering program proofs that errors are as likely in the proof as in the program: the response that when a proof error does not match the program some step of the deduction becomes impossible, that the mismatch may lie on either side, and that the probability of a compensating error in a proof concealing one in a program is very small; together with the accompanying observation that assertions force one to look at a program from another point of view, which is the same shift of viewpoint that frequently exposes a bug when a programmer seeks help from a colleague, and the note that the danger of undetected errors is further reduced when verification plays a constructive role during development rather than a checking role afterwards.
