---
type: lesson
title: "Detectability falls off as you descend the stack, so reason about depth before reasoning about cleverness"
figure: thompson
works: [reflections-on-trusting-trust]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Detectability falls off as you descend the stack, so reason about depth before reasoning about cleverness

**Lesson:** The compiler is a rhetorical choice in Thompson's argument, not its subject. He says as much: the same reasoning applies to an assembler, a linker, or the microcode beneath the instruction set, and the deeper the layer, the less chance anyone notices. This turns a security argument into a general claim about layered systems. Each abstraction boundary you build is a place where the layer above stops looking, by design — that is what makes the boundary useful — and every such place is therefore a place where a defect, malicious or accidental, becomes cheaper to hide and more expensive to find.

The mechanism is straightforward once stated. Tooling, expertise, and attention are distributed unevenly across a stack, concentrated heavily near the top where most people work. Depth reduces the population capable of inspecting a layer, reduces the frequency with which anyone does, and reduces the resolution of the instruments available when they try. So the probability of detection is not a function of how subtle the defect is; it is dominated by how far down it sits. A crude fault in microcode outlives a sophisticated one in application source. This also explains why the usual intuition — that harder-to-write attacks are rarer and so less worrying — misleads: the effort is spent once, and the concealment is provided free by the architecture.

The behavioral consequence is that when you assess where a system can go wrong, you should order your worry by layer depth before you order it by ingenuity. Time spent auditing the layer everyone reads is time spent where detection was already likely. It also argues for keeping the number of trusted layers small and their implementations boring enough that independent inspection stays feasible, rather than accepting an ever-deeper tower on the grounds that each level is individually reasonable. And it suggests a specific kind of humility about claims of verification: a proof, a test suite, or a review establishes something about one layer while quietly assuming everything beneath it, and stating that assumption out loud is usually more valuable than strengthening the layer you already checked.

**Source:** [Reflections on Trusting Trust](../works/reflections-on-trusting-trust.md) — the closing moral, where the argument is generalized from the C compiler to any program-handling program down to hardware microcode, with the observation that such faults grow harder to detect as the level drops.
