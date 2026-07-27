---
type: lesson
title: "Let the system own correctness and the programmer own cost: write sequential code, mechanize the concurrency"
figure: herlihy
works: [a-methodology-for-implementing-highly-concurrent-data-objects, software-transactional-memory-for-dynamic-sized-data-structures]
axes: [cognitive-load, verifiability, parallelizability]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---

# Let the system own correctness and the programmer own cost: write sequential code, mechanize the concurrency

**Lesson:** There is a test for whether a concurrency technique is actually usable: can an ordinary programmer produce a correct concurrent priority queue without the result being a research contribution? If not, the technique is a demonstration, not a methodology. The way to pass that test is to refuse to make the programmer reason about concurrency at all. Have them write the data structure as a plain sequential program with no synchronization anywhere, then transform it mechanically — the transformation is small enough to live in a compiler or preprocessor — into an implementation that never blocks. The reasoning burden lands entirely in the sequential domain, where every familiar technique still applies, and the concurrency correctness argument is made once, by whoever wrote the transformation, rather than once per data structure by whoever needs one.

The load-bearing part is where the boundary is drawn, and it is drawn along a specific seam: correctness on one side, performance on the other. The mechanism guarantees that no interleaving can produce a result inconsistent with sequential behavior, and it does this without knowing anything about what the structure means. Cost, though, cannot be hidden the same way, because the technique works by producing a fresh version of the object rather than mutating in place, and how much of the old version a new one has to duplicate is a question only someone who understands the structure can answer. So for anything too big to copy wholesale, the programmer writes operations in a style that returns a logically new version while physically sharing whatever it can, and chooses a data structure whose updates disturb few nodes — a self-adjusting heap in place of an array heap, for exactly this reason. The programmer's ingenuity is spent on how little to copy, never on whether the result is correct.

That split is the transferable principle, and it is more general than concurrency: when mechanizing something hard, give the machine the property that is uniform and provable, keep for the human the property that requires understanding the domain, and make sure a mistake on the human's side costs performance rather than correctness. A programmer who works this way stops asking "is my locking right?" and starts asking "how much of this structure does an update actually have to touch?" — a question with a measurable answer.

**Source:** [A Methodology for Implementing Highly Concurrent Data Objects](../works/a-methodology-for-implementing-highly-concurrent-data-objects.md) — the two-step methodology stated in the overview, the introduction's framing of ease of reasoning and performance as the two practical obstacles, the large-object section requiring functional-style operations under programmer-controlled copying, and the conclusion's statement of which side owns correctness and which owns cost.
