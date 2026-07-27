---
type: lesson
title: "When an abstraction is too expensive to use the way the problem wants, look for two concerns fused inside it"
figure: rashid
works: [mach-a-new-kernel-foundation-for-unix-development, from-rig-to-accent-to-mach]
axes: [parallelizability, primitive-count, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# When an abstraction is too expensive to use the way the problem wants, look for two concerns fused inside it

**Lesson:** There is a recognizable failure signature in mature systems: an abstraction everybody agrees is the right unit turns out to be so costly that practitioners route around it, and the workarounds become folklore. Programs that need many concurrent activities stop asking the system for many of its concurrency units and start simulating them privately, because each one the system hands out drags along a whole apparatus of accounting the program did not ask for. The usual reading of this situation is that the implementation is slow and needs tuning. The more productive reading is that the unit is measuring two different things at once, and one of them is the expensive one.

The diagnostic move is to ask what an instance of the abstraction actually costs and then check whether every part of that cost is entailed by every use. If the answer is that a program creating a hundred of these things wanted a hundred of one ingredient and one of the other, the abstraction is a fusion of two independent axes and should be two abstractions. Separating a container of resources and rights from a bare locus of execution costs nothing conceptually — the old unit is recovered exactly as a container holding a single locus — while making the cheap thing cheap and letting programs buy each dimension in the quantity they need. Notice what this fixes that private workarounds cannot: the system now knows about these execution units, so it can place them on real processors. A simulated concurrency unit invisible to the scheduler can never use a second CPU, no matter how efficient it is, because the entity doing the placing does not know it exists.

The deeper point is that the shape of the abstraction determines which hardware configurations a program can express itself onto. Once resource containers and execution loci are separate primitives, one program text can address tightly shared memory, partially shared memory, and machines connected only by a wire, by choosing how many containers to spread its execution loci across. A single fused unit forces one answer to that question at design time. This is why the split reads as a hardware-affinity result and not merely a performance tweak: it aligns the primitives with the way real machines are actually built, as bundles of memory with some number of processors attached and some channel to elsewhere.

A programmer who internalizes this treats "everyone works around this abstraction" as evidence about the abstraction rather than about the workaround, and treats the observed cost profile of use as the specification for how to factor it. The discipline is unglamorous: enumerate what an instance owns, ask which owners the caller actually wanted, and split along whatever line that question exposes.

**Source:** [Mach: A New Kernel Foundation for UNIX Development](../works/mach-a-new-kernel-foundation-for-unix-development.md) — the section arguing that the conventional process abstraction was inadequate for servers and for shared-memory parallel machines, and its factoring of that abstraction into a resource-holding environment and a separate lightweight unit of computation.
