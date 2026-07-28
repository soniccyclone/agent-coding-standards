---
type: work
title: "A Behavioral Notion of Subtyping"
figure: liskov
description: Formalizes what it should mean, semantically rather than just syntactically, for one type to be a safe substitute for another — the condition now known as the Liskov Substitution Principle. Defines subtyping in terms of preserved invariants and behavioral properties, not just matching method signatures, so that code written against a supertype keeps working when handed a subtype instance. Became the standard citation for why naive inheritance hierarchies can silently break correctness.
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
year: 1994
url: https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf
survey_pages: 31
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: self-archived
tags: [work]
---

# A Behavioral Notion of Subtyping

**Author(s):** with Jeannette M. Wing
**Venue/year:** ACM Transactions on Programming Languages and Systems (TOPLAS) 16(6), November 1994
**Source:** https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf — self-archived PDF on co-author Jeannette Wing's CMU page, live and directly downloadable (HTTP 200; PDF metadata title/author confirmed).

## Lessons
- [Substitutability is a claim about what clients can prove, not about what they can call](../lessons/substitutability-is-about-what-is-provable-not-what-is-callable.md)
- [Extra capability is invisible only in a closed world](../lessons/extra-capability-is-invisible-only-in-a-closed-world.md)
- [Plan the variation at the top, or the family cannot exist at all](../lessons/plan-the-variation-at-the-top-or-the-family-cannot-exist.md)
- [Modularity bought by removing a proof rule must be paid back by hand](../lessons/modularity-bought-by-removing-a-proof-rule-must-be-paid-back-by-hand.md)
