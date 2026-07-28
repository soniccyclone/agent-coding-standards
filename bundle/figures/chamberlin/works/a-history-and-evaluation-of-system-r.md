---
type: work
title: "A History and Evaluation of System R"
figure: chamberlin
description: A retrospective on the System R project's three phases (roughly 1974-1979), written by the project team to distill what building a full-scale relational prototype had actually taught them about query languages, storage engines, and optimizer design. It's less an announcement of new results than a lessons-learned document, explaining design choices like SQL's syntax and cost-based access-path selection in light of what worked and what had to be revised along the way. It became one of the most-cited papers in database systems precisely because it captures hard-won engineering judgment rather than just an architecture diagram.
subdomains: [databases-and-data-management]
year: 1981
url: https://www.cs.cmu.edu/~natassa/courses/15-721/papers/p632-chamberlin.pdf
extraction: complete
survey_pages: 15
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: third-party-rehost
tags: [work]
---

# A History and Evaluation of System R

**Author(s):** D. D. Chamberlin, M. M. Astrahan, M. W. Blasgen, J. N. Gray, W. F. King, B. G. Lindsay, R. Lorie, J. W. Mehl, T. G. Price, F. Putzolu, P. G. Selinger, M. Schkolnick, D. R. Slutz, I. L. Traiger, B. W. Wade, R. A. Yost
**Venue/year:** Communications of the ACM 24(10), October 1981, pp. 632-646.
**Source:** https://www.cs.cmu.edu/~natassa/courses/15-721/papers/p632-chamberlin.pdf — verified live (HTTP 200, application/pdf), hosted as a course reading for CMU's 15-721 Database Systems course. Also mirrored at EPFL's dias course site. The stub's original claim of a self-archived copy on research.ibm.com does not hold up: no such page resolves, and IBM's own listing for the companion 1976 System R paper links through to a paywalled ACM PDF rather than a free copy, so the same is assumed here. The CACM original (dl.acm.org/doi/10.1145/358769.358784) is paywalled.
**Host:** third-party-rehost — CMU course-reading mirror.

## Lessons
- [Closure is what turns one facility into many](../lessons/closure-turns-one-facility-into-many.md)
- [Give performance tuning its own channel, and admit nothing into it that carries information](../lessons/give-tuning-its-own-channel-that-carries-no-meaning.md)
- [Learnability is a measurable property of a notation, so measure it](../lessons/measure-a-notation-dont-defend-it.md)
- [Make the system describe and constrain itself in the language it exposes](../lessons/let-the-system-describe-itself-in-its-own-language.md)
