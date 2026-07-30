---
type: lesson
title: "Scope a system to what one mind can hold, and treat added people as added coupling"
figure: wirth
works: [a-plea-for-lean-software]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Scope a system to what one mind can hold, and treat added people as added coupling

**Lesson:** The usual assumption is that a complex system requires a large organization, and that assumption should be inverted: if no single person can hold the whole system — its structure, its decisions, at least the significant detail of every part — that is evidence the system should not be built in that form. Comprehensibility by one mind is not a nice property of small projects; it is a design constraint that bounds what you are allowed to attempt, and it is the constraint that keeps a system from becoming something whose behavior nobody can predict and whose repairs nobody can validate. A working existence proof matters here more than argument: a full workstation environment — storage, files, windowing, networking, compiler, editors — built from bare hardware by two people in three years, and then described in its entirety, source included, in a single book. The book is the real claim. A system that can be written down and read end to end is one that stayed inside the constraint.

The reason large teams do not simply scale is that the dominant cost is not the coding, it is the communication, and communication cost grows with team size while the useful work does not. Once the coordination overhead dominates, the project is in trouble whether or not anyone has noticed yet — the symptoms show up as integration problems and duplicated functionality rather than as anything labeled a communication failure. This is why the response to a slipping schedule should never reflexively be more people: adding staff buys throughput on the part of the problem that was cheap and adds load to the part that was already the bottleneck.

There is a second organizational claim worth taking seriously because it follows from the same premise. Slicing a team into managers, designers, programmers, analysts and users installs exactly the communication boundaries you were trying to avoid, and each boundary is a place where an understanding gets summarized and degraded. Everyone should participate in every aspect, with different emphasis rather than different jurisdiction, and everyone — managers included — should spend real time using the product. There is no substitute for having built and used the thing when it comes to spotting the mistake, or the redundancy, that no specification review will catch. Judgment about a system is a byproduct of contact with it, so any structure that keeps decision-makers away from that contact is manufacturing bad decisions.

**Source:** [A Plea for Lean Software](../works/a-plea-for-lean-software.md) — the Project Oberon section on two people building and documenting a complete system, plus the closing lessons on systems not understood in their entirety by an individual, on communication problems growing with team size, and on role separation being detrimental with everyone including managers using the product.
