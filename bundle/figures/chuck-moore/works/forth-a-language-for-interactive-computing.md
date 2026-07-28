---
type: work
title: "FORTH — A Language for Interactive Computing"
figure: chuck-moore
description: An internal Mohasco Industries report documenting the first fleshed-out version of Forth, written just as Moore was carrying the system from NRAO telescope control into commercial use. It lays out the dictionary, stack mechanics, and text-interpreting definitions that later Forth systems build on — definitions here store the source character string in the parameter field and the scanner re-interprets that text; indirect-threaded code comes later, at NRAO in 1971 — aimed at programmers who need to interact with a running program rather than submit batch jobs. Reads as an internal spec more than a polished paper — terse, implementation-first, no surrounding literature review.
subdomains: [programming-languages-and-semantics]
year: 1970
url: https://www.ultratechnology.com/4th_1970.pdf
extraction: complete
access: public
host: third-party-rehost
tags: [work]
---

# FORTH — A Language for Interactive Computing

**Author(s):** Charles H. Moore, Geoffrey C. Leach
**Venue/year:** Mohasco Industries, Inc., internal publication, 1970.
**Source:** https://www.ultratechnology.com/4th_1970.pdf — PDF served directly (HTTP 200), hosted on Jeff Fox's UltraTechnology site, a Forth-chip collaborator's long-running preservation archive of Moore-adjacent material; link-only citation.

## Lessons
- [Reserve nothing: a system whose own words can be replaced puts no ceiling on its users](../lessons/an-environment-that-protects-its-own-vocabulary-caps-its-users.md)
- [The price of combining two pieces of code determines how well a system will be factored](../lessons/cheap-composition-makes-factoring-the-default.md)
- [Accept a restriction that makes the bookkeeping vanish rather than a generality that makes it permanent](../lessons/choose-the-restricted-regime-whose-bookkeeping-disappears.md)
- [Count the layers standing between you and the machine, because each one silently sets your limits](../lessons/every-intervening-layer-is-a-tax-you-cannot-audit.md)
- [A present, competent human is a system component; designing as if there were none inflates everything else](../lessons/leave-the-person-at-the-keyboard-inside-the-system.md)
- [A tool that removes limits multiplies whoever holds it, downward as readily as upward](../lessons/permissive-tools-amplify-the-programmer-in-both-directions.md)
- [Raise a vocabulary up to the problem instead of encoding the problem down into a language](../lessons/the-deliverable-is-a-vocabulary.md)
