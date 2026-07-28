---
type: work
title: "The UNIX Time-Sharing System"
figure: ritchie
description: The paper that introduced Unix to a wide technical audience, written jointly with Ken Thompson. It walks through the hierarchical file system, the treatment of devices as files, process creation via fork, and the shell's command interface, arguing that a small, uniform set of abstractions can replace the sprawling feature lists of contemporary operating systems. The clarity of its design case is a large part of why Unix's model spread beyond Bell Labs.
subdomains: [operating-systems-and-systems-programming]
year: 1974
url: https://www.nokia.com/bell-labs/about/dennis-m-ritchie/cacm.pdf
extraction: complete
survey_pages: 15
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# The UNIX Time-Sharing System

**Author(s):** Dennis M. Ritchie, Ken Thompson
**Venue/year:** Communications of the ACM 17(7), July 1974, pp. 365-375.
**Source:** https://www.nokia.com/bell-labs/about/dennis-m-ritchie/cacm.pdf — self-archived PDF on Ritchie's personal Bell Labs page, migrated to Nokia's Bell Labs site after the bell-labs.com/usr/dmr/www address was retired (original address now returns HTTP 410). Verified live, content confirmed against the original abstract and introduction.

## Lessons
- [Leave the bottom layer unstructured so every layer above can choose its own structure](../lessons/leave-the-bottom-layer-unstructured.md)
- [Put the variability in the joints between components, not inside the components](../lessons/put-the-variability-in-the-joints.md)
- [Pick the representation whose global invariant is cheap to check, not the one that reads best](../lessons/pick-representations-whose-invariants-are-cheap-to-check.md)
- [Decline the guarantees your actual environment never asks for, and be explicit about which ones you kept](../lessons/decline-the-guarantees-your-environment-never-needed.md)
