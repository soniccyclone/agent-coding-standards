---
type: lesson
title: "Make the substrate-independent form the authoritative one, not a translation you produce on demand"
figure: wilkes
works: [computers-then-and-now]
axes: [expressiveness, hardware-affinity, primitive-count]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Make the substrate-independent form the authoritative one, not a translation you produce on demand

**Lesson:** There are two ways to make a system movable between incompatible substrates. The easy one is to write it in whatever widely-supported vehicle already runs everywhere, which works and carries a hard ceiling: you inherit the vehicle's representations, and every efficiency your system might have gained from representations of its own is unavailable forever. The other way is to construct the system in substrate-independent form from the beginning, with an explicit, small set of primitives that each target supplies and mechanisms for bringing the system up on a target using an existing installation elsewhere. That is more work up front and it does not surrender the representation decision.

The deeper part is about which form counts as the real one. When the substrate-independent representation is treated as basic and every substrate-specific form is derived from it by algorithm, incompatibility between substrates stops being a property you have to work around and becomes a fact about derived artifacts, which are cheap and regenerable. That change of stance is what makes it reasonable to assemble a system out of parts that would otherwise be considered fundamentally incompatible — including, at the limit, parts of different kinds from different suppliers. Portability turns out not to be a translation problem at all; it is a question of which representation you are willing to regard as the original.

The habit to take from this is to identify, for any long-lived body of work, what form of it you would be willing to call authoritative — and to check that the form you actually maintain is that one. If the thing people edit is a substrate-specific artifact and the neutral version is generated occasionally as an export, then the neutral version is decorative and the substrate has you. If the neutral version is what gets edited and everything else is generated, then substrate changes cost a rebuild instead of a rewrite.

**Source:** [Computers Then and Now](../works/computers-then-and-now.md) — the discussion of the growing mobility of language systems between machines, contrasting the host-language route and its efficiency ceiling with writing systems in machine-independent form using bootstrapping and primitives, and the argument that the machine-independent form should be regarded as the basic one.
