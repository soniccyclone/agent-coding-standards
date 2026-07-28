---
type: lesson
title: "Promising something true is still a design error if you did not have to promise it"
figure: parnas
works: [on-the-criteria-to-be-used-in-decomposing-systems-into-modules]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Promising something true is still a design error if you did not have to promise it

**Lesson:** An interface is usually judged by whether what it says is accurate. That is the wrong test. The right test is whether every guarantee it makes is one a client genuinely needs, because each additional guarantee, however truthful, subtracts from the set of implementations that remain legal. A boundary that promises the order in which derived items appear has silently outlawed every future version that would rather produce them in some other order — including versions that would be dramatically cheaper. The promise costs nothing today and everything later, which is exactly why it slips past review: nobody can point at a bug.

This reframes hiding as a quantitative discipline rather than a binary one. It is not enough to have concealed the storage strategy and the algorithm; you must go back through what you did expose and ask, for each clause, what a client could not accomplish without it. Where the answer is "nothing," the clause is leakage. Parnas is unusually severe about this on his own work: having successfully hidden how a set of derived items was stored or computed, he had still fixed their order, and he calls that a design error rather than a stylistic preference — because the fixed order foreclosed a legitimate alternative structure that would have made a downstream component collapse to almost nothing.

The practical technique this implies is adversarial: for any interface you have drafted, try to enumerate the implementations it forbids, and check that each exclusion was intentional. Weakening a specification is real design work with a real payoff, and it is work almost nobody schedules. A programmer who internalizes this writes specifications that read as looser and less informative than instinct wants — stating that certain items will be present, that none repeats, that an inverse lookup exists, and pointedly not stating the sequence — and treats a client that depends on an unpromised regularity as a client that is broken, not as a client that got lucky.

There is a verification angle too. The fewer things a boundary asserts, the smaller the obligation an implementer must discharge and the smaller the surface a reviewer must check. Over-specification inflates both sides of the contract at once: more to prove, more to depend on, more to break.

**Source:** [On the Criteria To Be Used in Decomposing Systems into Modules](../works/on-the-criteria-to-be-used-in-decomposing-systems-into-modules.md) — the section revisiting the shift-generating component of the second decomposition, where the author retracts his own ordering guarantee, plus the specific decomposition recommendations that follow (hiding sequencing, character orderings, calling conventions, control-block layouts).
