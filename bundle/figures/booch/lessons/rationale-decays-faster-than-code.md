---
type: lesson
title: "Design rationale decays far faster than the code it explains, so treat intent as a perishable asset"
figure: booch
works: [the-promise-the-limits-and-the-beauty-of-software, architecting-the-unknown, the-future-of-software-engineering]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Design rationale decays far faster than the code it explains, so treat intent as a perishable asset

**Lesson:** Source code is durable and reasoning is not. The people who chose a decomposition can explain it vividly and at length; a decade later the decomposition still runs and the explanation is gone, held only in the memories of people who have moved on. What decays is not the what but the why: which alternatives were rejected, which constraint forced the awkward boundary, which apparent redundancy is load-bearing. Once that is lost, successors cannot distinguish a deliberate commitment from an accident, so they either freeze everything out of fear or change the wrong thing confidently. This is why most long-lived systems end up with structures nobody intended: not because no one made decisions, but because tens of thousands of local decisions accumulated with no surviving account of which were meant.

The asymmetry has a mechanism worth understanding. Rationale is held socially, in a group's shared memory, and social memory has a half-life set by turnover, reorganization, and the promotion of the original designers away from the work. Systems held together by one unusually strong personality are the extreme case: coherence persists exactly as long as that person does, and the interesting question about such a project is always what happens after. Geographic and temporal distribution accelerate the same decay, because rationale that was never spoken aloud in a shared room was never held anywhere but in individual heads.

The practical stance that follows is to treat intent as something actively maintained rather than assumed. Recover it while its holders are still reachable, record it at the granularity of decisions rather than of components, and expect to run periodic excavations on systems whose original designers are gone. The excavation is a real activity with real technique: find the kernel abstractions, name the recurring arrangements the team uses without having names for, and write down which of them are deliberate. A programmer who takes this seriously interviews people before they leave, writes down why rather than what, and treats an undocumented boundary as a liability that will be misread rather than as self-evidently correct.

**Source:** [The Promise, the Limits, and the Beauty of Software](../works/the-promise-the-limits-and-the-beauty-of-software.md) — the discussion of accidental versus intentional structure, the loss of shared team memory across distributed and long-lived projects, and the practice of excavating and naming a system's unnamed recurring arrangements. Also [Architecting the Unknown](../works/architecting-the-unknown.md) on structure surviving in code while its rationale evaporates as originators depart, and [The Future of Software Engineering](../works/the-future-of-software-engineering.md), which frames recovering the intent of legacy systems as an emerging specialty in its own right.
