---
type: lesson
title: "A field only matures when it can prove things impossible, not merely exhibit things that work"
figure: herlihy
works: [wait-free-synchronization]
axes: [verifiability, primitive-count]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---

# A field only matures when it can prove things impossible, not merely exhibit things that work

**Lesson:** Showing that something can be built takes one construction: display it, argue it works, done. Showing that something cannot be built takes a general technique, and without such a technique a field accumulates constructions indefinitely without ever learning where its boundaries lie. A body of concurrency literature had grown around building progressively fancier shared registers out of simpler ones, and the unasked question was what those registers were ultimately good for — which structures they could never support, no matter how clever the construction. The absence of a negative-result method meant nobody could distinguish "not yet solved" from "not solvable," so effort went where it could not possibly pay off.

The technique that unlocks this is to fix a single yardstick problem, reduce everything to it, and let the reduction carry the impossibility. If you can measure each primitive by the largest number of participants it can bring to agreement, then a composition argument does the rest: implementing a stronger object out of a weaker one would let you compose the weak object's implementation with the strong object's agreement protocol and thereby beat the weak object's own limit, which is a contradiction. The whole negative theory then reduces to computing one number per primitive. Notice what this buys: the argument is uniform, mechanical, and reusable, rather than a bespoke ad-hoc proof per pair of objects. And because the measure is a single integer, the result is a totally ordered ladder — a structure nobody would have guessed was there.

Two consequences a programmer should carry. First, the direction of an impossibility result is not discouraging but redirecting: a proof that read and write can never yield a fault-tolerant queue is precisely what tells you to go argue with the hardware architects instead of writing another algorithm. Several of the era's serious architecture efforts were building machines around a primitive that the theory showed could never be enough, and one published conjecture to the contrary was simply false. Second, negative results are fragile to model changes in an informative way: relaxing the guarantee from "always finishes in bounded steps" to "finishes in bounded expected steps" collapses the entire ladder, because randomization lets the weakest primitive reach the top. That is not a defect in the theory; it is the theory telling you exactly which assumption was carrying the weight.

**Source:** [Wait-Free Synchronization](../works/wait-free-synchronization.md) — the framing in the introduction that exhibiting an implementation is easy while ruling one out is not, the reduction-to-consensus technique and the composition theorem that founds the hierarchy, and the closing remarks on how randomized progress guarantees flatten it.
