---
type: lesson
title: "What the property depends on, plus what you already know, sets the floor on how much you must examine"
figure: reynolds
works: [the-craft-of-programming]
axes: [cognitive-load, expressiveness]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# What the property depends on, plus what you already know, sets the floor on how much you must examine

**Lesson:** Two searches over the same collection can have irreducibly different costs, and the difference is not in the loop — it is in what the property being sought depends on. Locating an element that equals a given value asks a question about one element at a time, so the first success ends the work and nothing else need be looked at. Locating a largest element asks a question about the element's relationship to every other one, so no partial scan can ever justify stopping: the next thing you have not looked at could invalidate the answer. Before trying to make a scan faster, classify its predicate as local or global. That classification, not ingenuity, decides whether early exit is available at all, and pursuing an early exit for a global property is wasted effort on a mathematically impossible goal.

The second determinant is what you knew before you started. With no information about the contents, there is no reason to prefer one probe order to another, every untested element is equally likely to be the one you want, and testing them one at a time is the best available — the linear cost is not a weakness of the program but a consequence of the programmer's ignorance. Supply a fact about the arrangement, though, and the picture changes out of recognition: if the contents are known to be ordered, one probe eliminates a whole region rather than one element, because the order lets a single comparison be read as a statement about everything on one side. The improvement did not come from a better loop. It came from an assumption, and it is only available to someone who arranged for that assumption to hold.

Read together, these two determinants tell you where to spend effort when something is too slow. Do not start with the inner loop; start by asking what the question depends on and what you are entitled to assume. If the predicate is global, either accept the full scan or change the question. If the predicate is local and you are still paying full price, the missing ingredient is an invariant about the data — sortedness, an index, a maintained summary — and the real work is deciding who maintains it and what that maintenance costs elsewhere. Every asymptotic improvement of this kind is a trade in which some other part of the system pays to keep a promise, and locating that promise is the design act; the fast algorithm is a consequence.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — the closing discussion of Section 2.2.9, which contrasts finding a maximum against finding an element of a given value on the grounds that one property depends on the entire segment while the other is a property of the element alone, argues that absent information about the contents there is no reason to prefer one search order and the linear program is the best available, and points forward to the dramatic change when the programmer possesses a priori information; together with Section 2.2.10's binary search, where ordering lets one inspection exclude an entire segment.
