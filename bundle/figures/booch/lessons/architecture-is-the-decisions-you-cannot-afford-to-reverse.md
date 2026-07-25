---
type: lesson
title: "Architecture is the small set of decisions whose reversal is expensive, and which decisions those are keeps moving"
figure: booch
works: [architecting-the-unknown, the-promise-the-limits-and-the-beauty-of-software, the-future-of-software-engineering]
axes: [primitive-count, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Architecture is the small set of decisions whose reversal is expensive, and which decisions those are keeps moving

**Lesson:** Every design act commits you to something, but only a few commitments are load-bearing. The useful test is not aesthetic or hierarchical; it is the cost of undoing. If a choice can be changed on a quiet afternoon without disturbing anything else, it is ordinary design work, however clever. If changing it forces a coordinated campaign across teams, releases, and customers, it belongs to the system's structure whether anyone wrote it down or not. This makes structural significance an economic property rather than a diagrammatic one, and it gives a practical filter for the perpetual question of what is worth arguing about in a review.

The same test explains why enormous systems have surprisingly small essences. A codebase of tens of millions of lines usually reduces to a handful of abstractions and a handful of recurring arrangements among them, with the remaining bulk devoted to formats, devices, interfaces, and accumulated adaptation. Those few abstractions are where the expensive decisions live; everything else is derivable, replaceable, or negotiable. A reader who can find that kernel understands the system, and a reader who tours the bulk without finding it does not, no matter how much of it they have read. So the first job on encountering an unfamiliar system is not to read it broadly but to search for the minimal set from which its shape follows.

The subtler half of the lesson is that the set is not stable. A decision that costs nothing to change today can become prohibitively expensive once volume, regulation, third-party dependence, or an underlying platform shift arrives, and a decision that once anchored everything can quietly become cheap again. Structure therefore has to be re-identified periodically rather than inherited from the original design documents. A programmer who takes this seriously behaves differently in two ways: they refuse to treat every design conversation as architectural, and they periodically re-audit which commitments have become load-bearing since the last time anyone looked.

**Source:** [Architecting the Unknown](../works/architecting-the-unknown.md) — the section defining architecture against ordinary design and pinning significance to the economic cost of change, including the observation that the significant set drifts over time. Also [The Promise, the Limits, and the Beauty of Software](../works/the-promise-the-limits-and-the-beauty-of-software.md) and [The Future of Software Engineering](../works/the-future-of-software-engineering.md) — the recurring account of examining large commercial systems and finding their real substance concentrated in a few dozen abstractions surrounded by peripheral machinery.
