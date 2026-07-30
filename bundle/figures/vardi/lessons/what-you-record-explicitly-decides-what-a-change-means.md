---
type: lesson
title: "What you chose to record explicitly decides what a change means, not the change operator"
figure: vardi
works: [on-the-semantics-of-updates-in-databases]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# What you chose to record explicitly decides what a change means, not the change operator

**Lesson:** The most surprising result in Vardi's update framework is that the operator does not determine the outcome — the representation does. The same request, resolved by the same minimality rule, against the same information, yields entirely different results depending on which facts were written down as first-class entries. In his worked example, recording the weaker projection of a relation explicitly, at its own standing, is precisely what makes an incoming assertion move an employee's department across all of that employee's rows instead of deleting them. Nothing about the request expressed that intent. It fell out of a schema decision made earlier.

That is worth sitting with, because it inverts where most designers think mutation semantics live. Effort goes into the operations — the transaction boundary, the cascade rule, the merge strategy — while the choice of what the schema asserts explicitly is treated as a modelling detail settled on other grounds. But the operations only ever get to rearrange the things you gave them, so the vocabulary of recorded facts is the actual control surface. Record only the widest facts and every correction becomes destructive, since the coarse record is all there is to sacrifice. Record the weaker projections too, and a correction to one dimension can preserve the others, because there is something left standing that says they should be preserved.

The reusable practice is to work backwards from the changes you expect. Before fixing a schema, take the two or three most common corrections the system will receive over its life and ask what would have to be separately recorded, and at what standing, for the desired outcome to be the minimal one. Then record exactly that. This also relocates responsibility honestly: the person choosing the representation is choosing the update semantics, and should know it, rather than discovering years later that the system's behaviour under correction was decided by a modelling choice nobody was reviewing for that purpose.

**Source:** [On the Semantics of Updates in Databases](../works/on-the-semantics-of-updates-in-databases.md) — section three's worked employee/child/department example, where a functional dependency plus explicitly recorded existential facts about the employee-child projection make the insertion of a new departmental fact resolve as a departmental change rather than a row deletion, and the closing observation that recording those projection facts was essential to obtaining that result and is the means by which an administrator controls how updates behave.
