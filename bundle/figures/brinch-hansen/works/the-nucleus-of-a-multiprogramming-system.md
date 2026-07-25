---
type: work
title: "The Nucleus of a Multiprogramming System"
figure: brinch-hansen
description: Describes the RC 4000 nucleus, a small nucleus of code that handles process creation, scheduling, and inter-process message passing while leaving all policy (scheduling strategy, resource allocation) to programs built on top of it. This mechanism/policy split let the same nucleus serve as the base for several different purpose-built operating systems on the same hardware. It's widely credited as the first working statement of what became the microkernel idea.
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
year: 1970
url: http://www.brinch-hansen.net/papers/1970a.pdf
access: public
host: self-archived
tags: [work]
---

# The Nucleus of a Multiprogramming System

**Venue/year:** Communications of the ACM 13(4), April 1970, pp. 238-242 (per the copyright footnote on the PDF itself; some of Brinch Hansen's own later reference lists cite 238-250).
**Source:** http://www.brinch-hansen.net/papers/1970a.pdf — author's self-archived papers site (brinch-hansen.net/papers), verified resolving 2026-07-24. Note: the site's HTTPS certificate is currently expired; the HTTP URL above resolves cleanly.

## Lessons
- [Assume every participant is broken or hostile, and make whoever opens an interaction carry its risk](../lessons/assume-every-participant-may-be-broken.md)
- [Build a base with no strategy in it, and make every policy an ordinary program above it](../lessons/build-a-base-with-no-strategy-in-it.md)
- [Design the machine you wish you had been given, then hold the layer above it to explaining itself without ever mentioning it](../lessons/design-the-machine-under-the-language.md)
- [Look for the concept that erases a boundary, because whatever sits on either side then becomes substitutable](../lessons/erase-the-boundary-to-gain-substitutability.md)
