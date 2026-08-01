---
type: lesson
title: "You choose the root; the dependency graph chooses the privileged set"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# You choose the root; the dependency graph chooses the privileged set

**Lesson:** A system that has a privileged region — a core loaded by special means, a trusted computing base, a bundle that ships inside the binary, anything that gets in before the ordinary mechanism exists — invites the belief that membership of that region is a design decision made component by component. It is not. Only one thing is chosen: the root, meaning the single capability the region has to provide. Everything else is admitted because something already admitted refers to it, and the region's true extent is the transitive closure of that reference relation. A design review that inspects the list of members is reviewing an output. The input is the root and the import edges.

Two consequences follow, and both are practical. First, the way to shrink a privileged region is never to argue about a member, it is to sever an edge — to find the reference that dragged in a subtree and remove the need for it, at which point everything below it leaves without further discussion. Second, the region grows silently. Adding an import to a component that happens to be inside the core enlarges the core by that import's whole closure, and nothing in the act of writing that import looks like a decision about privilege. If the region matters, its closure should be computed mechanically and checked, because the human process that would have caught the growth does not exist: nobody experiences adding a normal import as an architectural change.

The same reasoning turns the region into a design instrument rather than a burden. If the root is a name resolved at load time rather than a hard-wired component, the closure it drags in is whatever that name's dependencies are — so naming a different root produces a different privileged region, and the identical loading mechanism yields the running system, a stripped diagnostic environment, or a repair tool. That is the payoff for having made membership a consequence of the graph instead of a list: alternative configurations become alternative roots, and cost nothing to maintain.

**Source:** [Project Oberon](../works/project-oberon.md) — section 14.1's explanation of the inner core, where module Files is present because it is imported by Modules and FileDir because it is imported by Files, only the disk driver among device drivers is included, and the boot-linker commands of section 14.2 differ only in which module is named as the top of the hierarchy forming the core.
