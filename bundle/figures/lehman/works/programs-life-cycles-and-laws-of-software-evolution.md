---
type: work
title: "Programs, Life Cycles, and Laws of Software Evolution"
figure: lehman
description: The canonical statement of Lehman's laws, arguing that large software systems used in a real-world domain ("E-type" programs) must keep changing just to stay valid as their environment shifts, and that this ongoing change drives measurable growth in structural complexity unless deliberately countered. Classifies programs by their relationship to the environment they operate in and derives the evolutionary pressures from that classification rather than from anecdote. The empirical base is quantitative studies of real system release histories, not intuition about how software "should" behave.
subdomains: [software-engineering-and-architecture]
year: 1980
url: https://users.ece.utexas.edu/~perry/education/SE-Intro/lehman.pdf
extraction: complete
survey_pages: 17
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: third-party-rehost
tags: [work]
---

# Programs, Life Cycles, and Laws of Software Evolution

**Venue/year:** Proceedings of the IEEE 68(9), 1980, pp. 1060-1076.
**Source:** https://users.ece.utexas.edu/~perry/education/SE-Intro/lehman.pdf — hosted on David E. Perry's UT Austin course page (software engineering intro reading list), a legitimate academic third-party rehost. PDF resolves directly (HTTP 200); page-header text extracted from the file confirms title and venue.

## Lessons
- [Decide what kind of program you are writing before deciding what "correct" means for it](../lessons/ask-what-kind-of-program-before-asking-whether-it-is-correct.md)
- [A deployed program becomes part of the situation it models, so it keeps invalidating its own requirements](../lessons/a-deployed-program-changes-the-problem-it-was-built-to-solve.md)
- [Structural decay is the default outcome precisely because changing software is so cheap](../lessons/cheap-change-is-what-makes-structure-decay.md)
- [Free local decisions aggregate into a system with its own measurable dynamics — plan against the measurements, not the intent](../lessons/free-local-decisions-add-up-to-a-system-with-its-own-measurable-dynamics.md)
- [Push the world's uncertainty out to the seams so that every leaf module is fully specified](../lessons/quarantine-irreducible-uncertainty-at-module-boundaries.md)
