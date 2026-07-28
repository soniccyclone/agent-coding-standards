---
type: work
title: "A Note on the Confinement Problem"
figure: lampson
description: A short, precise treatment of a nasty security question — how do you let a program run on a client's data without giving it any way to leak that data back out, whether through obvious channels or side channels like resource usage patterns. Lampson names the "covert channel" problem here and lays out the conditions any real solution has to satisfy. Foundational to decades of later work on information-flow control and multi-level security.
subdomains: [operating-systems-and-systems-programming]
year: 1973
url: https://bwlampson.site/11-Confinement/Acrobat.pdf
extraction: complete
survey_pages: 5
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# A Note on the Confinement Problem

**Author(s):** Butler Lampson

**Venue/year:** Communications of the ACM 16(10), October 1973, pp. 613-615.

**Source:** https://bwlampson.site/11-Confinement/Acrobat.pdf — hosted on Lampson's own personal publications page (bwlampson.site), self-archived.

## Lessons
- [Every shared mechanism is a communication channel, so a component's real interface is everything an observer can measure about its execution — and containment becomes a quantity, not a yes or no](../lessons/every-shared-mechanism-is-a-channel.md)
- [A restriction is something you impose on a component when you invoke it, not a property the component has — so it holds only if it propagates to everything the component calls, and only over a trust base you have named](../lessons/restrictions-are-imposed-at-invocation-and-must-propagate.md)
