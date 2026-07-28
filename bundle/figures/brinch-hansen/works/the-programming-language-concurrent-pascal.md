---
type: work
title: "The Programming Language Concurrent Pascal"
figure: brinch-hansen
description: The design paper for Concurrent Pascal, which extended Pascal with processes, monitors, and classes so that concurrent correctness (mutual exclusion, condition synchronization) is checked by the compiler rather than left to programmer discipline. It was the first language to make Hoare and Brinch Hansen's monitor concept a real, compiler-enforced construct rather than a paper design, and Brinch Hansen used it to build a working operating system (Solo) as proof the approach scaled to real systems software.
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
year: 1975
url: http://www.brinch-hansen.net/papers/1975a.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# The Programming Language Concurrent Pascal

**Venue/year:** IEEE Transactions on Software Engineering SE-1(2), June 1975, pp. 199-207.
**Source:** http://www.brinch-hansen.net/papers/1975a.pdf — author's self-archived papers site (brinch-hansen.net/papers), verified resolving 2026-07-24. Note: the site's HTTPS certificate is currently expired; the HTTP URL above resolves cleanly.

## Lessons
- [Cut module boundaries where simultaneity demands them, not where the data would suggest](../lessons/cut-boundaries-where-simultaneity-demands.md)
- [Dependency among components is a graph, not a tree, so state it in the source and forbid the cycles](../lessons/dependency-is-a-graph-not-a-tree.md)
- [Design concurrent code for reproducible behavior, because the errors that matter are the ones testing can never reach](../lessons/design-for-reproducibility-because-testing-cannot-reach.md)
- [Design the machine you wish you had been given, then hold the layer above it to explaining itself without ever mentioning it](../lessons/design-the-machine-under-the-language.md)
- [Grow a system as a chain of subsystems that each already work, and arrange things so new code cannot break old code](../lessons/grow-through-subsystems-that-already-work.md)
- [Look for the concept that erases a boundary, because whatever sits on either side then becomes substitutable](../lessons/erase-the-boundary-to-gain-substitutability.md)
- [Put the permitted operations next to the data they touch, and give up language power until the compiler can enforce it](../lessons/put-the-operations-where-the-data-lives.md)
- [Settle design arguments by building whole systems, not with exercises or with objections nobody has tested](../lessons/settle-design-arguments-by-building-systems.md)
- [Systems code earns no exemption from the disciplines you would demand of any other program](../lessons/systems-code-earns-no-exemption.md)
- [Trade generality for tractability on purpose, and keep a ledger of what the trade cost you](../lessons/trade-generality-for-tractability-on-purpose.md)
- [When a class of mistakes needs a name to happen, remove the ability to name it](../lessons/remove-the-name-remove-the-error.md)
