---
type: lesson
title: "The startup sequence is the construction sequence"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, verifiability]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# The startup sequence is the construction sequence

**Lesson:** How a system comes up from nothing is usually treated as an implementation chore, described briefly if at all, and delegated to whoever is unlucky. That undervalues it twice over. The startup is a total order on the system's parts in which each stage can only use what earlier stages have already established, so writing it down forces every latent assumption about who depends on whom into the open — an assumption that survives a review can rarely survive an attempt to start from a bare machine. And the same order is the only order in which the system can be developed in the first place, because a stage cannot be exercised until everything below it exists. Designing the startup and planning the construction are therefore one activity, and doing them separately means discovering in the second that the first was wrong.

The practical consequence is to design in stages that are each independently reachable and independently testable, not merely conceptually layered. A stage is well chosen if you can stop there, on real hardware, with everything above it absent, and still do something — inspect memory, read a sector, load a module. That property is what makes the sequence a development plan rather than a diagram: it gives you a place to stand while you build the next stage, and it gives you a place to fall back to when the next stage is broken. Layering that reads well but cannot be halted partway through is layering that will not help you bring the system up, and will not help you diagnose it later.

The last stage deserves particular attention because it is where the character of the system is decided. If the final act of the boot is to load one named component, and that component's own act is to load another, then the identity of what the machine becomes is a small number of names rather than a structural property — which means the same machinery brings up the production system, a diagnostic shell, or a repair tool depending on what you name. Systems whose startup terminates in a hard-wired destination lose that for nothing, and lose it exactly when they need it.

**Source:** [Project Oberon](../works/project-oberon.md) — section 14.1's opening remark that startup is given little attention in system descriptions, is itself a non-trivial design consideration, and directly determines the steps in which a system is developed from scratch, mirroring the steps in which it builds itself up from a bare store; together with the four-stage sequence in which each stage's final act names the module that begins the next.
