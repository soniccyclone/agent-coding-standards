---
type: lesson
title: "Do not hide a difference in kind behind a uniform interface"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, verifiability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Do not hide a difference in kind behind a uniform interface

**Lesson:** There is a permanent temptation to make a remote thing look exactly like a local one, so that the code above stops caring which it has. Treated as an engineering challenge — get the syntax identical and push the difference down until it shows up only as reduced speed — it is a fine challenge, and that framing is where it goes wrong. Speed is not the only thing that differs. The remote case can fail while the local case cannot, can fail partially, can fail after apparently succeeding, and can be slower by a factor large enough that an algorithm which was reasonable becomes absurd. An interface that presents both as the same operation is not abstracting over a detail; it is asserting an equivalence that does not hold, and the code written against it will be correct only for the case its author happened to be imagining.

The alternative is to admit the second thing as its own kind of operation, named differently, invoked deliberately, and available in a layer that a program can decline to depend on. This looks like a step backwards in convenience and is a large step forward in what you can say about the resulting system. Now the places where a call can fail for reasons outside the machine are visible in the text, so they can be counted and reviewed. Now the cost of a design is visible at the point of design, because a programmer who has to write the transfer explicitly notices when they have written it inside a loop. And now the base system does not depend on the facility at all: it becomes an ordinary component built on the ordinary system, which means it can be absent, replaced, or wrong without the rest of the system being implicated.

The general rule is to ask which differences an abstraction is entitled to hide. It may hide details that do not change what the caller must handle — a layout, a device model, an algorithm choice. It must not hide a difference in failure modes, and it must not hide a difference in cost so large that it changes which algorithms are viable, because both of those are things the caller is obliged to reason about. When you find yourself hiding one of them, the honest move is usually to keep the transparency and lose the uniformity: two operations that differ visibly are easier to program against than one operation that is secretly two.

**Source:** [Project Oberon](../works/project-oberon.md) — section 10.1's contrast between the two views of a network of workstations, the more demanding one holding that all stations constitute a single unified address space in which the connections between processors are hidden from users and become apparent at worst as slower access rates, regarded as a challenge to implementors, and the more conservative view that the stations are essentially autonomous units exchanging data infrequently, so that access to data on a partner is initiated by explicit transfer commands and the commands handling external access are not part of the basic system but are implemented in modules regarded as applications; and the statement that the Oberon system adheres to the second view, with its network module described as an autonomous command module built on the driver.
