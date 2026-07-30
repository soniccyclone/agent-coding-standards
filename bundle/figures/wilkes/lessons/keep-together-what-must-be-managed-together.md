---
type: lesson
title: "Choose a representation by what the management operations must iterate over, not by which is conceptually cleaner"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [hardware-affinity, verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, databases-and-data-management]
tags: [lesson]
---
# Choose a representation by what the management operations must iterate over, not by which is conceptually cleaner

**Lesson:** There are two ways to distinguish a special kind of item from ordinary ones: keep all items of that kind in dedicated containers, or allow them anywhere and mark each one individually. The marking scheme is more uniform and more flexible, and it lets you place related things next to each other, which relieves real pressure elsewhere. It also destroys locality of management. Every operation that has to act on all items of the kind — enumerating them, relocating them, invalidating them, making them durable — becomes a scan of everything, whereas under segregation the same operation visits a known, small set of containers. So the decision should be driven by what your management operations need to iterate over, and that question is usually settled before anyone asks it, by the representation chosen for other reasons.

Two supporting considerations generalize beyond this example. A per-item mark widens every item, and a designer with competing requirements has to weigh that against whichever cost will dominate later rather than which dominates now — a small proportional overhead on the component whose cost grows to dominate the system is a large overhead on the whole. And segregation is usually rejected on the grounds of the pressure it creates elsewhere, which is a legitimate complaint that has to be quantified: the marking scheme is only worth its management cost if the relief it provides is measurably larger, and that comparison is rarely made.

The wider habit is to treat "which operations have to sweep the whole structure" as a first-class criterion when choosing a representation, alongside the usual ones. Representations are normally compared on how naturally they express the domain and how cheaply individual accesses run, both of which ignore the periodic bulk operations that end up dominating a real system's behaviour and complexity.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 5's assessment of tagged capability architecture, which credits tagging with reducing the number of small segments needing management but rejects it because the management methods depend on capabilities being confined to dedicated segments, whereas tagged capabilities scattered through memory would require extensive scans when preserving them or destroying what they refer to, and further notes that tagging lengthens the memory word at a time when memory cost is expected to dominate processor cost.
