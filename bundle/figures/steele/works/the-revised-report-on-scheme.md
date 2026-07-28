---
type: work
title: "The Revised Report on Scheme: A Dialect of LISP"
figure: steele
description: The first standardization pass on Scheme, written as a complete user manual for the language rather than a research memo. It fixes the core reference semantics — lexical scoping, tail-call behavior, the small set of "magic forms" and primitive procedures — that later Revised^n Scheme reports (R2RS through R7RS) extend rather than replace. Represents Steele and Sussman's own move from describing an interpreter to specifying a language.
subdomains: [programming-languages-and-semantics, foundations-of-computation]
year: 1978
url: http://web.archive.org/web/20250215082814/https://dspace.mit.edu/handle/1721.1/6283
extraction: complete
access: public
host: institutional
tags: [work]
---

# The Revised Report on Scheme: A Dialect of LISP

**Author(s):** Guy Lewis Steele Jr., Gerald Jay Sussman
**Venue/year:** MIT AI Lab Memo AIM-452, January 1978.
**Source:** http://web.archive.org/web/20250215082814/https://dspace.mit.edu/handle/1721.1/6283 — Wayback Machine snapshot of the MIT DSpace record (dspace.mit.edu/handle/1721.1/6283); the live DSpace host currently answers automated requests with an AWS WAF bot challenge. Chosen over the later, multi-author Revised^n reports (R2RS onward, edited by Clinger, Rees, and others with Steele as one of many credited contributors) as the cleanest Steele-authored standardization document.

## Lessons
- [Specify an irreducible kernel plus the right to grow it; anything you can define away is not part of the language](../lessons/specify-the-kernel-and-the-means-of-growth-not-the-feature-list.md)
- [Refuse to specify the things you do not want depended on, even when every implementation agrees on them](../lessons/refuse-to-specify-what-you-do-not-want-depended-on.md)
- [To find out which level a construct really lives on, strip the language until it can no longer describe itself](../lessons/impoverish-the-language-to-find-which-level-a-construct-lives-on.md)
- [Minimality is priced per construct, and the price is how often the construct gets written](../lessons/price-each-simplification-against-how-often-it-will-be-written.md)
- [A dynamic phenomenon cannot be governed by a construct with lexical scope, and shipping one anyway is worse than shipping nothing](../lessons/a-dynamic-phenomenon-cannot-be-controlled-by-a-lexical-construct.md)
- [A description of a thing is not the thing; specify a constructor by the behaviour it must yield, never by the form it must produce](../lessons/specify-a-constructor-by-the-behaviour-it-must-yield-not-the-form.md)
