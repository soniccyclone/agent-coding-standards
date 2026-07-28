---
type: lesson
title: "Transmit access, not the thing itself, and make duplication an explicit act"
figure: milner
works: [a-calculus-of-mobile-processes]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---
# Transmit access, not the thing itself, and make duplication an explicit act

**Lesson:** Faced with modelling one component handing another the ability to work with a third, the obvious design sends the third component itself in the message. The alternative taken here is to send only a name by which the third component can be reached, and the reasoning behind that choice generalizes far past process calculus. Sending the thing means that if the recipient mentions its parameter twice, the thing gets replicated — so duplicating a stateful component becomes an accidental side effect of ordinary communication. Sending the thing also grants total access, when what actually needs modelling is partial access: the recipient gains one way of interacting while the original keeps others, possibly with parties the recipient knows nothing about.

Holding a reference is therefore not a weaker version of holding the thing; it is a different and more precise relation, and the precision is what buys expressiveness. Different recipients can be handed different names into the same component and thereby granted different powers over it. Nothing about the transfer implies exclusivity, copying, or a change in the component's own identity. The paper shows that reference-passing loses nothing in raw power — process-passing can be simulated by handing over a name that acts as a trigger, and a translation from a higher-order calculus into this first-order one exists — while remaining more discriminating about what was actually granted.

What reference-passing genuinely cannot do by itself is copy. That looks like a limitation and is treated as a feature: since duplication does not fall out of communication, it has to be asked for, and it is introduced as a separate explicit construct that spawns a fresh instance per invocation. The paper observes that this is the only form of recursion needed to encode a full functional calculus. Aliasing and copying, conflated in most designs, become two independently controllable powers.

The programmer who takes this seriously stops treating "pass the object" and "pass a handle to the object" as an implementation detail chosen for efficiency. It is a semantic decision about who may do what to shared state, and about whether the system can silently acquire a second copy of something that was supposed to be unique. Designs where every transfer might be a copy have no way to express single ownership; designs where transfer is always a grant of partial access must say explicitly when a copy is intended, which is exactly the sentence you want in the source.

**Source:** [A Calculus of Mobile Processes, I and II](../works/a-calculus-of-mobile-processes.md) — Part I's enumerated justification for instantiating names to names rather than to processes, and the later examples comparing parameter-passing of processes against passing a trigger link, culminating in the introduction of an explicit replication construct.
