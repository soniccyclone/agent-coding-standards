---
type: work
title: "The Protection of Information in Computer Systems"
figure: saltzer
description: A tutorial survey of the hardware and software mechanisms needed to keep computer-stored information from unauthorized use or modification, covering descriptor-based addressing and a comparison of access-control-list versus capability-based protection architectures. Distills the reasoning into a short list of design principles — economy of mechanism, fail-safe defaults, complete mediation, least privilege among them — that became the standard checklist cited in later security engineering work. Draws its worked examples heavily from Multics, which both authors had direct hands-on experience building.
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
year: 1975
url: https://web.mit.edu/Saltzer/www/publications/protection/index.html
extraction: complete
access: public
host: self-archived
tags: [work]
---

# The Protection of Information in Computer Systems

**Author(s):** Michael D. Schroeder
**Venue/year:** Proceedings of the IEEE 63, 9 (September 1975), invited paper.
**Source:** https://web.mit.edu/Saltzer/www/publications/protection/index.html — self-archived on Saltzer's own MIT publications page; page fetched and verified directly (title, authors, and tutorial structure confirmed).

**Navigation note (2026-07-28):** the URL is the entry page of a *hypertext*
edition, not the whole paper — `index.html` carries the abstract and glossary and
about 4.9k characters of text, while the body lives in sibling pages linked from
it: `Basic.html` (Section I, design principles), `Descriptors.html` (Section II,
protection architectures), `State.html` (Section III, state of the art),
`References.html`, `notes.html`, and the `figN.html` figures. Follow the links;
reading only `index.html` would miss the paper. This is the shape of the source,
not a defect.

## Lessons
- [A requirement that nothing bad happens cannot be tested into existence](../lessons/a-requirement-that-nothing-bad-happens-cannot-be-tested-into-existence.md)
- [Pick the default whose mistakes are self-reporting](../lessons/pick-the-default-whose-mistakes-are-self-reporting.md)
- [Every remembered decision is a decision you can no longer take back](../lessons/every-remembered-decision-is-a-decision-you-can-no-longer-take-back.md)
- [No system can bootstrap its own trust](../lessons/no-system-can-bootstrap-its-own-trust.md)
- [People and institutions are inside the mechanism](../lessons/people-and-institutions-are-inside-the-mechanism.md)
