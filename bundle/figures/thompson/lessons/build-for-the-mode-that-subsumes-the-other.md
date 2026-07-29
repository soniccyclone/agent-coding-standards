---
type: lesson
title: "Build for the mode that subsumes the other, not the one that looks simpler"
figure: thompson
works: [the-unix-time-sharing-system]
axes: [expressiveness, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Build for the mode that subsumes the other, not the one that looks simpler

**Lesson:** When a system could be built for either of two usage modes, the instinct is to pick the one that is cheaper to implement and bolt the other on later. That instinct ignores the question that actually decides the matter: whether the two modes are symmetrically reachable from each other. Often they are not. One of them, once built, degrades gracefully into the other for free, while the reverse direction requires inventing a whole parallel mechanism. The interactive-versus-scripted split is the canonical case — a system that can hold a live conversation with a person can trivially be handed a canned sequence instead, but a system designed around submitted batches has no natural place to put a human in the loop, so interactivity has to be retrofitted as a separate subsystem that duplicates the first one's logic.

The asymmetry holds because the harder mode carries strictly more state and strictly more decision points. Serving a participant who may change their mind mid-stream forces you to name every intermediate state, expose every step as separately invocable, and keep the system responsive between steps. All of that structure is exactly what a non-interactive driver needs in order to script the thing. The easy mode, by contrast, is free to fuse steps, hide intermediate states, and assume the whole request is known in advance — and every one of those economies is a wall you later have to knock down. Cheapness in the easy direction is bought by foreclosing the hard one.

A programmer who has internalized this stops comparing implementation costs directly and instead asks which of the candidate designs contains the other. That question has a real answer, discoverable before writing code, and it frequently reverses the ranking that a naive effort estimate produces. It also reframes what looks like gold-plating: paying for the richer mode up front is not indulgence, it is buying the second mode at zero marginal cost. The same reasoning generalizes past interactivity — a streaming interface subsumes a whole-input one, an incremental computation subsumes a from-scratch one, a multi-participant model subsumes the single-participant case. In each pair, build the container, then collapse it.

**Source:** [The UNIX Time-Sharing System](../works/the-unix-time-sharing-system.md) — the retrospective section on design considerations, where the authors justify having arranged the system for interactive use even when only one user could be served, resting the argument explicitly on the one-way adaptability between the two modes.
