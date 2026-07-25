---
type: lesson
title: "Authority That Routes Through the Center Is a Bottleneck"
figure: corbato
works: [introduction-and-overview-of-the-multics-system, multics-the-first-seven-years]
axes: [parallelizability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Authority That Routes Through the Center Is a Bottleneck

**Lesson:** Multics treated the right to allocate resources as something to be subdivided and handed down rather than exercised from a single point. Budgets flow from a system administrator to project administrators to team leaders, and at every step the holder can reallocate what he controls without consulting anyone above him. Responsibility for the system's own software was split the same way, with individual translators delegated to independent groups, and the 1965 paper calls this isolation and distribution of responsibility mandatory for the growth of large systems rather than merely convenient.

The seven-years paper shows what that bought. A project administrator could define which procedures his members could reach and what ran when they logged in, which meant a group could construct an entire alternative environment on top of the system — a BASIC machine that mimicked Dartmouth's, an emulation of the batch operating system, an APL machine — without negotiating with the center and without modifying anything shared. The extensions happened in parallel with each other and with the system's own development, because nobody was queued behind the same scarce approver.

The underlying claim generalizes past administration. Any capability that requires a central party's attention to exercise converts that attention into the system's limiting resource, and attention does not scale with anything. Delegation is what turns a serial queue into independent work, and the mechanism that makes delegation safe is the same access control that was already needed for privacy. A designer who believes this measures a facility by what someone else can build with it without asking, and reads "file a request with our team" as a defect report about the interface rather than a description of a process.

**Source:** [Introduction and Overview of the Multics System](../works/introduction-and-overview-of-the-multics-system.md) — the software design features section on hierarchical, reallocatable resource budgets and decentralized system programming. The seven-years paper's sections on administration and environment shaping report the delegated subsystems that resulted.
