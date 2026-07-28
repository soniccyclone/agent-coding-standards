---
type: lesson
title: "Sort problems by whether better technology would erase them"
figure: saltzer
works: [traffic-control-in-a-multiplexed-computer-system]
axes: [cognitive-load, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Sort problems by whether better technology would erase them

**Lesson:** Before designing anything, split the requirement list into two piles: the problems that exist only because the machine is too small, too slow, or too few, and the problems that would still exist on infinitely fast hardware. Sharing one scarce resource among many claimants is the first kind — it is a tax collected by the current state of the art, and a future machine can simply pay it off. Letting independent parties cooperate, signal each other, express parallelism, and see different views of the same facility is the second kind — no amount of speed retires it, because it comes from the structure of the problem, not the cost of the equipment.

The split matters because the two piles deserve different engineering. Scarcity-driven mechanism should be treated as replaceable plumbing: build it cleanly, but expect it to be thrown away when the constraint moves, and do not let its shape leak into what callers see. Structure-driven mechanism is the part worth spending abstraction budget on, because whatever interface you give it will outlive several generations of hardware. Getting the classification backwards is expensive in both directions — you end up canonizing a workaround for a shortage that later evaporates, or treating a permanent coordination problem as a temporary optimization and never giving it a real interface.

A programmer who believes this reads a feature request twice: once for what is being asked, once for whether the asking would survive a tenfold improvement in the underlying machine. It changes where the effort goes. Multiplexing tricks, packing, batching, and cache-conscious layout are all scaffolding around a shortage, so they get isolated behind a boundary and measured. Naming, signalling, coordination, and the ability for two clients to hold different policies are permanent, so they get designed rather than discovered. It also gives an honest answer to the perennial "will this still matter in ten years" question, without appealing to taste.

**Source:** [Traffic Control in a Multiplexed Computer System](../works/traffic-control-in-a-multiplexed-computer-system.md) — the opening chapter separates the utility's problems into two named classes and then assigns each of the seven traffic-control objectives to one of them; the closing summary returns to the same split to say which parts of the design are provisional and which are not.
