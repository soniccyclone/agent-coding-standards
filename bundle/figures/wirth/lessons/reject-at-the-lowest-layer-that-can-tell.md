---
type: lesson
title: "Reject at the lowest layer that can tell, and give it the one fact it needs"
figure: wirth
works: [project-oberon]
axes: [hardware-affinity, cognitive-load, parallelizability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Reject at the lowest layer that can tell, and give it the one fact it needs

**Lesson:** In any system exposed to a shared medium, most of what arrives is not for you. The cost of that traffic is decided entirely by how deep it gets before somebody notices. If the decision is made at the top, every layer beneath has already done its full work — buffered, signalled, woken a handler, spent the attention of the general-purpose processor — and all of it is discarded. If the decision is made at the very bottom, the irrelevant traffic costs nothing that competes with anything else. The difference between these two arrangements is not a constant factor; it scales with how much of the medium's traffic is other people's, which is a number that grows as the system succeeds.

The useful move is to work out the minimum information a rejection needs, and then push exactly that fact down to the lowest layer capable of holding it. It is usually startlingly little — one field, at a fixed position, compared against one value the layer can be told once at initialisation. The reason the decision commonly sits high is not that the low layers lack the capability, it is that the identifying fact was buried inside a structure only the high layers know how to parse. So the format is part of the design: putting the discriminator first, at a fixed offset, in a fixed width, is what makes early rejection physically possible. A format that requires you to decode the whole unit before learning whether you wanted it has already decided that you will pay for everything.

Two disciplines keep this from becoming a trap. First, the filter must be defeatable, because the ability to see everything on the medium is exactly what diagnosis needs, and a filter welded shut turns a debuggable system into an opaque one — make it a mode, with the discriminating mode as the normal one and the promiscuous mode available. Second, be clear that a low filter is an optimisation and not a security boundary: it drops what is not addressed to you, which is a statement about the sender's cooperation, not about the sender's intent. Whatever correctness or protection argument the upper layers make, they must still make in full, because everything the filter admits is exactly what they would have received anyway. The filter earns its place by removing cost, and it should be judged only on that.

**Source:** [Project Oberon](../works/project-oberon.md) — section 9.3's description of the network interface's address filter, where the packet format places the destination address in the first byte after the flag so the controller can compare it against the station's own address held in one of its registers and discard the packet on mismatch, with the module's start procedure taking a boolean parameter selecting filtered operation, the filtered mode described as the normal one on the grounds that discarded packets then require no interaction with the computer's processor.
