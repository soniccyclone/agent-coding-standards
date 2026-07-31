---
type: lesson
title: "Let the application tell you which foundation you need"
figure: strachey
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Let the application tell you which foundation you need

Scott and Strachey close by admitting that their project was built in the wrong order. Logically the mathematical apparatus should come first and the application of it second, and they say so plainly — and then observe that you generally cannot tell which apparatus you need until you have tried some applications. The sequence in which a thing is best presented is not the sequence in which it can be discovered, and treating the presentation order as a work plan means committing to a foundation before you know what it has to support.

The evidence they offer is their own earlier attempt, which they describe unsparingly: it had the semantic ideas but no rigour, and worse, some of the objects it freely used were not known to exist. That is normally a description of a failure. Here it is the instrument that identified the problem, because the unrigorous version is what wrote down the space of values a reasonable language wants — one that contains its own function space — and made visible that no ordinary construction yields it. Nothing on the foundations side would ever have raised that question. There is no reason, working within set theory, to want such a space until a language design asks for it, so the requirement could only be discovered from the application end.

What keeps this from being a licence to hand-wave is the second half of the pattern, which they also carried out: they went back. The later paper covers the same ground with the existence questions settled, and the theory then genuinely does separate into apparatus and application, just not in the order of construction. A first pass that uses objects you cannot justify is a probe, and a probe is only worth anything if you return to close what it opened. Never returning leaves you with a system resting on assumptions nobody has checked, which is exactly the situation the exercise was supposed to reveal and repair.

The working method that follows is to write the application against the abstractions you wish existed, without pausing to establish them, and then read off which ones you cannot actually justify. That list is the foundational work, and it is a much shorter and better-aimed list than the one you would have produced by building the general machinery first. Both failure modes are common: generalising before you have a consumer, so the framework fits nothing in particular; and shipping the sketch, so the gaps it exposed stay open permanently.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the conclusion, which concedes that foundations logically precede application while noting one cannot know what apparatus is required until applications have been attempted, and recounts how the authors' earlier and mathematically unsatisfactory paper — in which the existence of some objects used was not certain — is what forced the development of the machinery presented here.
