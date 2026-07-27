---
type: work
title: "Linux Kernel Coding Style"
figure: torvalds
description: The kernel's official style guide — tabs over spaces, 8-character indentation, K&R brace placement, short function names and tight scoping, and a general distrust of cleverness that obscures control flow. It's a working document maintained by the kernel community rather than a solo essay, but Torvalds wrote the original version and its opinionated, occasionally blunt tone (e.g. on typedef abuse) is unmistakably his.
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
year: 1990s-present
url: https://www.kernel.org/doc/html/latest/process/coding-style.html
access: public
host: self-archived
tags: [work]
---

# Linux Kernel Coding Style

**Venue/year:** Part of the kernel's in-tree documentation (Documentation/process/coding-style.rst); current form built up since the 1990s, still maintained today.
**Source:** https://www.kernel.org/doc/html/latest/process/coding-style.html — live, rendered from the kernel's own documentation tree on kernel.org, self-archived/institutional. The page itself doesn't carry a detailed authorship history in its text (it cites a 2002 Greg Kroah-Hartman OLS talk on the topic), but the coding-style document is long-standing kernel canon originating with Torvalds.

## Lessons
- [Choose conventions that make bad structure physically uncomfortable, so the layout itself reports design failure](../lessons/make-bad-structure-physically-uncomfortable.md)
- [Let names carry exactly what the checker cannot, scaled to how far the reader is from the definition](../lessons/names-carry-what-the-checker-cannot.md)
- [An abstraction may hide data, never control flow: a construct that looks like a call must behave like one](../lessons/never-let-an-abstraction-lie-about-control-flow.md)
- [Optimize against the machine's real cost hierarchy, not the operation you can see](../lessons/optimize-against-the-machines-cost-model-not-your-intuition.md)
- [Existence and coherence are different problems: count references to keep a thing alive, take locks to keep it consistent](../lessons/existence-and-coherence-are-different-problems.md)
- [Push every check to where it costs nothing, and never promote your own suspicion into someone else's outage](../lessons/check-early-where-it-is-free-be-humble-at-runtime.md)
- [Give failure a single unwind ladder whose rungs are named for what they undo](../lessons/unwind-in-one-ladder-named-for-what-it-undoes.md)
