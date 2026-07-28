---
type: lesson
title: "Keep the general mechanism ignorant of the subject matter, and put the judgment in what you choose to feed it"
figure: mccarthy
works: [programs-with-common-sense]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Keep the general mechanism ignorant of the subject matter, and put the judgment in what you choose to feed it

**Lesson:** The systems McCarthy contrasts his proposal against had a formal subject matter and a program full of domain-specific cleverness for navigating it. His inversion draws a hard line: the routine that draws conclusions is to know nothing whatsoever about what the conclusions are about, and is initially to do nothing more interesting than grinding out every one-step consequence of whatever it is handed. All the discrimination — which facts are worth combining, which line of attack to pursue — lives outside that routine, in the machinery that assembles the input. He says outright that whatever intelligence the system exhibits will not reside in the deduction routine.

What forces the split is not elegance but a cost argument he states plainly: you can never run the general mechanism over everything the system knows, because that does not finish. A mechanism that is complete over its input is only usable if something else bounds the input, and once you accept that, the bounding component stops being plumbing and becomes the substantive part of the design. This is the general shape of any system with an exhaustive core: a type checker, a constraint solver, a query planner, a rules engine, a test generator. The core's value comes precisely from its blindness, since blindness is what makes it correct on every domain and verifiable once rather than re-argued per application. The relevance layer's value comes from being unashamedly domain-specific, heuristic, and revisable.

Collapsing the two is the standard failure. Domain knowledge leaks into the engine as special cases, and each one buys local performance at the cost of the engine's universality, until nobody can say what the engine guarantees. Running the engine over everything is the opposite failure and simply does not scale. The discipline is to keep the boundary sharp enough that you can state what the engine promises without reference to any application, and to accept that the messy, approximate, frequently-wrong selection component is a permanent first-class part of the system rather than an embarrassment to be optimized away.

A programmer who thinks this way names the exhaustive component and the scoping component separately, and resists requests to teach the exhaustive one about specific cases. When such a system is too slow, they look first at what is being fed in rather than at the engine, because in this architecture almost all wasted work is selection error. And they judge the engine on whether its contract can be stated without mentioning any particular subject matter at all.

**Source:** [Programs with Common Sense](../works/programs-with-common-sense.md) — the construction section, where the immediate deduction routine is specified to use no heuristics depending on subject matter, followed immediately by the statement that the system's intelligence lies in the procedures selecting which premises to apply it to, together with the accompanying warning that the routine must never be turned loose on the whole body of what the system knows.
