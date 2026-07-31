---
type: lesson
title: "Read the shape of the optimization curve, not the size of the last gain — it tells you whether the design or the code is wrong"
figure: hoare
works: [the-emperors-old-clothes]
axes: [hardware-affinity, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Read the shape of the optimization curve, not the size of the last gain — it tells you whether the design or the code is wrong

**Lesson:** A performance rescue produces a sequence of rounds, and the sequence carries more information than any round in it. Doubling the throughput is encouraging in isolation. Doubling it again for twice the effort, and being able to see that the next doubling will cost more still, is a different message entirely: the cost per unit of improvement is rising while the yield falls, which is the signature of local repair applied to a structure that is wrong at the level of the design. Effort spent inside that regime is not progress with a slow start; it is progress toward an asymptote nowhere near where you need to be. The decision is made by arithmetic, not morale — take the distance still to cover, take the per-round yield and the per-round cost, and see whether the two ever meet.

Getting the distance right requires an external number rather than an internal one. Improvement measured against your own first attempt always looks like momentum; measured against the thing your users already have, it can be three orders of magnitude short. Whenever a predecessor system, a competitor, or a hand-written baseline exists, that figure is the denominator, and a gap of that magnitude is never closed by tuning, because tuning removes constant factors while the gap is structural — in the classic case, a working set that does not fit and therefore trades against a store an order of magnitude slower, which no amount of local reprogramming converts into a fit.

Two habits protect against burning a project in this regime. First, run the arithmetic before authorizing the next round, and be explicit that the alternative under consideration is abandonment or redesign, not merely a slower schedule. Second, distrust the escape hatch. Enlarging the machine is the move that makes the symptom go away without touching the cause, and where it is available it will be taken repeatedly, each time preserving the original error and raising the eventual bill. Where it is unavailable, the project is forced into an honest verdict early. Recognizing that the verdict is honest — and paying its cost once, in full — is cheaper than the alternative of spending years converting a design error into an operating expense.

**Source:** [The Emperor's Old Clothes](../works/the-emperors-old-clothes.md) — the account of the Mark II ALGOL compiler delivered at two characters per second against an existing implementation running at about a thousand, the successive rounds of reprogramming that doubled and redoubled the speed while requiring more work for less effect, the identification of thrashing against a fifteen-times-slower backing store as the cause, the unavailability of the usual remedy of enlarging main store, and the resulting decision to abandon the entire project.
