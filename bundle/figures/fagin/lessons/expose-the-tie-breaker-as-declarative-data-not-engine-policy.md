---
type: lesson
title: "Expose the tie-breaker as declarative data the domain owner controls"
figure: fagin
works: [on-the-semantics-of-updates-in-databases]
axes: [expressiveness, cognitive-load, verifiability]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Expose the tie-breaker as declarative data the domain owner controls

**Lesson:** A uniform minimal-disturbance rule for absorbing new information has an immediate defect once the body of information contains both ordinary facts and the rules those facts must obey. Nothing in a purely structural notion of "smallest change" prevents the cheapest repair from being the abandonment of a rule, and abandoning a rule because a datum contradicted it inverts the entire point of having rules. Fagin, Ullman and Vardi's fix is not to add a special case for rules to the engine. They attach a rank to every statement and redefine minimality to be evaluated rank by rank, most-privileged first, so that a lower-ranked statement can never be sacrificed to spare a higher-ranked one. Rules get the top rank by convention, and the resulting definition needs no clause that mentions rules at all.

The consequence they draw is more interesting than the fix. Because rank is data rather than engine behavior, the outcome of a change now depends on how the schema owner chose to rank and represent things, and the paper says outright that supplying that assignment is the administrator's job. Its extended example makes the dependence concrete: whether an insertion resolves into a tidy field update or something much cruder turns on whether certain partial facts were given standing of their own in the representation. Same engine, same rule, different declared structure, different answer. The engine has become a mechanism parameterized by policy instead of a mechanism with policy baked in, and the paper notices for free that the same ranks describe an access-control boundary, since capping which ranks a given user may perturb is now expressible in the vocabulary already present.

What generalizes is the recognition that a general mechanism will have discretion left over, and that the discretion belongs to whoever knows the domain. The failure mode is to spend that discretion inside the implementation, as a heuristic or a precedence table that nobody outside can see or change; the result is a system whose behavior on hard cases is folklore. Lifting the discretion into declared data has three payoffs the paper demonstrates in sequence: the core definition stays small and case-free, the behavior on hard cases becomes something a domain expert can predict and steer, and adjacent concerns turn out to be expressible in the same vocabulary rather than needing a second mechanism. A programmer who works this way, on encountering a conflict resolution the code has to make, asks who is actually qualified to make it before writing the branch.

**Source:** [On the Semantics of Updates in Databases](../works/on-the-semantics-of-updates-in-databases.md) — the section introducing ranked statements and the rank-by-rank redefinition of smaller change, its remark on the authorization boundary this makes available, and the relational example whose outcome hinges on the administrator's representation choices.
