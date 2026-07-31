---
type: work
title: "Designing Software for Ease of Extension and Contraction"
figure: parnas
description: Treats extensibility and the ability to strip a system down to a smaller variant as two sides of the same design problem, both solvable by controlling the "uses" relation between modules rather than just their calling structure. Shows that a program can be built as a well-ordered set of increasingly capable subsets, so a working (if minimal) system exists at every stage of assembly. Won the 1979 ACM Programming Systems and Languages Paper Award.
subdomains: [software-engineering-and-architecture]
year: 1979
url: https://ocw.mit.edu/courses/16-355j-software-engineering-concepts-fall-2005/1c68d0f98909a126ec5eb6a0ff358ec7_parnas_ease.pdf
extraction: complete
survey_pages: 14
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: institutional
tags: [work]
---

# Designing Software for Ease of Extension and Contraction

**Venue/year:** IEEE Transactions on Software Engineering SE-5(2), March 1979, pp. 128-138 (earlier version presented at ICSE 1978, pp. 264-277).
**Source:** https://ocw.mit.edu/courses/16-355j-software-engineering-concepts-fall-2005/1c68d0f98909a126ec5eb6a0ff358ec7_parnas_ease.pdf — MIT OpenCourseWare, 16.355J Software Engineering Concepts (Fall 2005), official MIT institutional course-materials repository. Verified live.

## Lessons
- [A dependency is a claim about correctness, not a record of who calls whom](../lessons/a-dependency-is-a-correctness-claim-not-a-call.md)
- [Find the smallest thing that could possibly run, and treat that as a requirement](../lessons/find-the-smallest-thing-that-could-run-before-designing-the-whole.md)
- [When two parts seem to need each other, one of them is really two parts](../lessons/when-two-parts-need-each-other-one-of-them-is-two-parts.md)
- [Generality and flexibility are two different purchases, paid for at different times](../lessons/generality-and-flexibility-are-bought-in-different-currencies.md)
- [Permission to depend has to be earned in both directions](../lessons/permission-to-depend-must-be-earned-in-both-directions.md)
- [A privileged core is the coarsest hierarchy you can build, and it freezes whatever you put inside](../lessons/a-privileged-core-is-the-coarsest-hierarchy-you-can-build.md)
- [Climbing a hierarchy buys simplicity, never power — so say convenience and mean it](../lessons/climbing-a-hierarchy-buys-simplicity-never-power.md)
- [Who is allowed to reuse what is a structural decision, not a local one](../lessons/who-may-reuse-what-is-not-a-local-decision.md)
- [How many of a thing there are is itself a secret, and leaking it blocks removal as hard as addition](../lessons/how-many-of-a-thing-there-are-is-itself-a-secret.md)
- [The right layering absorbs the tools you would otherwise have to build alongside it](../lessons/the-right-layering-makes-your-support-tooling-unnecessary.md)
- [Any structure can be forced to work, so compare structures by what comes out cleanly](../lessons/any-structure-can-be-forced-to-work-so-compare-them-on-removal.md)
- [Modules and levels are two independent structures over the same parts, and expecting them to coincide is what forces the splitting](../lessons/modules-and-levels-are-two-independent-structures.md)
- [A structure of deliverable subsets is insurance against your own schedule](../lessons/deliverable-subsets-are-insurance-against-your-own-schedule.md)
- [Build the richer mechanism on top of the plainer one, never inside it](../lessons/build-the-richer-mechanism-on-top-of-the-plainer-one.md)
