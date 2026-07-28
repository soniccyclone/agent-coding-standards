---
type: work
title: "The Mythical Man-Month: Essays on Software Engineering"
figure: brooks
description: A collection of essays distilling what Brooks learned managing IBM's OS/360 development, built around the claim now known as Brooks's Law — adding people to a late software project makes it later, because communication overhead among contributors grows faster than the work gets divided. The book generalizes from there into a broader argument that programming-in-the-large is a different activity from programming-in-the-small, with its own scheduling, conceptual-integrity, and organizational problems that naive manufacturing analogies get wrong. It remains the reference point most later software-engineering management writing either builds on or reacts against.
subdomains: [software-engineering-and-architecture]
year: 1975
url: https://bowringj.people.charleston.edu/classes/csis%20602/docs/The.Mythical.Man.Month.F.Brooks.pdf
extraction: complete
access: public
host: third-party-rehost
tags: [work]
---

# The Mythical Man-Month: Essays on Software Engineering

**Venue/year:** Addison-Wesley, 1975 (first edition); Anniversary Edition with two added chapters (including a retrospective on "No Silver Bullet") published 1995.
**Source:** https://bowringj.people.charleston.edu/classes/csis%20602/docs/The.Mythical.Man.Month.F.Brooks.pdf — course-reading mirror hosted on a College of Charleston faculty page (csis 602), verified live (200 OK, application/pdf, ~322 pages). No cost-free officially-sanctioned full copy exists (Addison-Wesley still sells the book; Internet Archive only offers time-limited controlled-lending "borrow" access, not an open download); this course mirror is a third-party rehost, linked here rather than redistributed.

## Lessons

- [Effort and elapsed time trade only for work whose parts need not agree; where they must agree, coordination grows faster than the division saves](../lessons/coordination-cost-outruns-the-division-of-labour.md)
- [Coherence cannot be produced by a committee, so name one mind to own the concepts and give the builders a constraint instead of a vote](../lessons/one-mind-must-own-the-concepts.md)
- [Score a design by how much function it delivers per concept the user must carry; maximising function and minimising primitives both fail this test](../lessons/measure-a-design-by-function-per-concept.md)
- [Design for the cost of changing the thing, knowing that every repair erodes the structure that made repair possible](../lessons/every-repair-degrades-the-structure-that-permitted-it.md)
- [The leverage lives in how the data is represented; when a program resists, stop reading the logic and go look at the tables](../lessons/study-the-data-before-the-control-flow.md)
- [Nobody can state what they want before using something, so make the system exist immediately and keep it alive while it acquires function](../lessons/keep-the-system-running-from-the-first-day.md)
- [Split difficulty into the part that belongs to the problem and the part your tools impose, then bound any proposed improvement by the fraction it can reach](../lessons/bound-any-improvement-by-the-work-it-can-actually-touch.md)
- [Method raises the floor of design and never the ceiling; the gap between competent and excellent design is not procedural](../lessons/method-raises-the-floor-of-design-not-the-ceiling.md)
- [Commit to what a thing does and refuse to commit to how, because the visible contract must outlive every mechanism that satisfies it](../lessons/commit-to-the-interface-and-leave-the-mechanism-free.md)
- [State what you do not guarantee as carefully as what you do, and make the mechanism reject it, or the running implementation becomes the specification](../lessons/specify-the-undefined-and-trap-it-in-the-mechanism.md)
- [A design is only good relative to alternatives costing the same, and the metric that decides belongs at the level of the user's result, not the component's](../lessons/compare-only-against-equal-cost-alternatives.md)
