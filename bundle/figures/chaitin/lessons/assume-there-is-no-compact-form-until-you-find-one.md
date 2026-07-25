---
type: lesson
title: "Assume the thing in front of you has no compact form until you find one"
figure: chaitin
works: [on-the-length-of-programs-for-computing-finite-binary-sequences, a-theory-of-program-size-formally-identical-to-information-theory, algorithmic-information-theory]
axes: [primitive-count, cognitive-load]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Assume the thing in front of you has no compact form until you find one

**Lesson:** Counting settles this before any cleverness gets involved. There are far fewer short descriptions than there are things of a given size to describe, so almost everything of that size must be described at close to full length. Compressibility is the rare property. The objects that admit a neat generating rule are a vanishing fraction, and the fraction shrinks as the objects get bigger.

The working consequence is a reversal of the usual optimism. When a body of rules, a data set, or a pile of special cases resists being folded into a compact form, the default explanation is not that the search was insufficiently clever. The default explanation is that most things are like that. A programmer who has internalised the counting argument budgets the search for the elegant general form and then stops, because failure carries no information about their ability. Irreducible material gets stored rather than derived: tax rules, protocol quirks, hardware errata, and accumulated business policy are frequently incompressible in exactly this sense, and building a mechanism to generate them from principles produces a mechanism larger than the table it replaced.

The mirror image is why finding structure matters so much. Because incompressibility is the background condition, every real compression is evidence that the domain has a constraint in it that was not obvious. That is worth substantial effort to find, and worth protecting once found, but it is a discovery rather than an entitlement. Treating compact form as normally available leads to speculative abstraction; treating it as normally absent leads to noticing the exceptions.

**Source:** [On the Length of Programs for Computing Finite Binary Sequences](../works/on-the-length-of-programs-for-computing-finite-binary-sequences.md) - the size-counting results establishing that most sequences of a given length need programs near the maximum length. Restated in sharper form in [A Theory of Program Size Formally Identical to Information Theory](../works/a-theory-of-program-size-formally-identical-to-information-theory.md) (the bounds on maximal complexity and the count of exceptions) and in the survey chapter of [Algorithmic Information Theory](../works/algorithmic-information-theory.md), where the same estimate is used to show minimal programs look statistically typical.
