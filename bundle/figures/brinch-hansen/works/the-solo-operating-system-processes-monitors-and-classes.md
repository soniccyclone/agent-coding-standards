---
type: work
title: "The Solo Operating System: Processes, Monitors, and Classes"
figure: brinch-hansen
description: Reports on Solo, a single-user operating system Brinch Hansen wrote in Concurrent Pascal to test whether monitor-structured concurrency held up outside of toy examples. The paper walks through the system's structure as a hierarchy of monitors and classes and notes that the whole thing was built from small, nearly independent components under a page of code each. It served as the working proof that compiler-enforced monitors were practical for real systems software, not just a theoretical convenience.
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
year: 1976
url: http://www.brinch-hansen.net/papers/1976c.pdf
access: public
host: self-archived
tags: [work]
---

# The Solo Operating System: Processes, Monitors, and Classes

**Venue/year:** Software: Practice and Experience 6(2), 1976, pp. 165-200.
**Source:** http://www.brinch-hansen.net/papers/1976c.pdf — author's self-archived papers site (brinch-hansen.net/papers), verified resolving 2026-07-24. Note: the site's HTTPS certificate is currently expired; the HTTP URL above resolves cleanly.

## Lessons
- [Dependency among components is a graph, not a tree, so state it in the source and forbid the cycles](../lessons/dependency-is-a-graph-not-a-tree.md)
- [Design the machine you wish you had been given, then hold the layer above it to explaining itself without ever mentioning it](../lessons/design-the-machine-under-the-language.md)
- [Grow a system as a chain of subsystems that each already work, and arrange things so new code cannot break old code](../lessons/grow-through-subsystems-that-already-work.md)
- [If writing a module is hard, the real work has not been done — choosing the modules is the design](../lessons/the-work-is-choosing-the-modules.md)
- [Put the permitted operations next to the data they touch, and give up language power until the compiler can enforce it](../lessons/put-the-operations-where-the-data-lives.md)
- [Settle design arguments by building whole systems, not with exercises or with objections nobody has tested](../lessons/settle-design-arguments-by-building-systems.md)
