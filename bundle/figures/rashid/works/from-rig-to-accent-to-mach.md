---
type: work
title: "From RIG to Accent to Mach: The Evolution of a Network Operating System"
figure: rashid
description: Rashid's own retrospective tracing three successive kernels he worked on - RIG at the University of Rochester, then Accent and Mach at CMU - explaining what each generation kept, discarded, and learned from its predecessor. Frames the throughline as a progressively more general message-passing/IPC model absorbing more of what used to be separate OS subsystems (virtual memory, device access, eventually UNIX compatibility itself). Useful as the figure's own account of why the Mach architecture ended up shaped the way it did, in his words rather than a third party's summary.
subdomains: [operating-systems-and-systems-programming]
year: 1986
url: https://www.seltzer.com/margo/teaching/CS508.19/papers/rashid86.pdf
extraction: complete
survey_pages: 10
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: third-party-rehost
tags: [work]
---

# From RIG to Accent to Mach: The Evolution of a Network Operating System

**Venue/year:** Fall Joint Computer Conference, 1986.
**Source:** https://www.seltzer.com/margo/teaching/CS508.19/papers/rashid86.pdf — course-reading mirror hosted by Margo Seltzer for a Harvard graduate systems course (CS508, 2019); confirmed serving a genuine 10-page PDF directly (`application/pdf`). A second independent course mirror exists at pages.cs.wisc.edu (~remzi/Classes/736/Fall2003/Papers/rig-accent-mach.pdf), corroborating the text is the same widely-taught paper.

## Lessons
- [Several unrelated-looking defects usually share one representational cause, and names that encode structure are a frequent culprit](../lessons/several-unrelated-defects-usually-share-one-representational-cause.md)
- [A capacity limit low in the system reappears as permanent structural complexity everywhere above it](../lessons/a-capacity-limit-low-down-becomes-structural-complexity-everywhere-above.md)
- [Write your usage assumptions down as predictions, then let measurement of the running system retire mechanism](../lessons/write-down-your-usage-assumptions-then-let-measurement-retire-mechanism.md)
- [Whether a design survives is decided outside its own quality: does it match the next machine, and can it host the software that already exists](../lessons/a-design-survives-by-matching-the-next-machine-and-hosting-the-existing-software.md)
- also carries [Choose the semantics you can reason about, then buy the cost back underneath](../lessons/choose-the-semantics-you-can-reason-about-and-buy-the-cost-back-underneath.md), [When an abstraction is too expensive to use the way the problem wants, look for two concerns fused inside it](../lessons/split-the-abstraction-that-bundles-ownership-with-execution.md), [Put mechanism in the privileged core and push every decision out of it](../lessons/the-privileged-core-should-hold-mechanism-and-refuse-to-hold-decisions.md), and [Name the role, never the thing currently filling it](../lessons/name-the-role-not-whatever-currently-implements-it.md)
