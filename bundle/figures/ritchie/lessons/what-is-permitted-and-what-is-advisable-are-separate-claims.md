---
type: lesson
title: "What is permitted and what is advisable are separate claims, and a definition should carry both"
figure: ritchie
works: [c-reference-manual]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# What is permitted and what is advisable are separate claims, and a definition should carry both

The reflex when writing a normative document is to flatten it: if something is bad, remove it; if it remains, describe it neutrally, because judgment feels unprofessional in a specification. The C manual refuses that flattening. It defines label variables completely and then says they are a bad idea and that the switch statement makes them nearly always unnecessary. It defines structure initialization and then says the operation is incompletely implemented, machine-dependent, and ill-advised outside a narrow case. It admits that the language is not block-structured and that this can fairly be called a defect — in the section defining scope, not in a footnote. It notes that a keyword is reserved but implemented nowhere. It even walks through an optimization in its own worked example and remarks that the faster version is less clear, leaving the tradeoff to the reader instead of settling it.

The reason to keep these two channels open is that they answer different questions and both questions get asked. An implementer needs to know exactly what is legal, because a compiler that rejects a legal program is broken regardless of whether the construct is wise. A programmer needs to know what to actually write, and a document that supplies only legality forces every reader to rediscover, by injury, which corners are load-bearing and which are historical residue. Removing the bad corners is often not available: existing programs use them, so the choice is not between having the feature and not having it, but between an undocumented trap and a documented one.

Stating a defect plainly also does something a hedge cannot. It tells you which parts of the design are settled and which are under negotiation, so readers can predict where the language is going — the manual says outright that certain currently-illegal operations on structures are expected to be allowed later. That is a forecast a reader can plan against. Vague neutrality gives no such signal, and worse, it spends the author's credibility: a document that praises everything is read as marketing, while one that names its own weak spots earns trust on the parts it does not qualify.

A programmer who internalizes this writes interface documentation with two layers — the contract, and the counsel — and never lets the second silently substitute for the first. Deprecation becomes a note attached to a still-precisely-specified feature rather than a vague warning that the behavior "may change." Code review comments distinguish "this is wrong" from "this is legal and I would not do it," which are different conversations with different resolutions. And the temptation to fix a design problem by pretending the sharp edge is not there, or by documenting it so vaguely that nobody can rely on it, loses its appeal, because the honest sentence costs one line and saves the reader an afternoon.

**Source:** [C Reference Manual](../works/c-reference-manual.md) — the scope-rules discussion conceding the absence of block structure, the treatment of label variables and structure initialization, and the commentary on the alternative implementations in the worked examples chapter.
