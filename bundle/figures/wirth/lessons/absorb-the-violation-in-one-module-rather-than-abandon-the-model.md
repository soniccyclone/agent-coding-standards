---
type: lesson
title: "When a requirement seems to break the global model, look for the one module that can absorb it"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, parallelizability, verifiability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# When a requirement seems to break the global model, look for the one module that can absorb it

**Lesson:** A system's simplifying assumption — one thing at a time, each action runs to completion, no interleaving anyone has to think about — is the most valuable thing it owns, because everything above it is written in the confidence that it holds. Sooner or later a requirement arrives that appears to contradict it outright. Two machines must act at once; something must be attended to before the current action finishes; an event has a deadline shorter than the work in progress. The instinct at that moment is to conclude the model was too naive and to generalise it, which means paying the full cost of concurrency everywhere, forever, in return for one requirement.

Before doing that, look for the smallest region that could absorb the violation on everyone else's behalf. Very often the true concurrency is confined to an instant — data arriving that must be taken now — and what makes it appear global is that the arrival and the *processing* of the arrival have been conflated. Separate them and the problem shrinks: one component accepts the event under whatever real-time discipline the world imposes and deposits it somewhere durable; everything above collects it later, at a moment of its own choosing, entirely within the original model. The concurrency has not been eliminated, it has been given an owner, and the owner is a piece of code small enough to be reasoned about by hand.

What makes this a design principle rather than a trick is the discipline about the boundary. The absorbing component must expose nothing of what it does internally — no callbacks that run at unpredictable moments, no state that the layer above must lock, no obligation to poll faster than it would anyway. If any of that leaks upward, the simplification is gone and you have the costs of both models. Judge the arrangement by the question: can a programmer working above this boundary still write ordinary sequential code and be right? If yes, the global model survived intact and the price was one module. If no, the containment failed, and it is better to know that than to enjoy the appearance of simplicity while the assumption it rests on has quietly become false.

**Source:** [Project Oberon](../works/project-oberon.md) — section 10.1's discussion of how a network command reconciles with the single-process discipline in which every command monopolises the processor until termination: the observation that a networked command engages two processors at once and so appears excluded by the paradigm, that the server senses the request only after any command currently executing has terminated while data arrive at the receiver immediately upon being sent, so that any sizeable delay is inadmissible, and the resolution that the genuine concurrency of sender and receiver is handled inside the driver module, which is activated by an interrupt and whose receiver buffer decouples the partners and removes the timing constraints, all of it remaining hidden within that module.
