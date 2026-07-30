---
type: work
title: "Tentative Steps Toward a Development Method for Interfering Programs"
figure: jones
description: The founding rely/guarantee paper. Extends Jones's VDM-style development method to concurrent programs whose components interfere with each other through shared state, by giving each component a rely condition (what interference it can assume from its environment) and a guarantee condition (what interference it promises not to exceed). This decomposes reasoning about a concurrent program into per-component proofs, avoiding the combinatorial blowup of reasoning about all possible interleavings directly.
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
year: 1983
url: https://ilyasergey.net/CS6213/_static/05-owicki/rg.pdf
survey_pages: 24
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: third-party-rehost
extraction: complete
tags: [work]
---

# Tentative Steps Toward a Development Method for Interfering Programs

**Venue/year:** ACM Transactions on Programming Languages and Systems (TOPLAS) 5(4):596-619, 1983.
**Source:** https://ilyasergey.net/CS6213/_static/05-owicki/rg.pdf — course-reading mirror on Ilya Sergey's (NUS, established PL researcher) graduate course site, explicitly labeled with this paper's title and author in the course's rely-guarantee reading list (HTTP 200, confirmed live; 24-page PDF matches the cited pp. 596-619 range exactly). The ACM Digital Library copy (https://dl.acm.org/doi/10.1145/69575.69577) is paywalled; no self-archived copy exists on Jones's own Newcastle homepage, which lists only the DOI for this entry. CORE (core.ac.uk) and ResearchGate both index copies but blocked automated fetch (403) so were not usable as citations.

## Lessons
- [Give every component a written statement of the interference it may assume and the interference it may inflict](../lessons/write-down-what-you-assume-about-interference.md)
- [A method is only usable at scale if no completed design step can be invalidated by a later check](../lessons/no-design-step-may-be-invalidated-by-a-later-check.md)
- [Describe what an operation does as a relation between before and after, not as an assertion about after](../lessons/specify-the-relation-not-the-final-state.md)
- [Choose the property that must hold at every intermediate moment before you design the parts that run](../lessons/choose-the-property-that-holds-mid-flight-first.md)
- [Let concurrent participants coexist by partitioning what each may change, not by scheduling when each may run](../lessons/partition-the-right-to-change.md)
- [Constrain shared state to move in one direction, and a stale read becomes merely conservative](../lessons/make-shared-state-move-in-one-direction.md)
- [Expect refinement to resurrect obligations the abstraction had no vocabulary to state](../lessons/refinement-resurrects-obligations-the-abstraction-could-not-state.md)
- [A component whose only job is to make things faster has a vacuous functional specification](../lessons/a-component-that-only-optimizes-has-a-vacuous-functional-spec.md)
- [Treat shared memory and message passing as alternative realizations of one abstraction, chosen late](../lessons/treat-shared-variable-versus-message-as-a-late-choice.md)
