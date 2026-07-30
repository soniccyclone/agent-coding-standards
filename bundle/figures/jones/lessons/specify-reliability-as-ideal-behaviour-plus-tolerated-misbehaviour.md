---
type: lesson
title: "Specify a fault-tolerant component as ideal behaviour plus the substrate misbehaviour it survives"
figure: jones
works: [development-methods-for-computer-programs-including-a-notion-of-interference]
axes: [verifiability, expressiveness]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Specify a fault-tolerant component as ideal behaviour plus the substrate misbehaviour it survives

**Lesson:** The standard way to pin down a component whose job is to work despite an unreliable foundation is to describe the machinery: the states each end goes through, the messages, the timers, the retries. That is not a specification, it is an implementation written in a language with fewer details. It cannot be used to judge an alternative implementation, it cannot be reviewed by anyone who wants to know what the component achieves, and it silently conceals the one number everybody actually needs. The alternative has two parts and no machinery. First, say what perfect thing the component appears to be — the simplest ideal object with the same externally visible behaviour, often something as plain as a container that gives back what it was given, in order. Second, say how badly the layer underneath may misbehave while that appearance still holds.

The second part is what makes the pair a specification rather than a wish, and it is exactly the same construction as declaring what interference a component tolerates from a concurrent neighbour, with the direction rotated: instead of naming the disturbance a sibling may inflict, you name the corruption a substrate may inflict. That symmetry is worth internalizing because it means one habit of thought covers both. In each case the component is granted an allowance it may lean on, and in each case a component that survives more than its allowance is a legitimate substitute for one that survives less.

Two consequences follow for engineering practice. A reliability claim with no stated fault allowance is empty, because every mechanism works when nothing goes wrong and none works when everything does; the interesting content of the component is entirely in where that line sits. And two components implementing the same protocol are comparable only along that line — not by their internals — so the allowance is the right thing to put in the interface and the right thing to argue about in review.

**Source:** [Development Methods for Computer Programs including a Notion of Interference](../works/development-methods-for-computer-programs-including-a-notion-of-interference.md) — the proof-rules subsection of the communication-based-parallelism chapter, discussing the trace-based treatment of protocols: its rejection of the prevailing practice of specifying a protocol by giving an abstract program for each node, its position that the specification is that the protocol behaves like a buffer together with a statement of the degree of misbehaviour of the medium under which that view is achieved, and Jones's observation that the misbehaving-wire process is in some sense the inverse of a rely-condition.
