---
type: lesson
title: "Trace a boundary problem back to the idealization that caused it"
figure: post
works: [finite-combinatory-processes-formulation-1]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [foundations-of-computation, operating-systems-and-systems-programming]
tags: [lesson]
---
# Trace a boundary problem back to the idealization that caused it

Post runs into a small, concrete irritation: if some outside party hands the machine its input already laid out, the machine has no way to find where that input begins and ends. It is the kind of wrinkle that invites a patch — adopt a convention, agree on a delimiter pattern, declare it a matter of practice. He does note that in practice one would use recognizable groupings. But he does not stop there. He asks what produced the wrinkle, and locates it in an assumption made much earlier and for unrelated reasons: the unbounded space of boxes. An outside party can no more supply an infinite tape than mark infinitely many cells of one. Once the space is finite and the process itself extends it as needed, the question of where the input ends is not a convention anymore — it is answered by construction.

The general shape is worth internalizing. An idealization adopted for convenience at the bottom of a design does not stay at the bottom. It shows up later as an inability to answer a question that should be trivially answerable, and the symptom appears at the interface, far from the assumption that caused it. Treating the symptom means encoding by convention what the design should have made structural, which works until two parties disagree about the convention. Treating the cause means giving up the idealization and letting the system generate what it had been assuming was given.

Post's other move in the same paper is the same instinct applied to input: rather than accepting problems from outside at all, he makes the enumeration of problems itself a process the machine runs, so a bare number suffices to specify which problem is meant and the two processes compose into one. The system becomes closed. Nothing is trusted to arrive well-formed, because nothing arrives from outside.

For working programmers this is the argument against every design that begins "assume the caller provides." Unbounded buffers, pre-populated caches, address spaces treated as endless, configuration that is simply present at startup — each is an idealization that will later surface as a boundary question with no principled answer, and the reflex to reach for a magic value or a sentinel is the reflex to patch the symptom. When you find yourself unable to determine where something ends or whether it is complete, go looking for the resource you assumed was handed to you fully formed, and make the system produce it instead.

**Source:** [Finite Combinatory Processes — Formulation 1](../works/finite-combinatory-processes-formulation-1.md) — the late discussion of the difficulty in recognizing an externally supplied marking, traced to the assumption of an infinite symbol space, alongside the earlier construction of a self-contained development in which the problem set is itself generated.
