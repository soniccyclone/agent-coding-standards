---
type: lesson
title: "Count the problems a design makes impossible to state, not just the features it provides"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [primitive-count, verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Count the problems a design makes impossible to state, not just the features it provides

**Lesson:** The largest benefits of a representation choice are usually invisible in any comparison of capabilities, because they take the form of well-known problems that simply do not arise. A famous difficulty that peer systems address with dedicated hardware and elaborate conventions can turn out to have no analogue in your design at all — not solved, not mitigated, unstatable, because the thing that makes it possible to express the dangerous situation does not exist in your naming scheme. When evaluating a design, that category has to be enumerated deliberately. Feature lists cannot show it, benchmarks cannot show it, and the design's own documentation will not mention a problem it never had.

The same choice will normally also show up as a limitation, and the two are the same fact seen from opposite sides. Whatever your representation forbids removes both a hazard and a convenience. The interesting question is what happens when you look at the convenience you have lost and ask what you do instead: sometimes the workaround forced on you turns out to be the practice you would have independently endorsed. If a structure is too complex to pass by value, the alternative is to bind it into a component and expose it only through operations — which is exactly what you should do with any structure that complicated. A constraint that pushes you toward the practice you would have chosen anyway is not costing you anything.

The discipline that keeps this honest is to check the direction of the reasoning. It is legitimate to observe that a constraint coincides with good practice; it is self-serving to derive the practice from the constraint. So ask whether you would defend the workaround in a system that permitted the alternative. If yes, the limitation is free and should be counted as a benefit alongside the problems it made unstatable. If no, it is a real cost that happens to have an available mitigation, and it should be recorded as one.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 5's treatment of the address argument validation problem, described as well known and addressed with hardware support in contemporary machines but having no counterpart in this system as a consequence of local naming; and the accompanying discussion of the inability to pass multi-segment structures between components, which proved not to be a limitation in practice because such a structure is complex enough to be worth hiding behind a component's operations anyway.
