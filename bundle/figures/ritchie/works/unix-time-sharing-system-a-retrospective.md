---
type: work
title: "UNIX Time-Sharing System: A Retrospective"
figure: ritchie
description: A candid self-assessment of Unix roughly seven years after it became operational, weighing what worked (the uniform byte-stream file model, integration of devices into the file system, the shell's I/O redirection and pipes) against areas Ritchie says the team deliberately left unaddressed. Written as a companion piece to the technical papers in the same BSTJ issue, it is closer to an engineering post-mortem than a specification.
subdomains: [operating-systems-and-systems-programming]
year: 1978
url: https://www.nokia.com/bell-labs/about/dennis-m-ritchie/retro.pdf
extraction: complete
survey_pages: 13
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# UNIX Time-Sharing System: A Retrospective

**Venue/year:** The Bell System Technical Journal (BSTJ) 57(6) Part 2, July-August 1978, pp. 1947-1969.
**Source:** https://www.nokia.com/bell-labs/about/dennis-m-ritchie/retro.pdf — self-archived PDF on Ritchie's personal Bell Labs page, migrated to Nokia's Bell Labs site. Verified live, content confirmed against the paper's own title and abstract.

## Lessons
- [One canonical form per kind of data is what makes independent programs combinable](../lessons/one-canonical-form-per-kind-of-data.md)
- [Promote something to a primitive only when its absence has a demonstrated cost, not a theoretical one](../lessons/promote-to-primitive-only-on-demonstrated-cost.md)
- [A component's output is an interface, so verbosity and interrogation are design errors rather than taste](../lessons/design-output-for-the-next-program-not-the-reader.md)
- [Know in advance which measurements could change your decision, and say so when none of them could](../lessons/know-which-measurements-can-change-a-decision.md)
