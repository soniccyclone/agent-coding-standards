---
type: lesson
title: "Treat whatever you do not control as an adversary, not a partner"
figure: pnueli
works: [on-the-synthesis-of-a-reactive-module]
axes: [verifiability, parallelizability]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---

# Treat whatever you do not control as an adversary, not a partner

**Lesson:** Showing that a requirement on a system's inputs and outputs is satisfiable establishes only that some joint history exists in which every participant behaves agreeably. If you are writing every participant, that is a fine thing to know, because you can build the agreeable behavior into each of them. The moment one of the participants is not yours, the guarantee evaporates. Existence of a cooperative history says nothing about whether your side can hold up its end when the other side chooses badly, and the other side's choices are exactly the thing you have no authority over. So consistency of a requirement and buildability of a component that meets it are different questions, and the second is strictly harder.

The correction is to stop reading a requirement as a description of a run and start reading it as a game with alternating moves. At each step the uncontrolled side commits a value, then your side commits a response knowing what just arrived. The question worth asking is whether your side has a policy that keeps the requirement true against every sequence of moves the other side could make. This reframing is not sentiment about hostile environments; nobody claims a network or a user is malicious. It is a device for getting the logical structure right, because quantifying over all opposing behaviors and then asking for a response is a different and stronger demand than asking for one behavior in which everything works out. Universal over what you cannot pick, existential over what you can, in that order.

The immediate practical consequence is that the line you draw between "the system" and "its surroundings" is load-bearing engineering, not documentation. That line decides which variables you are entitled to assign, and therefore which requirements are achievable at all. It also exposes the most common way a specification cheats: if a requirement says something about what the inputs will be, you have quietly assumed a cooperative opponent, and no implementation can enforce it. A requirement that constrains the arriving data rather than the produced response is unbuildable no matter how consistent it is, and spotting that is a matter of checking whether each clause talks about a quantity you actually set.

A programmer who works this way begins every component specification by partitioning the interface into what this component writes and what is written to it, then re-reads each requirement asking whether the other side can falsify it single-handedly. Requirements that fail this test get split into an obligation the component owes and an assumption about its surroundings that must be stated separately and justified separately, so that a later reader can see which promises rest on someone else's good behavior. Retrofitting that distinction after a system is built is where most integration surprises come from.

**Source:** [On the Synthesis of a Reactive Module](../works/on-the-synthesis-of-a-reactive-module.md) — the introduction's critique of earlier satisfiability-based synthesis as limited to closed systems, developed through the two-component argument where one component is the uncontrolled surroundings, and the section posing implementability, where a requirement constraining the arriving input is shown to admit no implementation.
