---
type: work
title: "Common Lisp the Language, 2nd Edition"
figure: steele
description: The de facto specification of Common Lisp before ANSI standardization, covering the full language including CLOS (the Common Lisp Object System) and the condition system for error handling. Steele arranged for the complete text to be released free online with the publisher's permission after the print edition went out of print, and it's this released text — not a summary — that circulates as the working reference.
subdomains: [programming-languages-and-semantics]
year: 1990
url: https://www.cs.cmu.edu/Groups/AI/html/cltl/cltl2.html
access: public
host: institutional
tags: [work]
---

# Common Lisp the Language, 2nd Edition

**Venue/year:** Digital Press, 1990.
**Source:** https://www.cs.cmu.edu/Groups/AI/html/cltl/cltl2.html — live page, full HTML text of the book mirrored at Carnegie Mellon's AI repository with the author's and publisher's permission; the page itself is the table-of-contents entry point into the complete text.

## Lessons
- [Some things belong in the core because everyone must agree on them, not because they cannot be built out of something smaller](../lessons/make-a-construct-primitive-to-force-agreement-not-because-it-is-irreducible.md)
- [Count your primitives by asking how much every tool that reads programs will be forced to hardcode](../lessons/size-the-primitive-set-by-what-every-program-reading-program-must-know.md)
- [A specification needs separate words for what a program must not do and what an implementation must catch, used with mechanical consistency](../lessons/give-forbidden-and-detected-separate-words-and-use-them-mechanically.md)
- [Where a name may be used and when it may be used are independent questions, and most confusion comes from treating them as one](../lessons/where-a-name-may-be-used-and-when-it-may-be-used-are-independent-questions.md)
- [A distinction that implementors apply inconsistently and users find confusing is a defect, however elegant it is](../lessons/a-distinction-nobody-applies-consistently-is-a-defect-however-elegant.md)
- [Let the expression that reads a location be the name of that location, and derive the writer from it](../lessons/let-the-way-you-read-a-location-be-the-way-you-name-it-for-writing.md)
- [Advice you attach to a program must never change what a correct program means, and the exceptions must be countable on one hand](../lessons/annotations-must-be-strippable-and-the-exceptions-countable-on-one-hand.md)
- [The features that move a proof obligation onto the programmer are the ones that need the most formal precision, not the least](../lessons/an-unsafe-escape-hatch-needs-more-formal-precision-than-a-safe-feature.md)
- [Design for the laziness you actually observe: make the safe variant cheaper to type than the unsafe one](../lessons/make-the-safe-variant-cheaper-to-type-than-the-unsafe-one.md)
- [Make names and argument conventions derivable by rule so users compute them instead of memorising them, and confess every place you broke the rule](../lessons/make-your-vocabulary-derivable-by-rule-and-confess-where-you-broke-the-rule.md)
- [When an abstraction fails in practice, suspect that the information was attached to the wrong thing at the wrong granularity](../lessons/when-an-abstraction-fails-suspect-the-granularity-it-was-attached-to.md)
