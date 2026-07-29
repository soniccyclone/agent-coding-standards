---
type: work
title: "UNIX Implementation"
figure: thompson
description: A high-level walkthrough of the actual mechanics inside the Unix kernel Thompson built, covering how it represents processes, users, and programs, how the I/O system dispatches to devices through a uniform interface, and how the file system lays out inodes, directories, and free space on disk. Where the 1974 CACM paper sold the design's virtues to outsiders, this piece is the implementer's account of how the pieces actually fit together. It's a primary source for understanding the concrete engineering choices behind Unix's abstractions.
subdomains: [operating-systems-and-systems-programming]
year: 1978
url: https://users.soe.ucsc.edu/~sbrandt/221/Papers/History/thompson-bstj78.pdf
extraction: complete
survey_pages: 10
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# UNIX Implementation

**Venue/year:** The Bell System Technical Journal 57(6), July-August 1978, pp. 1931-1946.
**Source:** https://users.soe.ucsc.edu/~sbrandt/221/Papers/History/thompson-bstj78.pdf — live PDF, UC Santa Cruz course-reading mirror (CS 221 papers archive). Content verified 2026-07-24 (decoded PDF text stream shows title, author, and abstract). The full BSTJ 57(6) issue is also freely downloadable from the Internet Archive (archive.org/details/bstj57-6-1931) as an alternate copy.

## Lessons
- [The layer nobody can replace should offer the common divisor of the options you skipped](../lessons/the-mandatory-layer-should-offer-the-common-divisor-of-the-options-you-skipped.md)
- [Admit complexity only where it can be quarantined, not where it pays best](../lessons/admit-complexity-only-where-it-can-be-quarantined.md)
- [When two sharing rules disagree about where a piece of state lives, you have found a missing layer](../lessons/when-sharing-rules-disagree-you-have-found-a-missing-table.md)
- [A primitive that carries no state has handed that state to every caller](../lessons/a-primitive-that-carries-no-state-hands-its-state-to-every-caller.md)
