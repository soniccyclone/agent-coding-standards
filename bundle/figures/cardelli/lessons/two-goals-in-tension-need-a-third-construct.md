---
type: lesson
title: "When two design goals genuinely fight, look for the construct that serves both instead of splitting the difference"
figure: cardelli
works: [basic-polymorphic-typechecking, on-understanding-types-data-abstraction-and-polymorphism]
axes: [expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# When two design goals genuinely fight, look for the construct that serves both instead of splitting the difference

**Lesson:** Two things are wanted from a program's structure and they pull against each other. One is the ability to rule out whole classes of failure before running anything, which requires committing to what each part is. The other is the ability to write a routine once and reuse it for cases that did not exist when it was written, which requires refusing exactly that commitment. The usual responses are to pick a side and pay: a language that fixes everything cannot express a sorting routine that works for more than one ordered set, and a language that fixes nothing lets the same routine be applied to anything at all with unpredictable results. Both responses accept the tension as fundamental.

It is not. There is a third possibility, which is to be precise about the dependency and vague only about the parameter: the code is fully determined given a type, and the type is supplied separately. That single construct delivers the safety of full commitment and most of the flexibility of no commitment, because the uniformity being exploited is stated rather than hoped for. The general shape of the move is to stop bargaining along the axis where the two goals conflict and to look for the axis they are both projections of. Here that axis is parameterization: once the varying part is named and abstracted, checking has something total to work with and reuse has something open to instantiate.

The habit generalizes past types. Whenever a design discussion settles into a trade between flexibility and guarantee, the useful question is which piece of information is being quantified over implicitly, and whether making it an explicit parameter dissolves the trade. Compromise positions along the original axis, by contrast, tend to lose both properties: they neither exclude the failures nor accommodate the new cases, and they are hard to explain because they encode where the argument happened to stop rather than a structure anyone can reason about.

**Source:** [Basic Polymorphic Typechecking](../works/basic-polymorphic-typechecking.md) — the pragmatic motivation section, which frames polymorphism as arising from the conflict between static checking and reusability and shows the parametric construct as the reconciliation rather than a midpoint. Also [On Understanding Types, Data Abstraction, and Polymorphism](../works/on-understanding-types-data-abstraction-and-polymorphism.md) — the discussion of how strict single-type discipline costs expressive power, and the later treatment of bounded abstraction, which recovers a lost input-to-output dependency by naming the constraint instead of weakening the type.
