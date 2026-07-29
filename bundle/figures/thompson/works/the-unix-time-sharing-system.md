---
type: work
title: "The UNIX Time-Sharing System"
figure: thompson
description: The original public description of Unix, written for a general CACM audience rather than Bell Labs insiders. It lays out the hierarchical file system, the uniform treatment of files/devices/inter-process I/O, and the small set of system calls the rest of the system is built from, arguing that a modest kernel plus a rich set of small user-level programs beats one large monolithic system. This is the paper that put Unix's design philosophy in front of the wider computing community and drove its spread beyond Bell Labs.
subdomains: [operating-systems-and-systems-programming]
year: 1974
url: https://www.nokia.com/bell-labs/about/dennis-m-ritchie/cacm.pdf
survey_pages: 15
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: institutional
tags: [work]
---

# The UNIX Time-Sharing System

**Author(s):** Dennis M. Ritchie and Ken Thompson
**Venue/year:** Communications of the ACM 17(7), July 1974, pp. 365-375.
**Source:** https://www.nokia.com/bell-labs/about/dennis-m-ritchie/cacm.pdf — live PDF, hosted on Nokia Bell Labs' official Dennis Ritchie memorial/archive page (Nokia is Bell Labs' corporate successor). Verified resolving and content-matched 2026-07-24.

## Lessons
- [Absorb hardware variety at the lowest boundary so nothing above it has to know](../lessons/absorb-variety-at-the-lowest-boundary.md)
- [Put the variety in the joints between programs, not inside them](../lessons/put-the-variety-in-the-joints-not-in-the-programs.md)
- [Decline to model what your layer does not need to know](../lessons/decline-to-model-what-your-layer-does-not-need-to-know.md)
- [A system you are forced to inhabit corrects itself; one built to a requirements list does not](../lessons/a-system-you-are-forced-to-inhabit-corrects-itself.md)
