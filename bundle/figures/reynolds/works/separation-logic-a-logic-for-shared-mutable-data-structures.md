---
type: work
title: "Separation Logic: A Logic for Shared Mutable Data Structures"
figure: reynolds
description: Extends Hoare logic with a "separating conjunction" that lets a proof assert two heap regions don't overlap, making it possible to reason locally about programs that mutate shared, pointer-linked data structures without tracking the entire heap at every step. Built on joint work with Peter O'Hearn and Samin Ishtiaq. It became the theoretical basis for a generation of automated verification and static-analysis tools aimed at pointer-heavy C and Java code.
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
year: 2002
url: https://www.cs.cmu.edu/~jcr/seplogic.pdf
survey_pages: 20
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
extraction: complete
tags: [work]
---

# Separation Logic: A Logic for Shared Mutable Data Structures

**Venue/year:** Proceedings of the 17th Annual IEEE Symposium on Logic in Computer Science (LICS '02), pp. 55-74.
**Source:** https://www.cs.cmu.edu/~jcr/seplogic.pdf — live PDF (HTTP 200), self-archived on Reynolds's own CMU faculty page.

## Lessons
- [If your specifications grow quadratically as you mention more things, the fix is a new connective, not more clauses](../lessons/build-the-invariant-into-the-connective.md)
- [Describe only what a component touches, and make the extension to a larger context somebody else's rule](../lessons/specify-the-footprint-and-let-a-rule-extend-it.md)
- [Say what the program is about before you say how it is stored, and define the link by recursion on the abstract value](../lessons/recurse-on-the-abstract-value-not-on-the-memory.md)
- [A proof step that refuses to fire is usually reporting a weak specification, not an inadequate rule](../lessons/a-blocked-proof-step-is-telling-you-the-specification-is-too-weak.md)
- [Types and program assertions are one continuum, divided by a decidability frontier you get to choose](../lessons/types-and-assertions-are-one-continuum-with-a-decidability-frontier.md)
- [Non-interference between processes is a claim about resource ownership, and syntax cannot check it for you](../lessons/non-interference-is-a-resource-partition-not-a-syntactic-rule.md)
