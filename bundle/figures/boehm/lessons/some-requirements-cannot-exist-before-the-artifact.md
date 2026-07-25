---
type: lesson
title: "Some requirements cannot exist until something exists to react to"
figure: boehm
works: [a-view-of-20th-and-21st-century-software-engineering]
axes: [expressiveness, verifiability]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Some requirements cannot exist until something exists to react to

**Lesson:** Top-down derivation assumes a fixed top. For a class of systems that assumption is not merely inconvenient, it is false: the people who will use the thing cannot state what they want in advance, not because they are careless but because their preference is not yet formed. It becomes formed by encountering a candidate and reacting to it. Boehm treats this as a property of the problem rather than a defect in the stakeholders, and he draws the consequence for method: where the target is emergent, a process that begins by demanding a complete specification is not slow, it is asking for something that does not exist and will therefore be answered with fiction.

The second route to the same conclusion runs through composition. When a system is assembled largely from parts that already exist, capability discovery flows the other way: you find out what the available pieces can do and derive what the system will do from that, rather than specifying behavior and then finding pieces to realize it. Both routes invert the direction of derivation, which is why Boehm lists top-down reductionism as a practice whose range has narrowed rather than as a principle that endures.

Diagnosis is the actual skill here. Specifiability is a property to assess before choosing an approach, and it varies within a single system: the data retention rule is knowable in advance, the interaction that will feel right is not. Getting this wrong in either direction is expensive. Demanding a specification for the unspecifiable produces documents nobody believes; treating a genuinely knowable constraint as emergent produces late discovery of something that could have been settled by asking. The corollary Boehm raises for teams working incrementally is worth keeping: preferences that emerge do so in a rough order, with survival needs surfacing before comfort ones, so the sequence of emergence is itself partly predictable even when the content is not.

A programmer who believes this builds something crude and shows it, treating the artifact as the medium in which intent becomes expressible rather than as the output of an intent already fixed. They also stay alert to the trap on the other side: the qualities that resist late retrofit, such as the ability to scale or to be secured, must be settled early even in a discovery-driven build, because no amount of subsequent reshaping repairs a foundational component chosen wrongly.

**Source:** [A View of 20th and 21st Century Software Engineering](../works/a-view-of-20th-and-21st-century-software-engineering.md) — the 1990s and 2000s discussion of user-interactive products whose capability requirements emerge rather than pre-exist, the bottom-up derivation forced by component-intensive development, and the account of scaling incremental teams where deferred system-level qualities cannot be recovered by later reshaping.
