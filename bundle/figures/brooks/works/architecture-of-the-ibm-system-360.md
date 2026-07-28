---
type: work
title: "Architecture of the IBM System/360"
figure: brooks
description: Defines "architecture" in the modern computing sense — the programmer-visible instruction set, registers, and data formats that a family of machines commits to, kept separate from the implementation details that vary across price and performance tiers. This separation let System/360 span a wide range of hardware while running the same software, an idea that seems obvious now precisely because this paper (and the project behind it) established the convention. It's the founding document of computer architecture as its own discipline, distinct from logic design on one side and software on the other.
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
year: 1964
url: https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/Arch/Architecture-of-the-IBM-System-360.pdf
extraction: complete
access: public
host: third-party-rehost
tags: [work]
---

# Architecture of the IBM System/360

**Author(s):** Gene M. Amdahl, Gerrit A. Blaauw, Frederick P. Brooks Jr.
**Venue/year:** IBM Journal of Research and Development 8(2), April 1964, pp. 87-101.
**Source:** https://people.cs.umass.edu/~emery/classes/cmpsci691st/readings/Arch/Architecture-of-the-IBM-System-360.pdf — course-reading mirror hosted on a UMass Amherst faculty page (CMPSCI 691ST), verified live (200 OK, application/pdf). The original IBM Journal of Research and Development issue is paywalled via IEEE Xplore/ACM; this is a third-party rehost linked here rather than redistributed.

## Lessons

- [Commit to what a thing does and refuse to commit to how, because the visible contract must outlive every mechanism that satisfies it](../lessons/commit-to-the-interface-and-leave-the-mechanism-free.md)
- [State what you do not guarantee as carefully as what you do, and make the mechanism reject it, or the running implementation becomes the specification](../lessons/specify-the-undefined-and-trap-it-in-the-mechanism.md)
- [The parts of a system improve at different speeds, so put the seams where the rates diverge and keep spare room in every vocabulary you fix](../lessons/design-where-the-rates-of-change-differ.md)
- [A design is only good relative to alternatives costing the same, and the metric that decides belongs at the level of the user's result, not the component's](../lessons/compare-only-against-equal-cost-alternatives.md)
