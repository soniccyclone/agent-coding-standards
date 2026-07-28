---
type: work
title: "Traffic Control in a Multiplexed Computer System"
figure: saltzer
description: Saltzer's doctoral dissertation, advised by Corbató, proposing a scheme for multiplexing several processors across many users through a distributed supervisor rather than one monolithic scheduler. Treats input/output as a special case of interprocess communication and works out how a process can request parallel execution or simultaneous I/O without relying on interrupt-driven logic. The earliest formal statement of the process-switching ideas that carried through into his later Multics kernel work.
subdomains: [operating-systems-and-systems-programming]
year: 1966
url: https://web.mit.edu/Saltzer/www/publications/TRs+TMs/Multics/TR-030.pdf
extraction: complete
survey_pages: 92
survey_text_layer: full
survey_fetch_mb: 4
access: public
host: self-archived
tags: [work]
---

# Traffic Control in a Multiplexed Computer System

**Venue/year:** Sc.D. dissertation, MIT Department of Electrical Engineering, July 1966. Also issued as MIT Project MAC Technical Report MAC-TR-30.
**Source:** https://web.mit.edu/Saltzer/www/publications/TRs+TMs/Multics/TR-030.pdf — self-archived on Saltzer's own MIT publications page (PDF resolves 200). Also independently mirrored at MIT DSpace (hdl.handle.net/1721.1/16316) and CSAIL Publications (publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-030.pdf, resolves 200), both institutional.

## Lessons
- [Sort problems by whether better technology would erase them](../lessons/sort-problems-by-whether-better-technology-would-erase-them.md)
- [Study the problem with the scarcity switched off](../lessons/study-the-problem-with-the-scarcity-switched-off.md)
- [Choose primitives that funnel every race into one](../lessons/choose-primitives-that-funnel-every-race-into-one.md)
- [Send the decision to the data, not the data to the decision](../lessons/send-the-decision-to-the-data-not-the-data-to-the-decision.md)
- [Keep only the state you could not rebuild](../lessons/keep-only-the-state-you-could-not-rebuild.md)
- [Decide up front what your overhead is allowed to scale with](../lessons/decide-up-front-what-your-overhead-is-allowed-to-scale-with.md)
