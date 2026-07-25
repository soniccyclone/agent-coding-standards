---
type: lesson
title: "If writing a module is hard, the real work has not been done — choosing the modules is the design"
figure: brinch-hansen
works: [the-solo-operating-system-processes-monitors-and-classes, monitors-and-concurrent-pascal-a-personal-history]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# If writing a module is hard, the real work has not been done — choosing the modules is the design

**Lesson:** The experience reported by someone who first got a language that let him separate and test pieces independently is worth taking as a claim about where difficulty lives. The creative work turned out to be entirely in picking the pieces and arranging their dependencies; once that was settled, writing each piece was usually trivial. That is not a remark about the author's ability. It is a diagnostic. Difficulty concentrated inside a component is evidence that the decomposition around it is wrong — the component is holding responsibilities that should have been split, or compensating for state it should not be able to see, or reconstructing information a neighbor should have handed it.

The operational form of this is a size limit, adopted deliberately rather than as a guideline: a page of text per component. A limit like that is useful precisely because it is arbitrary and inconvenient. It cannot be satisfied by writing more densely, so hitting it forces the decomposition question every time, which is exactly the question you want forced. A system built under it is a sequence of components each readable in isolation and each understandable knowing only what its neighbors do rather than how, which is what makes it possible to read a whole system the way one reads a book instead of reverse-engineering it. Two dozen such components can be a complete working operating system.

A discipline that supports this well is writing each component's purpose, its guarantees, and the obligations on its callers before writing its body, and keeping that specification next to the implementation. The reason is not documentation for its own sake — it is that a specification you cannot state briefly is the earliest available signal that the boundary is wrong, arriving long before the code gets unwieldy. A programmer who works this way spends what feels like a disproportionate share of the schedule before writing much code, and should expect that trade to look like slowness right up until the point where components start being finished on the first attempt.

**Source:** [The Solo Operating System](../works/the-solo-operating-system-processes-monitors-and-classes.md) — the body of the paper, which presents each component as a purpose, a specification, and then an implementation, and the conclusion reporting the component count, the typical component size, and the claim that the system reads component by component. Also [Monitors and Concurrent Pascal: A Personal History](../works/monitors-and-concurrent-pascal-a-personal-history.md) — the account of how programming style changed once modules could be developed separately, including the adoption of the one-page rule and the observation that selecting and arranging modules was the creative part.
