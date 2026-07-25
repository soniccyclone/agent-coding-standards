---
type: work
title: "Basic Polymorphic Typechecking"
figure: cardelli
description: A practical, implementation-oriented paper walking through a type inference algorithm (Algol/ML-style Hindley-Milner polymorphism) with working code, aimed at language implementors rather than type theorists. It demystifies unification-based type inference by presenting it as a small, self-contained algorithm rather than an abstract proof system. Notable for including runnable Modula-2 and ML source alongside the exposition, bridging the theory/practice gap that much of Cardelli's other type-theory work leaves open.
subdomains: [programming-languages-and-semantics]
year: 1987
url: http://lucacardelli.name/Papers/BasicTypechecking.pdf
access: public
host: self-archived
tags: [work]
---

# Basic Polymorphic Typechecking

**Venue/year:** Science of Computer Programming 8(2), 1987, pp. 147-172 (originating as AT&T Bell Labs Technical Report TR-112, September 1984, and a 1985 reprint in the ML/LCF/Hope Newsletter).
**Source:** http://lucacardelli.name/Papers/BasicTypechecking.pdf — self-archived on Cardelli's own site (verified 200, application/pdf). Note: the Phase 1/2 stub credited this "with Wegner" — the author's own bibliography lists it as solo-authored by Cardelli; corrected here.

## Lessons
- [Write down what must be decided before deciding how to decide it, and let the algorithm be answerable to that statement](../lessons/state-the-judgment-before-writing-the-checker.md)
- [There is a most general truth about what your code accepts, and declarations can only narrow it](../lessons/the-most-general-type-exists-before-you-declare-anything.md)
- [When two design goals genuinely fight, look for the construct that serves both instead of splitting the difference](../lessons/two-goals-in-tension-need-a-third-construct.md)
- [State the permissive rule you wish held, then spend real effort building the small program that breaks it](../lessons/attack-the-rule-you-want-to-be-true.md)
- [Treat guaranteed termination of your own tooling as a budget you may knowingly overspend](../lessons/spend-decidability-deliberately.md)
