---
type: work
title: "Hints for Computer System Design"
figure: lampson
description: A collection of design maxims Lampson distilled from hands-on work building the Alto and Dorado hardware and the Bravo and Star applications. Rather than a formal methodology, it's a running commentary on trade-offs he actually hit — simplicity versus generality, when to specialize, how to handle change over a system's lifetime. Became one of the most-cited "lessons learned" pieces in systems design pedagogy.
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
year: 1983
url: https://bwlampson.site/33-Hints/Acrobat.pdf
extraction: complete
survey_pages: 27
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# Hints for Computer System Design

**Author(s):** Butler Lampson

**Venue/year:** ACM Operating Systems Review 17(5), October 1983, pp. 33-48. Reprinted in IEEE Software 1(1), January 1984.

**Source:** https://bwlampson.site/33-Hints/Acrobat.pdf — hosted on Lampson's own personal publications page (bwlampson.site), self-archived.

## Lessons
- [Every interface you define is a small programming language, and the cost of using it is part of the contract whether you write it down or not](../lessons/an-interface-is-a-small-language-and-its-real-contract-includes-cost.md)
- [An abstraction exists to erase the properties you don't want, so anything good underneath must survive the trip upward](../lessons/abstraction-should-erase-defects-not-capabilities.md)
- [The normal case and the worst case are two different design problems with two different success criteria, and one mechanism serving both will serve neither](../lessons/normal-and-worst-case-are-two-different-design-problems.md)
- [Designate exactly one representation as authoritative, optimize it for being checkable rather than for being fast, and let every faster structure be a guess you are allowed to discard](../lessons/put-the-truth-in-one-place-and-let-everything-faster-be-a-guess.md)
- [A system's design has to budget for its own revision: expect the first build to be discarded, keep the unchangeable surfaces few, and always retain somewhere to stand while you change them](../lessons/design-for-your-own-later-revision.md)
