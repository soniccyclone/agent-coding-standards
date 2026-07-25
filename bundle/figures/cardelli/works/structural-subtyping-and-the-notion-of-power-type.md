---
type: work
title: "Structural Subtyping and the Notion of Power Type"
figure: cardelli
description: Argues for subtyping defined structurally (by the shape of a type's operations) rather than nominally (by declared relationships), and introduces "power types" to give a type-theoretic account of type hierarchies and metaclasses. It's an early attempt to formalize what class hierarchies actually mean mathematically, separate from any specific language's inheritance syntax. Solo-authored by Cardelli — not, as an earlier pass mistakenly noted, co-authored with Canning et al. (that's a different, unrelated POPL'89 paper on F-bounded polymorphism).
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
year: 1988
url: http://lucacardelli.name/Papers/StructuralSubtyping.pdf
access: public
host: self-archived
tags: [work]
---

# Structural Subtyping and the Notion of Power Type

**Venue/year:** Conference Record of the 15th Annual ACM Symposium on Principles of Programming Languages (POPL'88), San Diego, January 1988, pp. 70-79.
**Source:** http://lucacardelli.name/Papers/StructuralSubtyping.pdf — self-archived on Cardelli's own site (verified 200, application/pdf). Note: the Phase 1/2 stub dated this 1989 and credited "with Canning et al." — the author's own bibliography dates it 1988 and lists Cardelli as sole author; corrected here.

## Lessons
- [Let shape decide compatibility, and seal by hiding whatever invariant the shape fails to express](../lessons/let-shape-decide-compatibility-not-names.md)
- [Make a relaxation orthogonal: every way of building a thing owes an answer in every relation you care about](../lessons/every-constructor-owes-a-rule-in-every-relation.md)
- [Treat guaranteed termination of your own tooling as a budget you may knowingly overspend](../lessons/spend-decidability-deliberately.md)
- [Collapsing two levels to save concepts also destroys the questions those levels let you answer](../lessons/collapsing-two-levels-forfeits-the-decisions-above-them.md)
- [Decide what your descriptions denote, and the relations between them stop being matters of taste](../lessons/fix-what-your-types-denote-and-the-relations-follow.md)
- [Write down what must be decided before deciding how to decide it, and let the algorithm be answerable to that statement](../lessons/state-the-judgment-before-writing-the-checker.md)
