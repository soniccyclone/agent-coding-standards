---
type: work
title: "RC 4000 Software Multiprogramming System"
figure: brinch-hansen
description: The full Regnecentralen technical report behind the RC 4000 nucleus, written before the condensed 1970 CACM paper. It lays out the underlying philosophy in more detail: a multiprogramming system treated uniformly as a set of cooperating parallel processes communicating through the nucleus's message-passing primitives, with everything above the nucleus (scheduling policy, resource management, higher-level operating-system behavior) built as ordinary programs rather than baked into the kernel. As the primary source document, it's the fuller record of the mechanism/policy split that made RC 4000 the first working microkernel-style design.
subdomains: [operating-systems-and-systems-programming]
year: 1969
url: http://www.brinch-hansen.net/papers/1969c.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# RC 4000 Software Multiprogramming System

**Author(s):** Per Brinch Hansen (editor)
**Venue/year:** Regnecentralen technical report, RCSL No. 55-D17, April 1969 (complete version; an abridged version was also issued as 1969a).
**Source:** http://www.brinch-hansen.net/papers/1969c.pdf — author's self-archived papers site (brinch-hansen.net/papers), verified resolving 2026-07-24. Note: the site's HTTPS certificate is currently expired; the HTTP URL above resolves cleanly. (The Phase 1/2 stub cited a third-party mirror at pascal.hansotten.com; the author's own copy is used here as the higher-tier source.)

## Lessons
- [Assume every participant is broken or hostile, and make whoever opens an interaction carry its risk](../lessons/assume-every-participant-may-be-broken.md)
- [Build a base with no strategy in it, and make every policy an ordinary program above it](../lessons/build-a-base-with-no-strategy-in-it.md)
- [Design the machine you wish you had been given, then hold the layer above it to explaining itself without ever mentioning it](../lessons/design-the-machine-under-the-language.md)
- [Look for the concept that erases a boundary, because whatever sits on either side then becomes substitutable](../lessons/erase-the-boundary-to-gain-substitutability.md)
