---
type: lesson
title: "Stop choosing between methods with incomparable costs and race them, because the pointwise minimum is nearly free"
figure: stearns
works: [on-the-computational-complexity-of-algorithms]
axes: [parallelizability, cognitive-load]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Stop choosing between methods with incomparable costs and race them, because the pointwise minimum is nearly free

**Lesson:** Given two methods whose cost profiles cross — each better than the other on some inputs, neither dominant — the instinct is to characterise the crossover and dispatch on it. That work is usually unnecessary. Run both, interleaved, and emit the answer the moment either produces it: the combined method's cost at every input is the smaller of the two costs, and the only price is a constant factor from doing two things where you did one. The class of things achievable within a given budget is therefore closed under taking the pointwise minimum of budgets, and it is closed for a completely trivial reason. No analysis of where the crossover lies, no dispatch logic, no risk of dispatching wrongly.

The consequence is that "which method is better" is often a malformed question. It presupposes that you must commit, and commitment is only forced when the methods contend for a resource that cannot be duplicated. When the scarce resource is the thing being spent — time to first answer — duplicating the attempt costs a constant and buys the envelope of both. When the scarce resource is something the attempts genuinely share, such as exclusive access to a device or the right to perform a side effect, racing is unavailable and the crossover analysis is back on the table. Distinguishing those two situations is the actual decision, and it is a much easier one than characterising a crossover.

This is why hedged requests, speculative execution and running a fast heuristic alongside a complete method are not hacks but the standard exploitation of a structural fact. Two cautions come with it. The constant factor is a constant only if the racers do not interfere; contention for cache, bandwidth or locks turns the constant into something worse and can make the race slower than either racer alone, so the independence has to be checked rather than assumed. And the pattern demands that the losing attempt be abandonable without consequence, which means the effects must be confined until one racer wins — the discipline of keeping speculative work free of externally visible effects is the price of admission, and it is worth paying because it converts a modelling problem into a plumbing problem.

**Source:** [On the Computational Complexity of Algorithms](../works/on-the-computational-complexity-of-algorithms.md) — the intersection theorem in the time-limited-computations section, proved by constructing a single device that incorporates both machines, computes both ways simultaneously, and emits each output as soon as either of the two has produced it, thereby operating within the pointwise minimum of the two bounds.
